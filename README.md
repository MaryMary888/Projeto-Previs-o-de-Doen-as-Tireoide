# Projeto de Diagnóstico de Doenças da Glândula Tireoide
## Objetivo do Projeto
<p>As doenças da Tireoide representam um desafio relevante para a saúde 
pública, pois afetam diretamente o corpo humano e podem trazer graves
consequências, como alterações neurológicas, metabólicas, reprodutivas e 
até mesmo risco de câncer. A detecção precoce dessas alterações hormonais 
é fundamental para evitar complicações e garantir que o tratamento, seja 
iniciado de forma mais eficaz, com melhores resultados clínicos.</p>

<p>O objetivo deste projeto foi desenvolver uma ferramenta de apoio à 
tomada de decisão médica, utilizando técnicas de Aprendizado de Máquina 
para analisar dados e aumentar a precisão diagnóstica. Foram 
aplicadas estratégias como redução de dimensionalidade e otimização de 
hiperparâmetros, resultando em um modelo capaz de contribuir para 
diagnósticos mais confiáveis.</p>

<p>O trabalho também enfrentou restrições, como o tamanho limitado e o 
conjunto de dados desbalanceado, além da necessidade de interpretar os 
resultados com cautela para evitar conclusões precipitadas em um contexto 
clínico. Ainda assim, a abordagem proposta pode reduzir custos, melhorar a 
qualidade de vida dos pacientes e fortalecer estratégias de prevenção, 
tornando-se um recurso valioso tanto para profissionais da área quanto 
para o bem-estar da população.</p>

> #### **AVISOS!**
>- *Este projeto tem a utilidade apenas de informar sobre a existência de 
>alterações da gândula Tireoide, não havendo a intenção de diagnosticar 
>precisamente o tipo de doença! A variável alvo em questão (binaryClass), 
>- classifica se há (Positivo) ou não há (Negativo) presença de alguma 
>doença. A investigação mais profunda e diagnóstico final sobre a doença 
>do paciente em questão, deve ser realizada pelo profissional. Os 
>possíveis diagnósticos são: **Hipertireoidismo, Hipotireoidismo, Bócio, 
>Nódulos/Tumores e condições associadas.***
>- Os valores dos resultados dos exames são fictícios, não atendendo aos 
>níveis normais e alterados dos moldes de exames clínicos reais, porém, 
>possuem padrões próprios para identificação das doenças abordadas.

