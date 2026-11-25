PYTHON ?= python3

.PHONY: test validate check hf hf-export

test:
	PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -v

validate:
	PYTHONPATH=src $(PYTHON) scripts/validate_data.py

check: validate test

hf:
	$(PYTHON) scripts/build_hf_export.py

hf-export: hf

