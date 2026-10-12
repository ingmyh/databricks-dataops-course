# dprevenue_w_dq

Same as [dprevenue](../dprevenue/README.md), but `revenue_by_borough` has `expect_all_or_fail` data quality
expectations (borough not null and not `Unknown`). Deployed as its own Databricks Asset Bundle.

Prod output schema: `acme_transport_taxinyc.dprevenue_w_dq`. Dev resources are prefixed with `dev_<username>_`.

Deploy from the UI: open this folder in your Git folder, open the **Deployments** panel, select `dev`,
press **Deploy**, then run `dprevenue_w_dq` under **Bundle resources**. From a terminal:

```
databricks bundle deploy -t dev
databricks bundle run dprevenue_w_dq -t dev
```

## Expected failure (teaching case)

The pipeline is **expected to fail** on the first run. `revenue_by_borough` uses `expect_all_or_fail`,
and the source data has trips where `pickup_borough` is NULL, which violates `pickup_borough_not_null`
(and `pickup_borough_not_unknown`). The update stops with an `EXPECTATION_VIOLATION` error, and
`revenue_per_inhabitant` does not run.

To fix it, either switch to `dp.expect_all_or_drop`, or filter out NULL/`Unknown` boroughs before the aggregation.
