# Exercícios Práticos para Fixação — Unidade 2

## Enunciado

| **Bloco 1 — Derivação** | **Bloco 2 — GLC** | **Bloco 3 — Classificação** |
|---|---|---|
| **Dada G₁:** `S → aS \| b` | **Dada G₂:** `S → aSb \| ε` | **Classifique como:** Regular ou Livre de Contexto |
| **A)** Gere a palavra `aaab`. | **A)** Gere a palavra `aaabbb`. | **Gramática:** `S → aA \| A → b` |
| **B)** Explique como você sabe que a derivação terminou. | **B)** É possível gerar `aabbb`? Justifique. | |

---

# Respostas aos Exercícios Práticos para Fixação

## Bloco 1 — Derivação

### A) Gere a palavra `aaab`

A gramática é:

**G = (V, T, P, S)**

Logo:

**G₁ = ({S}, {a,b}, {S → aS, S → b}, S)**

### Produções

**S → aS:** substitui `S` por `aS`, permitindo continuar a derivação, pois o `S` permanece.

**S → b:** substitui `S` por `b`, finalizando a derivação, pois não sobra nenhuma variável.

Como precisamos de três `a`, vamos precisar aplicar a produção `S → aS` três vezes e, no final, aplicar `S → b`.

### Derivação

**S ⇒ aS**

Aplicamos `S → aS`.

**aS ⇒ aaS**

Aplicamos novamente `S → aS`.

**aaS ⇒ aaaS**

Aplicamos novamente `S → aS`.

Agora temos os três `a` que precisamos. Podemos aplicar `S → b`:

**aaaS ⇒ aaab**

### Derivação completa

**S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab**

**Palavra gerada:** `aaab`

---

### B) Explique como você sabe que a derivação terminou

A derivação terminou porque a gramática possui duas regras de produção:

- **S → aS:** ainda existe `S`, portanto podemos continuar a derivação.
- **S → b:** o `S` é substituído por `b`, e não sobra nenhuma variável.

Como a palavra desejada é `aaab` e ela possui somente símbolos terminais (`a` e `b`), não existe mais nenhuma variável (não terminal), como `S`, para ser substituída.

Portanto, não é possível aplicar nenhuma outra regra de produção e **a derivação está encerrada**.

---

# Bloco 2 — Gramática Livre de Contexto (GLC)

### A) Gere a palavra `aaabbb`

A gramática é:

**G = (V, T, P, S)**

Logo:

**G₂ = ({S}, {a,b}, {S → aSb, S → ε}, S)**

### Produções

**S → aSb:** adiciona um `a` à esquerda e um `b` à direita, mantendo o `S` para continuar a derivação.

**S → ε:** substitui `S` pela palavra vazia `ε`, finalizando a derivação, pois não sobra nenhuma variável.

### Objetivo

Como precisamos de três `a` e três `b`, vamos aplicar `S → aSb` três vezes e, no final, `S → ε`.

### Derivação

**S ⇒ aSb**

Aplicamos `S → aSb`.

**aSb ⇒ aaSbb**

Aplicamos novamente `S → aSb`.

**aaSbb ⇒ aaaSbbb**

Aplicamos novamente `S → aSb`.

Agora temos os três `a` e três `b` que precisamos. Podemos aplicar `S → ε`:

**aaaSbbb ⇒ aaaεbbb ⇒ aaabbb**

Como `ε` representa a palavra vazia, ele não adiciona nenhum símbolo à palavra e permite finalizar a derivação.

### Derivação completa

**S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaaεbbb ⇒ aaabbb**

**Palavra gerada:** `aaabbb`

---

### B) É possível gerar `aabbb`? Justifique.

Não é possível gerar a palavra `aabbb` utilizando a gramática **G₂**, pois a única regra que adiciona símbolos é:

**S → aSb**

Essa regra sempre adiciona **um `a` e um `b` ao mesmo tempo**.

Para gerar dois `a`, precisamos aplicar `S → aSb` duas vezes:

**S ⇒ aSb ⇒ aaSbb**

Nesse ponto, podemos aplicar:

**S → ε**

Obtendo:

**aaSbb ⇒ aaεbb ⇒ aabb**

Portanto, conseguimos gerar:

**aabb**

mas não:

**aabbb**

Isso acontece porque, para cada `a` produzido pela regra `S → aSb`, é produzido exatamente um `b`. Logo, a quantidade de `a` e `b` deve ser sempre igual.

**Resposta:** Não é possível gerar `aabbb`.

---

# Bloco 3 — Classificação

### Classifique como Regular ou Livre de Contexto

**Gramática:**

**S → aA | A → b**

### Conceitos

Uma **Gramática Regular** é uma gramática com regras simples e restritas, que permitem gerar estruturas mais simples, normalmente mantendo a variável em uma extremidade da produção.

Uma **Gramática Livre de Contexto** permite regras mais flexíveis, sendo capaz de representar estruturas que exigem uma relação entre diferentes partes da palavra.

### Representação da gramática

Sabemos que:

**G = (V, T, P, S)**

Logo:

**G₃ = ({S,A}, {a,b}, {S → aA, A → b}, S)**

### Analisando as regras

**S → aA**

O lado esquerdo possui apenas uma variável `S` e o lado direito possui um terminal `a` seguido de uma variável `A`.

**A → b**

O lado esquerdo possui apenas uma variável `A` e o lado direito possui somente um terminal `b`.

As duas regras seguem o formato permitido por uma **Gramática Regular linear à direita**:

- **S → aA** → terminal seguido de variável.
- **A → b** → somente terminal.

### Classificação

Portanto, a gramática pode ser classificada como:

**Gramática Regular (Tipo 3).**