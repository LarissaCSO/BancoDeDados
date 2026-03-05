df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)
print("Pré-visualização dos dados:")
print(df_vendas.head())

# Converter coluna de data para formato datetime
df_vendas["Data_venda"] = pd.to_datetime(df_vendas["Data_venda"])

# Criar uma coluna com o mês
df_vendas["Mês"] = df_vendas["Data_venda"].dt.month
