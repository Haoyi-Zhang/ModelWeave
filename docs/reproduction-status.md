# Clean reproduction status

## Final recorded run

A complete integrated reproduction was run from the final standalone repository
with one child process at a time and a fresh nonexistent output directory:

```sh
PYTHONDONTWRITEBYTECODE=1 python reproduce_all.py --output /tmp/weaving-clean
```

Result: **PASS**.

- 16/16 phases exited 0.
- Integrated wall time: 44.002 seconds.
- Measured child CPU: 50.370 seconds.
- Cumulative child peak RSS: 110,616 KiB.
- Workers: 1.
- Network and non-standard Python dependencies: none.
- Hash/checksum manifest: not generated.

The phases were semantic tests, structural tests, source-guided examples, three
measured pilots, the 50-chunk campaign, five independent campaign-checker batches,
coverage regeneration, independent source-example checking, a policy demo, and
independent checking of the demo packet.

## Reconciled scientific records

The runner regenerated and exactly compared, after gzip decompression where
applicable:

- 50,000 campaign packet records across 50 streams;
- 231,071 direct replay query outcomes and associated scientific counters;
- 50,000 independently checked campaign certificates;
- the coverage summary, including 23,461 success packets with at least one retained
  occurrence and 49,861 checked occurrence receipts;
- seven semantic test methods and their evidence counters;
- all 165 structural inputs and the structural raw-record stream;
- six source-guided projection packets; and
- one generated policy-query packet.

Timing fields were intentionally excluded from semantic equality. Performance
measurements vary across executions and support only resource closure.

## Final fresh campaign measurements

The campaign phase itself completed 50,000 cases and 231,071 queries in 22.483 CPU
seconds and 22.498 wall seconds, with peak RSS 110,616 KiB and maximum recorded
case time 0.049 seconds. It produced 49,526 successful-outcome certificates and
474 local-obstruction certificates. All 50,000 packets were accepted by
`verify.py` in five 10,000-packet batches.

## Evidence locations

- Consolidated result: `results/clean-reproduction.json`
- Full command/exit/resource record: `results/final-recheck/clean-run.json`
- Fresh campaign summary: `results/final-recheck/campaign-summary.json`
- Fresh coverage: `results/final-recheck/coverage.json`
- Semantic and structural summaries: `results/final-recheck/semantic-tests.json`
  and `results/final-recheck/structural-summary.json`
- Independent checker decisions: `results/final-recheck/independent-*.json`

A successful clean command is not a proof of the general mathematical theorems.
Those remain written arguments in `proofs/semantics.md`; the executable result is
finite, deterministic evidence relative to the supplied packet semantics.
