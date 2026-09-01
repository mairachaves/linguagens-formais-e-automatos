EXERCÍCIOS PRÁTICOS DE FIXAÇÃO

🔹 Bloco 1 — Derivação

Gramática G₁:
S → aS | b

A) Gerar aaab

Derivação:

S ⇒ aS
  ⇒ aaS
  ⇒ aaaS
  ⇒ aaab

✅ Resultado: aaab

B) Quando a derivação termina?

A derivação termina quando não existem mais variáveis (não terminais) na palavra.

Neste caso:

aaaS ⇒ aaab

Como aaab possui somente símbolos terminais (a e b), a derivação terminou.

🔹 Bloco 2 — Gramática Livre de Contexto

Gramática G₂:
S → aSb | ε

A) Gerar aaabbb

S ⇒ aSb
  ⇒ aaSbb
  ⇒ aaaSbbb
  ⇒ aaaεbbb
  ⇒ aaabbb

✅ Resultado: aaabbb

B) É possível gerar aabbb?

❌ Não.

A regra S → aSb sempre acrescenta um a e um b ao mesmo tempo.

Assim:

S ⇒ aSb
  ⇒ aaSbb
  ⇒ aaεbb
  ⇒ aabb

Portanto, não é possível obter aabbb.

🔹 Bloco 3 — Classificação

Gramática:

S → aA
A → b

As regras seguem o formato de uma gramática linear à direita:

S → aA → terminal + variável
A → b → somente terminal

✅ Classificação: Gramática Regular (Tipo 3)

📝 Layout 2 — Formato de resposta acadêmica
Exercícios Práticos de Fixação — Unidade 2
1. Derivação

Dada a gramática:

G₁ = ({S}, {a,b}, {S → aS | b}, S)

a) Gere a palavra aaab

Para gerar três símbolos a, aplicamos a regra S → aS três vezes. Em seguida, utilizamos S → b.

Derivação:

S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab

Resposta: aaab

b) Explique como você sabe que a derivação terminou

A derivação termina quando não há mais símbolos não terminais na palavra.

No resultado aaab, temos somente os terminais a e b. Portanto, não existe mais nenhuma regra que possa ser aplicada.

2. Gramática Livre de Contexto

Dada a gramática:

G₂ = ({S}, {a,b}, {S → aSb | ε}, S)

a) Gere aaabbb

Derivação:

S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaaεbbb ⇒ aaabbb

Resposta: aaabbb

b) É possível gerar aabbb?

Não.

A regra S → aSb acrescenta sempre a mesma quantidade de a e b.

Com duas aplicações:

S ⇒ aSb ⇒ aaSbb ⇒ aabb

Logo, aabbb não pode ser gerada por essa gramática.

3. Classificação da Gramática

Gramática:

S → aA
A → b

As produções seguem o padrão de uma gramática regular linear à direita.

Classificação:
✅ Gramática Regular — Tipo 3

🎯 Layout 3 — Visual para GitHub/Markdown
📚 Unidade 2 — Gramáticas Formais

Exercícios Práticos de Fixação

🟦 BLOCO 1 — DERIVAÇÃO
Gramática G₁
S → aS | b
🎯 Objetivo

Gerar:

aaab
🔄 Derivação
S
↓
aS
↓
aaS
↓
aaaS
↓
aaab
✅ Resposta

Palavra gerada: aaab

💡 Por que terminou?

Porque não existem mais variáveis na palavra.

aaab

Possui somente símbolos terminais: a e b.

🟩 BLOCO 2 — GRAMÁTICA LIVRE DE CONTEXTO
Gramática G₂
S → aSb | ε
🎯 Objetivo

Gerar:

aaabbb
🔄 Derivação
S
↓
aSb
↓
aaSbb
↓
aaaSbbb
↓
aaaεbbb
↓
aaabbb
❓ É possível gerar aabbb?

Não. ❌

Isso ocorre porque:

S → aSb

sempre adiciona:

1 a + 1 b

Portanto:

2 a → 2 b

e não:

2 a → 3 b
🟥 BLOCO 3 — ESCUDO
Gramática
S → aA
A → b
🔎 Análise
Produção	Formato
S → aA	terminal + variável
A → b	terminal

As produções seguem o padrão de uma gramática regular linear à direita.

🏆 Classificação

GRAMÁTICA REGULAR — TIPO 3 ✅