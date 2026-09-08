# Checklist de estudo — Respostas

Antes de avançar para os próximos conteúdos, verifique se você consegue:

- [x] **Explicar o que é um alfabeto.**
  
  Um **alfabeto** é um conjunto finito e não vazio de símbolos.
  
  Exemplo:
  $\Sigma = \{a, b, c\}$
  
  Nesse caso, `a`, `b` e `c` são os símbolos do alfabeto.

- [x] **Identificar os símbolos de um alfabeto.**
  
  Os símbolos são os elementos que pertencem ao conjunto do alfabeto.
  
  Exemplo:
  $\Sigma = \{0, 1\}$
  
  Os símbolos são `0` e `1`.

- [x] **Diferenciar símbolo de palavra.**
  
  Um **símbolo** é um único elemento do alfabeto.
  
  Uma **palavra** é uma sequência finita de símbolos.
  
  Exemplo, considerando:
  $\Sigma = \{a,b\}$
  
  - `a` → símbolo
  - `b` → símbolo
  - `abba` → palavra

- [x] **Explicar o que é uma linguagem.**
  
  Uma **linguagem** é um conjunto de palavras formadas a partir de um alfabeto.
  
  Exemplo:
  $\Sigma = \{a,b\}$
  
  Podemos ter:
  $L = \{a, ab, abb, ba\}$
  
  Portanto, uma linguagem é um subconjunto de $\Sigma^*$:
  
  $L \subseteq \Sigma^*$

- [x] **Verificar se uma palavra pertence a uma linguagem.**
  
  Basta verificar se a palavra está entre os elementos da linguagem.
  
  Exemplo:
  
  $L = \{a, ab, abb\}$
  
  Então:
  
  $ab \in L$ → verdadeiro
  
  $aba \in L$ → falso
  
  Portanto, `ab` pertence à linguagem, mas `aba` não pertence.

- [x] **Interpretar $\Sigma^*$.**
  
  $\Sigma^*$ representa o conjunto de **todas as palavras finitas que podem ser formadas usando os símbolos de $\Sigma$**, incluindo a palavra vazia $\varepsilon$.
  
  Exemplo:
  
  $\Sigma = \{0,1\}$
  
  Então:
  
  $\Sigma^* = \{\varepsilon, 0, 1, 00, 01, 10, 11, 000, 001, \ldots\}$
  
  A palavra $\varepsilon$ possui tamanho zero.

- [x] **Diferenciar $\emptyset$ de $\varepsilon$.**
  
  São coisas diferentes:
  
  - $\emptyset$ → conjunto vazio, não contém nenhum elemento.
  - $\varepsilon$ → palavra vazia, possui zero símbolos.
  
  Portanto:
  
  $\emptyset \neq \varepsilon$
  
  A palavra vazia $\varepsilon$ pode pertencer a uma linguagem, por exemplo:
  
  $L = \{\varepsilon, a, aa\}$
  
  Já $\emptyset$ representa uma linguagem que não possui nenhuma palavra.

- [x] **Interpretar $w \in L$.**
  
  Significa que a palavra $w$ **pertence à linguagem $L$**.
  
  Exemplo:
  
  $L = \{a, ab, abb\}$
  
  Se:
  
  $w = ab$
  
  então:
  
  $w \in L$
  
  é verdadeiro.

- [x] **Identificar os componentes de uma gramática.**
  
  Uma gramática formal normalmente é representada por:
  
  $G = (V, \Sigma, P, S)$
  
  Onde:
  
  - $V$ → conjunto de símbolos não terminais.
  - $\Sigma$ → conjunto de símbolos terminais.
  - $P$ → conjunto de regras de produção.
  - $S$ → símbolo inicial.
  
  As regras de produção indicam como podemos substituir símbolos e construir palavras.

- [x] **Ler uma regra como $S\rightarrow aS$.**
  
  A regra:
  
  $S \rightarrow aS$
  
  significa que podemos substituir `S` por `aS`.
  
  Por exemplo:
  
  $S$
  
  usando $S\rightarrow aS$:
  
  $aS$
  
  usando novamente:
  
  $aaS$
  
  usando novamente:
  
  $aaaS$

- [x] **Realizar uma derivação passo a passo.**
  
  Considere a gramática:
  
  $S \rightarrow aS$
  
  $S \rightarrow \varepsilon$
  
  Para gerar a palavra `aaa`:
  
  $S$
  
  $\Rightarrow aS$
  
  $\Rightarrow aaS$
  
  $\Rightarrow aaaS$
  
  $\Rightarrow aaa\varepsilon$
  
  $\Rightarrow aaa$
  
  Portanto, a gramática consegue gerar `aaa`.

- [x] **Identificar quando uma derivação termina.**
  
  Uma derivação termina quando não existem mais **símbolos não terminais** na palavra.
  
  Por exemplo:
  
  $S \Rightarrow aS \Rightarrow aaS \Rightarrow aaaS \Rightarrow aaa$
  
  A derivação terminou em `aaa` porque todos os símbolos são terminais.

- [x] **Determinar se uma palavra pode ser gerada por uma gramática.**
  
  Para verificar se uma palavra pertence à linguagem gerada por uma gramática, começamos pelo símbolo inicial e tentamos aplicar as regras de produção até obter a palavra desejada.
  
  Exemplo:
  
  Gramática:
  
  $S \rightarrow aS$
  
  $S \rightarrow \varepsilon$
  
  Para verificar se `aaa` pode ser gerada:
  
  $S \Rightarrow aS \Rightarrow aaS \Rightarrow aaaS \Rightarrow aaa$
  
  Como conseguimos chegar exatamente em `aaa`, concluímos que:
  
  $aaa \in L(G)$
  
  Portanto, `aaa` pode ser gerada pela gramática.
