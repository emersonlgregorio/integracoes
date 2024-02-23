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
    
    dados = anvil.server.call('dadosOrigem', self.item)
    self.dados_origem = dados[0]['origem']
  #   print(self.origem)
  #   self.destino = dados[0]['destino']
  #   print(self.destino)
    
  @property
  def origem(self):
    return self._origem

  @origem.setter
  def origem(self):
    self._origem = self.dados_origem