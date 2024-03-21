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
                	ai.SEQ_PLANILHA "SeqPlanilha",
                	ai.rota "Rota",
                	ai.operacao "Operacao",
                	ai.TIPO_ENTRADA "TP",
                	ai.OUTROS_DADOS "Mensagem",
                	--to_date(TO_CHAR(ai.DATA_CRIACAO, "DD-MM-YYYY HH24:MI:SS"), "DD-MM-YYYY HH24:MI:SS") "DataCriacao",
                	--to_char(to_date(to_char(ai.data_criacao,'DD-MM-YYYY HH24:MI:SS'),'DD/MM/YYYY HH24:MI:SS')) "DataCriacao",
                  ai.data_criacao "DataCriacao",
                	--to_date(to_char(ai.DATAHORA_INTEGRACAO,'DD-MM-YYYY HH24:MI:SS'),'DD-MM-YYYY HH24:MI:SS') "DataHoraIntegracao",
                  ai.DATAHORA_INTEGRACAO "DataHoraIntegracao",
                	--to_date(to_char(ai.ULTIMA_ALTERACAO,'DD-MM-YYYY HH24:MI:SS'),'DD-MM-YYYY HH24:MI:SS') "UltimaAlteracao",
                  ai.ULTIMA_ALTERACAO "UltimaAlteracao",
                	ai.status "Status",
                	ai.ID_INTEGRACAO "IdIntegracao",
                    decode(nvl(ai.cod_filial,0),0,m.FILIAL,ai.cod_filial) "Filial",
                   nvl(ai.nr_documento, m.NR_DOCUMENTO) "NrDocumento",
                   ai.nome_form "NomeForm"
                FROM  AC_INTEGRACOES ai 
                LEFT JOIN AC_VW_PROD_MOVIMENTOS m ON ai.SEQ_PLANILHA = m.SEQ_PLANILHA     
                {filtro} 
          """
    items = anvil.server.call('oracleSelect',query)
    return items

@anvil.server.callable
def reprocessar(id_integracao):
  query = f"""
          UPDATE AC_INTEGRACOES SET DATAHORA_INTEGRACAO = SYSDATE, status = 'O' 
          WHERE ID_INTEGRACAO = '{id_integracao}'
      """
  anvil.server.call('oracleExecute',query)
