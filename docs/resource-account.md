# Resource evidence and accounting scope

Scientific intake observed five visible logical processors under a four-core cgroup
CPU quota, a 4 GiB cgroup memory limit, no swap, and approximately 30 GiB writable
space. Every scientific run used one worker. No GPU, external computation, model API,
private dataset, networked experiment, real device/service, or new human participant
was used by the executable artifact.

The final complete integrated reproduction is `results/clean-reproduction.json`.
It ran 16 phases in 44.002 wall seconds with 50.370 measured child CPU seconds and
110,616 KiB cumulative child peak RSS. The fresh 50,000-case campaign within that run
used 22.483 CPU seconds, 22.498 wall seconds, 110,616 KiB peak RSS, and a maximum
recorded case time of 0.049 seconds. These measurements support resource closure only;
they are not a speedup or external-tool comparison.

The original campaign record remains preserved under `results/campaign/`. CPU is
process CPU, wall time is monotonic elapsed time, and RSS is the operating system's
process high-water mark in KiB. The final runner regenerated and semantically compared
50,000 campaign records, 165 structural inputs, six source-guided projections, and
the reported scientific counters. It checked all 50,000 packets in five bounded
10,000-packet batches. Runtime fields were excluded from semantic equality because
they are expected to vary.

Counters are named semantic, Boolean, and checking operations, not hardware
instructions. Two early exploratory smoke invocations did not record CPU. Their
missing values are not reconstructed or reported as zero, so a fully measured total
for all exploratory work is unavailable. All structured pilots, the original
campaign, and the final reproduction are separately retained.

No scholarly PDF or upstream tool is redistributed in the artifact. Browser-readable
papers supported reasoning and attribution; stable scholarly URLs and actual reading
scope are recorded in `external_resources.csv`. No external baseline internals were
modified or executed. The supplied ACM assets are retained only in the complete
project's `paper/` directory under their supplied license. No hash, checksum, commit,
release, or toolchain-fingerprint manifest is generated.
