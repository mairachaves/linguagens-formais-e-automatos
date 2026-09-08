                # Conceitos básicos de Linguagens Formais
* 1 . O que é um alfabeto Σ?
É um conjunto finito e não vazio de símbolos.
Exemplo: Σ = {a, b}.

*  que é uma cadeia?
É uma sequência finita de símbolos de um alfabeto.
Exemplo: abba é uma cadeia sobre Σ = {a, b}.

* que significa ε?
É a cadeia vazia, ou seja, uma cadeia que não possui nenhum símbolo.

* Por que |ε| = 0?
Porque ε não possui símbolos. Portanto, seu tamanho (comprimento) é 0.

* O que é um prefixo?
É uma cadeia formada pelos primeiros símbolos de outra cadeia.
Exemplo: os prefixos de abc são ε, a, ab e abc.

* O que é um sufixo?
É uma cadeia formada pelos últimos símbolos de outra cadeia.
Exemplo: os sufixos de abc são ε, c, bc e abc.

* O que significa Σ*?
É o conjunto de todas as cadeias finitas que podem ser formadas usando os símbolos de Σ, incluindo ε.
Se Σ = {a, b}:
Σ* = {ε, a, b, aa, ab, ba, bb, aaa, ...}.

* Σ* possui limite de tamanho?
Não. Embora cada cadeia individual tenha tamanho finito, podemos formar cadeias de qualquer tamanho. Portanto, Σ* é infinito.

* O que é uma linguagem formal L?
É um conjunto de cadeias definido sobre um alfabeto.
Exemplo: L = {a, ab, abb, abbb}.

* O que significa L ⊆ Σ*?
Significa que toda cadeia pertencente a L também pertence a Σ*. Ou seja, L é um subconjunto das cadeias que podem ser formadas com o alfabeto Σ.

* O que é uma gramática formal?
É um conjunto de regras que define como formar cadeias válidas de uma linguagem.

* O que são terminais e não terminais?
Terminais: símbolos que aparecem nas palavras finais. Ex.: a, b.
Não terminais: símbolos usados durante a geração das palavras. Ex.: S, A, B.
O que é uma regra de produção?
É uma regra que indica como substituir um símbolo por outros símbolos.
Exemplo: S → aS.

* Como ler S → aS | ε?
Lê-se: “S pode ser substituído por aS ou por ε.”
O símbolo | significa “ou”.

* Como gerar palavras usando uma gramática?
Começamos pelo símbolo inicial e aplicamos as regras de produção até não haver mais não terminais.

        Exemplo:

        Gramática: S → aS | ε
        Começamos com S
        S → aS
        aS → aaS
        aaS → aaaS
        aaaS → aaaε
        Resultado: aaa
    Essa gramática pode gerar: ε, a, aa, aaa, aaaa, ..., ou seja, todas as cadeias formadas apenas por a