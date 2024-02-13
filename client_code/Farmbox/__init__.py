from ._anvil_designer import FarmboxTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime


class Farmbox(FarmboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.date_picker_data.format = "%d/%m/%Y"
    # self.date_picker_data.date = datetime.date.today()
    # if not self.date_picker_data.date and not self.drop_down_deposito.selected_value:
    #   self.flow_panel_2.visible = False
    #   self.xy_panel_1.visible = False

    # Any code you write here will run before the form opens.
  def search(self, **event_args):
    data = str(self.date_picker_data.date)
    status = self.drop_down_status.selected_value
    status = status if status != None else ''
    
    if data == 'None':
      dataInicial = ''
      dataFinal = ''
    else:
      dataInicial = data+' 00:00:00'
      dataFinal = data+' 23:59:59'
      
      
    ap = self.text_box_ap.text
    ap = ap if ap != None else ''
    
    filtro = f"""
        where (ultima_alteracao >= to_date('{dataInicial}','YYYY/MM/DD HH24:MI:SS')
          or to_date('{dataInicial}','YYYY/MM/DD HH24:MI:SS') is null
          or to_date('{dataInicial}','YYYY/MM/DD HH24:MI:SS') = '')
          and
          (ultima_alteracao <= to_date('{dataFinal}','YYYY/MM/DD HH24:MI:SS')
          or to_date('{dataFinal}','YYYY/MM/DD HH24:MI:SS') is null
          or to_date('{dataFinal}','YYYY/MM/DD HH24:MI:SS') = '')
          and
          (numero = '{ap}' or '{ap}' is null or '{ap}' = '')
          and 
          (status = '{status}' or '{status}' is null or '{status}' = '')
    """
    print(filtro)
    retorno = anvil.server.call('movFarmbox', filtro)
    # print(retorno)
    self.repeating_panel_1.items = retorno
    self.flow_panel_2.visible = True
    self.xy_panel_1.visible = True
