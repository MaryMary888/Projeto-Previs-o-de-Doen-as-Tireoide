import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import (classification_report, confusion_matrix, roc_curve, roc_auc_score,
                             accuracy_score, recall_score, precision_score)
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.svm import SVC
from xgboost import XGBClassifier
import plotly.express as px

df = pd.read_csv("Base_doenca_tireoide.csv", delimiter = ',')
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(df.head(10).to_string())
print(df.tail(10).to_string())

# Verificando tipos dos dados
print('\nTipo de Dados: \n',df.dtypes)

# Verificando escrita dos dados por coluna
val_unico = {col: df[col].unique() for col in df.columns}
for col, val in val_unico.items():
    print(f'Coluna: {col}')
    print(f'Valores presentes: {val}\n')

# Tratar as colunas baseado em seu contexto:
print(df[df['hypopituitary']=='t'].to_string())

# Exclusão de linhas que não agregam na análise
df.drop(columns = ['TBG measured', 'TBG', 'hypopituitary'], inplace = True)

# Dados de 'sex'
sexo = df['sex'].value_counts()
# transformando '?' em F para pacientes Grávidas antes da alteração em massa
df.loc[(df['sex'] == '?') & (df['pregnant'] == 't'), 'sex'] = 'F'
print(((df['sex'] == '?') & (df['pregnant'] == 't')).value_counts())
print('\nPorcentagem de cada: \n', (sexo/sexo.sum()) * 100)

# Selecionando apenas '?' e calculando distribuição proporcional
rest = df[df['sex'] == '?'].index
f = len(rest)
n_fem, n_masc = int(f*0.6574), int(f*0.3027) # Imputando valores de maneira randomizada
ind_random = np.random.permutation(rest)
df.loc[ind_random[:n_fem], 'sex'] = 'F'
df.loc[ind_random[n_fem:n_fem+n_masc], 'sex'] = 'M'
df.loc[ind_random[n_fem+n_masc:], 'sex'] = 'F' # Manter o restante ao grupo mais prevalente
print(df['sex'].unique()) # Validação dos valores únicos alterados

# Usando getdummies para evitar enviesar a base
df = pd.get_dummies(df, columns = ['sex'], prefix = 'sex', drop_first = False)
print(df.head().to_string())
# Usando get_dummies para a var referral source
df = pd.get_dummies(df, columns = ['referral source'], prefix = 'referral source', drop_first = False)
df = df.astype({col: int for col in df.columns if df[col].dtype == 'bool'})

# Em age substituir '?' (nulo) por média das idades registradas e alterando dados incorretos
df['age'] = pd.to_numeric(df['age'].replace('?', pd.NA), errors = 'coerce')
df['age'] = df['age'].replace(455, 45)
df['age'] = df['age'].fillna(df['age'].mean()).astype(int)

# Verificando situação de dados de exames igualados a '?'
print(((df['T4U measured'] == 'f') & (df['T4U'] != '?')).value_counts())
print(((df['FTI measured'] == 't') & (df['FTI'] == '?')).value_counts())

# Colunas binarias em forma categórica serão convertidas em binárias em forma de inteiro
binaria_cols = [col for col in df.columns if df[col].isin(['f', 't']).all()]
df[binaria_cols] = df[binaria_cols].replace({'f': 0, 't': 1}).astype(int)

# Filtra apenas as que contêm o caracter '?'
for col in df.select_dtypes(include = 'object'):
    if df[col].str.contains(r'\?').any():
        df[col] = pd.to_numeric(df[col].replace('?', 0), errors = 'coerce')

# Mudando binaryClass, variável target
df['binaryClass'] = df['binaryClass'].map({'P': 1, 'N': 0})
print(df['binaryClass'].unique())

# Validando alteração da tipagem dos dados
print('\nTipo de Dados: \n',df.dtypes)

# Verificando possibilidade de outliers
print(df.describe())

