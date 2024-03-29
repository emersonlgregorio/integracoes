from ._anvil_designer import ModalEsbocoTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ModalEsboco(ModalEsbocoTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.width = '80%'
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
    print(dados)
    self.repeating_panel_1.items = dados