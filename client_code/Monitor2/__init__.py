from ._anvil_designer import Monitor2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime
from tabulator.Tabulator import Tabulator
from tabulator.Tabulator import row_selection_column

Tabulator.modules.remove("FrozenColumns")
Tabulator.default_options["selectable"] = True
Tabulator.theme = "midnight"
Tabulator.theme = "standard"
Tabulator.theme = "simple"
Tabulator.theme = "modern"
Tabulator.theme = "bootstrap3"

class Monitor2(Monitor2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
  
    self.card_1.visible = False
    self.drop_down_unidade.items = [
      ("Colorado","3"),
      ("Curupai","5"),
      ("Arm.Germ.BRA","11"),
      ("Germ. Sementes","7"),
      ("Arm.Germ.TGA","8"),
      ("Querência","1"),
      ("Que.Emp.TGA","9"),
      ("Que.Emp.CJO","10"),
      ("Promissão","2"),
      ("São Carlos","4"),
    ]
  
  def search(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    dtInicial = self.date_picker_data.date.strftime("%d/%m/%Y") 
    dtFinal = self.date_picker_final.date.strftime("%d/%m/%Y")
    
    if not dtInicial or not dtInicial:
      alert("O período é obrigatório!! Por favor, selecione a Data Inicial e Data Final.")
    else:
      dtInicial = dtInicial+" 00:00:00" 
      dtFinal = dtFinal+" 23:59:59" 
      orderby = "order by data_criacao desc"
      filtro = f"""
                  where (ai.DATA_CRIACAO >= to_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS')
                        or to_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') is null 
                        or to_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') = '')
                    and (ai.DATA_CRIACAO <= to_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS')
                        or to_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS') is null 
                        or to_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS') = '')
                    {orderby}
                """
      self.tabulator.data = anvil.server.call('get_integracoes', filtro)
      self.tabulator. = True
      # self.contadores(self.repeating_panel_1.items)
      self.card_1.visible = True

  def date_picker_data_change(self, **event_args):
    """This method is called when the selected date changes"""
    hoje = self.date_picker_data.date.strftime("%d/%m/%Y")
    self.repeating_panel_1.items = anvil.server.call('get_hoje',hoje)
    self.data_grid_1.border = "1px solid #888888"
    self.contadores(self.repeating_panel_1.items)
    
  def contadores(self, items):
    sucessos = 0
    erros = 0
    process = 0
    novos = 0
    for i in items:
      if i['status'] == 'C':
        sucessos += 1
      elif i['status'] == 'E':
        erros += 1
      elif i['status'] == 'I':
        process += 1
      else:
        novos += 1
    self.label_1.text = f'Sucessos: {sucessos}'
    self.label_2.text = f'Erros: {erros}'
    self.label_3.text = f'Processando: {process}'
    self.label_4.text = f'Novos: {novos}'