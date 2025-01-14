As histórias de usuário são uma declaração de uma pequena funcionalidade que o cliente pretende ver desenvolvida no produto, ou seja, algo que o produto precisa fazer. É capturada em um cartão, não devendo ter detalhes de comportamento do produto, os quais são deixados para ser desenvolvidos mais tarde por meio de conversas e critérios de aceitação entre a equipe e o proprietário do produto.

### História de Usuário 01 - Cadastro no Sistema

#### Cartão

"Como usuário eu quero me cadastrar no sistema para que eu consiga escolher o meu curso."

#### Conversação

- O usuário pode se cadastrar de qualquer forma?
- O que é essencial para o cadastro?
- Caso falte alguma informação, o sistema deve validar os campos obrigatórios?

**Resposta:** O usuário precisa fornecer **email**, **senha** e **curso** para completar o cadastro. Campos incompletos ou inválidos devem gerar mensagens de erro.

#### Confirmação

- O usuário deverá se cadastrar fornecendo seu **endereço de e-mail**, **senha** e **curso**.

**(US01)** Como usuário, eu quero me cadastrar no sistema para que eu consiga escolher o meu curso

---

### História de Usuário 02 - Seleção de Disciplinas

#### Cartão

"Como usuário, eu quero selecionar as disciplinas que estou cursando no semestre dentro da plataforma."

#### Conversação

- O usuário pode selecionar quantas disciplinas ele quiser?
- O que acontece se o usuário estiver cursando apenas uma disciplina? Ele pode escolher apenas uma?
- O usuário busca disciplinas pelo nome ou código?
- Podemos incluir a busca por professor também?

**Resposta:** O usuário pode escolher **pelo menos uma disciplina** e a busca será feita por **nome da disciplina** ou **código**. A busca por professor não é necessária para a funcionalidade.

#### Confirmação

- O usuário poderá escolher **uma ou mais disciplinas**.
- A busca pelas disciplinas será feita através do **nome** ou **código** da disciplina.

**(US02)** Como usuário, eu quero selecionar as disciplinas que estou cursando no semestre com base no **código da disciplina** e no **nome** da disciplina.

---

#### História de Usuário 03 - Cálculo de Menção

#### Cartão

"Como usuário, eu quero receber o valor que preciso tirar em cada prova para alcançar uma menção desejada."

#### Conversação

- O usuário indica a **nota que obteve** ou o sistema calcula as **notas mínimas** necessárias?
- O sistema deve considerar diferentes formas de calcular a média: média simples, média ponderada ou outro cálculo?
- O usuário escolhe a menção que deseja ou o sistema sugere? Qual deve ser a interação?

**Resposta:** O usuário **indica** como deseja calcular a média (simples, ponderada ou personalizada), depois escolhe a **menção** desejada (MM, MS ou SS), e o sistema retornará as **notas mínimas necessárias** para alcançar a menção.

#### Confirmação

- O usuário indicará como o cálculo da média será feito (média aritmética, média ponderada ou fórmula específica).
- O usuário indicará qual menção deseja alcançar, e o sistema fornecerá as notas mínimas necessárias.

**(US03)** Como usuário, eu quero receber o valor que preciso tirar em cada prova para alcançar uma menção desejada.

---

### História de Usuário 04 - Cálculo do Índice de Rendimento Acadêmico (IRA)

#### Cartão

"Como usuário, eu quero calcular o meu Índice de Rendimento Acadêmico (IRA) com base nas disciplinas já cursadas."

#### Conversação

- O IRA será calculado com base nas **disciplinas já cursadas** ou também pode considerar disciplinas em andamento?
- O sistema deve permitir a consulta a qualquer momento, mesmo sem incluir disciplinas em andamento?

**Resposta:** O IRA será calculado apenas com base nas **disciplinas já cursadas** e **aprovadas**, com o usuário podendo consultar a qualquer momento. Disciplinas em andamento não entram no cálculo.

#### Confirmação

- O sistema calculará o **Índice de Rendimento Acadêmico (IRA)** com base nas disciplinas **já cursadas** e **aprovadas**.

**(US04)** Como usuário, eu quero calcular o meu Índice de Rendimento Acadêmico (IRA) com base nas disciplinas já cursadas.

---

### História de Usuário 05 - Gerar Calendário de Provas e Avaliações

#### Cartão

"Como usuário, eu quero gerar um calendário para acompanhar as datas das provas e avaliações acadêmicas."

#### Conversação

- O usuário tem as **datas das provas e das avaliações** previamente ou o sistema irá puxá-las de algum lugar?
- O usuário pode **adicionar ou editar** as datas manualmente?
- E quanto às **provas ou avaliações de reposição** ou outras informações extras, como tratá-las?

**Resposta:** O sistema puxará as **datas das provas e das avaliações** diretamente do **calendário acadêmico** fornecido pela instituição, mas o usuário também poderá **adicionar ou editar** as datas. O sistema também permitirá o **registro de provas e avaliações de reposição**.

#### Confirmação

- O usuário poderá **gerar um calendário** com as datas das provas, com informações fornecidas pelo **calendário acadêmico** ou inseridas manualmente pelo usuário.

**(US05)** Como usuário, eu quero gerar um calendário para acompanhar as datas das provas.

---

## História de Usuário 06 - Integração com Google Calendar

#### Cartão

"Como usuário, eu quero integrar o calendário de provas com o meu Google Calendar."

#### Conversação

- O usuário pode **sincronizar** as datas diretamente com o **Google Calendar**? Ou ele precisa adicionar as provas manualmente no calendário do Google?
- O que acontece após a integração? O usuário recebe uma **confirmação por e-mail**?

**Resposta:** O usuário poderá **integrar as datas** das provas com o **Google Calendar**, e o sistema enviará uma **confirmação por e-mail** com o link para o calendário.

#### Confirmação

- O usuário poderá **integrar** as datas das provas com o **Google Calendar**.
- O sistema enviará uma **confirmação por e-mail** com o link para o calendário integrado.

**(US06)** Como usuário, eu quero integrar o calendário de provas com o meu **Google Calendar**.
