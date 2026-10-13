"""Lakeflow Spark Declarative Pipeline: taxi revenue aggregates with data quality checks."""

from pyspark import pipelines as dp
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

spark = SparkSession.getActiveSession()


@dp.materialized_view
def trips() -> DataFrame:
    return spark.read.table("training.taxinyc_trips.yellow_taxi_trips_curated_sample")


@dp.materialized_view(
    name="revenue_by_borough",
    comment="Aggregated revenue by pickup borough",
    table_properties={"quality": "silver"},
)
@dp.expect_all_or_fail(
    {
        "pickup_borough_not_null": "pickup_borough IS NOT NULL",
        "pickup_borough_not_unknown": "pickup_borough <> 'Unknown'",
    }
)
def revenue_by_borough() -> DataFrame:
    return (
        spark.read.table("trips")
        .groupBy("pickup_borough")
        .agg(F.sum("total_amount").alias("amount"))
        .sort(F.col("pickup_borough").asc())
    )


@dp.materialized_view(
    name="revenue_by_tripmonth",
    comment="Aggregated revenue by trip month",
    table_properties={"quality": "silver"},
)
def revenue_by_tripmonth() -> DataFrame:
    return (
        spark.read.table("trips")
        .groupBy("pickup_borough", "trip_year", "trip_month")
        .agg(F.sum("total_amount").alias("amount"))
        .sort(["pickup_borough", "trip_year", "trip_month"], ascending=True)
    )


@dp.materialized_view(
    name="borough_population",
    comment="Population per borough",
    table_properties={"quality": "silver"},
)
def borough_population() -> DataFrame:
    return spark.read.table("training.taxinyc_trips.borough_population")


@dp.materialized_view(
    name="revenue_per_inhabitant",
    comment="Aggregated revenue by pickup borough per inhabitant",
    table_properties={"quality": "silver"},
)
def revenue_per_inhabitant() -> DataFrame:
    revenue_by_borough_df = spark.read.table("revenue_by_borough")
    borough_population_df = spark.read.table("borough_population")
    return (
        revenue_by_borough_df.where(
            F.col("pickup_borough").isNotNull() & (F.col("pickup_borough") != "Unknown")
        )
        .join(
            borough_population_df,
            revenue_by_borough_df.pickup_borough == borough_population_df.borough,
            "inner",
        )
        .withColumn("rounded_amount", F.round("amount", 2))
        .withColumn(
            "revenue_per_inhabitant",
            F.round(F.col("rounded_amount") / borough_population_df.population, 2),
        )
        .sort("revenue_per_inhabitant", ascending=False)
    )
