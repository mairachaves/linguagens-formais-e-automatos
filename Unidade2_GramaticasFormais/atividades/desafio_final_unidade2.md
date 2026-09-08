Desafio final
Gramática:

G
:
{
S
→
a
S
S
→
b

A palavra b pode ser gerada?
Sim.
S
→
b

A palavra ab pode ser gerada?
Sim.
S
→
a
S
→
a
b

A palavra aab pode ser gerada?
Sim.
S
→
a
S
→
a
a
S
→
a
a
b

A palavra aaab pode ser gerada?
Sim.
S
→
a
S
→
a
a
S
→
a
a
a
S
→
a
a
a
b

A palavra aba pode ser gerada?
Não.
A gramática sempre termina com b, portanto não é possível gerar uma palavra que termine em a.

Derivação completa de aaaab:

S
→
a
S
→
a
a
S
→
a
a
a
S
→
a
a
a
a
S
→
a
a
a
a
b

Padrão das palavras geradas:
A gramática gera uma ou mais letras a, seguidas de um b. Portanto:

L(G) ={a^n b | n ≥ 0}

Exemplos:

b, ab, aab, aaab, aaaab, ...

Em palavras simples: podemos repetir a quantas vezes quisermos e, no final, precisamos colocar exatamente um b.