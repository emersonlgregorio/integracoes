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
def get_integracoes(filtro = "where status = 'O'"):
    query = f"""
                SELECT 
                	ai.SEQ_PLANILHA,
                	ai.rota,
                	ai.operacao,
                	ai.TIPO_ENTRADA,
                	ai.OUTROS_DADOS,
                	to_date(to_char(ai.data_criacao,'DD-MM-YYYY HH24:MI:SS'),'DD-MM-YYYY HH24:MI:SS') data_criacao,
                	to_date(to_char(ai.DATAHORA_INTEGRACAO,'DD-MM-YYYY HH24:MI:SS'),'DD-MM-YYYY HH24:MI:SS') DATAHORA_INTEGRACAO,
                	to_date(to_char(ai.ULTIMA_ALTERACAO,'DD-MM-YYYY HH24:MI:SS'),'DD-MM-YYYY HH24:MI:SS') ULTIMA_ALTERACAO,
                	ai.status,
                	ai.ID_INTEGRACAO,
                  m.FILIAL,
                  nvl(ai.nr_documento, m.NR_DOCUMENTO) nr_documento,
                  ai.nome_form
                FROM  AC_INTEGRACOES ai 
                LEFT JOIN AC_VW_DOCUMENTOS m ON ai.SEQ_PLANILHA = m.SEQ_PLANILHA   
                {filtro} 
          """
    # print(query)
    items = anvil.server.call('oracleSelect',query)
    for i in items:
      if i['filial'] == 17:
        i['filial'] = 4
      elif i['filial'] == 17:
        i['filial'] = 4
      elif i['filial'] == 17:
        i['filial'] = 4
      elif i['filial'] == 17:
        i['filial'] = 4
      elif i['filial'] == 17:
        i['filial'] = 4
      elif i['filial'] == 17:
        i['filial'] = 4
      elif i['filial'] == 17:
        i['filial'] = 4
      
    return items

@anvil.server.callable
def reprocessar(id_integracao):
  query = f"""
          UPDATE AC_INTEGRACOES SET DATAHORA_INTEGRACAO = SYSDATE, status = 'O' 
          WHERE ID_INTEGRACAO = '{id_integracao}'
      """
  anvil.server.call('oracleExecute',query)
