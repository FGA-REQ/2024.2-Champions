As histórias de usuário são uma declaração de uma pequena funcionalidade que o cliente pretende ver desenvolvida no produto, ou seja, algo que o produto precisa fazer. É capturada em um cartão, não devendo ter detalhes de comportamento do produto, os quais são deixados para ser desenvolvidos mais tarde por meio de conversas e critérios de aceitação entre a equipe e o proprietário do produto.

### História de Usuário 01 - Acesso do Usuário no Sistema

#### Cartão

"Eu como usuário quero poder acessar o sistema para que eu consiga gerenciar as minhas disciplinas"

#### Conversação

- O usuário pode se cadastrar de qualquer forma?
- O que é essencial para o cadastro?
- O usuário pode recuperar a senha?
- O usuário pode fazer login de que forma?
- Caso falte alguma informação, o sistema deve validar os campos obrigatórios?

**Resposta:**

O usuário precisa fornecer **email** e **senha** para completar o cadastro.

O usuário caso esqueça a senha pode recuperá-la, fornecendo seu **email**, sua **nova senha** e **confirmação da nova senha**.

O usuário pode fazer login no sistema fornecendo seu **email** e **senha**.

Campos incompletos ou inválidos devem gerar mensagens de erro.

#### Confirmação

- O usuário deverá acessar o sistema fornecendo seu **endereço de e-mail** e **senha**.

**(US01)** Eu como usuário quero acessar o sistema para que eu consiga gerenciar as minhas disciplinas.

---

### História de Usuário 02 - Gerenciamento de Disciplinas

#### Cartão

"Eu como usuário quero poder gerenciar as disciplinas que estou cursando no semestre dentro da plataforma."

#### Conversação

- O usuário pode selecionar quantas disciplinas ele quiser?
- O que acontece se o usuário estiver cursando apenas uma disciplina? Ele pode escolher apenas uma?
- O usuário busca disciplinas pelo nome ou código?
- Podemos incluir a busca por professor também?
- O usuário poderá cadastrar disciplinas no sistema?
- O usuário poderá visualizar a disciplina?
- O usuário poderá remover a disciplina?

**Resposta:**

O usuário pode escolher **pelo menos uma disciplina** e a busca será feita por **nome da disciplina** ou **código**. A busca por professor não é necessária para a funcionalidade.

O usuário **não poderá** cadastrar nenhuma disciplina, isso será feito com um serviço de Webscraping do site do SIGAA.

O usuário poderá **visualizar** a disciplina para que possa efetuar as operações disponíveis no sistema.

O usuário também poderá **remover** a disciplina do seu menu de disciplinas.

#### Confirmação

- O usuário poderá escolher **uma ou mais disciplinas**.
- A busca pelas disciplinas será feita através do **nome** ou **código** da disciplina.
- O usuário não poderá cadastrar disciplinas novas.
- O usuário poderá visualizar a disciplina.
- O usuário poderá remover as disciplinas.

**(US02)** Como usuário, eu quero poder gerenciar as disciplinas que estou cursando dentro do meu semstre.

---

### História de Usuário 03 - Cálculo de Menção e de Média

#### Cartão

"Eu como usuário quero saber minhas médias parciais e totais das disciplinas que estou cursando e ao final do semestre ver a menção."

#### Conversação

- O usuário indica a **nota que obteve** ou o sistema calcula as **notas mínimas** necessárias?
- O sistema deve considerar diferentes formas de calcular a média: média simples, média ponderada ou outro cálculo?

**Resposta:**

O usuário indica a **quantidade de avaliações** e os seus respectivos **pesos**, sendo em seguida calculada a sua média.

O sistema deve considerar apenas o cálculo de médias personalizadas, o qual o usuário oferece a **quantidade de avaliações** e os seus respectivos **pesos**.

#### Confirmação

- O usuário indicará a quantidade de avaliações e seus respectivos pesos

**(US03)** Eu como usuário quero saber minhas médias parciais e totais das disciplinas que estou cursando e ao final do semestre ver a menção.

---

### História de Usuário 04 - Gerenciar o Calendário de Provas e Avaliações

#### Cartão

"Como usuário, eu quero gerar um calendário para acompanhar as datas das provas e avaliações acadêmicas."

#### Conversação

- O usuário tem as **datas das provas e das avaliações** previamente ou o sistema irá puxá-las de algum lugar?
- O usuário pode **adicionar ou editar** as datas manualmente?
- O usuário poderá **integrar** o calendário com outras ferramentas? (ex: Google Calendar)

**Resposta:**

O sistema permitirá que o usuário **adicione** ou **edite** as avaliações nas respectivas datas com o seu devido título de forma manual.

O sistema permitirá que o usuário faça a integração do calendário com o **Google Calendar**

#### Confirmação

- O usuário poderá **gerar um calendário** com as datas das provas, com informações inseridas manualmente pelo usuário.

- O usuário poderá integrar o calendário do sistema com o **Google Calendar**

**(US04)** Como usuário, eu quero gerar um calendário para acompanhar as datas das provas.

---

<!--
### História de Usuário 06 - Gerar Link para Salvar Dados

#### Cartão

"Como usuário, eu quero gerar um link para salvar meus dados e progresso, para que eu possa acessá-los ou compartilhá-los facilmente de qualquer dispositivo."

#### Conversação

- Os dados salvos incluirão quais informações?
- Como o usuário acessará os dados salvos?

**Resposta:** Os dados incluirão perfil do usuário, disciplinas escolhidas, notas calculadas, índice de rendimento acadêmico (IRA) e calendário de provas/avaliações. E, ao acessar o link, o sistema restaurará o estado salvo, permitindo que o usuário continue de onde parou ou utilize as informações compartilhadas.

#### Confirmação

- O usuário poderá **gerar** um link contendo informações sobre perfil, progresso, disciplinas, notas, IRA e calendário
- Esse link será acessível em **qualquer** dispositivo e permitirá **compartilhamento** fácil.

**(US07)** Como usuário, eu quero gerar um link para salvar meus dados e progresso, para que eu possa acessá-los ou compartilhá-los facilmente de qualquer dispositivo. -->
