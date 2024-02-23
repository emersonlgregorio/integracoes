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
    self.init_components(**properties)
    for p in properties:
      print(p)

    # Any code you write here will run before the form opens.
    self.origem = [
      {
        "id": 1,
        "descricao": 'DDR5 32Gb 4800Mhz'
      }
    ]
    print(self.origem)