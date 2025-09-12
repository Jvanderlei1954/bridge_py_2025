#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#         Relatório Financeiro - Academia de Pilates
# Cálculo revisado por uma IA: Receita Total x Custo Total Mensal


# In[1]:


import pandas as pd

# ============================================================
# 1. DADOS DA ACADEMIA
# ============================================================
planos = {
    "Mensal": {"preco": 423, "alunos": 80},       # R$ 423 por mês
    "Trimestral": {"preco": 1200, "alunos": 40},  # R$ 1200 a cada 3 meses
    "Anual": {"preco": 4308, "alunos": 20}        # R$ 4308 por ano
}

# Custos fixos mensais
custos_fixos = {
    "Aluguel": 5000,
    "Associados": 12000,
    "Energia": 350,
    "Água": 180,
    "Manutenção": 400,
    "Marketing": 500
}

# ============================================================
# Parâmetros de divisão de pró-labore (devem somar 100%)
# Ex.: 0.6 + 0.4 = 1.0  (60% / 40%)
# ============================================================
socios = {
    "Sócio 1": 0.60,
    "Sócio 2": 0.40,
}

assert abs(sum(socios.values()) - 1.0) < 1e-9, "As porcentagens dos sócios devem somar 100%."

# ============================================================
# 2. CÁLCULO DA RECEITA
# ============================================================
receita_dados = []
for plano, dados in planos.items():
    if plano == "Trimestral":
        receita_mensal = (dados["preco"] / 3) * dados["alunos"]  # distribui por mês
    elif plano == "Anual":
        receita_mensal = (dados["preco"] / 12) * dados["alunos"] # distribui por mês
    else:
        receita_mensal = dados["preco"] * dados["alunos"]
    receita_dados.append([plano, dados["alunos"], dados["preco"], receita_mensal])

df_receita = pd.DataFrame(
    receita_dados,
    columns=["Plano", "Qtde Alunos", "Preço (R$)", "Receita Mensal (R$)"]
)

receita_total = df_receita["Receita Mensal (R$)"].sum()

# ============================================================
# 3. CÁLCULO DOS CUSTOS
# ============================================================
df_custos = pd.DataFrame(list(custos_fixos.items()), columns=["Custo", "Valor (R$)"])
custo_total = df_custos["Valor (R$)"].sum()

# Tributos (simplificado)
tot_tributos = receita_total * 0.06

# ============================================================
# 4. PRÓ-LABORE (simplificado)
# Base: 40% do lucro operacional (receita - custos fixos), menos INSS (11%) e IRPF (14%)
# ============================================================
base_prolab = max((receita_total - custo_total) * 0.40, 0)  # evita negativo
desc_inss = base_prolab * 0.11
desc_irpf = base_prolab * 0.14
val_prolab_liq = base_prolab - desc_inss - desc_irpf

# Distribuição entre sócios
dist_prolab = {nome: val_prolab_liq * pct for nome, pct in socios.items()}
tot_prolab = sum(dist_prolab.values())

# ============================================================
# 5. RESULTADO FINAL
# ============================================================
lucro_liquido = (receita_total - custo_total) - (tot_prolab + tot_tributos)
perc_liq = (lucro_liquido / receita_total) * 100 if receita_total else 0.0
despesa_total = receita_total - lucro_liquido     # = custos + tributos + pró-labores
perc_despesa_total = (despesa_total / receita_total) * 100 if receita_total else 0.0

#================================================================
# Imprimindo os resultados
#================================================================
print("="*56)
print(" RELATÓRIO FINANCEIRO - ACADEMIA DE PILATES ")
print("="*56)

print("\n--- Receita por Plano ---")
print(df_receita.to_string(index=False))
print("="*56)

print(f"\nReceita Total Mensal: R$ {receita_total:,.2f}")
print(f"Custos Fixos (sem tributos/pró-labore): R$ {custo_total:,.2f}")
print(f"Tributos (6% s/ receita): R$ {tot_tributos:,.2f}")

print("\n--- Pró-Labore (líquido, após INSS e IRPF simplificados) ---")
for nome, valor in dist_prolab.items():
    print(f"{nome:<15} R$ {valor:,.2f}")
print(f"Somatório dos Pró-labores: R$ {tot_prolab:,.2f}")

print("\n--- Despesas & Resultado ---")
print(f"Despesas Totais Mensais: R$ {despesa_total:,.2f}")
print(f"Perc. Despesa Total: {perc_despesa_total:,.2f}%")
print("="*56)
print(f">>> Lucro Líquido Mensal: R$ {lucro_liquido:,.2f}")
print(f">>> Lucro Líquido: {perc_liq:,.2f}% da Receita Total Mensal")
print("="*56)


# In[ ]:




