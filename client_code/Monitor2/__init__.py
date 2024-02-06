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

class Monitor2(Monitor2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    self.date_picker_data.format = "%d/%m/%Y"
    self.date_picker_data.date = datetime.date.today()
    self.date_picker_data_change()
    self.set_event_handler('x-refresh', self.date_picker_data_change)
    self.drop_down_status.items = [
      ("Erros", "E"),
      ("Novos", "O"),
      ("Processando", "I"),
      ("Sucessos", "C")
    ]
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
    
  

  def search2(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.text_box_search.text = ""  
    f1 = self.date_picker_data.date.strftime("%d/%m/%Y")
    dtInicial = f1+" 00:00:00"
    dtFinal = f1+" 23:59:59"
    rota = self.drop_down_rota.selected_value
    status = self.drop_down_status.selected_value
    unidade = self.drop_down_unidade.selected_value

    if f1 and f4 and f5 and f6:
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{f2}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{f3}', 'DD-MM-YYYY HH24:MI:SS')
                    AND ROTA = '{f4}' AND STATUS = '{f5}' AND m.filial = '{f6}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif f1 and f4 and not f5 and not f6:
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{f2}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{f3}', 'DD-MM-YYYY HH24:MI:SS')
                    AND ROTA = '{f4}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif f1 and not f4 and not f5 and not f6:
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{f2}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{f3}', 'DD-MM-YYYY HH24:MI:SS')
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif f1 and not f4 and f5:
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{f2}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{f3}', 'DD-MM-YYYY HH24:MI:SS')
                    AND STATUS = '{f5}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not f1 and not f4 and not f5:
      Notification('Informe pelo menos 1 filtro (data, rota ou status)')
      self.contadores(self.repeating_panel_1.items)
    elif not f1 and f4 and not f5:
      filtro = f"""where rota = {f4}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not f1 and not f4 and f5:
      filtro = f"""where status = {f5}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not f1 and f4 and f5:
      filtro = f"""where status = {f5} and rota = {f4}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    
  def search(self, **event_args):
    self.repeating_panel_1.items = anvil.server.call('get_seqPlanilha', self.text_box_search.text)

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