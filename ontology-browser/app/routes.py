from app import app
from flask import render_template, request
import pandas as pd
import requests
import json


# Add file location of personal ontology and API key to the NIH UMLS here
df_umls_dut = pd.read_csv('data/umls_dutch.csv', delimiter=',', header=0)
API_KEY = '##'

def lookup(cui):
    subset_dut = df_umls_dut[df_umls_dut['cui'] == cui]
    # subset_off = df_umls_off[df_umls_off['cui'] == cui]

    return subset_dut

def getDefinition(url):
    r = requests.get(f'{url}?apiKey={API_KEY}')
    definitions = json.loads(r.text)['result']
    for definition in definitions:
        if definition['rootSource'] in ['NCI', 'MSH', 'FMA', 'CSP']:
            return definition['value']

def getAtoms(url):
    print(url)
    r = requests.get(f'{url}?apiKey={API_KEY}')
    atom_names = []
    for atom in json.loads(r.text)['result']:
        if atom['language'] == 'DUT' or atom['language'] == 'ENG':
            atom_names.append([atom['rootSource'], atom['name']])
    return atom_names

def queryApi(cui):
    r = requests.get(f'https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{cui}?apiKey={API_KEY}')
    atoms_url = json.loads(r.text)['result']['atoms']
    definition_url = json.loads(r.text)['result']['definitions']
    atoms = getAtoms(atoms_url)
    if definition_url != 'NONE':
        definition = getDefinition(definition_url)
    else:
        definition = ''
    return atoms, definition

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/browser')
def browse():
    query = request.args.get('query')
    splitted = query.split('C')
    result_1_dut = lookup(f"C{splitted[1]}")
    result_1_off, definition_1 = queryApi(f"C{splitted[1]}")

    if len(splitted) > 2:
        result_2_dut = lookup(f"C{splitted[2]}")
        result_2_off, definition_2 = queryApi(f"C{splitted[2]}")

        return render_template('index.html', result_1_dut=list(result_1_dut.values), result_1_off=result_1_off, result_2_dut=list(result_2_dut.values), result_2_off=result_2_off, definition_1=definition_1, definition_2=definition_2)

    return render_template('index.html', result_1_dut=list(result_1_dut.values), result_1_off=result_1_off, result_2=None, definition_1=definition_1, definition_2='')

