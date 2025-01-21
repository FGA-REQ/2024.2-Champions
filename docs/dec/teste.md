# testes
## Regra de Negócio 1: Status de Aprovação
- Se a média final de um aluno em uma determinada disciplina for maior ou igual a 5 e a frequência for superior a 75%, então o aluno será considerado aprova
### Requisito Relacionado:
- Permitir um cálculo automatizado das menções necessárias para aprovação nas disciplinas, evitando erros humanos e proporcionando mais segurança ao aluno.
- Otimizar a gestão do rendimento acadêmico, permitindo que o estudante tenha um controle preciso de suas notas e prazos.

## Regra de Negócio 2: Identificação de Disciplinas Concluídas
- Se a média final for maior ou igual a 5 e o total de aulas assistidas for maior ou igual a 75%, então a disciplina será marcada como "concluída".
### Requisito Relacionado:
- Facilitar o acompanhamento das datas de avaliações e atividades, centralizando essas informações em um único lugar acessível.

## Regra de Negócio 3: Menção Final
- **SS (Superior)**: Se a nota final do estudante estiver entre 9,0 e 10,0, então a menção será SS.
- **MS (Médio Superior)**: Se a nota final do estudante estiver entre 7,0 e 8,9, então a menção será MS.
- **MM (Médio)**: Se a nota final do estudante estiver entre 5,0 e 6,9, então a menção será MM.
- **MI (Médio Inferior)**: Se a nota final do estudante estiver entre 3,0 e 4,9, então a menção será MI.
- **II (Inferior)**: Se a nota final do estudante estiver entre 0,1 e 2,9, então a menção será II.
- **SR (Sem Rendimento)**: Se o estudante tiver mais de 25% de faltas nas aulas, independentemente da nota final, a menção será SR.
### Requisito Relacionado:
- Permitir um cálculo automatizado das menções necessárias para aprovação nas disciplinas, evitando erros humanos e proporcionando mais segurança ao aluno.

## Regra de Negócio 4: Recomendação de Priorização
- Se a média final do aluno em uma disciplina for menor que 5, então a disciplina será marcada como "prioritária" para estudos futuros.
### Requisito Relacionado:
- Instruir o aluno no planejamento de suas atividades acadêmicas, ajudando-o a organizar melhor seu tempo e a gerenciar sua carga de estudos de forma eficaz.

## Regra de Negócio 5: Matéria Disponível
- A matéria será exibida como **Disponível** se:
  - Houver vagas disponíveis;
  - O estudante atender a todos os pré-requisitos;
  - O estudante ainda não cursou a matéria.
### Requisito Relacionado:
- Facilitar o acompanhamento das disciplinas disponíveis para matrícula, incluindo as condições de pré-requisitos e vagas.

## Regra de Negócio 6: Matéria Não Disponível (Por Falta de Vaga)
- A matéria será exibida como **Não Disponível - Falta de Vaga** se não houver vagas disponíveis, independentemente dos outros critérios.
### Requisito Relacionado:
-Facilitar o acompanhamento das disciplinas disponíveis para matrícula, incluindo as condições de pré-requisitos e vagas.

## Regra de Negócio 7: Matéria Não Disponível (Por Requisitos)
- A matéria será exibida como **Não Disponível - Pré-requisitos Não Atendidos** se o estudante não atender aos requisitos necessários (pré-requisitos ou restrições de curso/semestre), mesmo que haja vagas disponíveis.
### Requisito Relacionado:
-Facilitar o acompanhamento das disciplinas disponíveis para matrícula, incluindo as condições de pré-requisitos e vagas. 

## Regra de Negócio 8: Matéria Já Cursada
- A matéria será exibida como **Não Disponível - Já Cursada** se o estudante já a tiver cursado anteriormente (com aprovação ou reprovação).
### Requisito Relacionado:
- Facilitar o acompanhamento das disciplinas disponíveis para matrícula, indicando as já cursadas.

## Regra de Negócio 9: Poder Selecionar Cursos
- O usuário pode selecionar cursos **SE E SOMENTE SE** houver ao menos um curso cadastrado no sistema.
### Requisito Relacionado:
- Permitir que o usuário selecione cursos com base na grade curricular disponível no sistema.

## Regra de Negócio 10: Visualizar Cursos
- O usuário poderá visualizar os cursos disponíveis **SE houver ao menos um curso cadastrado no sistema**.
### Requisito Relacionado:
- Facilitar o acompanhamento das disciplinas e cursos disponíveis para seleção.

## 11. Cadastro de Matéria
- Uma matéria pode ser cadastrada **SE** o curso correspondente já estiver selecionado no sistema.
### Requisito Relacionado:
-Permitir o cadastro de matérias relacionadas a um curso previamente selecionado no sistema.

## Regra de Negócio 12. Calculador de IRA
- O simulador do IRA pode ser executado **SE** o aluno tiver ao menos uma nota cadastrada.
### Requisito Relacionado:
- Otimizar a gestão do rendimento acadêmico, permitindo o cálculo do Índice de Rendimento Acadêmico (IRA).

## Regra de Negócio 13. Simulador de Menção
- A menção final de um aluno pode ser simulada **SE todas as notas parciais das avaliações forem inseridas**.
### Requisito Relacionado:
- Permitir um cálculo automatizado das menções necessárias para aprovação nas disciplinas, evitando erros humanos e proporcionando mais segurança ao aluno.

Regras de Geração de Alertas
Alerta de Proximidade de Avaliação
Requisito Relacionado:

Facilitar o acompanhamento das datas de avaliações e atividades, centralizando essas informações em um único lugar acessível.
Alerta de Nota Inferior a 5
Requisito Relacionado:

Instruir o aluno no planejamento de suas atividades acadêmicas, ajudando-o a organizar melhor seu tempo e a gerenciar sua carga de estudos de forma eficaz.
Alerta de Frequência Crítica
Requisito Relacionado:

Facilitar o acompanhamento da frequência do estudante e alertar sobre o impacto no rendimento acadêmico.
Alerta de Peso em Avaliações
Requisito Relacionado:

Permitir que o estudante calcule de forma automatizada as menções necessárias, considerando pesos nas avaliações.
Alerta de Ausência de Dados
Requisito Relacionado:

Facilitar o acompanhamento das notas cadastradas e alertar sobre a falta de informações para um cálculo preciso.
Simulador de IRA
Requisito Relacionado:

Otimizar a gestão do rendimento acadêmico, permitindo o cálculo do Índice de Rendimento Acadêmico (IRA).
Simulador de Menções
Requisito Relacionado:

Permitir um cálculo automatizado das menções necessárias para aprovação nas disciplinas, evitando erros humanos e proporcionando mais segurança ao aluno.
Regras de Diretriz
Exemplos de alertas relacionados às regras de diretriz podem ser vinculados a vários requisitos, como:

Otimizar a gestão do rendimento acadêmico.
Facilitar o acompanhamento das datas de avaliações e atividades.