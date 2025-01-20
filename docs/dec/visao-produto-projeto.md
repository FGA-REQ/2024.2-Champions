
## Visão do Produto 

### 1.1 Problemática

Os estudantes da UNB possuem uma grade bastante complexa e um dos principais desafios para a gestão de seu rendimento acadêmico é fazer o cálculo das notas para alcançar a menção desejada e ter conhecimento sobre as datas das avaliações no decorrer das disciplinas. Os principais problemas identificados incluem:

- Erro Humano: 
    O estudante pode errar o cálculo para alcançar a menção MM, por exemplo, e tirar menos do que o necessário para passar na disciplina.

- Falta de centralização das informações:
     Os dados presentes no plano de ensino nem sempre facilitam a compreensão do estudante.

- Dificuldade em gestão de tempo:       
    Muitos estudantes enfrentam desafios em administrar o tempo devido à grande quantidade de atividades acadêmicas e prazos de avaliação.

Tais problemas tem impacto direto tanto no rendimento acadêmico dos estudantes, como na saúde mental, especialmente quando um facilitador não está presente para organizar os prazos, notas e metas a serem alcançadas.

### 1.2 Declaração da posição do produto

O produto a ser desenvolvido é um software de gestão de disciplinas projetado para atender à necessidade dos estudantes da Universidade de Brasília para o acompanhamento das disciplinas e cálculo de menções.


A solução não só permitirá otimizar o trabalho dos estudantes para com as matérias, mas também irá prevenir a desorganização dos estudantes, evitando descontroles e ansiedade ao decorrer dos semestres.

| **Para**                        | **Quem**               | **O (nome do produto)**                   | **Que**                                                                                             | **Ao contrário**       | **Nosso produto**                                                                                                                                                                                                                          |
|----------------------------------|------------------------|-------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Estudantes da Universidade de Brasília         | Grupo Champions    | MediaMestre                               | Auxilia na gestão do rendimento acadêmico dos estudantes da UNB                                      | Ferramentas tradicionais de gestão acadêmica e processos manuais de acompanhamento de disciplinas | é um software desenvolvido sob medida para atender às necessidades específicas dos estudantes da UNB, oferecendo usabilidade aprimorada e facilitada para o acompanhamento de notas, prazos e menções, presente em um sistema web. |


### 1.3 Qual o objetivo do produto?

O **MediaMestre** tem como objetivo ser um sistema interativo e eficiente para o estudante, atendendo às demandas que aparecem no ano acadêmico e auxiliando o aluno a buscar sempre ser mais eficiente no dia a dia.

1. **Otimizar** a gestão do rendimento acadêmico, permitindo que o estudante tenha um controle preciso de suas notas e prazos.
2. **Permitir** um cálculo automatizado das menções necessárias para aprovação nas disciplinas, evitando erros humanos e proporcionando mais segurança ao aluno.
3. **Facilitar** o acompanhamento das datas de avaliações e atividades, centralizando essas informações em um único lugar acessível.
4. **Instruir** o aluno no planejamento de suas atividades acadêmicas, ajudando-o a organizar melhor seu tempo e a gerenciar sua carga de estudos de forma eficaz.

### 1.4 O projeto MediaMestre será construído com quais tecnologias?

O projeto **MediaMestre** será desenvolvido utilizando as seguintes tecnologias:

- **Backend**: Python (FastAPI)
- **Banco de dados**: PostgreSQL
- **Frontend**: Angular



## Visão do Projeto 

### 2.1 Organização do Projeto MediaMestre

A equipe responsável pelo desenvolvimento do projeto foi estruturada de acordo com o conhecimento em desenvolvimento, com o intuito de facilitar o trabalho e acelerar a construção do site. 

| Papel | Atribuições | Responsável | Participantes |
|-------|-------------|-------------|---------------|
| Desenvolvedor | Desenvolvimento do projeto utilizando práticas de engenharia de software, desde a codificação até o deploy do produto | Lucas Bottino | Todos os integrantes do grupo |
| Cliente | Responsável por validar o produto final, garantindo que esteja de acordo com os requisitos levantados ao longo do desenvolvimento do produto | Carlos Eduardo | Carlos Eduardo| 



### 2.2 Planejando as fases e iterações do projeto

O projeto foi dividido em duas sprints, com metade das entregas estando na primeira sprint e, por consequência, a segunda metade sendo entregue na segunda sprint.

