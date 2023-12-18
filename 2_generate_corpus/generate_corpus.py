# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
import json
import pickle as pkl
import re
from urllib.parse import unquote
import json

# Regex for finding hyperlinks on Wikipedia pages
pattern = '<a href=\\"(.+?)\\">(.+?)<\/a>'


def parseDocument(doc):
        """
        Spit 
        """
        samples = ""
        datasample_id = 0
        text = nlp(doc['text'])
        for sent in text.sents:
                matches = re.findall(pattern, str(sent))
                subbed = str(sent).replace("'", "")

                cuis = []
                for url in matches:
                        try:
                                subbed = re.sub(pattern, url[1], subbed, 1)
                        except:
                                continue
                        if str(sent[0:2]) == '<a':
                                continue

                        try:
                                idd = title_to_CUI[unquote(url[0])]

                                try:
                                        CUI = to_CUI[idd]
                                        start_index = subbed.index(url[1])
                                        end_index = start_index + len(url[1])
                                        cuis.append((url[1], CUI, start_index, end_index))
                                except:
                                        continue
                        except:
                                continue
                if len(cuis) > 0 and '<' not in subbed and '>' not in subbed:
                        sample = {
                                'sentence' : subbed.replace('\n', ''),
                                'annotations' : []
                        }

                        for cui in cuis:
                                sample['annotations'].append({
                                        'mention' : cui[0],
                                        'CUI' : cui[1],
                                        'start' : cui[2],
                                        'end' : cui[3]
                                })
                        return sample

# Load Dutch Spacy pipeline
nlp = spacy.load("nl_core_news_sm")

with open('wiki_title_to_CUI_geneeskunde_aandoening_fysiologie_4', 'rb') as f:
        title_to_CUI = pkl.load(f)


_keys = title_to_CUI.keys()

samples = {
        'samples' : []
}

for line in open('all/AA/wiki_00', 'rb'):
        doc = json.loads(line)
        matches = re.findall(pattern, doc['text'])

        for url in matches:
                if url[0] in _keys:
                        sample = parseDocument(doc)
                        if sample:  
                                samples['samples'].append(sample)
                        break

print(len(samples['samples']))