___
## Coleta de Dados
- Os dados da base foram disponibilizados na plataforma [Kaggle](https://www.kaggle.com/datasets/yasserhessein/thyroid-disease-data-set/data). 
São dados públicos disponibilizados por <b>Ross Quinlan</b> e são voltados 
principalmente para aprendizado de máquina e outras aplicações. O site da 
base original encontra-se [aqui](https://archive.ics.uci.edu/ml/datasets/Thyroid+Disease).

___
## Dados da base
<p>Abaixo, a lista inicial dos dados disponibilizados serão 
apresentados para melhor entendimento e contextualização ao longo 
do projeto:<p>

1. **SEX:** Sexo do paciente (categórico)*;
2. **AGE:** Idade do paciente (numérico);
3. **ON THYROXINE:** Se há indicador de uso de hormônio tireoidiano 
(levotiroxina) (binário)*;
4. **QUERY ON THYROXINE:** Se há dúvida ou suspeita sobre uso de 
hormônio tireoidiano (binário);
5. **ON ANTITHYROID MEDICATION:** Se há uso de medicamentos 
para reduzir a função da Tireoide (ex.: metimazol) (binário);
6. **SICK:** Se apresenta algum sintoma clínico de doença (binário);
7. **PREGNANT:** Se a paciente está grávida (binário);
8. **THYROID SURGERY:** Se há histórico de cirurgia na glândula 
Tireoide (binário);
9. **I131 TREATMENT:** Se realizou tratamento com radioiodo (Iodo radioativo). 
Usado principalmente para tratar câncer da Tireoide (binário);
10. **QUERY HYPOTHYROID:** se há suspeita de hipotireoidismo (binário);
11. **QUERY HYPERTHYROID:** se há suspeita de hipertireoidismo (binário);
12. **LITHIUM:** Se houve uso de lítio. Geralmente utilizado para 
tratamento de bipolaridade (binário);
13. **GOITRE:** Se há presença de bócio (aumento da glândula) (binário);
14. **TUMOR:** Se há presença de tumor ou nódulo na Tireoide (binário);
15. **HYPOPITUITARY:** Se há presença de hipopituitarismo (deficiência 
da hipófise que afeta hormônios gerados pela glândula) (binário);
16. **PSYCH:** se há histórico de distúrbios psiquiátricos (binário);
17. **TSH MEASURED:** indica se o exame de TSH foi realizado (binário);
18. **TSH:** Níveis do hormônio estimulante da glândula no sangue (numérico);
19. **T3 MEASURED:** indica se o exame de T3 foi realizado (binário);
20. **T3:** Níveis do hormônio triiodotironina no sangue (numérico);
21. **TT4 MEASURED:** indica se o exame de TT4 foi realizado (binário);
22. **TT4:** Valor da tiroxina total no sangue (numérico);
23. **T4U MEASURED:** indica se o exame de T4U foi realizado (binário);
24. **T4U:** Níveis de tiroxina livre presentes no sangue (numérico);
25. **FTI MEASURED:** indica se FTI foi calculado (binário);
26. **FTI:** Índice de tiroxina livre no sangue, calculados a partir 
de TT4 e T4U (numérico);
27. **TBG MEASURED:** indica se TBG foi medida (binário);
28. **TBG:** Níveis da globulina ligadora de tiroxina presente no 
sangue(numérico);
29. **REFERRAL SOURCE:** Qual a origem do encaminhamento do paciente 
(hospital, clínica, outro) (categórico);
30. **BINARYCLASS:** Variável alvo, indica se há ou não doença da 
Tireoide (binário)*.

> - *Dados **Categóricos**: variáveis textuais. No contexto desta base, a 
> categorização dos pacientes são feitas com siglas, como *referral source* 
> e *sex*.
> - *Dados **Binários**: variáveis verdadeiras ou falsas indicados nessa 
> base por T/F. Apesar de categóricas, se comportam como binárias.
>> - *A única exceção se encontra na variável binaryClass onde os dados 
>>binários são indicados como Positivo e Negativo (P/N).
___
## Tratamento dos dados
<p>Para que a base de dados seja utilizada na análise e posteriormente na 
etapa de aprendizagem dos modelos, os dados serão adaptados para valores 
numéricos e as devidas alterações na base serão realizadas de acordo com 
seu contexto.</p>

- Dados que não possuíam variedade de valores foram descartados pelos 
motivos abaixo:
    1. *TBG measured* e <b>TBG</b> serão excluídos por não ocorrerem 
    realizações do exame em nenhum paciente, não há necessidade de 
    realização deste exame para a detecção da doença em nenhum 
    caso registrado.
    2. *Hypopituitary* ou Hipopituitarismo apresenta apenas um caso 
    positivo dentre as mais de 3 mil linhas de registro de pacientes. 
    Por mais que o diagnóstico de doenças da Tireoide deste caso seja 
    positivo, não é possível levar tal dado com seriedade e 
    considerá-lo relevante para o projeto em questão, visto que este 
    representa apenas 0,026% do total de registros, não trazendo 
    robustez e confiabilidade para diagnóstico.

<p>Foram encontrados poucos erros de digitação para correção. Além 
disso, dada a enorme quantidade de dados desconhecidos, estes foram 
ajustados como necessários, como descritos abaixo:</p>

- A variável *sex* possui quase 4% dos seus dados sem especificação 
F (Feminino) ou M (Masculino). Para evitar descarte dessa porcentagem 
de linhas, a determinação do sexo de cada paciente com dados 
ausentes será feita proporcional e aleatóriamente, visto que, quase 
66% dos pacientes são mulheres e 30% são constituídos por homens. 
Antes, pacientes grávidas foram alterados manualmente para 
obrigatoriamente serem do sexo Feminino. Por fim, a variável foi 
separada em duas colunas a partir do get dummies, evitando viés e as 
transformando em binárias para melhor leitura na análise.
- Valores desconhecidos de idade dos pacientes em *age* foram 
substituídos pela média das idades registradas para manter a 
consistência e evitar enviesamento dos dados. Os erros de digitação 
das idades acima de 100 anos foram ajustadas.
- O método get_dummies também foi implementado na coluna *referral 
source* da mesma forma, evitando viés e para utilização nas análises 
posteriormente.

<p>Todos os dados referentes aos números de resultados de exame que
indicam '?' se dão pela constatação F (Falso) da variável de
realização do exame, ou seja, por constar que determinado exame não 
foi feito, não existe resultado, indicando assim o '?'. Portanto, 
para fins de análise, estes serão transformados em 0.</p>

<p>Os demais dados categóricos representados com Verdadeiro (T) e 
Falso (F) foram ajustados para se comportarem como binárias em 
valores inteiros, utilizando 1 e 0 para os respectivos valores. No 
mesmo padrão, a coluna de diagnóstico <em>binaryClass</em> com 
valores Positivo (P) e Negativo (N) foram estruturadas da mesma 
maneira com 1 e 0.</p>

<p>Por fim, após uma breve avaliação na função describe, foi possível
observar possíveis outliers não captados inicialmente na etapa de 
tratamento. Poucos valores muito acima do normal em resultados de 
exames de TSH foram devidamente corrigidos para valores abaixo de 100. 
Os padrões do diagnóstico foram levados em consideração para a 
alteração desses dados.</p>

___
## Análise Exploratória dos Dados
### Análise Univariada
<p>Nesta sessão, serão postas análises das variáveis separadamente, 
expondo pontos relevantes sobre o impacto dos dados disponíveis. </p>

#### Boxplot de age
<p>Geralmente, pacientes registrados para realização dos exames e 
recebimento do diagnóstico estão entre as idades de 36 e 67 anos, 
o que sugere que os problemas na Tireoide são mais propensos a 
aparecerem entre a fase adulta e no início da terceira idade.</p>

#### Barras de binaryClass
<p>A variável target encontra-se extremamente desbalanceada, havendo
pouca quantidade de pacientes que não foram diagnosticados com 
doenças de Tireoide, havendo necessidade de um futuro balanceamento 
desses dados para a implementação dos modelos de Aprendizado de Máquina.</p>

#### Barras de query hypothyroid
<p>Geralmente, pacientes que realizaram exames não haviam suspeitas 
de hipotireoidismo. No banco de dados, pacientes que possuem essa 
suspeita são totalizados em 234 pacientes.</p>

#### Barras de query hyperthyroid
<p>Para a suspeita de hipertireoidismo, a maioria dos pacientes não 
possuia suspeitas. No total, os registros de suspeita positiva 
foram em 237 casos.</p>

#### Barras de on thyroxine
<p>O total de pacientes que utilizam a Tiroxina é de 464, não é uma 
quantidade alta, mas é considerável e relevante para a análise.</p>

#### Barras de query on thyroxine
<p>Existem registros de 50 pacientes que possuem suspeita de 
utilizarem este medicamento. Este dado pode existir devido à 
possível omissão do paciente sobre a utilização da Tiroxina ou 
apenas um detalhe que não foi questionado pelo médico inicialmente 
no momento das consultas realizadas. O dado em questão aparenta não 
indicar relevância suficiente para o projeto, pois não se pode 
concluir se o paciente realmente estaria utilizando a medicação e, 
se o paciente estiver de fato tomando a medicação, o diagnóstico 
positivo seria algum tipo de consequência de seu uso indevido. Dado 
a justificativa e a quantidade, este item será desconsiderado no 
momento da aplicação dos modelos de Aprendizado de Máquina.</p>

#### Barras de psych
<p>184 pacientes possuem histórico psiquiátrico. Apesar de pequena 
a quantidade de registros positivos, podem ser relevantes e 
influentes para o diagnóstico de problemas na Tireoide. Muitos 
diagnósticos psiquiátricos estão diretamente relacionados a 
alterações hormonais, principalmente estes relacionados à glândula.</p>

#### Barras de TSH measured
<p>90% dos pacientes registrados realizaram exames para verificação 
dos níveis de TSH, o que indica que este exame é um fundamental 
indicador de variações relevantes nos níveis de hormônios 
produzidos pela Tireoide.</p>

#### Barras de T3 measured
<p>Aproximadamente 80% dos pacientes realizaram exames para 
verificações dos níveis do Hormônio T3. Este dado também mostra 
que o exame é um forte indicador de problemas na Tireoide, mas não 
é algo universal nos protocolos clínicos, que o incluiria dentro 
das baterias de exames, devido aos 20% dos pacientes que não 
realizaram a verificação dos níveis do hormônio em seu sistema.</p>

#### Barras de TT4 measured
<p>93% dos pacientes realizou este exame. Além de se mostrar que 
este exame é quase indispensável e padrão dentro da bateria de 
exames, é também notável que há uma confiabilidade alta para 
avaliar o funcionamento geral da Tireoide.</p>

#### Barras de T4U measured
<p>Apesar de estar altamente relacionado ao TT4, a frequência de 
pedidos de exame de T4U é levemente mais baixa, obtendo 89,7% do 
total de pacientes. Este dado pode nos mostrar que, apesar da 
diferença, também é altamente indicado para a avaliação das funções 
da Tireoide e resultam na conclusão mais precisa ao apresentar 
para o profissional da saúde.</p>

#### Barras de FTI measured
<p>Este exame, assim como os indicados acima, possui grande 
representatividade devido à quantidade de pacientes que realizaram 
os exames, também com 89,7%. Há uma grande indicação da realização 
do exame auxiliando no panorama do quadro clínico do paciente.</p>

#### Gráfico de barras de sex
<p>O sexo feminino é predominante na lista de pacientes, compondo 
68,5% do total, enquanto o sexo masculino representa 31,5% 
aproximadamente. Os dados deste banco nos indica que doenças da 
Tireoide tendem a acometer mais mulheres do que homens, 
proporcionalmente.</p>

#### Barras de tipos de Encaminhamentos
<p>É compreendido que quase 60% dos pacientes que foram em busca do 
diagnóstico de doenças da Tireoide, obtiveram encaminhamentos para 
investigação de maneiras que deveriam ser menos convencionais, indicadas 
no banco de dados dentro da categoria <b><em>Others</em></b> (Outros). 
Estes encaminhamentos podem ser feitos por conta própria, de origem 
externa como instituições que não se encontram nas redes médicas 
principais ou não identificada pela equipe médica. Em relação aos 
demais encaminhamentos, seguindo em ordem decrescente, cerca de 27% 
foram encaminhados por Institutos Médicos (SVI), 10% por indicação 
de Centros Hospitalares (SVHC), aproximadamente 0,3% por Enfermarias 
(STMW), e 0,1% por Departamentos Hospitalares Específicos (SVHD).</p>

___
### Análise Bivariada
<p>Nesta etapa, o cruzamento entre variáveis é realizado e novamente, 
levantando possíveis padrões e como se relacionam.</p>

#### Mulheres grávidas tendem a ter doenças de Tireoide?
<p>A variável pregnant é muito importante para a análise dos modelos 
de Aprendizado de Máquina, todas as mulheres registradas que constam como 
grávidas, possuem algum tipo de doença da Tireoide, podendo ser um 
fator definitivo na análise de um caso de uma paciente feminina e 
caso de teste positivo de gravidez.</p>

#### Qual fase da vida é mais propensa a desenvolver essas doenças?
<p>Apesar de existir uma quantidade considerável de jovens e adultos, 
entre 16 e 30 anos, a maior porcentagem de pacientes com diagnóstico 
de doenças da Tireoide encontra-se a partir dos 31 anos, se 
estendendo até os 75 anos. Isso indica que uma maior quantidade de 
pacientes dentro dessas faixas, não só procuram saber sobre o 
diagnóstico como também possuem diagnóstico positivo em boa parte das 
vezes, sendo por alguns sintomas ou exames anteriores que mostraram 
determinadas alterações hormonais.</p>

#### Qual a média do TSH de pacientes com doenças de Tireoide e sem? (Apenas pacientes que realizaram o exame)
<p>Pacientes que possuem diagnóstico Positivo das doenças tendem a 
possuir uma média de TSH bem mais baixa do que pacientes que não 
possuem diagnóstico destas doenças. Enquanto pessoas com 
diagnóstico Positivo têm média 1,81, o grupo Negativo apresenta 
uma média de 20,16. Lembrando que, estes dados foram levantados 
com pacientes que fizeram o exame que mede os níveis de TSH.</p>

#### Qual encaminhamento possui maior taxa de confirmação de doenças da Tireoide?
<p>Em sua maioria, a categoria others possuem maior taxa de 
encaminhamentos e por consequência uma maior quantidade de 
diagnósticos positivos. Apesar dos demais também apresentarem maioria 
de diagnóstico positivo, proporcionalmente, podemos concluir que 
esta categoria consegue identificar melhor pacientes potencialmente 
acometidos por essas doenças. Esta categoria pode abranger 
encaminhamento por consultas particulares de profissionais 
específicos, auto encaminhamento, terapêuticos, entre outros.</p>

#### Como a alteração do TSH fazem T3, FTI e TT4, T4U se comportarem?
<p>Tsh em comparação ao FTI e TT4: É possível observar que o 
comportamento dos hormônios são bem parecidos. Quanto maiores os 
níveis de TSH, menores são os níveis de FTI e TT4. Além disso, a
situação inversa ocorre da mesma maneira, ou seja, os resultados 
dos exames são inversamente proporcionais. Isso nos informa que, a 
produção elevada de um é feita para ter uma compensação do que não é 
produzido pelo outro. Isso pode nos mostrar também que existe uma 
facilidade maior em analisar possíveis desequilíbrios hormonais, 
principalmente se medirmos estes dois hormônios em conjunto com TSH.</p>

<p>Já se tratando de T3 e T4U, os níveis de ambos tendem a se manter 
mais estáveis com produção baixa, independente dos níveis de TSH no 
sangue do paciente, mesmo T3 possuindo uma oscilação levemente maior 
em seus níveis quando os níveis de TSH estão mais baixos. Em suma, 
não há relação forte entre estes dois hormônios e os níveis de TSH do 
paciente.</p>

#### Geralmente, pessoas registradas com suspeita de hipotireoidismo estão com a suspeita correta? E com hipertireoidismo?
<p>Do total de 452 suspeitas vindos da soma de ambos problemas, 400 
pacientes de fato possuíam diagnósticos positivos de algum deles. 
Dentro deste total, 234 possuem suspeitas de hipotireoidismo e foram 
confirmadas com diagnóstico positivo de presença de doenças da 
Tireoide.</p>

<p>Deste mesmo total, 222 pacientes que possuíam alguma suspeita de 
hipertireoidismo, tiveram diagnóstico positivo. Além disso, 19 
pacientes possuem suspeita de ambas doenças os quais 17 foram 
diagnosticados com positivo, porém não há especificação de qual 
delas, devido a <em>binaryClass</em> ser uma classe que apenas prevê 
Positivo e Negativo para alterações da glândula de maneira 
generalizada. Quanto aos demais que possuem apenas uma, podemos supor 
que elas estavam corretas, pelo fato do outro diagnóstico ser 
descartado por motivos específicos.</p>

#### Pessoas com histórico psiquiátrico tendem problemas na Tireoide?
<p>Apesar da maioria dos pacientes não possuírem histórico 
psiquiátrico, vemos que, de 184 pacientes, 176 possuem histórico 
psiquiátrico. Sendo assim, podemos concluir que é provável que um 
paciente que possui histórico psiquiátrico possua alguma doença da 
Tireoide, demonstrando que o dado de histórico possui relevância para 
a análise.</p>

#### Qual sexo tem maior tendência a possuir o diagnóstico?
<p>A incidência de casos Positivos para ambos os sexos é bem alta,
demonstrando maioria de pacientes com doenças de Tireoide na base, 
como indicado anteriormente. Apesar de ambos possuírem maior número 
em diagnóstico Positivo, proporcionalmente, o sexo feminino possuí 
incidência levemente maior.</p>

#### Pessoas que realizam o tratamento com iodo radioativo, costumam desenvolver doenças da Tireoide?
<p>Assim como a variável <b><em>Psych</em></b> relacionada com diagnóstico, 
existe uma probabilidade grande de pacientes que realizaram 
tratamento com iodo radioativo possuir algum tipo de doença de 
Tireoide. No total de 59 pacientes que realizaram este tratamento, 
apenas 5 deles não tem diagnóstico destas doenças.</p>

#### O lítio (usado para tratar transtorno bipolar) é um fator de risco para desenvolver doenças da Tireoide? Quantos pacientes com histórico psiquiátrico fazem uso deste medicamento? Alguém que não possuí histórico faz?
<p>Neste caso, também percebemos que há uma maioria de pacientes que 
não realizam tratamento com lítio, porém, os pacientes que utilizam 
o lítio, tem maior probabilidade de estar acometidos com alguma 
doença da Tireoide, possuindo apenas 1 paciente dentre 18 com 
resultado negativo para as doenças.</p>

<p>Apesar de ser um remédio recomendado para tratamento de 
bipolaridade e outras doenças psicológicas, geralmente diagnosticado 
por profissionais da área da psiquiatria, 15 dos 18 pacientes não 
possuem histórico psiquiátrico, mostrando que o uso é feito por conta 
própria sem avaliação médica para tal uso, insinuando que pelo menos 
14 desses pacientes estão sendo afetados pelo suposto uso indevido de 
lítio.</p>

#### O tratamento com medicação antitireoidiana está alinhado com as suspeitas de hipertireoidismo? E a tiroxina, está alinhada ao de hipotireoidismo?
<p>É visto nitidamente que, apesar de haver poucas pessoas que 
utilizam a medicação antitireoidiana, apenas 15 dos 43 pacientes 
possuem suspeita. Isso nos informa que as suspeitas não se alinham 
ao uso da medicação, visto que outros 222 pacientes possuem suspeita 
de hipertireoidismo e não estão utilizando a medicação, quase 15 
vezes a quantidade total do cenário anterior. A pequena parcela que 
usa o remédio e não tem suspeita, possívelmente se medica de maneira 
indevida.</p>

<p>Tratando-se do outro cenário para hipotireoidismo, há uma 
situação mais alarmante. Existem mais pessoas utilizando a tiroxina 
sem suspeita, do que pessoas que realmente possuem suspeita. Apesar 
da possível existência de falhas no registro da suspeita de alguns 
pacientes, se caso os pacientes estejam manuseando a tiroxina de 
maneira indevida, poderá gerar complicações no organismo, como o 
desenvolvimento de hipertireoidismo, outras alterações neurológicas 
e piora no desempenho metabólico.</p>

#### Das pessoas que possuem tumor, quantas têm doenças de Tireoide?
<p>Observamos uma quantidade pequena, totalizando 96 pacientes que 
possuem algum tipo de tumor na região da glândula, onde encontramos 
88 deles que testaram positivo para o diagnóstico de doença da 
Tireoide. É possível deduzir que, ao possuir qualquer tipo de tumor, 
em sua maioria, existe maior tendência a alterações hormonais na 
glândula, causando as doenças da glândula, não necessariamente 
importando a natureza do tumor. Pacientes que não possuem a doença e 
possuem tumor, podem estar diante de uma situação de investigação 
mais profunda para descobrir a natureza do tumor, visto que a 
possibilidade destas doenças foi descartada.</p>

<p>Os pacientes que não possuem tumor e apresentam doenças da 
Tireoide constituem maioria, totalizando 3393 casos, nos mostrando 
que as doenças surgem de maneira multifatorial.</p>

#### O bócio (goitre) parece ser associado à presença das doenças da Tireoide?
<p>Encontramos 34 pacientes com bócio, que consiste no aumento 
anormal da glândula. Todos os pacientes registrados com 
este aumento possuem alguma doença na Tireoide, indicando que este 
problema está diretamente associado com elas, podendo ser hipo, 
hipertireoidismo, nódulos ou doenças autoimunes.</p>

#### Pacientes que se medicam e tem suspeita dos cenários acima, testaram positivo para doenças da Tireoide?
<p>Extraindo apenas pacientes que possuem suspeita e que estão sendo 
medicados de ambos cenários, é percebido que todos que possuíam 
suspeitas de hipertireoidismo de fato foram diagnosticados 
positivamente com doença de Tireoide, demonstrando boa acurácia nos 
casos dessa doença. Porém, para pacientes com hipotireoidismo, não 
possuímos mesma taxa de acerto, por mais que alta, visto que 3 dos 57 
não são acometidos pela doença.</p>

<p>Estes dados reforçam a importância de saber o diagnóstico antes da 
aplicação de medicamentos. Apesar de ocorrer em uma parcela pequena 
da total de pacientes, as alterações podem ser difíceis de se 
remediar ou até mesmo irreversíveis, havendo necessidade de 
tratamento vitalício, por exemplo.</p>
  
#### Os tipos de encaminhamento realizado interferem na bateria d exames realizados para verificar o diagnóstico?
<p>O encaminhamento dos pacientes vindos de alguma unidade 
hospitalar, tendem a possuir protocolos mais padronizados nas 
baterias de exames, com pequena oscilação e boa consistência na 
quantidade de pedidos dentro do total de pacientes direcionados para 
cada um dos tipos de encaminhamento. Unidades Hospitalares como <b>STMW</b>, 
<b>SVHC</b> e <b>SVHD</b> possuem uma margem curta de pedidos não 
realizados, com <b>STMW</b> tendo de 111 pedidos de TSH até 101 para T3, 
<b>SVHC</b> com maioria de 385 pacientes realizando TT4 e 373 realizando 
T3, e em <b>SVHD</b> 39 para TSH e 36 pacientes em T3 (demais exames 
inclusos dentro das margens apresentadas).</p>

<p>A situação é diferente para as categorias <b>SVI</b> e <b><em>Other</em></b>, 
onde aparenta não existir protocolo certo ou universal, e sim que os 
exames foram feitos de maneira individual conforme o levantamento 
das suspeitas. Essas maiores diferenças ocorrem também devido à 
variedade de instituições, clinicas particulares que não seguem 
protocolos estabelecidos entre os ambientes de redes hospitalares. 
Vemos uma grande discrepância entre o exame mais e menos pedido. Em 
<b>SVI</b>, TT4 foi o exame com mais pedidos, totalizando 1030, já T3 
possui apenas 986 pacientes que realizaram este exame. A diferença se 
torna muito mais evidente na categoria <b><em>Other</em></b>, onde o exame 
TT4 tem 1978 pedidos e T3 com apenas 1507.</p>

___
## Pré-Processamento dos Dados, Modelagem e Avaliação Inicial
<p>As etapas a seguir consistem na identificação das variáveis mais bem 
relacionadas com a variável alvo, indicação dos modelos utilizados dentro 
do projeto, definição da melhor formatação dos dados para, em seguida, dar 
início às fases de teste destes modelos. A base de dados foi separada em 
bases de treino e de teste com proporção de 70% para base de treino e 30% 
para base de teste.</p>

<p>As próximas etapas de Modelagem e Avaliação Inicial dos modelos estão 
descritas abaixo.</p>

### Matriz de Correlação
<p>Existem poucas variáveis que possuem correlações mais elevadas 
com a variável alvo: TSH, TT4 e FTI. Tratando-se de correlações 
entre demais variáveis, as relações de determinadas <em>features</em> 
entre si, também aparentam relevância e podem contribuir com os resultados 
de acurácia dos modelos de Aprendizado de Máquina a serem aplicados. As 
que possuem mais variáveis correlacionadas a elas são: <em>Age, referral 
source (SVI, SVHC e Other), sick, psych,</em> exames realizados (colunas 
<em>measured</em>), resultados dos exames e <em>pregnant</em>.</p>

### Modelos Selecionados
<p>Os modelos de Aprendizado de Máquina a serem utilizados para a 
comparação de melhor desempenho serão modelos robustos que realizam 
classificações de maneiras diferentes: <b><em>XGBoost</em></b> e 
<b><em>SVC</em></b>.</p>

<p><b><em>XGBoost</em></b> é um modelo não linear que utiliza múltiplas 
árvores de decisão em sequência para que, com a correção de cada uma, 
cheguemos em um modelo final mais ideal, com maior quantidade de acertos 
mais precisos nas previsões. Já o <b><em>SVC</em></b> busca encontrar um 
hiperplano ideal que possa separar as classes de uma maneira mais clara, 
baseada na maior margem possível que o algoritmo gerar neste hiperplano, 
a partir de uma abordagem matemática sólida, melhorando assim a capacidade 
de generalização.</p>

### Padronização das bases com StandardScaler
<p>A utilização do StandardScaler é fundamental para o projeto, pois 
melhora o desempenho dos algoritmos de Aprendizado de Máquina, 
contribuindo com maior precisão, diminuindo enviesamento e trazendo maior 
equilíbrio entre valores elevados, ajudando assim algoritmos mais 
sensíveis a estas oscilações como o <b><em>SVC</em></b> e <b><em>PCA</em></b>, 
mantendo média igualada a 0 e desvio padrão em 1.</p>

### Redução de Dimensionalidade com PCA (Análise de Componentes Principais)
<p>A Redução de Dimensionalidade também é de extrema importância 
para este projeto, visto que existe uma quantidade considerável de 
variáveis que não aparentam estar bem relacionadas com a alvo, ou 
entre os demais elementos da base, conforme a Matriz de Confusão 
realça.</p>

<p>Além disso, a diminuição com o <b><em>PCA</em></b> tende a melhorar o 
desempenho, diminui o risco de <em>overfitting</em>>*, elimina 
redundâncias e é uma ferramenta útil para algoritmos sensíveis à grandes 
volumes de variáveis. A quantidade ideal encontrada para o melhor 
resultado, foi de 22 componentes dentre os 32 presentes ao final do 
tratamento.</p>

> **Overfitting*: O *overfitting* ocorre quando o modelo apenas 
> aprende os detalhes específicos presentes dentro da base de treino, 
> perdendo assim a capacidade de entender e classificar novos dados. 
> Em suma, o algoritmo decora a base de treino, não aprendendo de 
> maneira efetiva classificar bem os novos registros.

### Aplicação de Balanceamento com SMOTE 
<p>Como visualizado na fase inicial da Análise dos Dados, existe um 
grande desbalanceamento da variável alvo, onde 92,3% dos pacientes 
registrados possuem doenças da Tireoide, enquanto apenas 7.7% não tem 
o diagnóstico. Essa diferença entre as classes pode causar problemas 
de classificação da classe minoritária, assim havendo a necessidade 
de balanceá-las.</p> 

<p>Foi optado realizar a criação de linhas de pacientes fictícios 
baseado nesta minoria presente. Por isso, o SMOTE será utilizado a 
fim de igualar a quantidade de casos em ambos os grupos. Este 
procedimento é chamado de <em>oversampling</em>.</p>

### Funções
<p>A função <b><em>PLOT_ROC_AUC</em></b> tem o objetivo de gerar o 
gráfico da curva <b>ROC-AUC</b>, que avalia a capacidade do modelo de 
distinguir a classe de escolha, neste caso, a classe Positiva. Ele faz 
isso traçando a relação entre a taxa de verdadeiros positivos e a taxa de 
falsos positivos, formando uma curvatura no gráfico. A métrica AUC 
calcula a área entre a reta neutra (0.5) e a borda da curvatura. Quanto 
mais próximo este cálculo estiver de 1, melhor a excelência do algoritmo.</p>

<p>As avaliações dos modelos selecionados serão realizadas pela função 
<b><em>AVALIAR_MODS</em></b>, que realiza previsões e mostra um 
relatório de desempenho contendo valores de precisão*, sensibilidade*, 
acurácia*, <b>f1-score</b>*, além de disponibilizar uma Matriz de 
Confusão para mostrar acertos e erros de cada classe em quantidade.</p>

<p>Ao executar <b><em>EXEC_RANDOM_SEARCH</em></b> é criado uma função 
<b><em>RandomizedSearchCV</em></b> realizando uma busca das melhores 
combinações de hiperparâmetros através de arranjos aleatórios e 
selecionando o modelo que apresenta melhor desempenho.</p>

<p>A função <b><em>ESCOLHER_THRESHOLD</em></b> nos permite achar um 
<em>threshold*</em> ideal para que precisão e a sensibilidade consigam 
alcançar os valores que atendam aos critérios mínimos definidos, 
focando em um bom desempenho para a classe de diagnóstico negativo.</p>

<p>Tratando-se da função <b><em>RELATORIO_THRESHOLD</em></b>, esta 
exibe os valores de limiar escolhidos para cada um dos <em>scorings</em>* 
selecionados, além de um novo relatório de classificação que exibe os 
resultados com os limiares aplicados aos modelos, seguido da matriz 
de confusão e avaliação final da acurácia.</p>

>**Threshold* ou limiar: é o valor de corte escolhido para 
> transformar a probabilidade em uma decisão binária (classe 0 ou 1).
> 
> **Accuracy* ou Acurácia: Exibe proporção de previsões corretas em relação ao total de previsões realizadas.
> 
> **Precision* ou Precisão: Calcula a proporção de previsões positivas feitas corretamente.
> 
> **Recall* ou Sensibilidade: Mede a capacidade do algoritmo de identificar corretamente casos positivos.
>
> **F1-score*: É o cálculo da média harmônica de precisão e sensibilidade.
> 
> **Scoring*: Nesta função, é o que determina a escolha dos parâmetros para melhor favorecer o resultado da métrica escolhida.

### Modelo XGBoost: Desempenho inicial da base de teste pós-treinamento
<p>A fase de teste nos mostrou um retorno de 98% de acurácia, obtendo 99% 
nas três métricas na classe de pacientes com diagnóstico Positivo, 
indicando boa generalização desta classificação, assim como também 
exposto na curva <b>ROC-AUC</b>, onde o modelo é quase perfeito para o 
mesmo cenário, com 99%. Por outro lado, possuímos pacientes com 
diagnóstico Negativo com apenas 89% do <b>f1-score</b>, com essa média 
constituída por 84% de precisão e 93% de sensibilidade, uma diferença de 
10% de acertos entre as classes.</p>

<p>O modelo de teste possui uma quantidade desbalanceada de 1045 casos 
Positivos e 65 Negativos. Segundo a Matriz de Confusão, os valores dos 
casos verdadeiros e falsos, positivos e negativos, ressaltam uma situação 
ótima, mas que também pode ser melhorada para os casos de pacientes sem 
diagnóstico, devida à pouca quantidade de amostras da classe e quantidade 
de erros que, em proporção, implica mais dificuldade da identificação da 
classe, com 6 erros. Esta recorrência de gafes do algoritmo podem causar 
tratamentos indevidos e causar danos ao paciente, caso não apurado com 
mais cautela pelos profissionais da saúde.</p>

### Modelo SVC: Desempenho inicial da base de teste pós-treinament
<p>Na fase de teste do algoritmo em questão, percebemos uma mesma 
acurácia vista no modelo anterior, porém com a curva <b>ROC-AUC</b> 
exibindo 98% de sua área preenchida para casos positivos, 1% a menos.
Iniciando atrás de <b><em>XGBoost</em></b>, apesar de pontualmente 
superando valores de precisão totalizando 100% e 98% de sensibilidade para
classes Positivas e Negativas, respectivamente, o algoritmo peca nos valores 
de precisão da classe Negativa, com 77%, indicando desempenho menor em 
classificar casos Negativos reais, baixando o <b>f1-score</b> desta 
classificação para 86%.</p>

<p>A Matriz novamente nos revela os valores de cada previsão correta e 
incorreta, com bom desempenho no acerto dos valores negativos, apesar das 
porcentagens mais baixas nas métricas e 25 erros da classe com o 
diagnóstico, nos evidenciando a importância e necessidade de melhor 
calibrar do modelo.</p>

___
## Melhorando Desempenho dos Modelos
<p>Para tais problemas observados e potenciais riscos, visando melhora da 
qualidade e do desempenho dos acertos das classes, evitando falsos 
positivos e negativos, os algoritmos passarão por alterações nos 
hiperparâmetros, visando melhora balanceada da classe sem diagnóstico e 
diminuição de erros da classe Positiva, validação cruzada através do 
<b><em>RandomizedSearchCV</em></b> e novas comparações dos algoritmos 
ocorrerão.</p>

### Cross Validation com StratifiedKFold
<p>O <em>StratifiedKFold</em> foi utilizado para realizar separação 
da base de treino em partes iguais e aleatóriamente selecionadas, porém 
sem retirar a proporção das classes em cada uma das partes, a fim de 
manter a avaliação justa e representativa entre classes e melhorar assim 
a confiabilidade da validação cruzada ao usar <b><em>RandomizedSearchCV</em></b>. 
A melhor quantidade encontrada no decorrer dos testes foram 7 partições.</p>

### Feature Engineering
<p>Os hiperparâmetros mais relevantes foram selecionados para 
auxiliar na melhoria dos modelos em questão. Cada um especificado 
abaixo para seus respectivos modelos:</p>

> **Parâmetros XBoost:**
> - *n_estimators*: Estabelece diferentes quantidades de árvores para as combinações;
> - *max_depth*: Altera profundidade das árvores, controlando complexidade do modelo;
> - *learning_rate*: Controla a taxa de aprendizado do modelo, auxilia na melhor generalização;
> - *subsample*: Determina a fração de amostra usada em cada árvore, ajudando a controlar *overfitting*;
> - *colsample_bytree*: Determina a fração de variáveis usada na árvore;
> - *gamma*: Estipula valor mínimo de ganho de informação para que ocorra uma divisão de nó na árvore;
> - *min_child_weight*: Define peso mínimo da soma das instâncias em cada nó, controlando *overfitting*;
> - *scale_pos_weight*: Aplica pesos para dar mais importância à classe minoritária.

>**Parâmetros SVC:**
> - *C*: Regulariza penalização, mantendo ou não a rigidez dos erros;
> - *kernel*: Define como o modelo realiza a separação das classes;
> - *gamma*: Estabelece nível de influência nos pontos de treino para *kernels* não lineares;
> - *class_weight*: Também funciona aplicando peso, dando importância à classe minoritária.

### RandomizedSearchCV
<p>Para esta etapa, foi realizada a implementação de duas instâncias 
de <b><em>RandomizedSearchCV</em></b>, onde a primeira instância 
estabelece os melhores valores dos parâmetros disponibilizados e assim é 
visualizado o resultado de ambos modelos na fase de teste. Para ambos 
os modelos, inicialmente, o foco de <em>scoring</em> é melhorar 
<b>f1-score</b> utilizando <b>f1-macro</b>, para que o desempenho de 
cada classe do modelo seja calculado separadamente e traga um melhor 
balanceamento das demais métricas.</p>

### Segunda avaliação de desempenho de XGBoost
<p>Imediatamente, percebemos um aumento visível na precisão em 7%, 
enquanto em sensibilidade houve uma diminuição de mesmo valor, 
totalizando <b>f1-score</b> em 89% para a classe Negativa da mesma forma.
A Matriz de confusão expõe o dobro da quantidade de erros nesta mesma 
classe, porém, um aumento de 8 acertos na classe Positiva, apesar de 
manter os valores das métricas em 99%. A curva <b>ROC-AUC</b> também nos 
mostra um desempenho perfeito de 99% para a classe em questão.</p>

<p>Percebe-se que a Acurácia do modelo se manteve em 98% e não apresentou 
melhorias consideráveis nos valores percentuais. A Matriz de Confusão 
salienta um aumento na dificuldade de classificar casos Negativos. A fim
de melhorar a precisão do algoritmo para esse cenário, o segundo 
<b><em>RandomizedSearchCV</em></b> utilizará foco do <em>scoring</em> em 
<em>recall</em> e verificar se houve mudanças no desempenho do modelo 
de maneira positiva.</p>

### Segunda avaliação de desempenho de SVC
<p>Tratando-se do modelo <b><em>SVC</em></b>, sua Acurácia, assim como a 
curva <b>ROC-AUC</b> também se manteve estável em 98%. Houve uma clara 
mudança no desempenho da classe Negativa, diminuindo a sensibilidade 
do modelo em 24%, uma queda preocupante, além de um aumento de 16% na 
precisão. A Matriz de Confusão exibe um aumento de 21 erros na 
classificação Negativa. Por outro lado, os casos Positivos foram 
de 25 para apenas 5 erros de classificação, mostrando que o aumento 
na sensibilidade desta classe foi crucial para os acertos, mesmo que 
apenas 2%.</p>

<p>Observando o panorama, <b><em>XGBoost</em></b> ainda aparenta fazer 
melhor generalização dos dados no momento, visto que a performance da 
classe Negativa teve queda significativa de <b>f1-score</b> para 82%. Para 
escolher um modelo definitivo, a segunda implementação do 
<b><em>RandomizedSearchCV</em></b> em <b><em>SVC</em></b> terá foco de 
<em>scoring</em> novamente em <b>f1-macro</b>, por haver a necessidade de 
aumento no desempenho e melhor balanceamento na classe 0 em todos os 
aspectos levantados em análise.</p>

___
## Ajustes e Avaliação Final
<p>Para a última etapa, a busca de um limiar ideal será implementada para 
cada modelo a partir das funções <b><em>ESCOLHER_THRESHOLD</em></b> e 
<b><em>RELATORIO_THRESHOLD</em></b>. Por fim, foi realizada a segunda 
implementação do <b><em>RandomizedSearchCV</em></b>, onde os parâmetros 
serão ajustados buscando valores próximos do que foram escolhidos pela 
instância anterior, visando refiná-los e buscar melhores resultados, 
combinados com os melhores limiares a partir dos novos parâmetros. Assim, 
ambos modelos serão comparados pela última vez.</p>

### Resultados
<p>Após uma avaliação cautelosa, chegamos aos seguintes desfechos e 
decisões.</p>

#### Avaliação Final Pós-alterações XGBoost
<p>Com limiares ajustados e hiperparâmetros reestabelecidos, conseguimos 
um aumento de 2% em <b>f1-score</b>, com 87% e 97% de precisão e 
sensibilidade, respectivamente, uma melhora e um balanceamento mais 
consistente para a classe sem diagnósticos. Os erros da classe foram 
diminuídos para 3, segundo a Matriz de Confusão, uma melhora 
impressionante nesta classificação.</p> 

<p>A Matriz também demonstra um total de 13 falsos Positivos, com 6 erros 
a mais que o relatório anterior, mas uma quantidade aceitável, visto que 
precisão obteve o marco de 100 pontos percentuais nesta classe e mantendo 
a mesma pontuação nas demais métricas, revelando por fim a acurácia de 
99% do modelo, um valor bem mais consistente e ideal para implementações.</p> 

#### Avaliação Final Pós-alterações SVC
<p>O modelo final <b><em>SVC</em></b>, por outro lado, mesmo após 
refatoração dos valores de limiar e hiperparâmetros, não conseguiu 
superar os valores de <b><em>XGBoost</em></b>. A porcentagem de 
<b>f1-score</b> se manteve abaixo com 86%, resultado de uma precisão de 
83% e sensibilidade de 90% na classe minoritária. A Matriz ainda mostra 
uma melhora nos acertos, porém a proporção permite concluir que a 
quantidade de erros não é ideal.</p>

<p>Enquanto isso, a classe que compõe maioria de amostras se mantém com 
valores entre 98% e 99%, finalizando estacionado com acurácia em 98% e 
erros na identificação de positivos em 16 casos.</p>

### Tomada de Decisão Referente ao uso dos Modelos
<p>É chegada à definição de que, por possuír valores melhores e mais 
balanceados, dentro dos padrões ótimos, dentro de proporções de acertos e 
erros, que o algoritmo de Aprendizado de Máquina XGBoost é o 
mais adequado para implementação, por mostrar maior confiabilidade em 
ambas as classificações da base de dados.</p>

### Conclusões
<p>O projeto de Diagnóstico de Doenças da Tireoide demonstrou a 
importância do uso de técnicas de Aprendizado de Máquina para apoiar 
decisões médicas, oferecendo maior precisão e rapidez na identificação de 
pacientes em risco.</p>

<p>Após a análise comparativa de diferentes modelos, o XGBoost se mostrou 
o mais eficiente, garantindo melhor equilíbrio entre métricas. Para 
potencializar os resultados, aplicamos redução de dimensionalidade com 
<b><em>PCA</em></b>, otimizamos hiperparâmetros através da função 
<b><em>RandomizedSearchCV</em></b> e registramos os melhores parâmetros 
para futura replicação.</p>

<p>Compreende-se que esse grande leque de artifícios não só aumentaram a 
confiabilidade do diagnóstico, mas também forneceram uma base sólida para 
aplicações clínicas e pesquisas futuramente, reforçando o papel deste 
recurso como aliado dos profissionais da área da saúde.</p>