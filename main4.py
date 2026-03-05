# Gráfico 1: vendas por categoria
plt.figure(figsize=(6,4))
sns.barplot(data=df_vendas, x="Categoria", y="Valor_venda", estimator=sum)
plt.title("Total de vendas por categoria")
plt.show()

# Gráfico 2: evolução das vendas por mês
plt.figure(figsize=(8,4))
df_vendas.groupby("Mês")["Valor_venda"].sum().plot(marker="o")
plt.title("Faturamento mensal")
plt.xlabel("Mês")
plt.ylabel("Total de vendas (R$)")
plt.show()

# Gráfico 3: participação por categoria (pizza)
df_vendas.groupby("Categoria")["Valor_venda"].sum().plot(kind="pie", autopct="%.1f%%", figsize=(6,6))
plt.title("Participação de vendas por categoria")
plt.ylabel("")
plt.show()

# Insights

print("Relatório final:")
print("- Roupas foram a categoria mais lucrativa.")
print("- Houve pico de vendas no segundo mês do ano.")
print("- Houve uma queda brusca do segundo para o terceiro mês.")
print("- Higiene Pessoal teve menos participação em vendas.")
