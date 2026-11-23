# Ética e Impactos da Inteligência Artificial: Análise e Declaração de Uso de IA

**Acadêmica:** Maira Priscila Faustino Dias Chaves  
**Professora:** Kadidja Valéria  
**Instituição:** UDF Centro Universitário  
**Disciplina:** Linguagens Formais e Autômatos (LFA)   
**Projeto:** Sistema Especialista para Tomada de Decisão na Compra de Material Escolar

## 2.2 Aspectos éticos

Nesta parte, apresento alguns cuidados éticos relacionados ao meu sistema especialista de compra de material escolar.

A coluna **“No protótipo?”** indica se a funcionalidade faz parte da versão desenvolvida ou se é uma melhoria proposta para o futuro. As classificações devem ser confirmadas na versão final do código.

### Privacidade e dados

**Situação concreta:** O sistema solicita informações como orçamento disponível, produtos escolhidos, marcas e quantidades. É importante garantir que esses dados sejam utilizados apenas para ajudar na compra. Por exemplo, se uma pessoa informar que possui R$ 50,00, esse valor deve servir para encontrar produtos dentro do orçamento.

**Quem pode ser afetado:** Estudantes, pais e responsáveis que utilizam a ferramenta.

**Medidas adotadas:**

| Medida | No protótipo? |
|---|---|
| Solicitar apenas as informações necessárias, como orçamento e produtos. | Sim |
| Permitir que o usuário inicie uma nova compra. | Sim |
| Evitar solicitar CPF, endereço e telefone. | sim |
| Não armazenar informações de compras anteriores sem necessidade. | Proposta |

### Viés e equidade

**Situação concreta:** Se um lápis Faber-Castell estiver indisponível, o sistema poderá recomendar um lápis genérico. Porém, o produto mais barato nem sempre possui as mesmas características ou qualidade.

**Quem pode ser afetado:** Estudantes, pais e responsáveis que dependem das recomendações.

**Medidas adotadas:**

| Medida | No protótipo? |
|---|---|
| Considerar o orçamento informado pelo usuário. | Sim |
| Verificar a disponibilidade dos produtos no estoque. | Sim |
| Recomendar alternativas quando o material estiver indisponível. | Sim |
| Considerar marca, preço e quantidade nas informações dos produtos. | Sim |
| Melhorar a comparação entre características e qualidade dos materiais. | Proposta |

### Transparência

**Situação concreta:** Se um caderno custa R$ 35,00 e o orçamento é de R$ 20,00, o sistema pode recomendar outro de R$ 18,00. É importante explicar que a troca foi sugerida porque o produto original ultrapassou o orçamento.

**Quem pode ser afetado:** Usuários que recebem sugestões de substituição.

**Medidas adotadas:**

| Medida | No protótipo? |
|---|---|
| Informar quando um produto estiver indisponível. | Sim |
| Identificar quando o orçamento não for suficiente. | Sim |
| Apresentar recomendações de produtos alternativos. | Sim |
| Explicar qual regra SE–ENTÃO motivou cada recomendação. | A verificar |
| Apresentar claramente preço e quantidade dos produtos recomendados. | A verificar |

### Supervisão e responsabilidade

**Situação concreta:** O sistema pode recomendar um caderno menor apenas por ser mais barato, mesmo quando o estudante precisa de um caderno de dez matérias. A recomendação pode não atender à necessidade escolar.

**Quem pode ser afetado:** Estudantes e responsáveis que utilizam o sistema.

**Medidas adotadas:**

| Medida | No protótipo? |
|---|---|
| Permitir escolher produtos para adicionar ao carrinho. | Sim |
| Permitir remover produtos do carrinho. | Sim |
| Permitir alterar a compra. | Sim |
| Apresentar alternativas quando um produto não atender ao orçamento. | Sim |
| Permitir aprovar ou rejeitar individualmente cada substituição antes de aplicá-la. | Proposta |

### Impacto social

**Situação concreta:** Famílias com orçamento limitado podem usar o sistema para encontrar materiais escolares mais econômicos. Por outro lado, uma recomendação inadequada pode levar à compra de um material que não atende ao pedido da escola.

**Quem se beneficia:** Estudantes, pais e responsáveis que precisam economizar.

**Quem pode ser prejudicado:** Usuários que recebam recomendações incorretas ou substituições inadequadas.

**Medidas adotadas:**

| Medida | No protótipo? |
|---|---|
| Recomendar produtos mais econômicos quando o orçamento for insuficiente. | Sim |
| Oferecer alternativas quando o produto estiver indisponível. | Sim |
| Permitir que o usuário informe seu orçamento. | Sim |
| Considerar a quantidade solicitada. | Sim |
| Melhorar a análise da qualidade e das características dos materiais. | Proposta |