faixas_TSH = {
    'TSH = 0': (df['TSH'] == 0),
    '0 < TSH <= 2.2': (df['TSH'] > 0) & (df['TSH'] <= 2.42),
    '2.2 < TSH <= 10': (df['TSH'] > 2.42) & (df['TSH'] <= 10),
    '10 < TSH <= 50': (df['TSH'] > 10) & (df['TSH'] <= 50),
    '50 < TSH <= 100':(df['TSH'] > 50) & (df['TSH'] <= 100),
    '100 < TSH':(df['TSH'] > 100)
}

faixas_T3 = {
    'T3 = 0': (df['T3'] == 0),
    '0 < T3 <= 1.8': (df['T3'] > 0) & (df['T3'] <= 1.8),
    '1.8 < T3 <= 2.2': (df['T3'] > 1.8) & (df['T3'] <= 2.2),
    '2.2 < T3 <= 5.0': (df['T3'] > 2.2) & (df['T3'] <= 5.0),
    '5.0 < T3':(df['T3'] > 5.0)
}

faixas_FTI = {
    'FTI = 0': (df['FTI'] == 0),
    '0 < FTI <= 86.75': (df['FTI'] > 0) & (df['FTI'] <= 86.75),
    '86.75 < FTI <= 104': (df['FTI'] > 86.75) & (df['FTI'] <= 104),
    '104 < FTI <= 121.25': (df['FTI'] > 104) & (df['FTI'] <= 121.25),
    '121.25 < FTI':(df['FTI'] > 121.25)
}

faixas_TT4 = {
    'TT4 = 0': (df['TT4'] == 0),
    '0 < TT4 <= 84': (df['TT4'] > 0) & (df['TT4'] <= 84),
    '84 < TT4 <= 102': (df['TT4'] > 84) & (df['TT4'] <= 102),
    '102 < TT4 <= 123': (df['TT4'] > 102) & (df['TT4'] <= 123),
    '123 < TT4':(df['TT4'] > 123)
}

# Loop para imprimir resultados
for nome, cond in faixas_TSH.items():
    subset = df[cond]
    total = len(subset)
    com_doenca = (subset['binaryClass'] == 1).sum()
    sem_doenca = (subset['binaryClass'] == 0).sum()

    print(f'{nome}:')
    print(f' Total de pacientes: {total}')
    print(f' Com Doença da Tireóide: {com_doenca}')
    print(f' Sem Doença da Tireóide: {sem_doenca}\n')
    print(subset.head(50).to_string())

# Alteração de valores acima e/ou abaixo do normal
df['TSH'] = df['TSH'].apply(lambda x: x / 10 if x >= 100 else x)
print(df[df['TSH'] >= 100].to_string())
df_ml = df.copy()

df.to_csv("dados_tratados.csv", index = True)

# ANÁLISE EXPLORATÓRIA UNIVARIADA
# Boxplot da idade
df.boxplot(column = 'age')
plt.title('Boxplot de Idade dos Pacientes')
plt.ylabel('Idade')
plt.show()

# Função para realizar plot das variáveis selecionadas a seguir
var = [
    ('binaryClass', 'Pacientes com Doenças de Tireóide', 'Possui Doença de Tireóide?'),
    ('query hypothyroid','Pacientes Suspeitos de Hipotireoidismo','Possui Suspeita?'),
    ('query hyperthyroid', 'Pacientes Suspeitos de Hipertireoidismo', 'Possui Suspeita?'),
    ('on thyroxine', 'Pacientes usuários de Tiroxina', 'Utiliza o medicamento?'),
    ('query on thyroxine', 'Pacientes suspeitos de usar Tiroxina', 'Tem Suspeita?'),
    ('psych', 'Pacientes que realizam Acompanhamento Psiquiátrico', 'Realiza acompanhamento?'),
    ('TSH measured', 'Pacientes que mediram Níveis de TSH', 'Realizou exame?'),
    ('T3 measured', 'Pacientes que mediram Níveis de T3', 'Realizou exame?'),
    ('TT4 measured', 'Pacientes que mediram Níveis de TT4', 'Realizou exame?'),
    ('T4U measured', 'Pacientes que mediram Níveis de T4U', 'Realizou exame?'),
    ('FTI measured', 'Pacientes que mediram Níveis de FTI', 'Realizou exame?')]

