from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import json
from ..ModalIntegracao import ModalIntegracao

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if self.item['status'] == 'C':
      self.button_reprocessar.visible = False
      self.background = "#C8E6C9"
    elif self.item['status'] == 'I':
      self.background = "#FFF9C4"
    elif self.item['status'] == 'E':
      self.background = "#FFCDD2"

    # Any code you write here will run before the form opens.

  def button_reprocessar_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.item['rota'] == 'AplicacoesFarmbox':
      self.reprocessarFarmbox(self.item['seqPlanilha'])
    else:
      anvil.server.call('reprocessar', self.item['id_integracao'])

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    modal = ModalIntegracao(item=self.item)
    alert(modal, large=True, title="Dados da Integração", buttons=[])
    
  def reprocessarFarmbox(self,idFarmbox, **event_args):
    url = "https://crestani.api.integrasky.cloud/GJ9fZFjNbe"
    payload = {
      "id": {idFarmbox}
    }
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Basic Zmxvdy1HSjlmWkZqTmJlQGNyZXN0YW5pOlNlbmhhQDIwMjMj'
    }
    try:
      anvil.http.request(url=url, method="POST", data=payload,
                         headers=headers)
    except anvil.http.HttpError as e:
      print(f"Error {e.status}")

  
