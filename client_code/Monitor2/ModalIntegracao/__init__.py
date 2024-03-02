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
    
  
  # self.preencheOrigem()
    
  def preencheOrigem(self, **properties):
    self.origem = properties['origem'][0]
    print(self.origem)
    if self.item['rota'] != 'AplicacoesFarmbox': 
      self.headline_origem.text = 'Origem: UNISYSTEM'
      self.date_picker_data_mvto.date = self.origem['data_mvto']
      self.text_box_deposito.text = self.origem['deposito']
      self.text_box_destino.text = self.origem['destino']
      self.text_box_destino.text = self.origem['destino']
      self.text_box_nr_documento.text = self.origem['nr_documento']
      self.text_box_item.text = self.origem['item']
      self.text_box_desc_item.text = self.origem['descricao_produto']
      self.text_box_quantidade.text = self.origem['quantidade']
      self.text_box_modulo.text = self.origem['modulo']
    else:
      self.origem = properties['origem'][0]
      self.detalhe = properties['detalhe'][0]
      print(self.detalhe)
      self.headline_origem.text = 'Origem: FARMBOX'
      self.column_panel_unisystem.visible = False
      self.date_picker_created_at.date = self.origem['created_at']
      self.date_picker_closed_date.date = self.origem['closed_date']

 

  