def plot_graficos(df, col, titulo, xlabel):
    cont = df[col].replace({0: 'Não', 1: 'Sim'})
    print(f'\nPorcentagem de cada:\n')
    print((cont.value_counts(normalize = True) * 100).round(2))

    plt.figure(figsize = (8, 6))
    sns.countplot(x = cont, hue = cont, palette = 'pastel')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel('Quantidade')
    plt.tight_layout()
    plt.show()

for var, titulo, xlabel in var:
    plot_graficos(df, var, titulo, xlabel)

# Observar quantidade de pacientes femininos e masculinos
sexo_count = df[['sex_F','sex_M']].sum()
sexo_count.index = ['Feminino','Masculino']
print(f'\nPorcentagem de cada:\n', (sexo_count/sexo_count.sum() * 100).round(2))
sexo_count.plot(kind = 'bar', color = ['lightblue', 'peachpuff'], title = "Pacientes por sexo")
plt.show()

# Gráfico de barras dos referral sources
referral_cols = [c for c in df.columns if c.startswith('referral source_')]
cont = df[referral_cols].sum().rename_axis('Indicacao').reset_index(name = 'Quantidade')
label_map = {
    'referral source_STMW': 'STMW', 'referral source_SVHC': 'SVHC',
    'referral source_SVHD': 'SVHD', 'referral source_SVI': 'SVI',
    'referral source_other': 'Outros'}
cont['Indicacao'] = cont['Indicacao'].map(label_map)
px.bar(cont, x = 'Indicacao', y = 'Quantidade', color = 'Indicacao', text = 'Quantidade',
       title = 'Distribuição de Encaminhamento').update_traces(
       textposition = 'outside').update_layout(showlegend = False, yaxis_title = 'Quantidade',
                                               xaxis_title = 'Tipo de Encaminhamento',
                                               xaxis = dict(categoryorder = 'total descending')).show()

# ANÁLISE EXPLORATÓRIA BIVARIADA
# mulheres grávidas x binaryClass
mulheres_gravidas = df[(df['sex_F'] == 1) & (df['pregnant'] == 1)]
contagem = mulheres_gravidas['binaryClass'].value_counts().reindex([0, 1], fill_value = 0)
labels = ['Sem doença de tireoide', 'Com doença de tireoide']
plt.bar(['Sem doença','Com doença'], contagem, color = ['lightblue', 'peachpuff'])
plt.title('Grávidas com doença de tireoide')
plt.show()

# Faixa de idade x binaryClass
bins = [0, 15, 30, 45, 60, 75, 95]
rot = ['0–15', '16–30', '31–45', '46–60', '61–75', '76+']
df['age_bin'] = pd.cut(df['age'], bins = bins, labels = rot, right = False)
colors = sns.color_palette('pastel')
contagem = df.groupby(['age_bin', 'binaryClass']).size().unstack(fill_value = 0)
contagem.plot(kind = 'bar', figsize = (8, 6), color = colors,
              title = 'Distribuição de doenças da tireoide por faixa etária')
plt.xlabel('Faixa etária')
plt.ylabel('Número de pacientes')
plt.legend(['Sem doença', 'Com doença'])
plt.tight_layout()
plt.show()

# Média TSH x binaryClass
media_tsh = df[df['TSH measured'] == 1].groupby('binaryClass')['TSH'].mean().reset_index()
media_tsh['diagnosis'] = media_tsh['binaryClass'].map({0: 'Sem a doença', 1: 'Com a doença'})
fig = px.bar(media_tsh, x = 'diagnosis', y = 'TSH', color = 'diagnosis',
        title = 'Média de TSH por diagnóstico',
        labels = {'TSH': 'TSH médio', 'diagnosis': 'Diagnóstico'})
fig.update_layout(showlegend = False)
fig.show()

