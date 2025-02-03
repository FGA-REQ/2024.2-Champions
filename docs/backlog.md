# Backlog do Produto

## Scaled Agile Framework (SAFe)

O **SAFe** é uma metodologia de desenvolvimento ágil projetada para escalar as práticas ágeis em grandes organizações, com o intuito de alinhar as equipes, programas e portfólios de forma eficaz, permitindo trabalhar de forma coordenada e entregas de valor de maneira contínua.

O trabalho dentro da **SAFe** é definido em diferentes níveis de backlog, sendo eles:

- **Portfolio Backlog**: Contém os **épicos** do negócio e as estratégias de alto nível.
- **Program Backlog**: Contém as **features**, que são derivadas dos épicos.
- **Team Backlog**: Contém as **histórias de usuário**, que são os requisitos mais detalhados e priorizados para o desenvolvimento de uma funcionalidade.

---

## Portfolio Backlog (Épicos)

Os **épicos** representam grandes iniciativas estratégicas que guiam os objetivos mais amplos que o **MediaMestre** busca atender. Esses épicos servem como a base para as funcionalidades que serão desenvolvidas.

| **Épico**                                   | **Descrição**                                                                                                         |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Gestão do Desempenho Acadêmico**          | Implementar funcionalidades para o estudante calcular notas, monitorar desempenho e acompanhar sua jornada acadêmica. |
| **Integração e Organização de Informações** | Criar ferramentas que centralizem informações acadêmicas em uma plataforma acessível e organizada.                    |

---

## Program Backlog (Features)

As **features** são as funcionalidades principais do produto. Elas são derivadas dos épicos e representam os objetivos que as equipes devem alcançar nas iterações de desenvolvimento.

| **Feature**                                                | **Descrição**                                                                                                                   |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Cálculo Automatizado de Notas**                          | Permitir que o estudante calcule automaticamente as notas mínimas para alcançar a menção desejada.                              |
| **Geração e Sincronização de Calendário de Provas**        | Criar um sistema para gerar e sincronizar as datas das provas com o Google Calendar, facilitando o acompanhamento do estudante. |
| **Acompanhamento do Índice de Rendimento Acadêmico (IRA)** | Calcular o IRA com base nas disciplinas cursadas e acompanhar o progresso do estudante ao longo dos semestres.                  |
| **Armazenamento e Compartilhamento de Dados**              | Permitir que os dados acadêmicos do estudante sejam armazenados e acessados de maneira fácil através de links.                  |

---

## Team Backlog (Histórias de Usuário)

As **histórias de usuário** representam os requisitos mais detalhados e priorizados que são desenvolvidos nas sprints. Elas são criadas a partir das features e entregues de forma iterativa nas sprints.

### Priorização das User Stories para o MVP

A priorização das **User Stories** foi feita com base no valor que cada funcionalidade entrega ao usuário, garantindo que as funcionalidades mais essenciais e de maior impacto sejam entregues primeiro, no MVP. As **User Stories** que entram no **MVP** estão indicadas com a tag **(MVP)**.

| **ID** | **História de Usuário**                                                                                                                              | **Feature**                               | **Sprint** | **Critérios de Aceitação**                                                                                                                                              | **Prioridade** | **MVP** |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------- |
| US01   | Eu, como **usuário**, quero me cadastrar no sistema para poder escolher o meu curso.                                                                 | Cadastro de Usuário                       | Sprint 1   | O sistema deve permitir o cadastro de usuários com campos obrigatórios como nome, e-mail e curso.                                                                       | Alta           | ✅      |
| US02   | Eu, como **usuário**, quero selecionar as disciplinas que estou cursando no semestre para planejar meu semestre.                                     | Seleção de Disciplinas                    | Sprint 1   | O sistema deve permitir ao usuário selecionar disciplinas de um catálogo de cursos oferecidos pela UNB, vinculando-os ao seu perfil.                                    | Alta           | ✅      |
| US03   | Eu, como **usuário**, quero calcular a nota mínima necessária para alcançar uma menção específica em cada disciplina, para garantir minha aprovação. | Cálculo de Notas Mínimas                  | Sprint 1   | O sistema deve calcular corretamente as notas mínimas que o estudante precisa para atingir a menção desejada, levando em consideração os pesos das provas e atividades. | Alta           | ✅      |
| US04   | Eu, como **usuário**, quero calcular o meu Índice de Rendimento Acadêmico (IRA), para monitorar meu desempenho ao longo do tempo.                    | Acompanhamento do IRA                     | Sprint 2   | O sistema deve calcular o IRA automaticamente com base nas notas e pesos das disciplinas selecionadas pelo estudante.                                                   | Média          | ❌      |
| US05   | Eu, como **usuário**, quero gerar um calendário de provas e avaliações para visualizar e me organizar de acordo com os prazos.                       | Geração de Calendário de Provas           | Sprint 2   | O sistema deve gerar automaticamente um calendário de provas e avaliações com base nas disciplinas do estudante e exibir de forma clara as datas de cada avaliação.     | Alta           | ✅      |
| US06   | Eu, como **usuário**, quero integrar o calendário de provas com o meu Google Calendar para sincronizar as datas das avaliações.                      | Sincronização com Google Calendar         | Sprint 2   | O sistema deve permitir a integração com o Google Calendar, criando eventos com as datas de provas e avaliações das disciplinas selecionadas.                           | Média          | ❌      |
| US07   | Eu, como **usuário**, quero gerar um link para salvar e acessar meus dados e progresso acadêmico facilmente de qualquer dispositivo.                 | Armazenamento e Compartilhamento de Dados | Sprint 2   | O sistema deve gerar um link único para cada usuário que possibilite o acesso aos dados e progresso acadêmico em qualquer dispositivo com internet.                     | Baixa          | ❌      |

---

### Definição das User Stories para o MVP

A **Release 1 (MVP)** será composta pelas **User Stories** de maior prioridade, que são essenciais para o funcionamento inicial do produto. Com isso, garantimos que os usuários possam se cadastrar, selecionar disciplinas, calcular notas mínimas e visualizar o calendário de provas.

**User Stories do MVP**:

- **US01**: Cadastro de Usuário
- **US02**: Seleção de Disciplinas
- **US03**: Cálculo de Notas Mínimas
- **US05**: Geração de Calendário de Provas

Essas funcionalidades garantirão que o **MediaMestre** forneça valor imediato aos estudantes, permitindo que eles se cadastrem, planejem seu semestre e acompanhem o desempenho acadêmico de forma básica.

---

## Priorização e Planejamento das Releases

**Release 1 (MVP)**: Focado nas funcionalidades essenciais, conforme as **User Stories** listadas acima.

**Release 2 (Próxima iteração)**: Após o MVP, as funcionalidades adicionais como **Cálculo do IRA**, **Integração com Google Calendar** e **Armazenamento de Dados** serão implementadas.

---

## Conclusão

A metodologia SAFe é ideal para projetos grandes e complexos como o **MediaMestre**, pois ela permite escalar o trabalho entre várias equipes e alinhar as entregas com as prioridades estratégicas do negócio. Ao organizar o backlog de produto nas camadas de **portfolio**, **programa** e **time**, garantimos que todos os requisitos sejam atendidos de forma organizada e eficiente.

## Referências

- **SAFe Team Backlog**: [https://scaledagileframework.com/team-backlog/](https://scaledagileframework.com/team-backlog/)
- **Enterprise Backlog Structure and Management**: [https://scaledagileframework.com/enterprise-backlog-structure-and-management/](https://scaledagileframework.com/enterprise-backlog-structure-and-management/)
