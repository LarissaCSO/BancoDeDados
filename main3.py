print("Total de vendas por categoria:")
print(df_vendas.groupby("Categoria")["Valor_venda"].sum())

print("Faturamento mensal:")
print(df_vendas.groupby("Mês")["Valor_venda"].sum())