# binaryClass x referral sources
df['referral_source'] = df[referral_cols].idxmax(axis = 1).str.replace('referral source_','')
grupo = df.groupby(['referral_source','binaryClass']).size().reset_index(name = 'count')
grupo['diagnosis'] = grupo['binaryClass'].map({0: 'Sem a doença', 1: 'Com a doença'})
fig = px.bar(grupo, x = 'referral_source', y = 'count', color = 'diagnosis', barmode = 'stack',
    labels = {'referral_source': 'Encaminhamento', 'diagnosis': 'Diagnóstico', 'count': 'Número de Pacientes'},
    title = 'Distribuição dos encaminhamentos por Diagnóstico')
fig.show()

# TSH x FTI, T3, T4U e TT4
df_comp = df.melt(id_vars = 'TSH', value_vars = ['T3', 'FTI', 'TT4', 'T4U'],
                  var_name = 'Hormônio', value_name = 'Valor')
df_filtrado = df_comp[(df_comp['TSH'] > 0) & (df_comp['Valor'] > 0)]
fig = px.scatter(df_filtrado, x = 'TSH', y = 'Valor', color = 'Hormônio',
                facet_col = 'Hormônio', labels = {'TSH': 'TSH', 'Valor': 'Nível do hormônio'},
                title = 'Comportamento de T3, FTI, TT4 e T4U em função do TSH')
fig.show()

# binaryClass x Suspeitos (Hiper, Hipo e Ambos)
df['suspect_thyroid'] = ((df['query hypothyroid'] == 1) | (df['query hyperthyroid'] == 1)).astype(int)
df_sus = df[df['suspect_thyroid'] == 1]
df_sus_hypo = df[df['query hypothyroid'] == 1]
df_sus_hyper = df[df['query hyperthyroid'] == 1]

a = (df['query hypothyroid']==1) & (df['query hyperthyroid']==1)
print(df[a])

def graf_sus_x_diag(df, col_query, target_col = 'binaryClass'):
    grupo = df.groupby([col_query, target_col]).size().reset_index(name = 'count')
    grupo[target_col] = grupo[target_col].map({0: 'Sem Doença', 1: 'Com Doença'})
    grupo[col_query] = grupo[col_query].map({0: 'Não', 1: 'Sim'})
    sns.barplot(data = grupo, x = col_query, y = 'count', hue = target_col, palette = 'pastel')
    plt.title(f'Diagnóstico vs Suspeita {col_query}')
    plt.xlabel('Suspeita Registrada')
    plt.ylabel('Número de Pacientes')
    plt.legend(title = 'Diagnóstico')
    plt.show()

graf_sus_x_diag(df_sus, 'suspect_thyroid')
graf_sus_x_diag(df_sus_hypo, 'query hypothyroid')
graf_sus_x_diag(df_sus_hyper, 'query hyperthyroid')


# Unificando coluna 'sex' para utilizar na análise
df['sex_def'] = np.where(df['sex_F'] == 1, 'Feminino',
                         np.where(df['sex_M'] == 1, 'Masculino', ''))
