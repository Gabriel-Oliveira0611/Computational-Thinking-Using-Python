
1
1   # Check Point 4 - (CP1 2º Semestre de 2026)
2   
3       Nome Completo:
4       RA:
5   
6   -----------------------------------------
7   
8   
9   ## COMO SALVAR O ARQUIVO:
10   
11       Use o seu primeiro nome, seguido de '_' com seu último nome, novamente '_' e seu RA. 
A extensão deste arquivo é '.zip'
12       Exemplo:
13   
14       Fulano Cricrano de Souza
15       RA 573312
16   
17       fulano_souza_573312.zip
18   
19       O mesmo para o/s arquivos extras e/ou que acharem pertinentes.
20   
21       **Façam a compactação de todos em um único arquivo 
22    e subam no ambiente que foi solicitado!**
23   
24   -----------------------------------------
25   
26   ## CP4 - Exercício 1
27   
28   Crie um módulo, chamado 'checaCadastroPet.py', que contenha os seguintes elementos:
29   
30   
31   ### 1-a) **(15 Pontos)** 
32   
Uma função que faça a verificação do número de identificação (ID) do PET, sendo que, 
este identificador deve ter 11 caracteres e a seguinte lógica:

33       Como entrada, a função deve receber:
34           - uma dicionário de listas (use a dica/"hint" para o parâmetro conforme visto em 
sala)
35           - A STRING com ID do Pet;
36           - Uma lista com nome, tipo e ano de nascimento (estes não serão testados) como 
no exemplo:
37               ["Lulu", "Cachorro", 2020]
38   
39       
40   
41       * Os 2 primeiros digitos devem ser do tipo de animal:
42           - CC para cães;
43           - GT para gatos;
44           - MM para demais mamíferos;
45           - AV para aves no geral;
46           - RP para repteis no geral;
47           - OT para outros.
48   
49       * Os 5 dígitos subsequentes são o REGISTRO sequencial (começa em 1 e não em 0);
50   
51       * os demais 4 dígitos devem ser o ano do nascimento do PET (exemplo 2024).
52   
53   
54       O ID recebido deve ser no assim (formato 1):
55   
56           'TT-IIIII-AAAA'
57   
58       Mas deve aceitar entradas sem os hífens (formato 2):
59   
60           'TTIIIIIAAAA'
61   
62   
63       ** E rejeitar quaisquer outros tipos de entrada!!! **
64   
65               - Primeiro checar o tamanho da string de entrada;
66   
67               - Primeira dica é tratar os dados de entrada começando pela diferença entre 
os formatos 1 e 2;
68   
69               - Checar o tipo usando uma lista de referência;
70   
71               - Depois checar o registro sequencial como número e se está no item 
correpondente das chaves
72                   do dicionário de entrada
73                       - Se estiver recuse;
74   
75               - Depois checar a data, como número.
76   
77   
78       Devem INDICAR os parâmetros de entrada da função (como já dito acima), bem como o 
tipo e saída!
79   
80   
81       Devem inserir o texto descritivo da função (def checaCadastroPET ...), conforme 
explicado em sala!
82   
83   
84       A SAÍDA (RETORNO) DEVE SER o proprio dicionário que entrou:
85           - Acrescido com o elemento se passar em todo o teste
86           - Ou do mesmo jeito que entrou no caso contrário
87   
88   
89   
90   ### 1-b) **(5 Pontos)**
91   
92       Crie um bloco de teste dentro do módulo, usando laço condicional e a variável 
"__name__" 
93       para testar a função usando a lista abaixo e dois IDs fornecidos abaixo:
94   
95           db_pets = {
96               ("CC","00001",2024"):
97               [
98                   'Max',
99                   'Cachorro',
100                   2024
101               ],
102               ("GT","00002",2018):
103               [
104                   'Miau',
105                   'Gato',
106                   2018
107               ],
108           }
109   
110       cadastroTeste1 = ("CC","00001",2023):
111               [
112                   'Lulu',
113                   'Cachorro',
114                   2020
115               ]
116   
117       cadastroTeste2 = ("AV","00003",2025):
118               [
119                   'Loro',
120                   'Ave',
121                   2025
122               ]
123   
124       O teste deve rodar sempre que o módulo for executado por si só, e nunca quando 
importado.
125   
126   
127   
128   -----------------------------------------
129   
130   ## CP4 - Exercício 2
131   
132   Crie um módulo, chamado 'cadastroPet.py', que contenha os seguintes elementos:
133   
134   
135   ### 2-a) **(8 pontos)**
136   
137       Criar uma função (def petCreate) para criar um cadastro de pets onde:
138   
139       Nos parâmetros de entrada, deve inserir:
140   
141           - O dicionário atual de PETS cadastrados;
142           - O tipo do PET (Por extenso: "Cachorro");
143           - O ano de nascimento do PET;
144           - O nome do PET.
145   
146       A lista de PETS cadastrados deve ser um dicionário de listas, e este deve ser 
atualizado e devolvida com o **RETURN** no programa;
147   
148       Exemplo dde dados está no arquivo petsDB.py
149   
150   
151       - Quando executar o programa, o ID deve ser atribuído automáticamente, levando em 
conta que ele é sequêncial!!!
152           Lembrem dos métodos para dicionários para facilitar!!
153   
154       - Deve também identificar o tipo do PET (dê preferência para usar uma extrutura de 
decisão do tipo macth/case, e não perca tempo com maiúsculas e minúsculas, deixe 
tudo em 'lower' case)
155   
156       USEM A FUNÇÃO " ChecaCadastroPest" ANTES DO "RETURN".
157   
158       Devem definir os parâmetros de entrada da função, que serão do tipos pertinentes, 
bem como o tipo e saída!
159   
160       Devem inserir o texto descritivo da função (def cadastroPET ...), conforme explicado 
em sala!
161   
162   
163   
164   
165   ### 2-b) **(8 pontos)**
166       Crie um procedimento (def petRead) que, ao receber a lista de cadastro de PETS, 
167    e o ID de um PET, faça a impressão dos dados de um PET cadastrado, 
168    buscando ele na lista de dicionários, pelo "ID":
169   
170       * print('Dados do seu PET: ... \n')
171       * print(f 'Nome: {nome} \n')
172       * print(f'Ano de nascimento: {ano} \n')
173       * print(f'Raça: {tipo}')
174       * print(f'ID: {id}')
175   
176       Para casos sem erros. 
177   
178       E:
179   
180       * print('O ID no PET não foi encontrado no cadastro \n')
181       * print(f'Confira os dados e tente novamente!')
182   
183       Considerendo que podem haver dois pets com mesmo nome, pensem em usar listas ou 
outras estruturas para construir a saída. 
184   
185   
186       Devem definir os parâmetros de entrada da função, que serão do tipos pertinentes, 
bem como o tipo e saída!
187   
188       Devem inserir o texto descritivo da função (def petRead ...), conforme explicado em 
sala!
