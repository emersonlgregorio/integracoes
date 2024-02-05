from ._anvil_designer import MonitorTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import datetime

class Monitor(MonitorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.width = '200px'
    anvil.users.login_with_form()
    self.date_picker_2.format = "%d/%m/%Y"
    self.date_picker_2.date = datetime.date.today()
    self.repeating_panel_1.items = anvil.server.call('get_hoje')
    self.data_grid_1.border = "1px solid #888888"
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

  def button_hoje_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = anvil.server.call('get_hoje')
    self.data_grid_1.border = "1px solid #888888"

  def search(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.repeating_panel_1.items = anvil.server.call('get_seqPlanilha', self.text_box_search.text)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('MonitorIntegracoes')

  def main_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Main')

  def esbocos_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Esbocos')


