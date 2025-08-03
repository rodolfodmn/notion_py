import os
from notion_crud import create_item, read_items, update_item, delete_item

def menu():
    while True:
        print("\n=== Menu Notion CRUD ===")
        print("[1] Listar")
        print("[2] Nova")
        print("[3] Atualizar status")
        print("[4] Deletar")
        print("[0] Sair")
        choice = input("> ").strip()
        
        if choice == "1":
            items = read_items()
            for i, item in enumerate(items):
                print(f"[{i}] {item['nome']} - {item['status']}")

        elif choice == "2":
            nome = input("Nome do Item: ").strip()
            status = input("Status (padrão: Pendente): ").strip() or "Pendente"
            tags_str = input("Tags separadas por virgula").strip()
            tags = [t.strip() for t in tags_str.split(",")] if tags_str else []
            page_id = create_item(nome, status, tags)
            print(f"Item criado com ID: {page_id}")

        elif choice == "3":
        elif choice == "4":
        elif choice == "0":
