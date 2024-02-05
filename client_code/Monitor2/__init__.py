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
    # self.contadores(self.repeating_panel_1.items)
    # hoje = self.date_picker_2.date.strftime("%d/%m/%Y")
    # self.repeating_panel_1.items = anvil.server.call('get_hoje',hoje)
    # self.data_grid_1.border = "1px solid #888888"
    # Any code you write here will run before the form opens.
      
  def button_error_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = anvil.server.call('get_integracoes_erros')

  def button_process_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = anvil.server.call('get_integracoes_processamento')

  def button_success_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = anvil.server.call('get_integracoes_success')

  def button_all_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = anvil.server.call('get_integracoes_all')

  def search2(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.text_box_search.text = ""  
    f1 = self.date_picker_data.date.strftime("%d/%m/%Y")
    f2 = f1+" 00:00:00"
    f3 = f1+" 23:59:59"
    f4 = self.drop_down_rota.selected_value
    f5 = self.drop_down_status.selected_value

    if f1 and f4 and f5:
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{f2}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{f3}', 'DD-MM-YYYY HH24:MI:SS')
                    AND ROTA = '{f4}' AND STATUS = '{f5}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
    elif f1 and f4 and not f5:
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{f2}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{f3}', 'DD-MM-YYYY HH24:MI:SS')
                    AND ROTA = '{f4}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
    elif f1 and not f4 and not f5:
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{f2}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{f3}', 'DD-MM-YYYY HH24:MI:SS')
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
    elif f1 and not f4 and f5:
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{f2}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{f3}', 'DD-MM-YYYY HH24:MI:SS')
                    AND STATUS = '{f5}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
    elif not f1 and not f4 and not f5:
      Notification('Informe pelo menos 1 filtro (data, rota ou status)')
    elif not f1 and f4 and not f5:
      filtro = f"""where rota = {f4}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
    elif not f1 and not f4 and f5:
      filtro = f"""where status = {f5}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
    elif not f1 and f4 and f5:
      filtro = f"""where status = {f5} and rota = {f4}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
    
  def search(self, **event_args):
    self.repeating_panel_1.items = anvil.server.call('get_seqPlanilha', self.text_box_search.text)

  def date_picker_data_change(self, **event_args):
    """This method is called when the selected date changes"""
    hoje = self.date_picker_data.date.strftime("%d/%m/%Y")
    self.repeating_panel_1.items = anvil.server.call('get_hoje',hoje)
    self.data_grid_1.border = "1px solid #888888"
    # self.contadores(self.repeating_panel_1.items)
    
    
  # def contadores(self, items):
  #   for i in items:
  #     sucessos = 0
  #     erros = 0
  #     process = 0
  #     if i['status'] == 'C':
  #       sucesso += 1
  #     elif i['status'] == 'E':
  #       erro += 1
  #     elif i['status'] == 'I':
  #       process += 1
  #   self.label_1.text = f'Sucesso: {sucesso}'
  #   self.label_2.text = f'Erros: {erros}'
  #   self.label_3.text = f'Processando: {process}'