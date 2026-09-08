Parte 1 — Fundamentos
Exercício 1 — Entendendo um autômato finito

A lâmpada possui dois estados:

Desligado
Ligado

A cada acionamento do botão, ocorre uma mudança de estado.

1. Quantos estados existem?

Existem 2 estados:

Q = {Desligado, Ligado}
2. Qual é o estado inicial?

O estado inicial é:

Desligado

pois a lâmpada começa apagada.

3. Qual entrada provoca uma transição?

A entrada é:

pressionar

Cada vez que o botão é pressionado, ocorre uma transição.

4. Partindo de Desligado, qual será o estado após um acionamento?
Desligado --pressionar--> Ligado

Portanto, após um acionamento, a lâmpada estará Ligada.

5. Partindo de Desligado, qual será o estado após dois acionamentos?

Primeiro acionamento:

Desligado --pressionar--> Ligado

Segundo acionamento:

Ligado --pressionar--> Desligado

Portanto, após dois acionamentos, a lâmpada estará Desligada.

6. Explique o funcionamento

O sistema possui dois estados e uma única entrada. O acionamento do botão sempre provoca a mudança para o estado oposto. Assim, quando a lâmpada está desligada, pressionar o botão faz com que ela seja ligada; quando está ligada, pressionar novamente faz com que seja desligada.

Exercício 2 — Porta automática

A porta possui dois estados:

Fechado
Aberto

O comportamento depende da presença ou ausência de uma pessoa.

Tabela de transição
Estado atual	Entrada	Próximo estado
Fechado	pessoa_detectada	Aberto
Fechado	nenhuma_pessoa	Fechado
Aberto	pessoa_detectada	Aberto
Aberto	nenhuma_pessoa	Fechado
Estado inicial

O estado inicial é:

Fechado
Diagrama
                 pessoa_detectada
          ┌─────────────────────────┐
          │                         ▼
       → (Fechado) ─────────────> ((Aberto))
          ▲   │                       │
          │   │ nenhuma_pessoa        │
          │   │                       │
          └───┘                       │
              ▲                       │
              └──── nenhuma_pessoa ───┘

De forma mais organizada:

→ Fechado --pessoa_detectada--> Aberto
  Fechado --nenhuma_pessoa----> Fechado

  Aberto --pessoa_detectada----> Aberto
  Aberto --nenhuma_pessoa------> Fechado

O estado inicial é Fechado.

Parte 2 — Anatomia e definição formal
Exercício 3 — Identificando os elementos

Temos:

Σ = {0,1}

Q = {q0,q1}

Estado inicial = q0

F = {q1}

Tabela:

δ	0	1
q0	q0	q1
q1	q0	q1
1. Alfabeto Σ

O alfabeto é:

Σ = {0,1}

Isso significa que o autômato pode receber somente os símbolos 0 e 1.

2. Conjunto de estados Q
Q = {q0,q1}

O autômato possui dois estados.

3. Estado inicial

O estado inicial é:

q0

É o estado em que o processamento começa.

4. Conjunto de estados finais
F = {q1}

Portanto, q1 é o único estado de aceitação.

5. Símbolos que podem ser lidos

Os símbolos são:

0 e 1
6. Significado do círculo duplo

No diagrama de um AFD, um círculo duplo representa um estado final ou estado de aceitação.

Se o processamento da cadeia terminar nesse estado, a cadeia é aceita.

7. Significado da seta sem origem

A seta sem origem representa a seta de estado inicial.

Ela indica em qual estado o processamento começa.

Exercício 4 — A quíntupla do AFD

Um AFD é representado por:

M = (Σ, Q, δ, q0, F)
Elemento	Significado
Σ	Alfabeto de entrada
Q	Conjunto finito de estados
δ	Função de transição
q0	Estado inicial
F	Conjunto de estados finais
Explicação

Esses cinco elementos são suficientes para definir um AFD porque:

