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
            	T0.SEQ_PLA_NOTA SEQ_PLANILHA,
            	T0.NR_DOCUMENTO,
            	T0.FORM_LANCAMENTO MODULO,
            	T0.DATA_EMISSAO DATA_MVTO
            FROM AC_VW_NF_SAIDAS T0
            WHERE t0.SEQ_PLA_NOTA = '{filtro}'
            UNION 
            SELECT 
            	T0.SEQ_PLA_NOTA SEQ_PLANILHA,
            	T0.NR_DOCUMENTO,
            	T0.FORM_LANCAMENTO MODULO,
            	T0.DATA_EMISSAO DATA_MVTO
            FROM AC_VW_NF_ENTRADAS T0
            WHERE t0.SEQ_PLA_NOTA = '{filtro}'
  """
  queryDetalhe = f"""
            SELECT
            	T1.ITEM,
            	T1.DESC_PRODUTO DESCRICAO_PRODUTO,
            	T1.QUANTIDADE,
            	T1.DEPOSITO,
            	T1.DESTINO
            FROM AC_VW_NF_SAI_ITENS T1
            WHERE t1.SEQ_PLA_NOTA = '{filtro}'
            UNION 
            SELECT 
            	T1.ITEM,
            	T1.DESC_PRODUTO DESCRICAO_PRODUTO,
            	T1.QUANTIDADE,
            	T1.DEPOSITO,
            	NULL DESTINO
            FROM AC_VW_NF_ENT_ITENS T1
            WHERE t1.SEQ_PLA_NOTA = '{filtro}'
  """
  origem = anvil.server.call('oracleSelect',query)
  detalhe = anvil.server.call('oracleSelect',queryDetalhe)

  return origem, detalhe

