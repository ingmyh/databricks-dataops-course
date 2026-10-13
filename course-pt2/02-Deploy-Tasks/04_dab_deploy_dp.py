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
# MAGIC 5. Run the `dprevenue` pipeline by pressing the Play button on the Pipeline symbol.

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
# MAGIC `acme_transport_taxinyc.dprevenue`. Prod is shared, so only one copy exists. See the prod deploy task later.
