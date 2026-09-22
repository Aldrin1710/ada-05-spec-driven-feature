import pytest
import os
import tempfile
import json
from src.storage import load_customers
from src.model import Customer

def create_temp_json(data):
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        json.dump(data, f)
        return f.name

def test_load_customers_success():
    data = [
        {"id": 1, "name": "A", "last_name": "B", "email": "a@b.com"}
    ]
    temp_path = create_temp_json(data)
    try:
        customers = load_customers(temp_path)
        assert len(customers) == 1
        assert customers[0].name == "A"
    finally:
        os.remove(temp_path)

def test_load_customers_file_not_found(capsys):
    with pytest.raises(SystemExit) as exc_info:
        load_customers("non_existent_file.json")
    
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: No se pudo cargar la base de datos de clientes" in captured.out

def test_load_customers_invalid_json(capsys):
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        f.write("invalid json")
        temp_path = f.name
        
    try:
        with pytest.raises(SystemExit) as exc_info:
            load_customers(temp_path)
        assert exc_info.value.code == 1
    finally:
        os.remove(temp_path)

def test_load_customers_not_list(capsys):
    temp_path = create_temp_json({"id": 1})
    try:
        with pytest.raises(SystemExit):
            load_customers(temp_path)
    finally:
        os.remove(temp_path)

def test_load_customers_not_dict(capsys):
    temp_path = create_temp_json([1, 2, 3])
    try:
        with pytest.raises(SystemExit):
            load_customers(temp_path)
    finally:
        os.remove(temp_path)

def test_load_customers_missing_keys(capsys):
    temp_path = create_temp_json([{"id": 1, "name": "A"}])
    try:
        with pytest.raises(SystemExit):
            load_customers(temp_path)
    finally:
        os.remove(temp_path)
