# Reversible model-weaving semantics

This is the standalone executable artifact for the internal research draft
*Observation-Stable Model Unweaving: Local Certificates and a Two-Write Boundary*.
It is not a production model weaver and not a proof-assistant development.

The semantic interface is intentionally narrow: a fixed finite catalog of typed
cells; an already executed, occurrence-ordered trace of closed constant-overwrite
events; explicit unary observations; and one keep/erase decision per aspect tag.
Retaining a tag retains all of its occurrences in original order. There is no
rematching, fresh identity creation, hidden read, external effect, arbitrary
relational guard, or production repository claim.

## Results represented by this artifact

The written development in `proofs/semantics.md` establishes, under the declared
assumptions:

- forward typing and complement-backed round trips;
- the need to regenerate retained-event receipts after selective erasure;
- exact observation factorization and last-occurrence normalization;
- a representation-qualified local prime-obstruction result;
- the distinction between local minimum explanations and global policy conflicts;
- a conservative commuting-diamond condition;
- NP-complete policy feasibility in the unbounded finite language;
- sound finite refusal trees and minimum-cardinality policy-core checking;
- an exact no-hidden-variable Boolean expressivity characterization; and
- a polynomial one-write-per-cell fragment versus NP-completeness with at most two
  writes per cell, plus unbounded global cores despite ternary local primes.

Those are written mathematical arguments. The executable protocols below are
finite falsification and certificate-replay evidence, not general mechanization.

## Clean reproduction

Use Python 3.10 or later on POSIX/Linux, the standard library, one CPU worker, and
a fresh nonexistent output directory. No package installation or network access
is needed.

```sh
python reproduce_all.py --output /tmp/weaving-clean
```

The integrated command runs semantic tests, structural tests, source-guided
projections, three pilots, the 50-chunk campaign, five bounded independent-checker
batches, coverage regeneration, an example check, a policy demonstration, and
exact semantic reconciliation against the delivered records. It refuses an
existing output directory and runs one child process at a time.

The final recorded clean run passed all 16 phases in 44.002 wall seconds and
50.370 measured child CPU seconds. Its cumulative child peak RSS was 110,616 KiB.
It exactly compared 50,000 decompressed campaign records, 165 structural inputs,
six source-guided projections, and the scientific counters while deliberately
excluding timing fields from semantic equality. All 50,000 campaign packets were
accepted by the separately implemented checker. See
`results/clean-reproduction.json` and `results/final-recheck/`.

Useful individual commands are:

```sh
python tests/test_semantics.py /tmp/weaving-tests.json
python tests/test_structural.py /tmp/weaving-structural
python tests/test_examples.py /tmp/weaving-examples
python reproduce.py --out /tmp/weaving-campaign
python verify.py /tmp/weaving-campaign/cases-*.jsonl.gz
python verify.py results/examples/example-02.json
```

The campaign can also be produced in resumable 1,000-case chunks numbered 0-49:

```sh
python reproduce.py --out /tmp/weaving-chunks --chunk 0
# repeat for the remaining chunk numbers
python reproduce.py --out /tmp/weaving-chunks --aggregate
```

Aggregation summarizes present chunks; it is not an integrity or correctness
check and is incomplete until all 50 reports exist.

For a bounded policy query:

```sh
python demo.py results/examples/example-02.json --on 2 --off 1 --output /tmp/weaving-query.json
python verify.py /tmp/weaving-query.json
```

A bit in `--on` forces a tag kept; a bit in `--off` forces it erased; the two masks
must be disjoint. The producer minimizes optional removals. An infeasible request
includes a cardinality-minimum conflicting subpolicy and a checked refusal tree.

## Finite evidence

The main campaign has 50,000 deterministic input traces and 231,071 exact replay
queries:

| Population | Inputs | Queries | Invalid queries |
|---|---:|---:|---:|
| Exhaustive scalar | 12,350 | 98,800 | 5,976 |
| Generated small scalar | 36,400 | 127,401 | 6,808 |
| Generated medium | 1,200 | 4,670 | 1,384 |
| Maximum-dimension graph catalog | 50 | 200 | 67 |
| **Total** | **50,000** | **231,071** | **14,235** |

It contains 49,526 successful-replay certificates and 474 local-obstruction
certificates. Of the successful packets, 21,213 select the empty mask and 26,065
execute no retained occurrence; 23,461 execute at least one retained occurrence
and collectively check 49,861 occurrence receipts. Exactly 548 retain the full tag
set. Thus the headline case count is not described as 50,000 nonempty inversions.

The structural protocol has 165 inputs, 2,784 direct retention queries, 7,776
one-writer partial-policy queries, 18 two-writer SAT constructions, and five
binary-choice trees. The largest checked global core has seven facts. The semantic
mutation suite rejects 19 inconsistent changes and accepts one deliberately
consistent replacement, exposing the packet-origin trust boundary.

Six source-guided encodings cover five published figures or passages. They are
small original projections, not six independent benchmarks and not the initially
contemplated 30 published examples. No upstream model-weaving, lens, event-
structure, SAT, or graph-rewrite implementation was executed.

## Producer/checker boundary

`src/checker.py` imports only the Python standard library. It does not import the
producer, normalizer, semantic engine, generator, baselines, or oracle. It parses
the packet independently; replays the original and selected traces; validates
observations, typing, receipt domains, old values, order, local minimum
cardinality, refusal-tree partitioning, and minimum-policy-core claims.

This source separation reduces common-mode implementation risk. It is not
independent authorship, blind review, cryptographic authentication, or a proof of
the source that recorded the input. A coordinated change to an input and its
certificate may define another valid packet and be accepted by design.

The checker trusts Python, the execution environment, and the supplied packet as
the specification. It establishes bounded internal consistency, not a Lean, Coq,
Isabelle, or comparable machine-checked theorem.

## Bounds and resources

The executable schema admits at most 12 tags, 96 occurrences, 512 cells, 64
designated nodes, 192 designated edges, 256 integer-coded values per cell, and
10,000 proof nodes. Proof depth is bounded by the tag count. The mathematical
complexity results quantify over unbounded finite inputs; NP-completeness is not a
claim about a fixed twelve-bit universe.

The final fresh campaign within the integrated run used one worker, 22.483 CPU
seconds, 22.498 wall seconds, peak RSS 110,616 KiB, and a maximum recorded case
time of 0.049 seconds. These values establish resource closure only and are not a
comparative performance claim. The earlier recorded campaign remains preserved;
runtime fields are expected to vary and are excluded from semantic comparison.

## Repository map

- `proofs/semantics.md` - definitions and written proofs T1-T26.
- `src/` - semantic engine, producer, checker, direct oracle, input construction,
  structural construction, and transparent information ablations.
- `tests/` - semantic, structural, source-projection, mutation, and pilot protocols.
- `results/` - exact input streams, summaries, coverage, and final clean-run record.
- `claim_evidence_ledger.csv` - claim-to-proof/test/raw-record mapping and scope.
- `external_resources.csv` - scholarly/workflow sources, reading scope, licensing,
  and integration mode.
- `docs/` - schema, source-projection notes, resource account, calibrated literature
  matrix, and reproduction status.

All generated and source-guided inputs in this repository are original artifact
material. Literature PDFs and upstream tools are not redistributed. The license
for original repository material is in `LICENSE`; publisher template assets are
outside this standalone repository in the complete project package.