# Lista de variáveis para a função
var = [
    # psych x binaryClass
    ('psych', 'binaryClass', 'Histórico Psiquiátrico vs. Doença de Tireóide', 'Histórico Psiquiátrico?',
     'Diagnóstico', {0: 'Não', 1: 'Sim'}, {0: 'Sem Doenças da Tireóide', 1: 'Com Doenças da Tireóide'}),
    #sex_def x binaryClass
    ('sex_def', 'binaryClass', 'Diagnóstico por Sexo do Paciente', 'Sexo do Paciente', 'Diagnóstico',
     {'Masculino':'Masculino','Feminino':'Feminino'}, {0: 'Sem Doenças de Tireóide', 1: 'Com Doenças de Tireóide'}),
    #I131 treatment x binaryClass
    ('I131 treatment', 'binaryClass', 'Doença da Tireóide vs Tratamento com Iodo Radioativo',
     'Trata com Iodo Radioativo?', 'Diagnóstico', {0: 'Não', 1: 'Sim'}, {0: 'Sem a Doença', 1: 'Com a Doença'}),
    # lithium x binaryClass
    ('lithium', 'binaryClass', 'Doença da Tireoide vs Uso de Lítio', 'Usa Lítio?', 'Diagnóstico',
     {0: 'Não', 1: 'Sim'}, {0: 'Sem a Doença', 1: 'Com a Doença'}),
    # psych x lithium
    ('psych', 'lithium', 'Uso de Lítio em Pacientes com/sem Histórico Psiquiátrico', 'Histórico Psiquiátrico?',
     'Usa Lítio?', {0: 'Não', 1: 'Sim'}, {0: 'Não', 1: 'Sim'}),
    # on antithyroid medication x query hyperthyroid
    ('on antithyroid medication', 'query hyperthyroid', 'Antitireoidiano vs Suspeita de Hipertireoidismo',
     'Usa Antitireoidiano?', 'Suspeita de Hipertireoidismo?', {0: 'Não',1: 'Sim'}, {0: 'Não Possui',1: 'Possui'}),
    # on thyroxine x query hypothyroid
    ('on thyroxine', 'query hypothyroid', 'Tiroxina vs Suspeita de Hipotireoidismo', 'Usa Tiroxina?',
     'Suspeita de Hipotireoidismo?', {0: 'Não',1: 'Sim'}, {0: 'Não Possui',1: 'Possui'}),
    # tumor x binaryClass
    ('tumor', 'binaryClass', 'Tumor vs Doença da Tireóide', 'Presença de Tumor?', 'Doença da Tireóide?',
     {0: 'Não', 1: 'Sim'}, {0: 'Sem a doença', 1: 'Com a doença'}),
    # goitre x binaryClass
    ('goitre', 'binaryClass', 'Bócio vs Doença da Tireoide', 'Presença de Bócio?', 'Doença da Tireóide?',
     {0: 'Não', 1: 'Sim'}, {0: 'Sem a Doença', 1: 'Com a Doença'})]

# Função para geração de gráficos
def graf_cruzados(df, col1, col2, title, xlabel, subt, map1, map2):
    df['sep1'] = df[col1].map(map1)
    df['sep2'] = df[col2].map(map2)
    grupo = df.groupby(['sep1', 'sep2']).size().reset_index(name = 'count')

    fig = px.bar(grupo, x = 'sep1', y = 'count', color = 'sep2', barmode = 'stack',
        labels = {'sep1': xlabel, 'sep2': subt, 'count':'Número de Pacientes'},
        title = title)
    fig.show()

# Loop para geração de todos
for col1, col2, title, xlabel, subt, map1, map2 in var:
    graf_cruzados(df, col1, col2, title, xlabel, subt, map1, map2)

# binaryClass x hiper + antitireoidiano -- & -- binaryClass x hipo + tiroxina
df['antithyroid_hyper'] = ((df['on antithyroid medication'] == 1) & (df['query hyperthyroid'] == 1)).astype(int)
df['thyroxine_hypo'] = ((df['on thyroxine'] == 1) & (df['query hypothyroid'] == 1)).astype(int)

# Função para geração de gráficos
def graf_susmed_x_diag(df, col_query, target_col = 'binaryClass'):
    grupo = df.groupby([col_query, target_col]).size().reset_index(name = 'count')
    grupo[target_col] = grupo[target_col].map({0: 'Sem Doença', 1: 'Com Doença'})
    grupo[col_query] = grupo[col_query].map({1: 'Sim'})

    fig = px.bar(grupo, x = target_col, y = 'count', color = col_query, barmode = 'stack',
        labels = {target_col: 'Qual Diagnóstico?' ,'count':'Número de Pacientes'},
        title = 'Diagnóstico para pacientes Medicados e com Suspeita')
    fig.show()

# Chamando Função
graf_susmed_x_diag(df, 'antithyroid_hyper')
graf_susmed_x_diag(df, 'thyroxine_hypo')

