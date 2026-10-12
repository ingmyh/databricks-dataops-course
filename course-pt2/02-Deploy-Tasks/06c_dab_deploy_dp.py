# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy declarative pipelines with a Databricks Asset Bundle (DAB)
# MAGIC
# MAGIC The `dprevenue` and `dprevenue_w_dq` pipelines are the modern versions of `dltrevenue` and `dltrevenue_w_dq`:
# MAGIC
# MAGIC - Source is plain python files using `from pyspark import pipelines as dp`, not notebooks.
# MAGIC - Deployment and environment naming is done by a DAB (`databricks.yml`), not brickops.
# MAGIC
# MAGIC ## Study: the bundle
# MAGIC
# MAGIC Look at the files in `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue/`:
# MAGIC
# MAGIC - `databricks.yml`: bundle name, `catalog` variable and the `dev`/`prod` targets
# MAGIC - `resources/pipelines.yml`: the pipeline
# MAGIC - `resources/schemas.yml`: the schema the pipeline writes to
# MAGIC - `transformations/`: the pipeline source code

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Deploy to dev with the Deploy button
# MAGIC
# MAGIC 1. In your Git folder, open the folder `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue`.
# MAGIC 2. Open the **Deployments** panel (rocket icon) in the left sidebar of the editor.
# MAGIC 3. Select the target `dev`.
# MAGIC 4. Press **Deploy**.
# MAGIC 5. Under **Bundle resources**, press the run icon next to the `dprevenue` pipeline.
# MAGIC 6. Optional: repeat for `flows/prep/dprevenue_w_dq`, which adds data quality expectations.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Find the deployed pipeline and schema
# MAGIC
# MAGIC 1. Find the pipeline under Jobs & Pipelines. Which prefix was added to its name?
# MAGIC 2. Find the schema in catalog `acme_transport_taxinyc`. Which prefix was added?
# MAGIC 3. Where in `databricks.yml` does the prefixing come from?
# MAGIC
# MAGIC Answer here...

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Redeploy after a change
# MAGIC
# MAGIC 1. Change a transformation in `transformations/revenue.py`, e.g. the rounding in `revenue_per_inhabitant`.
# MAGIC 2. Press **Deploy** again and rerun the pipeline.
# MAGIC
# MAGIC ## Task: Deploy to prod
# MAGIC
# MAGIC Select the target `prod` and press **Deploy**. Prod resources get no prefix, so the schema becomes
# MAGIC `acme_transport_taxinyc.dprevenue`. This fails if someone else has already deployed prod, as there can only be one.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run `dprevenue_w_dq` and study the failure
# MAGIC
# MAGIC `dprevenue_w_dq` is **expected to fail**. This is intentional.
# MAGIC
# MAGIC 1. Deploy and run `dprevenue_w_dq` as above.
# MAGIC 2. Open the failed update and find the `EXPECTATION_VIOLATION` error. Which flow failed, and which expectations were violated?
# MAGIC 3. Why does the expectation fail? Look at the output record in the error message.
# MAGIC 4. Why did `revenue_per_inhabitant` not run?
# MAGIC 5. Optional: fix the pipeline, either with `dp.expect_all_or_drop` or by filtering out the bad rows before the aggregation, then redeploy and rerun.
# MAGIC
# MAGIC Answer here...
