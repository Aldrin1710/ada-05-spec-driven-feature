import sys
import os

# Para poder ejecutar python src/cli.py directamente desde la raíz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.service import search_customers

def main():
    if len(sys.argv) < 2:
        print("No se encontraron clientes")
        sys.exit(0)
        
    term = sys.argv[1]
    
    # Validaciones
    # VR-01 / AC-01: El término no puede ser vacío y debe contener alfanuméricos
    if not term or not term.strip() or not any(c.isalnum() for c in term):
        print("No se encontraron clientes")
        sys.exit(0)
        
    # VR-02: El término debe contener al menos 3 caracteres
    if len(term) < 3:
        print("No se encontraron clientes")
        sys.exit(0)
        
    try:
        results = search_customers(term)
        
        # EH-01: Sin ninguna coincidencia deberá mostrar el mensaje
        if not results:
            print("No se encontraron clientes")
            sys.exit(0)
            
        for c in results:
            print(f"[{c.id}] {c.name} {c.last_name} - {c.email}")
            
    except SystemExit as e:
        # Permitir que el SystemExit de storage.py fluya
        sys.exit(e.code)
    except Exception as e:
        # Prevenir que el usuario vea un stacktrace
        print("Error: Ocurrió un error inesperado en la aplicación.")
        sys.exit(1)

if __name__ == "__main__":
    main()
