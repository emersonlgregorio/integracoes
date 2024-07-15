import anvil.email
import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.pdf
import io
from datetime import datetime

@anvil.server.callable
def fetch_data():
    rows = anvil.server.call('get_integracoes_email')
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
    
    pdf = anvil.pdf.render_html(pdf_content)
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