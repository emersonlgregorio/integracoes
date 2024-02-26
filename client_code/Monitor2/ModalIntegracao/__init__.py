from ._anvil_designer import ModalIntegracaoTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ModalIntegracao(ModalIntegracaoTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.origem = {"id": "teste01"}
    self.init_components(self.origem,**properties)
    # self.init_components()
    # self.origem = anvil.server.call('dadosOrigem',self.item)
    for p in properties:
      print(p)
    