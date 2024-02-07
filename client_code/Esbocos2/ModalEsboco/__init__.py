from ._anvil_designer import ModalEsbocoTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

class ModalEsboco(ModalEsbocoTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.getItems(self.item['DocEntry'], self.item['ObjType'])
    
    # Any code you write here will run before the form opens.

  def getItems(self,docentry, objtype):
    print(docentry, objtype)
    filtro = f"""
                where i."DocEntry" = {docentry}
	              AND i."ObjType" = '{objtype}'
              """
    print(filtro)
    dados = anvil.server.call('get_drafts_items', filtro)
    i = 0
    for d in dados:
      dados[i]['LineTotal'] = f"{int(d['LineTotal']):.2f}"
      i += 1
    print(json.dumps(dados,indent=4))
    self.repeating_panel_1.items = dados