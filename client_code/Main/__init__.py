from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Monitor2 import Monitor2
from ..Esbocos2 import Esbocos2
from ..Conferencia import Conferencia

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()

  def switch_to_home(self, **event_args):
      """Switch to the Gallery view."""
      self.content_panel.clear()
      self.headline_main.text = 'CRESTANI'
      self.deselect_all_links()
      self.link_home.role = 'selected'
  
  def switch_to_monitor(self, **event_args):
    """Switch to the Gallery view."""
    self.content_panel.clear()
    self.content_panel.add_component(Monitor2(), full_width_row=True)

    self.headline_main.text = 'Monitor de Integrações'
    self.deselect_all_links()
    self.monitor_link.role = 'selected'

  def switch_to_esbocos(self, **event_args):
    """Switch to the Gallery view."""
    self.content_panel.clear()
    self.content_panel.add_component(Esbocos2(), full_width_row=True)
    self.headline_main.text = 'Documentos em Esboço no SAP'
    self.deselect_all_links()
    self.esboco_link.role = 'selected'

  def switch_to_conferencia(self, **event_args):
    """Switch to the Gallery view."""
    self.content_panel.clear()
    self.content_panel.add_component(Conferencia(), full_width_row=True)
    self.headline_main.text = 'Conferência'
    self.deselect_all_links()
    self.conferencia_link.role = 'selected'

  def deselect_all_links(self):
    """Reset all the roles on the navbar links."""
    for link in self.link_home, self.monitor_link, self.esboco_link:
      link.role = ''

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('send_email_with_pdf')

