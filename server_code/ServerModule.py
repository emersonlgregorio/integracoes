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
    rows = anvil.server.call('get_integracoes_email')
    return rows
  

@anvil.server.callable
def generate_pdf(data):
    pdf_content = "<h1>Relatório de erros de integração</h1>"
    pdf_content += "<table border='1'>"
    pdf_content += "<tr><th>Seq Planilha</th><th>Rota</th><th>Data</th><th>Documento</th><th>Mensagem</th></tr>"

    for item in data:
        pdf_content += f"<tr><td>{item['seq_planilha']}</td><td>{item['rota']}</td><td>{item['Data']}</td><td>{item['Documento']}</td><td>{item['Mensagem']}</td></tr>"

    pdf_content += "</table>"

    pdf = anvil.pdf.render_form(pdf_content)
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