import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
db_id = os.getenv("NOTION_DB_ID")

def create_item(nome, status="Pendente", tags=None):
    props = {
        "Nome": {
            "title": [
                {
                    "text": { "content": nome }
                }
            ]
        },
        "Status": {
            "select": { "name": status }
        },
    }

    if tags: 
        props["Tags"] = {
            "multi_select": [{ "name": tag } for tag in tags]
        }

    response = notion.pages.create(
        parent = { "database_id": db_id },
        properties = props
    )

    return response["id"]

def read_items():
    respose = notion.databases.query(database_id=db_id)
    items = []
    for page in respose["results"]:
        props = page["properties"]
        name = page["Nome"]["title"][0]["plain_text"] if props["Nome"]["title"] else ""
        status = page["Status"]["select"]["name"] if props["Status"]["select"] else ""
        page_id = page["id"]
        items.append({ "id": page_id, "nome": nome, "status": status })

    return items

def update_item(paga_id, new_status):
    response = notion.pages.update(
        page_id=paga_id,
        properties={
             "Status": { "select": {"name": new_status} }
        }
    )
    return response

def delete_item(page_id):
    return update_item(page_id, "Removido")
