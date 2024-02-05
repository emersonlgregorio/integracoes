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
  def switch_to_monitor(self, **event_args):
    """Switch to the Gallery view."""
    self.column_panel_body.clear()
    self.column_panel_body.add_component(open_form('Monitor'))
    self.headline_made_with_anvil.scroll_into_view()
    self.deselect_all_links()
    self.link_gallery.role = 'selected'

  def deselect_all_links(self):
    """Reset all the roles on the navbar links."""
    for link in self.home_link, self.monitor_link:
      link.role = ''
 

  # def monitor_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   open_form('Monitor')

  # def esboco_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   open_form('Esbocos')
