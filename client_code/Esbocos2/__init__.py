from ._anvil_designer import Esbocos2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Esbocos2(Esbocos2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_unidade.items = [
      ("Colorado","3"),
      ("Curupai","5"),
      ("Arm.Germ.BRA","11"),
      ("Germ. Sementes","7"),
      ("Arm.Germ.TGA","8"),
      ("Querência","1"),
      ("Que.Emp.TGA","9"),
      ("Que.Emp.CJO","10"),
      ("Promissão","2"),
      ("São Carlos","4"),
    ]
    self.drop_down_status.items = [
      ("Novos", "O"),
      ("Completo", "C")
    ]

  def search(self, **event_args):
    """This method is called when the button is clicked"""
    nroNota = self.text_box_nfe.text
    unidade = self.drop_down_unidade.selected_value
    status = self.drop_down_status.selected_value

    if not unidade and not nroNota and not status:
      alert("Preencha um filtro")
    elif unidade and nroNota and status:
      filtro = f"""
                WHERE o."BPLId" = {unidade}
                and o."Serial" = {nroNota}
                and o."DocStatus" = '{status}'
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
    elif unidade and nroNota and not status:
      filtro = f"""
                WHERE o."BPLId" = {unidade}
                and o."Serial" = {nroNota}
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
    elif unidade and not nroNota and status:
      filtro = f"""
                WHERE o."BPLId" = {unidade}
                and o."DocStatus" = '{status}'
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
    elif not unidade and nroNota and status:
      filtro = f"""
                WHERE o."DocStatus" = '{status}'
                and o."Serial" = {nroNota}
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
    elif not unidade and nroNota and not status:
      filtro = f"""
                WHERE o."Serial" = {nroNota}
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
    elif unidade and not nroNota and not status:
      filtro = f"""
                WHERE o."BPLId" = {unidade}
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)
    elif not unidade and not nroNota and status:
      filtro = f"""
                WHERE o."DocStatus" = '{status}'
              """
      self.repeating_panel_1.items = anvil.server.call('get_drafts', filtro)



