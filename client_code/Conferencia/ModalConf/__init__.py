from ._anvil_designer import ModalConfTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ModalConf(ModalConfTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def getItemsSap(self, **properties):
    seq_planilha
    filtro = f"""
                where i."DocEntry" = {docentry}
	              AND i."ObjType" = '{objtype}'
              """
    dados = anvil.server.call('get_drafts_items', filtro)