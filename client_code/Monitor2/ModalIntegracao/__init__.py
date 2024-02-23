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
    # for p in properties:
    #   print(p)
    # Any code you write here will run before the form opens.
    
    dados = anvil.server.call('dadosOrigem', self.item)
    print('item')
    print(self.item)
    print('Origem')
    print(dados[0]['origem'])
    # print(dados['origem'])
    self.repeating_panel_origem.items = dados[0]['origem']
    
    
  # def origem(self, planilha):
  #   dadosOrigem = anvil.server.call('dadosOrigem', planilha)
  #   self.repeating_panel_origem.items = dadosOrigem