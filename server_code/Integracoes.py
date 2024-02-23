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
    print("Alterado as 19h")
    query = f"""
                SELECT 
                	ai.SEQ_PLANILHA,
                	ai.rota,
                	ai.operacao,
                	ai.TIPO_ENTRADA,
                	ai.OUTROS_DADOS,
                	--to_date(TO_CHAR(ai.DATA_CRIACAO, 'DD-MM-YYYY HH24:MI:SS'), 'DD-MM-YYYY HH24:MI:SS') data_criacao,
                	ai.data_criacao,
                	ai.DATAHORA_INTEGRACAO,
                	ai.ULTIMA_ALTERACAO,
                	ai.status,
                	ai.ID_INTEGRACAO,
                    decode(nvl(ai.cod_filial,0),0,m.FILIAL,ai.cod_filial) filial,
                   nvl(ai.nr_documento, m.NR_DOCUMENTO) nr_documento,
                   ai.nome_form
                FROM  AC_INTEGRACOES ai 
                LEFT JOIN AC_VW_PROD_MOVIMENTOS m ON ai.SEQ_PLANILHA = m.SEQ_PLANILHA   
                {filtro} 
            """
    #print(query)
    items = anvil.server.call('oracleSelect',query)
    #print(items)
    return items

@anvil.server.callable
def reprocessar(id_integracao):
    query = f"""
            UPDATE AC_INTEGRACOES SET DATAHORA_INTEGRACAO = SYSDATE, status = 'O' 
            WHERE ID_INTEGRACAO = '{id_integracao}'
    """
    anvil.server.call('oracleExecute',query)
