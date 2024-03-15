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
def get_drafts(filtro="""where o."DocStatus" = 'O'"""):
  query =   f"""
            SELECT 
                o."DocDate", o."TaxDate", o."Serial", 
                o."CardCode", o."CardName",  o."BPLId", 
                o."BPLName", o."VATRegNum", o."DocStatus",
                o."DocEntry", o."DocType", o."ObjType"            
            FROM SBO_CRESTANI_PRD.ODRF o
            {filtro}
            order by o."TaxDate" desc
                            """
  print(query)
  items = anvil.server.call('hanaSelect', query)
  return items

@anvil.server.callable
def get_drafts_items(filtro = 'WHERE i."DocEntry" = 2028 AND i."ObjType" = 18'):
  query = f"""
            SELECT 
                i."LineNum" 
                ,i."ItemCode"
                ,i."Dscription"
                ,i."Quantity"
                ,i."Currency"
                ,i."LineTotal"
                ,i."WhsCode"
                ,i."AcctCode"
                ,i."TaxCode"
                ,i."UomEntry" 
                ,i."Usage" 
                ,i."OcrCode"
                ,i."OcrCode2"
                ,i."OcrCode3"
                ,i."DocEntry"
            FROM SBO_CRESTANI_PRD.DRF1 i
            {filtro}
            order by i."LineNum"
                            """
  print(query)
  items = anvil.server.call('hanaSelect', query)

  return [
        {
            "LineNum": item[0],
            "ItemCode": item[1],
            "Dscription": item[2],
            "Quantity":float(item[3]),
            "Currency": item[4],
            "LineTotal": float(item[5]),
            "WhsCode": item[6],
            "AcctCode": item[7],
            "TaxCode": item[8],
            "UomEntry": item[9],
            "Usage": item[10],
            "OcrCode": item[11],
            "OcrCode2": item[12],
            "OcrCode3": item[13]
        } for item in items
    ]