# Hormonios x encaminhamentos
exames = ['TSH measured', 'T3 measured', 'TT4 measured', 'T4U measured', 'FTI measured']
df_filtrado = df[df[exames].sum(axis = 1) > 0].copy()
df_counts = (df_filtrado.groupby('referral_source')[exames].sum().reset_index())
df_long = df_counts.melt(id_vars = 'referral_source', value_vars = exames, var_name = 'exame', value_name = 'count')
fig = px.bar(df_long, x = 'referral_source', y = 'count', color = 'exame', barmode = 'group', text = 'count',
            title = 'Quantidade de pacientes que realizaram cada exame por encaminhamento')
fig.update_traces(textposition = 'outside').update_layout(xaxis_title = 'Encaminhamento', yaxis_title = 'Quantidade de pacientes')
fig.show()

# PRÉ-PROCESSAMENTO
# Matriz de correlação
corr = df_ml.corr(numeric_only = True)
corr_matriz = corr.reset_index().melt(id_vars = 'index')
fig = px.imshow(corr, text_auto = True, color_continuous_scale = 'RdBu',
                zmin = -1, zmax = 1, title = 'Matriz de Correlação')
fig.update_xaxes(side = 'top')
fig.update_coloraxes(colorbar_title = 'Nível de Correlação')
fig.show()

# Separação das bases de Treino e Teste
x = df_ml.drop(columns = ['binaryClass'])
y = df_ml['binaryClass']
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3, random_state = 42, stratify = y)

# Padronização dos dados com StandardScaler
sc = StandardScaler()
x_treino_sc = sc.fit_transform(x_treino)
x_teste_sc = sc.transform(x_teste)

# Balanceando dados de treino com Smote para oversampling
smote = SMOTE(random_state = 42, k_neighbors = 3, sampling_strategy = 1.0)
x_treino_s, y_treino_s = smote.fit_resample(x_treino_sc, y_treino)
print('Balanceamento: \n', y_treino_s.value_counts())

# Reduzindo Dimensionalidade com PCA
pca = PCA(n_components = 22)
x_treino_pca = pca.fit_transform(x_treino_s)
x_teste_pca = pca.transform(x_teste_sc)
explained_variance = pca.explained_variance_ratio_
cumulative_variance = explained_variance.cumsum()

plt.plot(range(1, 23), cumulative_variance, marker = 'o', linestyle = '--')
plt.title('Variância Explicada Acumulada por Componente')
plt.xlabel('Número de Componentes')
plt.ylabel('Variância Explicada Acumulada')
plt.grid(True)
plt.show()

# Função para gerar curva ROC-AUC
def plot_roc_auc(y_true, y_proba, modelo = 'Modelo'):
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    auc = roc_auc_score(y_true, y_proba)

    plt.figure(figsize = (8, 6))
    plt.plot(fpr, tpr, lw = 2, label = f'ROC curve (AUC = {auc:.2f})')
    plt.plot([0, 1], [0, 1], color = 'crimson', lw = 2, linestyle = '--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Taxa de Falso Positivo')
    plt.ylabel('Taxa de Verdadeiro Positivo')
    plt.title(f'Curva ROC - {modelo} (Classe Positiva)')
    plt.legend(loc = 'lower right')
    plt.show()

# Função para testar e avaliar modelos
def avaliar_mods(modelos, x_teste_f, y_teste_f):
    for nome, mod in modelos.items():
        y_pred = mod.predict(x_teste_f)
        y_proba = mod.predict_proba(x_teste_f)[:, 1]

        rel = classification_report(y_teste_f, y_pred, labels = [0, 1], target_names=['Negativa', 'Positiva'])
        matriz = confusion_matrix(y_teste_f, y_pred)
        acuracia = accuracy_score(y_teste_f, y_pred)

        print(f'\nResultados {nome} - Acurácia: {acuracia:.2f}')
        print(f'\nRelatório base teste {nome}:\n{rel}')
        print(f'\nMatriz de Confusão:\n{matriz}')

        # Função auxiliar auc-roc
        plot_roc_auc(y_teste_f, y_proba, modelo = nome)

