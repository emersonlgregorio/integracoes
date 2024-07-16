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
    dataInicial = self.date_picker_dataInicial.date 
    dataInicial = dataInicial if dataInicial != None else ''
    dataFinal = self.date_picker_dataFinal.date 
    dataFinal = dataFinal if dataFinal != None else ''
    
    if dataInicial != '' and dataFinal != '':
      print(dataInicial)
      print(dataFinal)
      dataInicial = dataInicial.strftime("%d/%m/%Y")
      dtInicial = dataInicial+" 00:00:00" if dataInicial != None else ''
      dataFinal = dataFinal.strftime("%d/%m/%Y")
      dtFinal = dataFinal+" 23:59:59" if dataFinal != None else ''
      orderby = "order by data_criacao desc"
    else:
      # data = ''
      dtInicial = ''
      dtFinal = ''
      orderby = "order by seq_planilha"
      
    rota = self.drop_down_rota.selected_value
    rota = rota if rota != None else ''
    
    status = self.drop_down_status.selected_value
    status = status if status != None else ''
    
    unidade = self.drop_down_unidade.selected_value
    unidade = unidade if unidade != None else ''
    
    seqPlanilha = self.text_box_search.text
    seqPlanilha = seqPlanilha if seqPlanilha != None else ''
    
    if dtInicial or dtFinal: #Verifica se todos os filtros estão selecionados
      filtro = f"""
                  where 
                        sistema <> 2
                    and (ai.DATA_CRIACAO >= to_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS')
                        or to_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') is null 
                        or to_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS') = '')
                    and (ai.DATA_CRIACAO <= to_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS')
                        or to_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS') is null 
                        or to_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS') = '')
                    AND (rota = '{rota}' or '{rota}' is null or '{rota}' = '')
                    AND (status = '{status}' or '{status}' is null or '{status}' = '')
                    AND (m.filial = '{unidade}' or '{unidade}' is null or '{unidade}' = '')
                    AND ((ai.seq_planilha = '{seqPlanilha}' or '{seqPlanilha}' is null or '{seqPlanilha}' = '') or
                         (ai.nr_documento = '{seqPlanilha}' or '{seqPlanilha}' is null or '{seqPlanilha}' = ''))
                    {orderby}
                """
      print(filtro)
      self.repeating_panel_1.items = anvil.server.call('get_integracoes', filtro)
      self.contadores(self.repeating_panel_1.items)
    else:
      alert("Data Inicial e Final são obrigatórios!")
      
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

  def enableFields(self, **event_args):
    print('Data Inicial:', self.date_picker_dataInicial.date)
    print('Data Final:', self.date_picker_dataFinal.date)
    
    if self.date_picker_dataInicial.date and self.date_picker_dataFinal.date:
      self.drop_down_rota.enabled = True
      self.drop_down_status.enabled = True
      self.drop_down_unidade.enabled = True
      self.text_box_search.enabled = True
    else: 
      self.drop_down_rota.enabled = False
      self.drop_down_status.enabled = False
      self.drop_down_unidade.enabled = False
      self.text_box_search.enabled = False