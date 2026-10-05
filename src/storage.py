import json
import sys
import os
from .model import Customer

def load_customers(file_path: str) -> list[Customer]:
    """Carga los clientes desde un archivo JSON y valida su estructura."""
    if not os.path.exists(file_path):
        print("Error: No se pudo cargar la base de datos de clientes")
        sys.exit(1)
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            print("Error: No se pudo cargar la base de datos de clientes")
            sys.exit(1)
            
        customers = []
        for item in data:
            if not isinstance(item, dict):
                print("Error: No se pudo cargar la base de datos de clientes")
                sys.exit(1)
                
            # Validación de campos requeridos
            required_keys = {'id', 'name', 'last_name', 'email'}
            if not required_keys.issubset(item.keys()):
                print("Error: No se pudo cargar la base de datos de clientes")
                sys.exit(1)
                
            # Validación de tipos de datos (evita null y tipos incorrectos)
            if not isinstance(item['id'], int) or \
               not isinstance(item['name'], str) or \
               not isinstance(item['last_name'], str) or \
               not isinstance(item['email'], str):
                print("Error: No se pudo cargar la base de datos de clientes")
                sys.exit(1)

                
            customers.append(Customer(
                id=item['id'],
                name=item['name'],
                last_name=item['last_name'],
                email=item['email']
            ))
        return customers
    except (json.JSONDecodeError, ValueError, TypeError):
        print("Error: No se pudo cargar la base de datos de clientes")
        sys.exit(1)
