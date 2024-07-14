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
              T0.DATA_EMISSAO DATA_MVTO,
              T1.ITEM,
              T1.DESC_PRODUTO DESCRICAO_PRODUTO,
              T1.QUANTIDADE,
              T1.DEPOSITO,
              T1.DESTINO
            FROM AC_VW_NF_SAIDAS T0
            INNER JOIN AC_VW_NF_SAI_ITENS T1 ON t0.SEQ_PLA_NOTA = t1.SEQ_PLA_NOTA
            WHERE t0.SEQ_PLA_NOTA = '{filtro}'
            UNION 
            SELECT 
              T0.SEQ_PLA_NOTA SEQ_PLANILHA,
              T0.NR_DOCUMENTO,
              T0.FORM_LANCAMENTO MODULO,
              T0.DATA_EMISSAO DATA_MVTO,
              T1.ITEM,
              T1.DESC_PRODUTO DESCRICAO_PRODUTO,
              T1.QUANTIDADE,
              T1.DEPOSITO,
              NULL DESTINO
            FROM AC_VW_NF_ENTRADAS T0
            INNER JOIN AC_VW_NF_ENT_ITENS T1 ON t0.SEQ_PLA_NOTA = t1.SEQ_PLA_NOTA
            WHERE t0.SEQ_PLA_NOTA = '{filtro}'
  """
  origem = anvil.server.call('oracleSelect',query)


@anvil.server.callable
def dadosOrigemRomaneio(filtro):
  query = f"""
            SELECT
            	t0.SEQ_PLA_ROMANEIO SEQ_PLANILHA,
            	t0.NR_ROMANEIO NR_DOCUMENTO,
              'RomaneioEntrada' MODULO,
            	t0.DATA_ENTRADA DATA_MVTO,
            	t0.ITEM,
            	t0.DESC_PRODUTO DESCRICAO_PRODUTO,
            	t0.QUANTIDADE,
            	t0.DEPOSITO,
            	NULL DESTINO
            FROM AC_VW_ROMANEIO_ENTRADA t0
            WHERE t0.SEQ_PLA_ROMANEIO = '{filtro}'
  """
  origem = anvil.server.call('oracleSelect',query)



  
  return origem

