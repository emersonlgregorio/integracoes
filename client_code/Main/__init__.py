from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    self.image_1.width = '205px'
    
  # Any code you write here will run before the form opens.

  def monitor_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Monitor')

  def esboco_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Esbocos')
