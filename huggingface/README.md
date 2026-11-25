---
pretty_name: Semantic Density Protocol Pilot
language:
- ru
- en
license: cc-by-4.0
task_categories:
- text-classification
tags:
- semantic-density
- interpretability
- cybernetics
- human-ai-interaction
- annotation-protocol
size_categories:
- n<1K
---

# Semantic Density Protocol Pilot

This is the dataset companion to the experimental Semantic Density Protocol v0.1 by Alexander Gorin / Lamed Group.

It treats semantic density as an observed relation:

P_observed = N * E / D

where N is the number of recognized semantic nodes, E is the reflection-to-reading time ratio, and D is interpretive dispersion across independent observations.

The score is always conditional on a declared lens and context. It is not an intrinsic property of a text.

## Contents

- data/pilot/texts.jsonl: three short interrupt signals used to illustrate lens-sensitive annotation.
- data/pilot/annotations.jsonl: illustrative, deliberately unmeasured hypotheses.
- data/historical/site_cases.jsonl: published site calculations preserved for provenance and marked for re-annotation.
- schemas/: machine-readable record definitions.

## Important limitation

This release is a protocol pilot, not a calibrated benchmark. The pilot annotations must not be used as ground-truth labels. Historical scores were produced during earlier stages of the methodology and are retained as an audit trail.

## Licensing

Original documentation and annotations are released under CC BY 4.0. Third-party source texts are not relicensed. See LICENSE-DATA.md.

## Canonical source

https://www.lamedgroup.info/semantic-density-methodology/

## Code repository

https://github.com/BigLamed/semantic-density-protocol
