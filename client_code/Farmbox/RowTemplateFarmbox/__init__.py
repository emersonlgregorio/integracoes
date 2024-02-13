from ._anvil_designer import RowTemplateFarmboxTemplate
from ._anvil_designer import RowTemplateFarmbox
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ModalConf import ModalConf

class RowTemplateFarmbox(RowTemplateFarmbox):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # # Any code you write here will run before the form opens.
    # if self.item['qtde_origem'] == self.item['qtde_destino'] and self.item['deposito_origem'] == self.item['deposito_destino']:
    #   # self.button_reprocessar.visible = False
    #   self.background = "#C8E6C9"
    # else:
    #   if self.item['qtde_origem'] == self.item['qtde_destino']:
    #     self.label_qtde_origem.background = "#C8E6C9"
    #     self.label_qtde_destino.background = "#C8E6C9"
    #   else:
    #     self.label_qtde_origem.background = "#FFF9C4"
    #     self.label_qtde_destino.background = "#FFF9C4"

    #   if self.item['deposito_origem'] == self.item['deposito_destino']:
    #     self.label_dep_origem.background = "#C8E6C9"
    #     self.label_dep_destino.background = "#C8E6C9"
    #   else:
    #     self.label_dep_origem.background = "#FFF9C4"
    #     self.label_dep_destino.background = "#FFF9C4"

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    modal = ModalConf(item=self.item)
    alert(modal, large=True, role= 'wide-alert-20vw',title="Dados da Integração", buttons=[("OK","ok")] )
