# Evidence maturity and ledger use

`claim_evidence_ledger.csv` separates mathematical claims, finite executable evidence,
completed delivery checks, and residual external-use holds. The standalone artifact
contains every mathematical argument in `proofs/semantics.md`; paper paths in the CSV
are cross-references only and are not required to execute the repository.

"Written mathematical proof" means a supplied human-readable argument. It does not
mean proof-assistant mechanization, external acceptance, independent authorship, or
blind review. "Separate checker" means implementation separation inside this packet;
it does not establish source authenticity or cryptographic provenance. Finite checks
falsify bounded instances and reconcile records but do not prove an unbounded theorem.

The literature matrix now contains 22 completed calibration records: 12 TOPLAS, 5
adjacent, and 5 influential papers. Completion means whole-paper structural traversal
and claim-level reading for the recorded fields, not replication or a bibliometric
proof of novelty. The historical Aspect Model Unweaving paper is recorded separately
and is not counted toward that 12/5/5 matrix.

The final clean run is recorded in `results/clean-reproduction.json` and
`results/final-recheck/`. Timing fields are intentionally excluded from semantic
record equality. `CURRENT-STATE.md` in the complete project is the authoritative
snapshot for delivery and external-readiness holds.
