import anvil.email
import anvil.secrets
import anvil.http
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import ujson
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def repFarmbox(idFarmbox, operacao):
  url = "https://crestani.api.integrasky.cloud/GJ9fZFjNbe"
  payload = ujson.dumps({
    "id": idFarmbox,
    "op": operacao
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic Zmxvdy1HSjlmWkZqTmJlQGNyZXN0YW5pOlNlbmhhQDIwMjMj'
  }
  response = anvil.http.request(url=url, method="POST", data=payload, headers=headers)
  return response


@anvil.server.callable
def fetch_data():
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%d/%m/%Y")
    dtInicial = data_atual+" 00:00:00" 
    dtFinal = data_atual+" 23:59:59"
    query = f"""
                SELECT 
                	ai.SEQ_PLANILHA,
                	ai.rota,
                	ai.operacao,
                	ai.OUTROS_DADOS,
                	to_date(to_char(ai.data_criacao,'DD-MM-YYYY HH24:MI:SS'),'DD-MM-YYYY HH24:MI:SS') data_criacao,
                  decode(nvl(ai.cod_filial, 0), 0, m.FILIAL, ai.cod_filial) filial,
                  nvl(ai.nr_documento, m.NR_DOCUMENTO) nr_documento
                FROM  AC_INTEGRACOES ai 
                LEFT JOIN AC_VW_DOCUMENTOS m ON ai.SEQ_PLANILHA = m.SEQ_PLANILHA   
                where 
                    sistema <> 2
                and (ai.DATA_CRIACAO >= to_date('{dtInicial}', 'DD-MM-YYYY HH24:MI:SS'))
                and (ai.DATA_CRIACAO <= to_date('{dtFinal}', 'DD-MM-YYYY HH24:MI:SS'))
                and status = 'E'
          """
    # print(query)
    rows = anvil.server.call('oracleSelect',query)
    return rows
  

# @anvil.server.callable
# def generate_pdf(data):
#     pdf_content = "<h1>Relatório de erros de integração</h1>"
#     pdf_content += "<table border='1'>"
#     pdf_content += "<tr><th>Seq Planilha</th><th>Rota</th><th>Data</th><th>Documento</th><th>Mensagem</th></tr>"

#     for item in data:
#         pdf_content += f"<tr><td>{item['seq_planilha']}</td><td>{item['rota']}</td><td>{item['Data']}</td><td>{item['Documento']}</td><td>{item['Mensagem']}</td></tr>"

#     pdf_content += "</table>"

#     pdf = anvil.pdf.render_form(pdf_content)
#     return pdf

# Função para gerar o PDF
@anvil.server.callable
def generate_pdf(data):
    pdf_content = """
    <html>
    <head>
        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 8px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <h1>Relatório Diário</h1>
        <table>
            <tr>
                <th>Seq Planilha</th>
                <th>Rota</th>
                <th>Data</th>
                <th>Documento</th>
                <th>Mensagem</th>
            </tr>
    """
    
    for item in data:
        pdf_content += f"""
            <tr>
                <td>{item['seq_planilha']}</td>
                <td>{item['rota']}</td>
                <td>{item['Data']}</td>
                <td>{item['Documento']}</td>
                <td>{item['Mensagem']}</td>
            </tr>
        """
    
    pdf_content += """
        </table>
    </body>
    </html>
    """
    
    pdf = anvil.pdf.PDFRenderer(pdf_content)
    return pdf


@anvil.server.callable
def send_email_with_pdf():
    data = fetch_data()
    pdf = generate_pdf(data)
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%d/%m/%Y")
    
    anvil.email.send(
        to="emerson.gregorio@agrocrestani.com.br",
        subject=f"Relatório Erros Integração - {data_atual} ",
        text=f"Segue em anexo o relatório de erros de integração do dia {data_atual} .",
        attachments=[("relatorio.pdf", pdf)]
    )