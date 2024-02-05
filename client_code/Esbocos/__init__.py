from ._anvil_designer import EsbocosTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Esbocos(EsbocosTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.width = '200px'

    # Any code you write here will run before the form opens.

  def main_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Main')

  def monitor_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Monitor')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.drop_down_unidade.selected_value and not self.text_box_nfe.text:
      alert("Preencha um filtro")
    elif self.drop_down_unidade.selected_value and self.text_box_nfe.text:
      filtro = f"""
                WHERE o."BPLId" = {self.drop_down_unidade.selected_value}
                and o."Serial" = {self.text_box_nfe.text}
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
    elif not self.drop_down_unidade.selected_value and self.text_box_nfe.text:
      filtro = f"""
                WHERE o."Serial" = {self.text_box_nfe.text}
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
    elif self.drop_down_unidade.selected_value and not self.text_box_nfe.text:
      filtro = f"""
                WHERE o."BPLId" = {self.drop_down_unidade.selected_value}
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
