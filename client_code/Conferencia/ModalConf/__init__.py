from ._anvil_designer import ModalConfTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ModalConf(ModalConfTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    seqPlanilha = self.item['id_origem']
    self.getItemsSap(seqPlanilha)
    self.getItemIntegracao(seqPlanilha)
    self.getItemOrigem(seqPlanilha)

    # Any code you write here will run before the form opens.

  def getItemsSap(self, seqPlanilha, **properties):
    filtro = f"""
                AND am."U_RSD_IDUnisystem" = '{seqPlanilha}'
              """
    # print(filtro)
    dados = anvil.server.call('movimentosSap', filtro)
    self.headline_sap.text = self.headline_sap.text+f' - Documentos econtrados {len(dados)}'
    self.repeating_panel_sap.items = dados

  def getItemIntegracao(self, seqPlanilha, **properties):
    filtro = f"""
        WHERE SEQ_PLANILHA = '{seqPlanilha}' 
    """
    dados = anvil.server.call('integracoes', filtro)
    self.headline_3.text = self.headline_3.text + f' - Documentos econtrados {len(dados)}'
    self.repeating_panel_integracoes.items = dados

  def getItemOrigem(self,seqPlanilha, **properties):
    filtro = f"""
            WHERE m.SEQ_PLANILHA = '{seqPlanilha}'
          """
    origem = anvil.server.call('dadosOrigem', filtro)
    origem = origem[0]
    # print(origem['seq_planilha'])
    self.text_box_seqPlanilha.text = str(origem['seq_planilha'])
    self.text_box_nrDocumento.text = origem['nr_documento']
    self.text_box_tipo.text = origem['modulo']
    self.date_picker_data.date = origem['data_mvto']
    self.text_box_item.text = str(origem['item']) + ' ' + origem['descricao_item']
    self.text_box_qtde.text = origem['qtde']
    self.text_box_deposito.text = origem['deposito']
    self.text_box_destino.text = origem['destino']

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    querySap = f"""
        
    """

    user = anvil.users.get_user()
    
    queryUni = f"""
        update ac_conf_movimentos
        set 
          data_conferencia = sysdate,
          usuario_conferencia = '{user['email']}',
          obs_conferencia = '{self.text_area_obs.text}'
        where id = '{self.item['id']}'
    """
    anvil.server.call('executeOracle', queryUni)
