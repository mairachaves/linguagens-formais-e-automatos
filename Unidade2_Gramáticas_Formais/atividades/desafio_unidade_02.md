# Desafio Final — Gramática

Considere a seguinte gramática:

```text
G = ({S}, {a, b}, {S → aS, S → b}, S)
```

As regras de produção são:

```text
S → aS
S → b
```

A regra `S → aS` permite adicionar um `a` antes de `S`.

A regra `S → b` encerra a derivação, produzindo o símbolo `b`.

---

## 1. A palavra `b` pode ser gerada?

**Sim.**

Basta aplicar diretamente a regra:

```text
S → b
```

Portanto:

```text
b ∈ L(G)
```

---

## 2. A palavra `ab` pode ser gerada?

**Sim.**

Aplicamos primeiro `S → aS` e depois `S → b`:

```text
S
⇒ aS
⇒ ab
```

Portanto:

```text
ab ∈ L(G)
```

---

## 3. A palavra `aab` pode ser gerada?

**Sim.**

Aplicamos `S → aS` duas vezes e depois `S → b`:

```text
S
⇒ aS
⇒ aaS
⇒ aab
```

Portanto:

```text
aab ∈ L(G)
```

---

## 4. A palavra `aaab` pode ser gerada?

**Sim.**

Aplicamos `S → aS` três vezes e finalizamos com `S → b`:

```text
S
⇒ aS
⇒ aaS
⇒ aaaS
⇒ aaab
```

Portanto:

```text
aaab ∈ L(G)
```

---

## 5. A palavra `aba` pode ser gerada?

**Não.**

A gramática possui apenas duas regras:

```text
S → aS
S → b
```

Podemos adicionar vários símbolos `a`, mas quando a derivação termina, obrigatoriamente utilizamos:

```text
S → b
```

Por isso, toda palavra gerada por essa gramática **termina com `b`**.

Como a palavra `aba` termina com `a`, ela não pode ser gerada.

Portanto:

```text
aba ∉ L(G)
```

---

# 6. Derivação completa de `aaaab`

Para gerar `aaaab`, precisamos utilizar a regra `S → aS` quatro vezes e, no final, utilizar `S → b`.

A derivação é:

```text
S
⇒ aS
⇒ aaS
⇒ aaaS
⇒ aaaaS
⇒ aaaab
```

Portanto:

```text
aaaab ∈ L(G)
```

---

# 7. Identificando o padrão das palavras

Observando as palavras geradas:

```text
b
ab
aab
aaab
aaaab
aaaaab
...
```

Percebemos que todas possuem:

* zero ou mais símbolos `a`;
* exatamente um símbolo `b`;
* o símbolo `b` aparece sempre no final.

Assim, a linguagem gerada pela gramática pode ser representada por:

```text
L(G) = {aⁿb | n ≥ 0}
```

Onde `n` representa a quantidade de símbolos `a`.

### Exemplos:

```text
n = 0 → b
n = 1 → ab
n = 2 → aab
n = 3 → aaab
n = 4 → aaaab
```

---

# 8. Em palavras simples

A gramática funciona da seguinte maneira:

```text
S → aS
```

Essa regra permite colocar quantos `a` quisermos.

Quando decidimos terminar a palavra, usamos:

```text
S → b
```

Por isso, podemos pensar na gramática como:

```text
a + a + a + ... + b
```

Ou seja:

> **Podemos repetir a letra `a` quantas vezes quisermos, inclusive nenhuma, mas a palavra sempre precisa terminar com exatamente um `b`.**

### Exemplos de palavras que pertencem à linguagem:

```text
b
ab
aab
aaab
aaaab
aaaaab
```

### Exemplos de palavras que não pertencem à linguagem:

```text
a
ba
aba
abb
aabb
```

Isso acontece porque essas palavras não seguem o padrão:

```text
aⁿb
```

---

# Conclusão

A gramática:

```text
G = ({S}, {a, b}, {S → aS, S → b}, S)
```

gera exatamente as palavras que possuem **zero ou mais `a` seguidos de um único `b`**.

Portanto:

```text
L(G) = {aⁿb | n ≥ 0}
```

**Regra prática para lembrar:**

> `S → aS` = continua adicionando `a`
> `S → b` = termina a palavra com `b`
