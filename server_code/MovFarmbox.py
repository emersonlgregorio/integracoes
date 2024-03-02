import anvil.email
import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
import json

@anvil.server.callable
def dadosOrigemFarmbox(filtro):
  print('Busca dados no farmbox')
  # import requests
  url = f"https://farmbox.cc/api/v1/applications/{filtro}"
  payload = {}
  headers = {
    'Authorization': 'pXZG_P61XsP73FIXbA81jw'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  f = json.loads(response.text)

  mestre = {
    "id": f['id'],
    "code": f['code'],
    "date": f['date'],
    "end_date": f['end_date'],
    "status": f['status'],
    "closed_date": f['closed_date'],
    "created_at": f['created_at'],
    "updated_at": f['updated_at'],
    "reopened_reference_id": f['reopened_reference_id']
  }
  print(mestre)
  movi = []
  movimentations = f['input_movimentations']
  for m in movimentations:
    m['nomeItem'] = buscaItem(m['input_id'])
    m['nomeDeposito'] = buscaDeposito(m['storage_id'])
    movi.append(m)
  
  linhas = {
    "input_movimentations": movi
  }
  print(linhas)
  return mestre, linhas


def buscaDeposito(filtro):
  url = f"https://farmbox.cc/api/v1/storages/{filtro}"
  payload = {}
  headers = {
    'Authorization': 'pXZG_P61XsP73FIXbA81jw'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  d = json.loads(response.text)
  nomeDeposito = d['name']
  return nomeDeposito


def buscaItem(filtro):
  url = f"https://farmbox.cc/api/v1/inputs/{filtro}"
  payload = {}
  headers = {
    'Authorization': 'pXZG_P61XsP73FIXbA81jw'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  p = json.loads(response.text)
  nomeItem = p['name']
  return nomeItem