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

    # Any code you write here will run before the form opens.

  def getItemsSap(self, seqPlanilha, **properties):
    filtro = f"""
                AND am."U_RSD_IDUnisystem" = '{seqPlanilha}'
              """
    print(filtro)
    dados = anvil.server.call('movimentosSap', filtro)
    self.headline_sap.text = self.headline_sap.text+f' - Documentos econtratos {len(dados)}'
    self.repeating_panel_sap.items = dados

  def getItemIntegracao(self, seqPlanilha, **properties):
    filtro = f"""
        WHERE SEQ_PLANILHA = '{seqPlanilha}' 
    """
    dados = anvil.server.call('integracoes', filtro)
    self.headline_3.text = self.headline_3.text + f' - Documentos econtratos {len(dados)}'
    self.repeating_panel_integracoes.items = dados