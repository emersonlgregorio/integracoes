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
    for i, p in enumerate(properties):
      if p == 'origem':
        origem = properties['origem'][0]
      elif p == 'detalhe':
        detalhe = properties['detalhe']
        print(detalhe)
      
    if self.item['rota'] != 'AplicacoesFarmbox':
      self.origemUnisystem(origem)
    else:
      self.origemFarmbox(origem, detalhe)

  
  def origemUnisystem(self,origem):
    self.headline_origem.text = 'Origem: UNISYSTEM'
    self.column_panel_farmbox.visible = False
    self.date_picker_data_mvto.date = origem['data_mvto']
    self.text_box_deposito.text = origem['deposito']
    self.text_box_destino.text = origem['destino']
    self.text_box_nr_documento.text = origem['nr_documento']
    self.text_box_item.text = origem['item']
    self.text_box_desc_item.text = origem['descricao_produto']
    self.text_box_quantidade.text = origem['quantidade']
    self.text_box_modulo.text = origem['modulo']
    # self.repeating_panel_detalhe.items = detalhe['input_movimentations']
    
  def origemFarmbox(self,origem, detalhe):
    self.headline_origem.text = 'Origem: FARMBOX'
    self.column_panel_unisystem.visible = False
    self.date_picker_created_at.date = origem['created_at']
    self.date_picker_closed_date.date = origem['closed_date']
    self.date_picker_updated_at.date = origem['updated_at']
    self.text_box_code.text = origem['code']
    self.text_box_id.text = origem['id']
    self.text_box_status.text = origem['status']
    self.repeating_panel_detalhe.items = detalhe['input_movimentations']

 

  