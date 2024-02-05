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
from ..Esbocos import Esbocos

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    self.image_1.width = '205px'

  def switch_to_home(self, **event_args):
      """Switch to the Gallery view."""
      self.content_panel.clear()
      self.headline_1.scroll_into_view()
      self.home_link.role = 'selected'
  
  def switch_to_monitor(self, **event_args):
    """Switch to the Gallery view."""
    self.content_panel.clear()
    self.content_panel.add_component(Monitor2(), full_width_row=True)
    self.headline_1.scroll_into_view()
    self.deselect_all_links()
    self.monitor_link.role = 'selected'

  def switch_to_esbocos(self, **event_args):
    """Switch to the Gallery view."""
    self.content_panel.clear()
    self.content_panel.add_component(Esbocos(), full_width_row=True)
    self.headline_1.scroll_into_view()
    self.deselect_all_links()
    self.esboco_link.role = 'selected'

  def deselect_all_links(self):
    """Reset all the roles on the navbar links."""
    for link in self.home_link, self.monitor_link, self.esboco_link:
      link.role = ''

