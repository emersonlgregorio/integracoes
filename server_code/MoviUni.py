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
              0.SEQ_PLA_NOTA SEQ_PLANILHA,
              0.NR_DOCUMENTO,
              0.FORM_LANCAMENTO MODULO,
              0.DATA_EMISSAO DATA_MVTO,
              1.ITEM,
              1.DESC_PRODUTO DESCRICAO_PRODUTO,
              1.QUANTIDADE,
              1.DEPOSITO,
              1.DESTINO
            FROM AC_VW_NF_SAIDAS T0
            INNER JOIN AC_VW_NF_SAI_ITENS T1 ON t0.SEQ_PLA_NOTA = t1.SEQ_PLA_NOTA
            WHERE t0.SEQ_PLA_NOTA = '{filtro}'
            UNION 
            SELECT 
              0.SEQ_PLA_NOTA SEQ_PLANILHA,
              0.NR_DOCUMENTO,
              0.FORM_LANCAMENTO MODULO,
              0.DATA_EMISSAO DATA_MVTO,
              1.ITEM,
              1.DESC_PRODUTO DESCRICAO_PRODUTO,
              1.QUANTIDADE,
              1.DEPOSITO,
              ULL DESTINO
            FROM AC_VW_NF_ENTRADAS T0
            INNER JOIN AC_VW_NF_ENT_ITENS T1 ON t0.SEQ_PLA_NOTA = t1.SEQ_PLA_NOTA
            WHERE t0.SEQ_PLA_NOTA = '{filtro}'
  """

  origem = anvil.server.call('oracleSelect',query)

  return origem

