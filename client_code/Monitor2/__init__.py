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
    data = self.date_picker_data.date.strftime("%d/%m/%Y")
    dtInicial = data+" 00:00:00"
    dtFinal = data+" 23:59:59"
    rota = self.drop_down_rota.selected_value
    status = self.drop_down_status.selected_value
    unidade = self.drop_down_unidade.selected_value

    if data and rota and status and unidade: #Verifica se todos os filtros estão selecionados
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS')
                    AND ROTA = '{rota}' AND STATUS = '{status}' AND m.filial = '{unidade}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif data and rota and not status and not unidade: #verifica se DATA e ROTA estão selecionados
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS')
                    AND ROTA = '{rota}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif data and not rota and not status and not unidade: #verifica se só Data está selecionada
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS')
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif data and not rota and status and not unidade: #verifica se DATA  e STATUS estão selecionados.
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS')
                    AND STATUS = '{status}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif data and not rota and not status and unidade: #verifica se DATA  e UNIDADE estão selecionados.
      filtro = f"""
                  where DATA_CRIACAO >= TO_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') 
                    AND DATA_CRIACAO <= TO_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS')
                    AND filial = '{unidade}'
                """
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not data and not rota and not status and not unidade:
      Notification('Informe pelo menos 1 filtro (data, rota ou status)')
      self.contadores(self.repeating_panel_1.items)
    elif not data and rota and not status and not unidade:
      filtro = f"""where rota = {rota}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not data and not rota and status and not unidade:
      filtro = f"""where status = {status}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not data and not rota and not status and unidade:
      filtro = f"""where filial = {unidade}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not data and rota and status and not unidade:
      filtro = f"""where status = {status} and rota = {rota}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not data and rota and not status and unidade:
      filtro = f"""where filial = {unidade} and rota = {rota}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not data and not rota and status and unidade:
      filtro = f"""where status = {status} and filial = {unidade}"""
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    elif not data and rota and status and unidade:
      filtro = f"""where status = {status} and filial = {unidade} and rota = {rota}"""
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