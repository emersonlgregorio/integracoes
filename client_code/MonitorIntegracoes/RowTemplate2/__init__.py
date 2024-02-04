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
      self.card_1.background = "#C8E6C9"
    elif self.item['status'] == 'I':
      self.card_1.background = "#FFF9C4"
    elif self.item['status'] == 'E':
      self.card_1.background = "#FFCDD2"

    self.label_3.width = 30
    self.text_box_4.width = 10
    self.label_4.width = 30
    self.text_box_5.width = 10
    
