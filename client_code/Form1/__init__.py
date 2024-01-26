from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form() 
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

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = anvil.server.call('get_hoje')

  def text_box_search_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.repeating_panel_1.items = anvil.server.call('get_seqPlanilha', self.text_box_search.text)

  def button_search_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = anvil.server.call('get_seqPlanilha', self.text_box_search.text)
