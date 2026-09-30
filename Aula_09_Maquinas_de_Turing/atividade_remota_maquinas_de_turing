# Atividade Remota — Máquinas de Turing

**Disciplina:** Linguagens Formais e Autômatos 
**Tema:** Máquinas de Turing  

## Objetivo

Esta atividade tem como objetivo compreender o conceito de Máquina de Turing, identificar seus principais componentes, entender sua importância para a computação, realizar uma simulação simples e refletir sobre computabilidade e limites computacionais.

---

## Etapa 1 — Introdução

### 1. O que é uma Máquina de Turing?

Trata-se de um modelo teórico de computador elaborado por Alan Turing. Foi desenvolvido para representar, de maneira simples, como uma máquina pode executar uma sequência de instruções para resolver um problema.

De acordo com sua definição, uma Máquina de Turing é um modelo matemático abstrato que nos ajuda a descrever, de forma rigorosa, o que significa computação.

### 2. Quais são os principais componentes de uma Máquina de Turing?

Os principais componentes são:

- **Fita:** funciona como uma memória, dividida em várias posições onde símbolos podem ser armazenados.
- **Cabeça de leitura e escrita:** lê o símbolo presente na fita, pode apagá-lo ou substituí-lo e se movimenta para a direita ou para a esquerda.
- **Estados:** representam a situação atual da máquina durante a execução.
- **Alfabeto:** conjunto de símbolos que podem aparecer na fita, como `0`, `1` e o símbolo de espaço em branco.
- **Regras de transição:** determinam o que a máquina deve fazer de acordo com o estado atual e o símbolo encontrado na fita.

### 3. Qual é a importância das Máquinas de Turing para a computação?

A Máquina de Turing contribuiu para estabelecer as bases teóricas da Ciência da Computação. Ela nos permite compreender quais problemas podem ser resolvidos por computadores e quais não podem.

Além disso, esse conceito mostra que uma única máquina pode executar diferentes programas, ideia fundamental para o funcionamento dos computadores modernos.

Ela também contribui para o estudo dos limites da computação, pois existem problemas para os quais não existe um algoritmo capaz de produzir uma solução em todos os casos.

### 4. Qual é a relação entre Máquina de Turing e algoritmo?

Um algoritmo é uma sequência organizada de passos utilizados para resolver determinado problema. Já a Máquina de Turing é uma forma matemática de representar a execução desses mesmos passos.

As regras de transição da máquina funcionam como as instruções do algoritmo. A máquina lê um símbolo, verifica seu estado, executa uma ação e passa para outro estado. Dessa maneira, se um problema pode ser resolvido por um algoritmo, ele pode, teoricamente, ser representado por uma Máquina de Turing.

---

## Etapa 2 — Simulação

A máquina criada reconhece palavras da forma:

```text
0ⁿ1ⁿ
```

Ou seja, ela verifica se existe a mesma quantidade de símbolos `0` e `1`, com todos os `0`s aparecendo antes dos `1`s.

### Descrição da Máquina de Turing criada

A Máquina de Turing criada reconhece palavras da forma `0ⁿ1ⁿ`, verificando se há a mesma quantidade de `0`s e `1`s, com todos os `0`s aparecendo antes dos `1`s.

Para isso, ela marca os símbolos já processados e compara cada `0` com um `1` correspondente. Se todos os símbolos forem corretamente pareados, a palavra é aceita; caso contrário, é rejeitada.

### Exemplos

**Palavras aceitas:**

- `01`
- `0011`
- `000111`
- `00001111`

**Palavras rejeitadas:**

- `0`
- `1`
- `001`
- `011`
- `00111`

---

## Etapa 3 — Registro da Simulação

Os testes foram realizados no JFLAP.

| Teste | Entrada | Resultado esperado | Resultado obtido | Estados percorridos |
|---|---|---|---|---|
| 1 | `01` | ACEITA | ACEITA | `q0 → q1 → q2 → q0 → q3 → q4` |
| 2 | `000111` | ACEITA | ACEITA | `q0 → q1 → q2 → q0 → q1 → q2 → q0 → q1 → q2 → q0 → q3 → q4` |
| 3 | `00111` | REJEITA | REJEITA | `q0 → q1 → q2 → q0 → q1 → q2 → q0 → q3 → q5` |

### Teste JFLAP
<img width="762" height="445" alt="Teste JFLAP" src="https://github.com/user-attachments/assets/b097cbfc-0027-43cc-ae56-b56435e9b64f" />

---

## Etapa 4 — Reflexão sobre os limites computacionais

### Uma Máquina de Turing consegue resolver qualquer problema?

Uma Máquina de Turing não consegue resolver qualquer problema. Um de seus objetivos teóricos é justamente ajudar a compreender quais problemas podem ou não ser resolvidos por meio de algoritmos.

Existem problemas para os quais não existe nenhum algoritmo capaz de sempre chegar a uma resposta correta em um número finito de passos. Esses problemas são chamados de **não computáveis** ou **indecidíveis**.

Isso mostra que, mesmo com máquinas muito potentes e computadores muito rápidos, ainda existem limites teóricos para o que pode ser resolvido por programas.

Um exemplo clássico é o **Problema da Parada**, que pergunta se um programa irá terminar sua execução ou ficará executando para sempre. Não existe um algoritmo geral que consiga responder corretamente essa questão para todos os programas possíveis.

---

## Questão Final — Computabilidade e limites computacionais

Para saber se um problema é apenas difícil ou se realmente não pode ser resolvido por nenhum algoritmo, é preciso analisar sua **computabilidade**.

Um problema é computável quando existe uma Máquina de Turing capaz de receber qualquer entrada válida e chegar a uma resposta correta em um número finito de passos.

Se existe um algoritmo que resolve o problema, mas ele exige muito tempo ou muitos recursos, então o problema é **computável, porém difícil**.

Já quando é possível demonstrar que nenhuma Máquina de Turing consegue resolver corretamente todos os casos e sempre terminar, o problema é considerado **indecidível ou não computável**.

Esses conceitos mostram os limites computacionais: alguns problemas podem ser resolvidos, mesmo que com grande dificuldade, enquanto outros estão fora do que qualquer algoritmo pode resolver de forma geral.

Um exemplo clássico é o **Problema da Parada**, para o qual não existe um algoritmo capaz de determinar corretamente, em todos os casos, se um programa irá terminar ou continuar executando para sempre.

---

## Ferramenta utilizada

A simulação foi realizada utilizando o **JFLAP**, ferramenta voltada ao estudo de autômatos, linguagens formais e Máquinas de Turing.

---

## Conclusão

A atividade permitiu compreender o funcionamento básico de uma Máquina de Turing e sua relação com algoritmos. Também possibilitou observar, por meio da simulação, como uma máquina pode reconhecer uma linguagem específica e como os conceitos de computabilidade ajudam a compreender os limites do que pode ou não ser resolvido por computadores.
