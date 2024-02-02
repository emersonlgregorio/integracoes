from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if self.item['status'] == 'C':
      self.button_reprocessar.visible = False
    

    # Any code you write here will run before the form opens.

  def button_reprocessar_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('reprocessar', self.item['id_integracao'])

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert(content=f"{self.item['rota']}",
         title='Dados da Integração',
         large=True
         )
    