Σ informa quais símbolos podem ser recebidos;
Q informa quais estados existem;
δ determina para qual estado o autômato deve ir ao receber cada símbolo;
q0 determina onde o processamento começa;
F determina quais estados representam aceitação.

Como o AFD é determinístico, para cada estado e cada símbolo existe exatamente um próximo estado.

Parte 3 — Tabela de transições e cadeias
Exercício 5 — Interpretando uma tabela

Temos:

Σ = {0,1}

Q = {q0,q1,q2}

q0 = estado inicial

F = {q1}

Tabela:

δ	0	1
q0	q0	q1
q1	q2	q1
q2	q1	q1
1. δ(q0,0)

Consultando a linha q0 e a coluna 0:

δ(q0,0) = q0
2. δ(q0,1)
δ(q0,1) = q1
3. δ(q1,0)
δ(q1,0) = q2
4. δ(q2,1)
δ(q2,1) = q1
5. Estado de aceitação

O conjunto de estados finais é:

F = {q1}

Portanto:

q1 = estado de aceitação
6. Diagrama
                 1
              ┌──────┐
              ▼      │
          → (q0) ──1──> ((q1))
             ▲           │  ▲
             │           │  │1
             │0          │0 │
             │           ▼  │
             └───────── (q2)
                          │
                          │1
                          └────> ((q1))

Uma representação completa das transições:

→ q0 --0--> q0
  q0 --1--> q1

  q1 --0--> q2
  q1 --1--> q1

  q2 --0--> q1
  q2 --1--> q1
7. Por que o autômato é determinístico?

Ele é determinístico porque, para cada combinação de estado e símbolo de entrada, existe exatamente uma transição possível.

Por exemplo:

δ(q0,0) = q0
δ(q0,1) = q1

Não existem duas possibilidades para a mesma entrada partindo do mesmo estado.

Exercício 6 — Aceita ou rejeita?

Utilizaremos o AFD do exercício anterior:

δ	0	1
q0	q0	q1
q1	q2	q1
q2	q1	q1

Estado inicial:

q0

Estado final:

q1
a) Cadeia 1

Começamos em q0.

q0 --1--> q1

Estado final:

q1

Como q1 é final:

Resultado: ACEITA

b) Cadeia 0011001

Processamento:

q0 --0--> q0
q0 --0--> q0
q0 --1--> q1
q1 --1--> q1
q1 --0--> q2
q2 --0--> q1
q1 --1--> q1

Estado final:

q1

Como q1 é final:

Resultado: ACEITA

c) Cadeia 010010
q0 --0--> q0
q0 --1--> q1
q1 --0--> q2
q2 --0--> q1
q1 --1--> q1
q1 --0--> q2

Estado final:

q2

q2 não é estado final.

Resultado: REJEITA

d) Cadeia 1101
q0 --1--> q1
q1 --1--> q1
q1 --0--> q2
q2 --1--> q1

Estado final:

q1

Como q1 é final:

Resultado: ACEITA

e) Cadeia 000011010
q0 --0--> q0
q0 --0--> q0
q0 --0--> q0
q0 --0--> q0
q0 --1--> q1
q1 --1--> q1
q1 --0--> q2
q2 --1--> q1
q1 --0--> q2

Estado final:

q2

q2 não é final.

Resultado: REJEITA

Tabela final
Cadeia	Caminho percorrido	Estado final	Resultado
1	q0 → q1	q1	ACEITA
0011001	q0 → q0 → q0 → q1 → q1 → q2 → q1 → q1	q1	ACEITA
010010	q0 → q1 → q2 → q1 → q1 → q2	q2	REJEITA
1101	q0 → q1 → q1 → q2 → q1	q1	ACEITA
000011010	q0 → q0 → q0 → q0 → q0 → q1 → q1 → q2 → q1 → q2	q2	REJEITA
Parte 4 — Construção de AFDs
Exercício 7 — Cadeias que terminam em 1

Queremos reconhecer:

