from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    if self.item['status'] == 'C':
      self.card_1.background = "#7FFFD4"
    elif self.item['status'] == 'I':
      self.card_1.background = "#FFFFE0"
    elif self.item['status'] == 'E':
      self.card_1.background = "#FF6347"
