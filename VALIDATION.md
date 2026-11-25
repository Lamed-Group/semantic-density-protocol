# Validation record

Release candidate: v0.1.0

Date: 2026-11-25

The package was checked in a clean local Python target using Python 3.12.

## Results

- Four unit tests passed.
- All three JSONL datasets passed the repository validator.
- All JSONL records passed their corresponding JSON Schema.
- Manifest counts matched: 3 pilot texts, 3 pilot annotations, 6 historical cases.
- The installed command-line calculator reproduced the published example: N=18, E=3, D=5, P_observed=10.8.
- The Hugging Face upload directory built successfully.

## Reproduce

    make check
    make hf-export

The validation confirms packaging and calculation consistency. It does not establish empirical validity or benchmark calibration.