L = {w ∈ {0,1}* | w termina em 1}

A ideia é simples: precisamos saber apenas se o último símbolo lido foi 1 ou não.

Estados
Q = {q0,q1}

Significado:

q0: a cadeia está vazia ou o último símbolo lido é 0;
q1: o último símbolo lido é 1.
Alfabeto
Σ = {0,1}
Estado inicial
q0
Estado final
F = {q1}
Tabela
δ	0	1
q0	q0	q1
q1	q0	q1
Diagrama
                  1
          ┌───────────────┐
          │               ▼
       → (q0) --1--> ((q1))
          ▲              │
          │              │ 1
          │              └──┐
          │                 │
          └------ 0 --------┘

De forma simplificada:

→ q0 --0--> q0
  q0 --1--> q1

  q1 --0--> q0
  q1 --1--> q1
Definição formal
M = (Σ,Q,δ,q0,F)

Σ = {0,1}
Q = {q0,q1}
q0 = q0
F = {q1}
Testes
1
q0 --1--> q1

Termina em q1.

ACEITA

01
q0 --0--> q0
q0 --1--> q1

ACEITA

101
q0 --1--> q1
q1 --0--> q0
q0 --1--> q1

ACEITA

0001
q0 --0--> q0
q0 --0--> q0
q0 --0--> q0
q0 --1--> q1

ACEITA

1101
q0 --1--> q1
q1 --1--> q1
q1 --0--> q0
q0 --1--> q1

ACEITA

Exemplos rejeitados

0:

q0 --0--> q0

REJEITA

10:

q0 --1--> q1
q1 --0--> q0

REJEITA

100:

q0 --1--> q1
q1 --0--> q0
q0 --0--> q0

REJEITA

1110:

q0 --1--> q1
q1 --1--> q1
q1 --1--> q1
q1 --0--> q0

REJEITA

Exercício 8 — Número par de símbolos 1

Precisamos reconhecer todas as cadeias que possuem uma quantidade par de 1s.

Precisamos controlar apenas duas situações:

quantidade par de 1s;
quantidade ímpar de 1s.
Estados
Q = {qPar,qImpar}

qPar significa que a quantidade de 1s lidos até aquele momento é par.

qImpar significa que a quantidade de 1s lidos até aquele momento é ímpar.

Alfabeto
Σ = {0,1}
Estado inicial
qPar

A quantidade inicial de 1s é zero, e zero é par.

Estado final
F = {qPar}
Tabela
δ	0	1
qPar	qPar	qImpar
qImpar	qImpar	qPar

O 0 não altera a quantidade de 1s.

O 1 troca a situação de par para ímpar ou de ímpar para par.

Diagrama
                  1
          ┌───────────────┐
          │               ▼
       → ((qPar))       (qImpar)
          ▲               │
          │               │
          └────── 1 ──────┘

qPar --0--> qPar
qImpar --0--> qImpar
Definição formal
M = (Σ,Q,δ,q0,F)

Σ = {0,1}

Q = {qPar,qImpar}

q0 = qPar

F = {qPar}
Processamento das cadeias
ε

Não há símbolos para processar.

qPar

Como qPar é final:

ACEITA

0
qPar --0--> qPar

ACEITA

1
qPar --1--> qImpar

qImpar não é final.

REJEITA

11
qPar --1--> qImpar
qImpar --1--> qPar

ACEITA

101
qPar --1--> qImpar
qImpar --0--> qImpar
qImpar --1--> qPar

Possui dois 1s.

ACEITA

1100
qPar --1--> qImpar
qImpar --1--> qPar
qPar --0--> qPar
qPar --0--> qPar

Possui dois 1s.

ACEITA

10101
qPar --1--> qImpar
qImpar --0--> qImpar
qImpar --1--> qPar
qPar --0--> qPar
qPar --1--> qImpar

Possui três 1s.

REJEITA

