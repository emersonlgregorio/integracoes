from ._anvil_designer import MonitorIntegracoesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MonitorIntegracoes(MonitorIntegracoesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = anvil.server.call('get_hoje')
    
