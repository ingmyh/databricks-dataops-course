# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy a bundle to prod
# MAGIC
# MAGIC A Databricks Asset Bundle (DAB) is deployed to an environment by selecting a **target**.
# MAGIC The targets are defined in `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue/databricks.yml`.
# MAGIC
# MAGIC | | `dev` | `prod` |
# MAGIC |---|---|---|
# MAGIC | `mode` | `development` | `production` |
# MAGIC | Resource names | prefixed with `dev_<username>_` | no prefix |
# MAGIC | Pipeline development mode | on | off |
# MAGIC | Bundle files deployed to | `~/.bundle/dprevenue/dev` (your home) | `/Shared/.bundle/dprevenue/prod` |
# MAGIC | Output schema | `acme_transport_taxinyc.dev_<username>_dprevenue` | `acme_transport_taxinyc.dprevenue` |
# MAGIC
# MAGIC Prod is not prefixed and lives in a shared path, so there is only one prod copy of the pipeline and the schema.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Deploy to prod
# MAGIC
# MAGIC **Ask the teacher before you deploy to prod**, since prod is shared by everyone in the workshop.
# MAGIC
# MAGIC 1. In your Git folder, open the folder `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue`.
# MAGIC 2. Open the **Deployments** panel (rocket icon) in the left sidebar of the editor.
# MAGIC 3. Select the target `prod`.
# MAGIC 4. Press **Deploy**.
# MAGIC 5. Run the `dprevenue` pipeline by pressing the Play button on the Pipeline symbol.
# MAGIC
# MAGIC The same can be done from a terminal:
# MAGIC
# MAGIC ```
# MAGIC databricks bundle validate -t prod
# MAGIC databricks bundle deploy -t prod
# MAGIC databricks bundle run dprevenue -t prod
# MAGIC ```
# MAGIC
# MAGIC After the deploy, the prod pipeline is called `dprevenue` and writes to `acme_transport_taxinyc.dprevenue`.
# MAGIC In practice, prod is normally deployed from CI/CD rather than from a developer's machine.