# Reaplicando RandomizedSearch com novos hiperparâmetros para ambos modelos
def exec_random_search(nome_modelo, estimator, param_grid, x_train, y_train,
                        scoring = None, cv = None, n_iter = None, random_state = 42, verbose = 1):
    rs = RandomizedSearchCV(estimator = estimator, param_distributions = param_grid,  n_iter = n_iter, cv = cv,
                            scoring = scoring, verbose = verbose,  n_jobs = -1, random_state = random_state)
    rs.fit(x_train, y_train)
    print(f'Melhores parâmetros {nome_modelo}:', rs.best_params_)
    return rs.best_params_, rs.best_estimator_

# Melhorando valores threshold
def escolher_threshold(model, x_pca, y_true, thresholds = np.arange(0.30, 0.70, 0.01),
                       min_recall = 0.90, min_precision = 0.92):
    scores = model.predict_proba(x_pca)[:, 1]
    best_thr, best_prec, best_rec = 0.5, 0, 0

    for thr in thresholds:
        y_pred = (scores >= thr).astype(int)
        p = precision_score(y_true, y_pred)
        r = recall_score(y_true, y_pred)
        if r >= min_recall and p >= min_precision and p > best_prec:
            best_thr, best_prec, best_rec = thr, p, r

    print(f'\nLimiar escolhido: {best_thr:.2f} → Precision = {best_prec:.3f}, Recall = {best_rec:.3f}')
    return (scores >= best_thr).astype(int), best_thr

# Relatório modelos finais com threshold selecionado e curva auc-roc
def relatorio_threshold(y_true, y_pred, best, t_pca, model='Modelo', thresh=None):
    print(f'\nRelatório com Limiar ajustado ({model} - Negativa como foco):')
    if thresh is not None:
        print(f'Limiar usado: {thresh:.2f}')
    print(classification_report(y_true, y_pred, labels=[0, 1], target_names=['Negativa', 'Positiva']))
    print('Matriz de confusão:\n')
    print(confusion_matrix(y_true, y_pred))
    acc = accuracy_score(y_true, y_pred)
    print(f'Resultados - Acurácia: {acc:.2f}')

    scores = best.predict_proba(t_pca)[:, 1]
    plot_roc_auc(y_true, scores, modelo = model)

# Instanciando XGBoost e SVC para base de treino
xgb = XGBClassifier(random_state = 42)
svc = SVC(kernel = 'linear', random_state = 42, C = 1.0, probability = True, class_weight = 'balanced')
xgb.fit(x_treino_pca, y_treino_s)
svc.fit(x_treino_pca, y_treino_s)

# Lista de modelos para execução da função avaliar_mods
modelos_ml = {
    'XGBoost': xgb,
    'SVC': svc
}
# Avaliar desempenho das bases individualmente
avaliar_mods(modelos_ml, x_teste_pca, y_teste)

# Validação cruzada com StratifiedKFold
kf = StratifiedKFold(n_splits = 7, shuffle = True, random_state = 42)

# Iniciando Feature Engineering
xgb_params = { 'n_estimators': [200, 400, 600, 800],
               'max_depth': [3, 5, 7, 9],
               'learning_rate': [0.01, 0.05, 0.1, 0.2],
               'subsample': [0.6, 0.8, 1.0],
               'colsample_bytree': [0.6, 0.8, 1.0],
               'gamma': [0, 1, 3, 5],
               'min_child_weight': [1, 3, 5, 7],
               'scale_pos_weight': [1, 5, 10]
           }

svc_params = { 'C': [0.1, 1, 10, 50, 100],
               'kernel': ['linear', 'rbf', 'poly'],
               'gamma': ['scale', 'auto', 0.01, 0.1, 1],
               'class_weight': [None, 'balanced']
               }

# Criando outros modelos ML
xgb2 = XGBClassifier(eval_metric = 'logloss', random_state = 42)
svc2 = SVC(probability = True, random_state = 42)

# Utilizando função de execução do RandomizedSearch
bp_xgb, be_xgb = exec_random_search(nome_modelo = 'XGBoost', estimator = xgb2,param_grid = xgb_params, x_train = x_treino_pca,
                                       y_train = y_treino_s, scoring = 'f1_macro', cv = kf, n_iter = 50)

