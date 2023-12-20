## Ontology-browser

Tool for comparing ontology entries in a custom ontology and the internation UMLS.

### Requirements

1. Add custom ontology as csv-file to data the data folder. The headers should look like:
   ```
   cui,name,type_ids,ontologies,name_status
   C0000039,"1,2-dipalmitoylphosphatidylcholine",T109|T121,RXNORM,A
   ```  

2. [Request](https://www.nlm.nih.gov/vsac/support/usingvsac/requestumlslicense.html) a UMLS license
3. Add your UMLS API-key to app/routes.py


### Usage

Input 2 CUI's without separator.

Example:
```
C0013395C0857257
```

<img src="https://github.com/fonshartendorp/dutch_biomedical_entity_linking/blob/main/ontology-browser/ontology-browser.png">
