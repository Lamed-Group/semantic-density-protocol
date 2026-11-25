# Publishing checklist

## GitHub

1. Create a public repository named `semantic-density-protocol` under `BigLamed`.
2. Upload the contents of this directory to the repository root.
3. Create the first release with tag `v0.1.0`.
4. Use the release title `Semantic Density Protocol v0.1 — experimental specification`.
5. Preserve the warning that the pilot is not a calibrated benchmark.

## Hugging Face

1. Run `make hf-export`.
2. Create a dataset repository, for example `BigLamed/semantic-density-protocol`.
3. Upload the contents of `dist/huggingface`, not the enclosing directory.
4. Confirm that the dataset card displays the experimental-status warning.
5. Keep historical records separate from future calibrated observations.

No deployment or model hosting is required. Both destinations publish files and documentation only.