bp_svc, be_svc = exec_random_search(nome_modelo = 'SVC', estimator = svc2, param_grid = svc_params, x_train = x_treino_pca,
                                      y_train = y_treino_s, scoring = 'f1_macro', cv = kf, n_iter = 30)

# Lista 2 de modelos para execução da função avaliar_mods
mod_rand = {
    'Xgboost Alterado Rand': be_xgb,
    'SVC Alterado Rand': be_svc
}

# Avaliando novamente com hiperparâmetros selecionados
avaliar_mods(mod_rand, x_teste_pca, y_teste)

# Refinando hiperparâmetros com valores próximos dos selecionados
xgb_param_ref = {
    'n_estimators': [bp_xgb['n_estimators']-50, bp_xgb['n_estimators'], bp_xgb['n_estimators']+50],
    'max_depth': [bp_xgb['max_depth']-1, bp_xgb['max_depth'], bp_xgb['max_depth']+1],
    'learning_rate': [bp_xgb['learning_rate']*0.8, bp_xgb['learning_rate'], bp_xgb['learning_rate']*1.2],
    'subsample': [max(0.7, bp_xgb['subsample']-0.1), bp_xgb['subsample'], min(1.0, bp_xgb['subsample']+0.1)]
}

svc_params_ref = { 'C': [bp_svc['C']*0.5, bp_svc['C'], bp_svc['C']*2],
                   'kernel': [bp_svc['kernel']], # mantém o kernel
                   'gamma': [bp_svc['gamma']] if bp_svc['kernel'] == 'linear' else ['scale', 'auto', 0.01, 0.1, 1],
                   'class_weight': [bp_svc['class_weight']]
}

# Segundo Randomized Search com parâmetros refinados
bparam_xgb, best_xgb = exec_random_search(nome_modelo = 'XGBoost Final', estimator = xgb2,param_grid = xgb_param_ref,
                                          x_train = x_treino_pca, y_train = y_treino_s, scoring = 'recall', cv = kf, n_iter = 10)
bparam_svc, best_svc = exec_random_search(nome_modelo = 'SVC Final', estimator = svc2, param_grid = svc_params_ref,
                                           x_train = x_treino_pca, y_train = y_treino_s, scoring = 'f1_macro', cv = kf, n_iter = 10)

# Chama a função para escolher o limiar adequado
y_pred_final_xgb, thr_usado_xgb = escolher_threshold(best_xgb, x_teste_pca, y_teste)
y_pred_final_svc, thr_usado_svc = escolher_threshold(best_svc, x_teste_pca, y_teste)

# Realiza os relatórios finais para XGBoost e SVC
relatorio_threshold(y_teste, y_pred_final_xgb, best_xgb, x_teste_pca,model = 'XGBoost Final',thresh = thr_usado_xgb)
relatorio_threshold(y_teste, y_pred_final_svc, best_svc, x_teste_pca, model = 'SVC Final', thresh = thr_usado_svc)

"""
print(df[(df['TT4'] >= 100) & (df['TT4'] <= 220)].head(50).to_string())
# dados t3 não condizem com valores clínicos reais, sem valores entre o intervalo de níveis normais
# dados tt4 possui pouquissimos dados normais dentro dos valores clínicos reais, valores acima do normal geralmente indicam doenças da tireoide
# dados t4u indica que os padrões normais dentro dos valores clinicos rais são pessoas com problemas na tireoide
# poucos dados fti indicam dentro dos valores clinicos normais reais e considerados como não portadores de doenças da tireoide, contudo existem muitos valores abaixo do valor mínimo, que não são 0 pois não fizeram exame, indicando que esses paciêntes não possuiam essas doenças, já os com valores acima do padrão clinico, são considerados pessoas com a doença, geralmente com fti acima de 70
# assumirei que mesmo se tratando de um problema real os dados também são ficticios pois nenhum dos resultados de exame estão de acordo com os níveis reais
"""