---

## 3. Debate em sala e reflexão individual

### 3.1 Dilema ético do projeto

**Dilema:** Quando um produto está indisponível ou ultrapassa o orçamento, o sistema deve realizar a substituição automaticamente ou permitir que o usuário escolha se deseja aceitar a recomendação?

Por exemplo, se um lápis Faber-Castell estiver indisponível, o sistema pode recomendar um lápis genérico. Entretanto, essa alternativa pode não ser exatamente o que o estudante precisa.

| | Alternativa A: substituição automática | Alternativa B: confirmação do usuário |
|---|---|---|
| **Vantagens** | A compra fica mais rápida e o sistema encontra alternativas automaticamente. | O usuário avalia a recomendação e decide se aceita a troca. |
| **Consequências negativas** | O produto substituto pode não atender à necessidade do estudante. | O processo pode ser mais demorado. |

**Minha posição:** Considero a alternativa B mais adequada. O sistema deve ajudar na tomada de decisão, mas a escolha final deve continuar sendo do usuário.

### 3.2 Ideia do artigo ou do vídeo que sustenta a análise

**Ideia do artigo:** Lacerda Júnior (2026) destaca a importância de utilizar a inteligência artificial de maneira ética, transparente e responsável. Em vez de apenas permitir ou proibir seu uso, é necessário estabelecer regras claras.

**Aplicação ao meu projeto:** O sistema utiliza regras SE–ENTÃO para recomendar produtos:

- **SE** o produto solicitado estiver indisponível, **ENTÃO** procurar uma alternativa semelhante.
- **SE** o valor ultrapassar o orçamento, **ENTÃO** recomendar uma opção mais econômica.

Essas regras precisam ser aplicadas com responsabilidade, considerando não apenas o preço, mas também a necessidade do estudante. O usuário deve entender o motivo da recomendação.

**Ideia do vídeo:** No trecho de **1:53:44 a 1:54:43** de *O Estado da Arte em Ética na Inteligência Artificial*, conforme a descrição utilizada nesta atividade, destaca-se que a ética deve ser considerada desde o planejamento do sistema até as consequências de seu uso. No meu projeto, isso significa desenvolver recomendações úteis e preservar a liberdade de escolha do usuário.

### 3.3 Reflexão individual

Durante o desenvolvimento do projeto, percebi que a inteligência artificial pode ajudar a resolver problemas do dia a dia. Meu sistema especialista busca facilitar a compra de materiais escolares, principalmente para quem possui um orçamento limitado.

Também entendi que a opção mais barata nem sempre é a melhor. Um produto pode custar menos e não ter as características necessárias. Por isso, acredito que o sistema deve apresentar alternativas, mas deixar a decisão final com o usuário.

**Sobre o debate em sala:** [Acrescentar aqui um argumento realmente apresentado no debate, caso ele tenha ocorrido.]

Para avaliar o sistema, considero importante testar situações de falta de estoque, orçamento insuficiente e mudanças nas regras. Esses testes ajudam a identificar erros e melhorar as recomendações.

Aprendi que desenvolver um sistema especialista envolve não apenas programação, mas também responsabilidade pelas decisões que ele apresenta.

---

## 4. Declaração de uso de sistemas de IA

### 4.1 IA incorporada ao projeto

Meu projeto utiliza um **sistema especialista baseado em regras SE–ENTÃO**, desenvolvido em Python, para auxiliar na compra de materiais escolares. Ele considera orçamento, preço, marca, quantidade e estoque dos produtos.

O sistema possui uma base de conhecimento com informações sobre materiais escolares e regras de recomendação. O motor de inferência analisa os dados fornecidos e verifica quais regras podem ser aplicadas. Quando um produto está indisponível, pode procurar uma alternativa; quando ultrapassa o orçamento, pode sugerir outra mais econômica.

O programa permite iniciar uma compra, adicionar e remover produtos do carrinho e modificar parâmetros das regras. Trata-se de **IA simbólica baseada em regras**, sem aprendizado de máquina para gerar recomendações.

Foram definidos cenários de teste envolvendo falta de estoque, orçamento insuficiente e alterações nas regras. Entre as limitações, as recomendações dependem dos dados cadastrados e o produto mais econômico nem sempre é o mais adequado. Por isso, o sistema deve servir como apoio à decisão.

Como responsável pelo projeto acadêmico, cabe a mim compreender seu funcionamento, revisar as regras e verificar as recomendações.

### 4.2 IA utilizada na elaboração do trabalho

Durante o desenvolvimento do projeto, utilizei o **ChatGPT, da OpenAI**, como ferramenta de apoio para estruturar o código em Python, elaborar regras SE–ENTÃO, organizar a base de conhecimento e compreender o motor de inferência.

