import anvil.email
import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def dadosOrigem(filtro):
  query = f"""
      SELECT
          m.SEQ_PLANILHA,
          m.NR_DOCUMENTO, 
          m.MODULO,
          m.DATA_MVTO,
          m.ITEM,
          p.DESCRICAO_PRODUTO,
          m.QUANTIDADE,
          m.DEPOSITO,
          m.DESTINO
      FROM AC_VW_PROD_MOVIMENTOS m 
      INNER JOIN produtos p ON m.SEQ_PLA_PRODUTO = p.SEQ_PLA_PRODUTO  
      {filtro}
  """

  items = anvil.server.call('oracleSelect',query)

  return [
      {
          "seq_planilha": item[0],
          "nr_documento": item[1],
          "modulo": item[2],
          "data_mvto": item[3].strftime("%d/%m/%Y %H:%M"),
          "item": item[4],
          "descricao_item": item[5],
          "qtde": item[6],
          "deposito": item[7],
          "destino": item[8]
      } for item in items
  ]

