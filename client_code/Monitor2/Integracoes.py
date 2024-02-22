import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from my_calsses import Oracle
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .Monitor2 import Module1
#
#    Module1.say_hello()
#

oracle = Oracle()

@anvil.server.callable
def get_integracoes(filtro = "where status = 'O'"):
    print("Debug")
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
    items = oracle.selectDb(query)
    #print(items)
    return [
        {
            "seqPlanilha": item[0],
            "rota": item[1],
            "operacao": item[2],
            "tipoEntrada": item[3],
            "mensagem": item[4],
            "criacao": item[5],
            "integracao": item[6],
            "alteracao": item[7],
            "status": item[8],
            "id_integracao": item[9],
            "filial": item[10],
            "documento": item[11],
            "nome_form": item[12]
        } for item in items
    ]

@anvil.server.callable
def reprocessar(id_integracao):
    query = f"""
            UPDATE AC_INTEGRACOES SET DATAHORA_INTEGRACAO = SYSDATE, status = 'O' 
            WHERE ID_INTEGRACAO = '{id_integracao}'
    """
    oracle.executeDB(query)
