# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Bonus task: Deploy a bundle with GitHub Actions
# MAGIC
# MAGIC In a real setup, prod is not deployed by hand from someone's machine, but by a CI/CD pipeline.
# MAGIC Normally your Databricks admin sets this up once. In this workshop, you do it yourself against your own fork.
# MAGIC
# MAGIC This task is intentionally open. **How you solve it is up to you.** Use whatever help you like,
# MAGIC including an AI assistant, the Databricks docs, and your instructor.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Deploy the `dprevenue` bundle with a GitHub Actions workflow
# MAGIC
# MAGIC Create a GitHub Actions workflow in your fork of the repo that deploys the bundle in
# MAGIC `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue`.
# MAGIC
# MAGIC ### Requirements
# MAGIC
# MAGIC 1. The workflow can be started manually from the Actions tab in GitHub.
# MAGIC 2. It validates and deploys the bundle to the **`dev`** target. Do not deploy to `prod` without asking your instructor.
# MAGIC 3. It authenticates to your workspace without any credentials committed to the repo.
# MAGIC 4. After a successful run, the deployed pipeline is visible in the workspace, and you can run it.
# MAGIC
# MAGIC ### Stretch goals
# MAGIC
# MAGIC - Also run the pipeline after the deploy.
# MAGIC - Deploy `dprevenue_w_dq` as well, from the same workflow.
# MAGIC - Trigger the workflow on a push to `main`, or when a release is published.
# MAGIC - Deploy `prod` from CI/CD, with the instructor's approval.
# MAGIC
# MAGIC ### Things to think about
# MAGIC
# MAGIC - How does the Databricks CLI get installed on the GitHub runner?
# MAGIC - Which secrets does the CLI need, and where do you store them in GitHub?
# MAGIC - Which identity should deploy: a personal user or a service principal? What are the trade-offs?
# MAGIC - The bundle `dev` target prefixes names with a username. Whose username will it be when CI deploys?
# MAGIC - The existing `.github/workflows/deploy.yaml` uses an older approach, `databricks repos update` followed by a job. Compare it with a bundle deploy.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Reflection
# MAGIC
# MAGIC What did you ask the AI assistant, and what did you have to correct or verify yourself?
# MAGIC
# MAGIC Answer here...