Resultado
Cadeia	Quantidade de 1s	Estado final	Resultado
ε	0	qPar	ACEITA
0	0	qPar	ACEITA
1	1	qImpar	REJEITA
11	2	qPar	ACEITA
101	2	qPar	ACEITA
1100	2	qPar	ACEITA
10101	3	qImpar	REJEITA
Exercício 9 — Pelo menos dois zeros consecutivos

Queremos reconhecer:

L(M) = {w ∈ {0,1}* | w possui pelo menos dois 0s consecutivos}

A estratégia será acompanhar se:

ainda não encontramos 0;
encontramos um 0, mas ele ainda não foi seguido por outro 0;
encontramos 00;
depois de encontrar 00, a cadeia permanece aceita.
1. O que o estado inicial representa?

Representa que ainda não encontramos um 0 isolado que possa iniciar a sequência 00.

Chamaremos esse estado de q0.

2. O que ocorre quando aparece o primeiro 0?

Passamos para q1.

q0 --0--> q1

Isso significa que acabamos de encontrar um 0.

3. O que ocorre quando outro 0 aparece imediatamente depois?

Passamos para q2.

q1 --0--> q2

Nesse momento encontramos 00.

4. Depois de encontrar 00, a cadeia pode deixar de ser aceita?

Não.

Depois que 00 foi encontrado, não importa quais símbolos apareçam posteriormente: a cadeia continuará contendo 00.

Por isso, q2 possui loops para 0 e 1.

5. Quantos estados são necessários?

São necessários 3 estados:

q0 = nenhum 0 relevante encontrado
q1 = um 0 foi encontrado
q2 = encontramos 00
Definição formal
M = (Σ,Q,δ,q0,F)

onde:

Σ = {0,1}

Q = {q0,q1,q2}

q0 = q0

F = {q2}
Tabela de transição
δ	0	1
q0	q1	q0
q1	q2	q0
q2	q2	q2
Diagrama
                    0
       ┌─────────────────────────┐
       │                         │
       ▼                         │
→ (q0) --0--> (q1) --0--> ((q2))
   ▲            │                 │
   │            │1                │
   └──── 1 ─────┘                 │
                                  │
                         0,1 ─────┘
Testes
00
q0 --0--> q1
q1 --0--> q2

ACEITA

001
q0 --0--> q1
q1 --0--> q2
q2 --1--> q2

ACEITA

100
q0 --1--> q0
q0 --0--> q1
q1 --0--> q2

ACEITA

1001
q0 --1--> q0
q0 --0--> q1
q1 --0--> q2
q2 --1--> q2

ACEITA

110011
q0 --1--> q0
q0 --1--> q0
q0 --0--> q1
q1 --0--> q2
q2 --1--> q2
q2 --1--> q2

ACEITA

0000
q0 --0--> q1
q1 --0--> q2
q2 --0--> q2
q2 --0--> q2

ACEITA

ε

Nenhuma transição é realizada.

q0

REJEITA

0
q0 --0--> q1

REJEITA

1
q0 --1--> q0

REJEITA

01
q0 --0--> q1
q1 --1--> q0

REJEITA

10
q0 --1--> q0
q0 --0--> q1

REJEITA

10101
q0 --1--> q0
q0 --0--> q1
q1 --1--> q0
q0 --0--> q1
q1 --1--> q0

REJEITA

Parte 5 — Desafios de modelagem
Exercício 10 — Semáforo

O sistema possui três estados:

Verde
Amarelo
Vermelho

A entrada é:

tempo

A cada ocorrência de tempo, o semáforo avança para o próximo estado.

Tabela
Estado atual	Entrada	Próximo estado
Verde	tempo	Amarelo
Amarelo	tempo	Vermelho
Vermelho	tempo	Verde
Estado inicial

Consideraremos:

Verde

como estado inicial.

Diagrama
           tempo
      ┌──────────────┐
      ▼              │
