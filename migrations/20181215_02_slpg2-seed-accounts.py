"""
Seed accounts
"""

from yoyo import step

__depends__ = {'20181215_01_DqBXW-create-table-accounts'}

steps = [
    step("""
INSERT INTO accounts 
(first_name, last_name, cpf) 
VALUES 
('John', 'Doe', '37999854840')""",
         "DELETE FROM accounts WHERE cpf = '37999854840'")
]
