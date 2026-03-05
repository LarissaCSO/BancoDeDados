# 1 Criando banco de dados

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar ou criar banco de dados
conexao = sqlite3.connect("dados_vendas.db")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS vendas1")

cursor.execute("""
CREATE TABLE vendas1 (
    Id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    Data_venda DATE,
    Produto TEXT,
    Categoria TEXT,
    Valor_venda REAL
)
""")

# Dados de exemplo
cursor.execute("""
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2024-01-01', 'Produto A', 'Cosméticos', 784.96),
    ('2024-02-05', 'Produto B', 'Roupas', 3485.74),
    ('2024-03-10', 'Produto C', 'Cosméticos', 976.85),
    ('2024-04-15', 'Produto D', 'Higiene Pessoal', 463.54),
    ('2024-05-20', 'Produto E', 'Cosméticos', 95.41),
    ('2024-06-02', 'Produto F', 'Roupas', 456.74),
    ('2024-07-05', 'Produto G', 'Higiene Pessoal', 748.14),
    ('2024-08-10', 'Produto H', 'Cosméticos', 796.52),
    ('2024-09-20', 'Produto I', 'Roupas', 1528.78),
    ('2024-10-25', 'Produto J', 'Cosméticos', 854.14),
    ('2024-11-12', 'Produto K', 'Roupas', 87.96),
    ('2024-12-02', 'Produto L', 'Higiene Pessoal', 145.85);
""")

conexao.commit()

print("Banco de dados criado com sucesso!") 