→ [Verde] ─tempo─> [Amarelo]
                     │
                     │ tempo
                     ▼
                 [Vermelho]
                     │
                     │ tempo
                     └────────> [Verde]
Definição formal
M = (Σ,Q,δ,q0,F)

onde:

Σ = {tempo}

Q = {Verde,Amarelo,Vermelho}

q0 = Verde

F = ∅
Por que não existem estados de aceitação?

Nesse modelo, o objetivo não é reconhecer uma linguagem ou determinar se uma sequência de entradas é válida. O objetivo é representar a evolução de um sistema físico entre diferentes estados.

Portanto, não há necessidade de estados finais.

Usamos:

F = ∅

porque nenhum estado representa uma condição de aceitação.

Exercício 11 — Sistema de login

Temos duas entradas:

senha_correta
senha_incorreta

O sistema deve bloquear o usuário após três tentativas incorretas.

Para contar as tentativas, precisamos saber quantas tentativas incorretas consecutivas já ocorreram.

1. Estados necessários

Podemos utilizar:

q0 = Aguardando, 0 erros
q1 = Aguardando, 1 erro
q2 = Aguardando, 2 erros
q3 = Autenticado
qB = Bloqueado

Assim conseguimos diferenciar:

nenhuma tentativa incorreta;
uma tentativa incorreta;
duas tentativas incorretas;
autenticação;
bloqueio.
2. Alfabeto
Σ = {senha_correta, senha_incorreta}
3. Estado inicial
q0
4. Estados finais

Para este modelo, podemos considerar:

F = {q3}

pois q3 representa que o usuário foi autenticado.

qB não é estado final porque estar bloqueado não representa sucesso.

5. Todas as transições
Estado	senha_correta	senha_incorreta
q0	q3	q1
q1	q3	q2
q2	q3	qB
q3	q3	q3
qB	qB	qB
Interpretação

A partir de q0:

senha_correta → q3
senha_incorreta → q1

Após uma tentativa incorreta, estamos em q1.

senha_correta → q3
senha_incorreta → q2

Após duas tentativas incorretas, estamos em q2.

senha_correta → q3
senha_incorreta → qB

A terceira tentativa incorreta provoca o bloqueio.

Depois da autenticação:

q3 --senha_correta--> q3
q3 --senha_incorreta--> q3

O sistema permanece autenticado.

Depois do bloqueio:

qB --senha_correta--> qB
qB --senha_incorreta--> qB

O sistema permanece bloqueado.

6. Apenas três estados seriam suficientes?

Não.

Os estados:

Aguardando
Autenticado
Bloqueado

não são suficientes porque o sistema precisa distinguir entre zero, uma e duas tentativas incorretas.

Se existisse apenas um estado Aguardando, não seria possível saber se a próxima senha incorreta corresponde à primeira, segunda ou terceira tentativa.

Portanto, são necessários estados intermediários para armazenar essa informação.

Diagrama
                     senha_correta
              ┌──────────────────────────┐
              │                          ▼
→ (q0) --senha_incorreta--> (q1) --senha_incorreta--> (q2)
   │                           │                         │
   │                           │                         │
   └──── senha_correta ────────┴──── senha_correta ─────┘
                               │
                               ▼
                             ((q3))
                               ↺
                         senha_correta,
                         senha_incorreta


q2 --senha_incorreta--> (qB)
                         ↺
                  senha_correta,
                  senha_incorreta
Parte 6 — Prática no JFLAP
Exercício 12 — Implementação e testes

Para facilitar, recomendo implementar no JFLAP o Exercício 7, pois é o AFD mais simples.

O objetivo é reconhecer cadeias que terminam em 1.

Estados
q0
q1
Estado inicial
q0
Estado final
q1
Transições
q0 --0--> q0
q0 --1--> q1
q1 --0--> q0
q1 --1--> q1
Testes
Cadeia	Resultado esperado	Resultado no JFLAP	Conferência
1	ACEITA	ACEITA	✓
01	ACEITA	ACEITA	✓
101	ACEITA	ACEITA	✓
0	REJEITA	REJEITA	✓
10	REJEITA	REJEITA	✓
1110	REJEITA	REJEITA	✓

