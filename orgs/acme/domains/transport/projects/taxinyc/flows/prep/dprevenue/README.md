# dprevenue

Revenue data product as Lakeflow Spark Declarative Pipelines, deployed with a
[Databricks Asset Bundle](https://docs.databricks.com/aws/en/dev-tools/bundles/) (DAB). No brickops is used.

Pipeline `dprevenue` has its source in `transformations/` and writes to `acme_transport_taxinyc.dprevenue` in prod.
The variant with data quality expectations is the separate bundle [dprevenue_w_dq](../dprevenue_w_dq/README.md).

## Environment naming

Naming per environment is done by the bundle targets in `databricks.yml`:

- `dev` (`mode: development`): pipeline and schema names are prefixed with `dev_<username>_`, and pipelines run in development mode.
- `prod` (`mode: production`): no prefix.

The catalog is the `catalog` bundle variable (default `acme_transport_taxinyc`), override with `--var catalog=...`.

## Deploy from the Databricks UI

1. Open this folder (the one containing `databricks.yml`) in your Git folder in the workspace.
2. Open the **Deployments** panel (rocket icon) in the left sidebar of the editor.
3. Select target `dev` and press **Deploy**.
4. Run the pipeline by pressing the Play button on the Pipeline symbol.

## Deploy from a terminal

```
cd orgs/acme/domains/transport/projects/taxinyc/flows/prep/dprevenue
databricks bundle validate -t dev
databricks bundle deploy -t dev
databricks bundle run dprevenue -t dev
```

Use `-t prod` for production.
