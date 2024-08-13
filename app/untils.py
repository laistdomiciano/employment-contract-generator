import os
from .models import Contract, db
def load_contract_template(contract_type):
    templates_dir = os.path.join(os.path.dirname(__file__), 'contracts')
    template_path = os.path.join(templates_dir, f"{contract_type}.txt")
    with open(template_path, 'r') as file:
        return file.read()

def create_contract(contract_type):
    template = load_contract_template(contract_type)
    new_contract = Contract(template=template, type=contract_type)
    db.session.add(new_contract)
    db.session.commit()
    return new_contract