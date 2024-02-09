from ._anvil_designer import ConferenciaTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

class Conferencia(ConferenciaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.date_picker_data.format = "%d/%m/%Y"
    # self.date_picker_data.date = datetime.date.today()
    if not self.date_picker_data.date and not self.drop_down_deposito.selected_value:
      self.flow_panel_2.visible = False

    # Any code you write here will run before the form opens.
  def search(self, **event_args):
    data = self.date_picker_data.date
    data = data if data != None else ''
    deposito = self.drop_down_deposito.selected_value
    deposito = deposito if deposito != None else ''
    filtro = f"""
        where (DATA_MOV_ORIGEM = to_date('{data}','YYYY/MM/DD HH24:MI:SS') 
          or to_date('{data}','YYYY/MM/DD HH24:MI:SS') is null 
          or to_date('{data}','YYYY/MM/DD HH24:MI:SS') = '')
          and
          (DEPOSITO_ORIGEM = '{deposito}' or '{deposito}' is null or '{deposito}' = '')
    """
    print(filtro)
    self.repeating_panel_1.items = anvil.server.call('movimentacoes', filtro)
  
  