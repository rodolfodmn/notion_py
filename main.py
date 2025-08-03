import os
from dotenv import load_dotenv
from notion_client import Client
from notion_crud import create_item, read_items, update_item, delete_item

load_dotenv()

notion_token = os.getenv("NOTION_TOKEN")
database_id = os.getenv("NOTION_DB")
notion = Client(auth=notion_token)

response = notion.search(filter={"property": "object", "value": "database"})

for result in response["results"]:
    print(result["id"])
    print(result["title"])


# Criar
id = create_item("Estudar API do Notion", status="Pendente", tags=["python", "api"])
print("Criado:", id)

# Listar
for item in read_items():
    print(item)

# Atualizar
update_item(id, "Feito")

# Deletar
delete_item(id)

