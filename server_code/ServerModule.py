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




