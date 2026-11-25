# Semantic Density Protocol

**Experimental protocol for annotating semantic density as an interaction between a construct, a context, and an observing lens.**

Version: **0.1.0 (pilot)**

Author: **Alexander Gorin / Lamed Group**

Canonical methodological source:
https://www.lamedgroup.info/semantic-density-methodology/

Russian documentation: [README_RU.md](README_RU.md)

## Core idea

Semantic density is not treated as a fixed property of a text. The protocol records the density that becomes observable when a particular lens encounters a construct in a particular context:

    P_observed = P(construct | lens, context)

The pilot operational score is:

    P_observed = N * E / D

where:

- **N** — number of semantic nodes that the lens can identify;
- **E** — resonance energy, operationalized as reflection time divided by reading time;
- **D** — interpretive dispersion among observations.

The score is an experimental diagnostic, not a truth, quality, safety, or intelligence score.

## Ashby lens constraint

The protocol uses W. Ross Ashby's law of requisite variety as a constraint on interpretation. If the lens cannot make enough distinctions to match the variety of the construct, part of the construct is collapsed into undifferentiated noise.

The lens is therefore recorded explicitly. A low observed score may indicate either a low-density construct or insufficient resolving variety in the lens.

See [docs/ASHBY_LENS.md](docs/ASHBY_LENS.md).

## Repository contents

- [docs/SPECIFICATION.md](docs/SPECIFICATION.md) — normative v0.1 specification;
- [docs/ANNOTATION_GUIDE.md](docs/ANNOTATION_GUIDE.md) — annotation procedure;
- [docs/ASHBY_LENS.md](docs/ASHBY_LENS.md) — lens model and requisite variety;
- [docs/LIMITATIONS.md](docs/LIMITATIONS.md) — methodological limitations;
- [docs/EXTENSIONS.md](docs/EXTENSIONS.md) — non-core experimental dimensions;
- [docs/SOURCE_MAP.md](docs/SOURCE_MAP.md) — source articles and case studies;
- [schemas/](schemas/) — JSON schemas;
- [data/pilot/](data/pilot/) — pilot annotations;
- [data/historical/](data/historical/) — historical site calculations;
- [examples/interrupt-signals.md](examples/interrupt-signals.md) — first calibration case;
- [src/semantic_density/](src/semantic_density/) — dependency-free calculator;
- [huggingface/README.md](huggingface/README.md) — dataset card template.

## Quick start

Requires Python 3.10 or newer.

    python -m pip install -e .
    semantic-density score --nodes 18 --reading-seconds 600 --reflection-seconds 1800 --dispersion 5

Validation and tests:

    make validate
    make test

Build a Hugging Face upload directory:

    make hf

## Data status

The pilot dataset contains:

1. an illustrative three-signal comparison;
2. a historical index of calculations published by Lamed Group.

Historical calculations were produced while the method was evolving. They are preserved as provenance and must not be treated as a calibrated benchmark.

## Citation

See [CITATION.cff](CITATION.cff).

## Licenses

- Code: Apache License 2.0 — see [LICENSE-CODE](LICENSE-CODE).
- Documentation and original dataset annotations: CC BY 4.0 — see [LICENSE-DATA.md](LICENSE-DATA.md).
- Linked third-party texts remain under their original rights. This repository stores metadata and analytical annotations, not full third-party works.

