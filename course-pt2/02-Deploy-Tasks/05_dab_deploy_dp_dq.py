# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy the dp pipeline with data quality checks
# MAGIC
# MAGIC `dprevenue_w_dq` is a variant of `dprevenue` with data quality expectations.
# MAGIC It is deployed as its own Databricks Asset Bundle (DAB), in the same way as `dprevenue` in the previous task.
# MAGIC
# MAGIC **This pipeline is expected to fail on the first run. This is intentional.**

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## In and out data
# MAGIC
# MAGIC ### Incoming data
# MAGIC
# MAGIC - A sample of NYC Taxi data, from Unity Catalog (UC) path `training.taxinyc_trips.yellow_taxi_trips_curated_sample`
# MAGIC - NYC population data
# MAGIC
# MAGIC ### Outgoing data product
# MAGIC
# MAGIC We produce a data product called revenue. For now it contains the following outgoing data sets:
# MAGIC
# MAGIC 1. `revenue_by_tripmonth`
# MAGIC 2. `revenue_by_borough`
# MAGIC 3. `revenue_per_inhabitant`
# MAGIC
# MAGIC `trips` and `borough_population` are intermediate internal datasets.
# MAGIC
# MAGIC In production, the data product will be written as the UC schema `acme_transport_taxinyc.dprevenue_w_dq`.
# MAGIC In dev, the schema and pipeline names are prefixed with your username by the bundle's `dev` target.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: the bundle
# MAGIC
# MAGIC Look at the files in `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue_w_dq/`:
# MAGIC
# MAGIC - `databricks.yml`: bundle name, `catalog` variable and the `dev`/`prod` targets
# MAGIC - `resources/pipelines.yml`: the pipeline
# MAGIC - `resources/schemas.yml`: the schema the pipeline writes to
# MAGIC - `transformations/revenue_w_dq.py`: the pipeline source code. Compare it to `dprevenue/transformations/revenue.py`. What is different?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Deploy to dev and run the pipeline
# MAGIC
# MAGIC 1. In your Git folder, open the folder `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue_w_dq`.
# MAGIC 2. Open the **Deployments** panel (rocket icon) in the left sidebar of the editor.
# MAGIC 3. Select the target `dev`.
# MAGIC 4. Press **Deploy**.
# MAGIC 5. Run the `dprevenue_w_dq` pipeline by pressing the Play button on the Pipeline symbol.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Investigate why the pipeline fails
# MAGIC
# MAGIC The pipeline should fail in the `revenue_by_borough` step with an `EXPECTATION_VIOLATION` error.
# MAGIC
# MAGIC 1. Open the failed update and find the error. Which flow failed, and which expectations were violated?
# MAGIC 2. Why does the expectation fail? Look at the output record in the error message.
# MAGIC 3. Why did `revenue_per_inhabitant` not run?

# COMMAND ----------

# MAGIC %md
# MAGIC _Add reason for the failure here..._

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Fix the failure by changing from fail to drop in the expectation
# MAGIC
# MAGIC Go to `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue_w_dq/transformations/revenue_w_dq.py`.
# MAGIC
# MAGIC Change
# MAGIC
# MAGIC ```
# MAGIC @dp.expect_all_or_fail({...})
# MAGIC ```
# MAGIC
# MAGIC To
# MAGIC
# MAGIC ```
# MAGIC @dp.expect_all_or_drop({...})
# MAGIC ```
# MAGIC
# MAGIC Press **Deploy** again, and rerun the pipeline by pressing the Play button on the Pipeline symbol. It should now work.
# MAGIC
# MAGIC Alternatively, filter out the bad rows before the aggregation.
