# %% [markdown]
# ### Importando o repositório

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('peru_student_enrollment_data_2023.csv', on_bad_lines='warn', sep=";")
df.head(5)

# %%
#print(df['GENDER'].dtype)
#print(df['GENDER'].unique()) #Descobrimos aqui, que 1 e 2 são STRINGS e não integers
df['GENDER'] = df['GENDER'].replace({'1': 'M', '2': 'F'})
#print(df['GENDER'].value_counts())

# %%
anoUm = df['TUITION PAYMENT MARCH 2022'].value_counts()
anoDois = df['TUITION PAYMENT MARCH 2023'].value_counts()
#print(f"Em 2022, teve {anoUm[1]} inscrições. Em 2023 entretanto, ocorreu {anoDois[1]}. Uma diferença de {anoUm[1] - anoDois[1]} inscrições!")


# %% [markdown]
# #### VERIFICANDO VALORES AUSENTES

# %%
for i in df.columns: #FILTRAGEM E SUBSTITUIÇÃO RESPECTIVAMENTE POR MODA E MEDIANA
    if df[i].dtype == object:
        df.loc[df[i].isna(), i] = df[i].mode()[0]
    else:
        df.loc[df[i].isna(), i] = df[i].median()
#print(df.isna().sum())
#print('Não há mais valores ausentes')

# %%
inscritas2022 = df[(df['TUITION PAYMENT MARCH 2022'] == 1) & (df['GENDER'] == 'F')].shape[0]
inscritas2023 = df[(df['TUITION PAYMENT MARCH 2023'] == 1) & (df['GENDER'] == 'F')].shape[0]

variaçãoFeminina = inscritas2022 - inscritas2023
#print(variaçãoFeminina)

inscritos2022 = df[(df['TUITION PAYMENT MARCH 2022'] == 1) & (df['GENDER'] == 'M')].shape[0]
inscritos2023 = df[(df['TUITION PAYMENT MARCH 2023'] == 1) & (df['GENDER'] == 'M')].shape[0]

variaçãoMasculina = inscritos2022 - inscritos2023
#print(variaçãoMasculina)

genDesconhecido2022 = df[(df['TUITION PAYMENT MARCH 2022'] == 1) & (df['GENDER'] == 'U')].shape[0]
genDesconhecido2023 = df[(df['TUITION PAYMENT MARCH 2023'] == 1) & (df['GENDER'] == 'U')].shape[0]

variaçãoDesconhecidos = genDesconhecido2022 - genDesconhecido2023
#print(variaçãoDesconhecidos)

# %%
pagamentos2022 = df['TUITION PAYMENT MARCH 2022'].eq(1).sum()
pagamentos2023 = df['TUITION PAYMENT MARCH 2023'].eq(1).sum()

data = [
    {'Ano': 2022, 'Pagamentos': pagamentos2022},
    {'Ano': 2023, 'Pagamentos': pagamentos2023}
]
df_variacao = pd.DataFrame(data)
#sns.set_style("whitegrid")
#sns.lineplot(x='Ano', y='Pagamentos', data=df_variacao, marker='o')
#plt.title('Variação dos Pagamentos de 2022 e 2023')
#plt.xlabel('Ano')
#plt.ylabel('Número de Pagamentos')
#plt.show()

# %%
df.to_csv('dadosUniversdade_limpo.csv', index=False)
#print("Arquivo exportado.")

# %%
df2 = pd.read_csv('dadosUniversdade_limpo.csv')
#df2.head(5)

# %%
district_options = [{'label': x, 'value': x} for x in df2['DISTRICT'].unique() ]
major_options = [{'label': x, 'value': x} for x in df2['PROGRAM/MAJOR'].unique()]




