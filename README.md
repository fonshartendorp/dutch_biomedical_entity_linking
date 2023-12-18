# Dutch biomedical entity linking

This repository contains the code, (the publically available) data and pretrained weights for the sapBERT+fine-tuned Biomedical Entity Linking model on the Dutch language as presented in the report.

### Overview
![overview](/report/overview.png)


The code for enhancing the UMLS and creating a biomedical ontology for biomedical entity linking (1\_enhance\_UMLS) is a slightly tweaked version from the [Dutch-medical-concepts](https://github.com/umcu/dutch-medical-concepts) repository from the UMCU. The code for sapBERT and fine-tuning is largely re-used from the [code base of the original paper](https://github.com/cambridgeltl/sapbert/tree/main). 

For enhancing the UMLS a UMLS and SNOMED NL license should be requested.

## UMLS-browser
The UMLS-browser is a minimal Flask-based browser tool for comparing UMLS entries.

[![UMLS-browser](/umls_browser/umls-browser.png "UMLS-browser")](/umls_browser/umls-browser.png)
