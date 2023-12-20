# Dutch biomedical entity linking

This repository contains the code for generating the training data and training and evaluating the sapBERT+fine-tuned Dutch biomedical entity linking model as presented in the report. The pre-trained weights of our optimal model are found on [Huggingface](https://huggingface.co/fonshartendorp/dutch_biomedical_entity_linking)

### Summary
- a RoBERTa-based basemodel that is trained from scratch on Dutch hospital notes ([medRoBERTa.nl](https://huggingface.co/CLTL/MedRoBERTa.nl)).
- that is 2nd-phase pretrained using [self-alignment](https://doi.org/10.48550/arXiv.2010.11784) on UMLS-derived Dutch biomedical ontology.
- and finally fine-tuned on automatically generated weakly labelled corpus from Wikipedia (WALVIS).
- evaluation results on [Mantra GSC](https://doi.org/10.1093/jamia/ocv037) corpus can be found in the [report](https://github.com/fonshartendorp/dutch_biomedical_entity_linking/blob/main/report/report.pdf)

### Overview
<img src="https://github.com/fonshartendorp/dutch_biomedical_entity_linking/blob/main/report/overview.png" width="80%" />

The code for enhancing the UMLS and creating a biomedical ontology for biomedical entity linking (1\_enhance\_UMLS) is a slightly tweaked version from the [Dutch-medical-concepts](https://github.com/umcu/dutch-medical-concepts) repository from the UMCU. The code for sapBERT and fine-tuning is largely re-used from the [code base of the original paper](https://github.com/cambridgeltl/sapbert/tree/main). 

For enhancing the UMLS a UMLS and SNOMED NL license should be requested.

### ONTOLOGY-browser
The ONTOLOGY-browser is a minimal Flask-based browser tool for comparing UMLS entries.


<img src="https://github.com/fonshartendorp/dutch_biomedical_entity_linking/blob/main/ontology-browser/ontology-browser.png" />