Cada sprint possui objetivos claros e prazos definidos, com as histórias de usuário já presentes no backlog. Todos os requisitos e funcionalidades foram construídos e estão prontos para serem implementados conforme o cronograma estabelecido.

O **backlog** pode ser acessado [aqui](backlog.md).

### 2.3 Matriz de comunicação

Os meios de comunicação serão um fator importante para definir como a equipe irá trabalhar em conjunto. A fim de alinhar o trabalho de todos os integrantes do grupo e resolver os problemas de forma eficiente, usaremos o **Discord** para as chamadas e o **WhatsApp** para comunicação rápida.

### 2.4 Gerenciamento de Riscos

A gestão de riscos é uma parte essencial do desenvolvimento do projeto **MediaMestre**, especialmente em um contexto ágil, onde as funcionalidades do produto são entregues ao longo de várias sprints. A seguir, o gerenciamento de riscos foi alinhado com o **Backlog de Produto**, que é estruturado com histórias de usuário e funcionalidades a serem entregues.

### Riscos Alinhados com o Backlog de Produto

| **Risco** | **Probabilidade** | **Impacto** | **História de Usuário Relacionada** | **Estratégia de Mitigação** |
|-----------|-------------------|-------------|-------------------------------------|----------------------------|
| **Atraso no desenvolvimento das funcionalidades principais** | Alta | Alto | US01, US02, US03 | Utilizar a metodologia ágil com sprints bem definidas e acompanhamento contínuo do progresso. As funcionalidades mais críticas (como o cadastro e seleção de disciplinas) devem ser priorizadas. |
| **Erros no cálculo de notas mínimas** | Média | Alto | US03 | Realizar testes de validação para garantir que o cálculo das notas esteja correto e validado com usuários antes de cada entrega. |
| **Problemas na integração entre o frontend (Angular) e backend (FastAPI)** | Média | Alto | US01, US02, US03 | Garantir que as APIs sejam bem definidas desde o início e realizar testes de integração para validar a comunicação entre o backend e o frontend, especialmente nas funcionalidades de cálculo de notas e cadastro. |
| **Resistência dos estudantes à nova ferramenta** | Baixa | Médio | US01, US02 | Realizar pesquisa de usabilidade nas fases iniciais de desenvolvimento para garantir que o produto atenda às necessidades dos usuários e incluir funcionalidades como o cálculo de menções e calendário de provas desde o início. |
| **Falha na sincronização de dados (Google Calendar)** | Média | Alto | US06 | Implementar testes de integração com o Google Calendar e realizar validações com usuários para garantir a sincronização correta do calendário de provas. |
| **Erros na visualização e geração do calendário de provas e avaliações** | Média | Médio | US05 | Testar a geração do calendário em diferentes cenários de uso, com validação das datas de provas e avaliações, antes de cada entrega. |
| **Problemas de desempenho no cálculo do Índice de Rendimento Acadêmico (IRA)** | Baixa | Médio | US04 | Testar o cálculo do IRA com diferentes conjuntos de dados para garantir que o sistema tenha desempenho adequado mesmo com grandes volumes de informações. |
| **Problemas na armazenagem e recuperação dos dados** | Baixa | Alto | US07 | Implementar práticas de backup regular e garantir que os dados possam ser salvos e recuperados de maneira eficiente. A funcionalidade de gerar links para salvar os dados será testada rigorosamente para garantir que o acesso seja fácil e seguro. |

### 2.5 Monitoramento e Controle de Riscos

- **Reuniões Semanais de Acompanhamento**: Durante as sprints, a equipe realizará reuniões semanais de acompanhamento para discutir os riscos e suas atualizações, com foco nas funcionalidades a serem entregues na sprint em andamento.
- **Ferramentas de Acompanhamento de Tarefas**: A equipe utilizará ferramentas como o Trello ou Jira para monitoramento das tarefas, riscos identificados e progresso do desenvolvimento das histórias de usuário.
- **Documentação de Riscos**: Todos os riscos serão documentados e atualizados no backlog, com suas ações de mitigação sendo revisadas conforme o andamento das entregas de cada sprint.
- **Plano de Contingência**: Em casos de risco crítico, como falhas de integração ou cálculos incorretos, a equipe estará pronta para replanejar as entregas, realocar recursos ou ajustar funcionalidades, sempre alinhado com as necessidades dos usuários.
