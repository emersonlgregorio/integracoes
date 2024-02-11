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
    print(seqPlanilha)
    self.getItemsSap(seqPlanilha)

    # Any code you write here will run before the form opens.

  def getItemsSap(self, seqPlanilha, **properties):
    print(seqPlanilha)
    filtro = f"""
                AND am."U_RSD_IDUnisystem" = '{seqPlanilha}'
              """
    print(filtro)
    dados = anvil.server.call('movimentosSap', filtro)
    print(dados)
    self.repeating_panel_sap.items = dados