Desafio final — Exercício 13

Vou escolher controle de acesso por senha porque é uma situação real e permite demonstrar bem o conceito de AFD.

Problema escolhido

Um sistema eletrônico de controle de acesso recebe uma senha. O sistema possui duas possibilidades de entrada:

senha_correta
senha_incorreta

Quando a senha correta é informada, o acesso é liberado.

Se o usuário errar a senha três vezes, o sistema é bloqueado.

O sistema começa aguardando a primeira tentativa.

Estados e significado
Estado	Significado
q0	Aguardando, nenhuma tentativa incorreta
q1	Uma tentativa incorreta
q2	Duas tentativas incorretas
q3	Acesso autorizado
qB	Sistema bloqueado
Alfabeto
Σ = {senha_correta, senha_incorreta}
Estado inicial
q0
Estado final
F = {q3}

O estado q3 representa o acesso autorizado.

Tabela de transições
δ	senha_correta	senha_incorreta
q0	q3	q1
q1	q3	q2
q2	q3	qB
q3	q3	q3
qB	qB	qB
Diagrama
                         senha_correta
                   ┌─────────────────────┐
                   │                     ▼
                → (q0) ──senha_incorreta──> (q1)
                   │                          │
                   │                          │ senha_incorreta
                   │                          ▼
                   │                         (q2)
                   │                          │
                   │                          │ senha_incorreta
                   │                          ▼
                   │                         (qB)
                   │
                   └──── senha_correta ─────> ((q3))


q1 --senha_correta--> q3
q2 --senha_correta--> q3

q3 --senha_correta------> q3
q3 --senha_incorreta----> q3

qB --senha_correta------> qB
qB --senha_incorreta----> qB
Definição formal
M = (Σ,Q,δ,q0,F)

onde:

Σ = {senha_correta, senha_incorreta}

Q = {q0,q1,q2,q3,qB}

q0 = q0

F = {q3}

A função de transição é definida pela tabela apresentada anteriormente.

Testes realizados
Teste 1 — Senha correta na primeira tentativa

Entrada:

senha_correta

Processamento:

q0 --senha_correta--> q3

Estado final:

q3

Resultado:

ACEITA — acesso autorizado.

Teste 2 — Um erro e depois senha correta

Entrada:

senha_incorreta, senha_correta

Processamento:

q0 --senha_incorreta--> q1
q1 --senha_correta----> q3

Resultado:

ACEITA — acesso autorizado.

Teste 3 — Dois erros e depois senha correta
q0 --senha_incorreta--> q1
q1 --senha_incorreta--> q2
q2 --senha_correta----> q3

Resultado:

ACEITA — acesso autorizado.

Teste 4 — Três erros consecutivos
q0 --senha_incorreta--> q1
q1 --senha_incorreta--> q2
q2 --senha_incorreta--> qB

Resultado:

REJEITA — sistema bloqueado.

Teste 5 — Sistema bloqueado e nova senha correta
q0 --senha_incorreta--> q1
q1 --senha_incorreta--> q2
q2 --senha_incorreta--> qB
qB --senha_correta----> qB

Mesmo informando a senha correta depois do bloqueio, o sistema permanece em qB.

Resultado:

REJEITA — sistema continua bloqueado.

Tabela de testes
Entrada	Resultado esperado	Resultado obtido
senha_correta	ACEITA	ACEITA
senha_incorreta, senha_correta	ACEITA	ACEITA
senha_incorreta, senha_incorreta, senha_correta	ACEITA	ACEITA
senha_incorreta, senha_incorreta, senha_incorreta	REJEITA	REJEITA
senha_incorreta, senha_incorreta, senha_incorreta, senha_correta	REJEITA	REJEITA