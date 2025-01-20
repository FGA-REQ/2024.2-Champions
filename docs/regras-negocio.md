# Regras de Negócio (MediaMestre)
# Regras de Dedução

## 1. Status de Aprovação
- Se a média final de um aluno em uma determinada disciplina for maior ou igual a 5 e a frequência for superior a 75%, então o aluno será considerado aprovado.

## 2. Identificação de Disciplinas Concluídas
- Se a média final for maior ou igual a 5 e o total de aulas assistidas for maior ou igual a 75%, então a disciplina será marcada como "concluída".

## 3. Menção Final
- **SS (Superior)**: Se a nota final do estudante estiver entre 9,0 e 10,0, então a menção será SS.
- **MS (Médio Superior)**: Se a nota final do estudante estiver entre 7,0 e 8,9, então a menção será MS.
- **MM (Médio)**: Se a nota final do estudante estiver entre 5,0 e 6,9, então a menção será MM.
- **MI (Médio Inferior)**: Se a nota final do estudante estiver entre 3,0 e 4,9, então a menção será MI.
- **II (Inferior)**: Se a nota final do estudante estiver entre 0,1 e 2,9, então a menção será II.
- **SR (Sem Rendimento)**: Se o estudante tiver mais de 25% de faltas nas aulas, independentemente da nota final, a menção será SR.

## 4. Recomendação de Priorização
- Se a média final do aluno em uma disciplina for menor que 5, então a disciplina será marcada como "prioritária" para estudos futuros.

## 5. Matéria Disponível
- A matéria será exibida como **Disponível** se:
  - Houver vagas disponíveis;
  - O estudante atender a todos os pré-requisitos;
  - O estudante ainda não cursou a matéria.

## 6. Matéria Não Disponível (Por Falta de Vaga)
- A matéria será exibida como **Não Disponível - Falta de Vaga** se não houver vagas disponíveis, independentemente dos outros critérios.

## 7. Matéria Não Disponível (Por Requisitos)
- A matéria será exibida como **Não Disponível - Pré-requisitos Não Atendidos** se o estudante não atender aos requisitos necessários (pré-requisitos ou restrições de curso/semestre), mesmo que haja vagas disponíveis.

## 8. Matéria Já Cursada
- A matéria será exibida como **Não Disponível - Já Cursada** se o estudante já a tiver cursado anteriormente (com aprovação ou reprovação).

## 9. Poder Selecionar Cursos
- O usuário pode selecionar cursos **SE E SOMENTE SE** houver ao menos um curso cadastrado no sistema.

## 10. Visualizar Cursos
- O usuário poderá visualizar os cursos disponíveis **SE houver ao menos um curso cadastrado no sistema**.

## 11. Cadastro de Matéria
- Uma matéria pode ser cadastrada **SE** o curso correspondente já estiver selecionado no sistema.

## 12. Calculador de IRA
- O simulador do IRA pode ser executado **SE** o aluno tiver ao menos uma nota cadastrada.

## 13. Simulador de Menção
- A menção final de um aluno pode ser simulada **SE todas as notas parciais das avaliações forem inseridas**.

---

# Regras Computacionais ou de Cálculo

1. A nota final é a soma de todas as notas, multiplicadas pelo respectivo peso de cada uma delas, e dividida pelo total de pesos aplicados.
2. Um aluno será considerado aprovado caso a média final na disciplina for maior ou igual a 5 e a frequência for superior a 75%.
3. Uma disciplina será marcada como “feita”, caso a média final na disciplina for maior ou igual a 5 e a frequência for superior a 75%.
4. A menção final de um aluno será definida pelas seguintes condições:
    - **SS**: A nota final do aluno está entre 9,0 e 10,0 com frequência acima de 75%.
    - **MS**: A nota final do aluno está entre 7,0 e 8,9 com frequência acima de 75%.
    - **MM**: A nota final do aluno está entre 5,0 e 6,9 com frequência acima de 75%.
    - **MI**: A nota final do aluno está entre 3,0 e 4,9 com frequência acima de 75%.
    - **II**: A nota final do aluno está entre 0,1 e 2,9 com frequência acima de 75%.
    - **SR**: A nota final do aluno foi 0 ou o aluno teve frequência menor do que 75%.
5. Uma disciplina será considerada “prioritária” caso a nota final do aluno for inferior a 5.
6. Uma matéria será exibida como “disponível” para seleção do aluno se:
    1. Existirem vagas disponíveis na matéria.
    2. O aluno atender aos pré-requisitos (se houver).
    3. O aluno não tiver cursado a matéria.

---

# Geração de Alertas

## 1. Alerta de Proximidade de Avaliação
- O sistema deverá alertar o aluno se a data de uma avaliação estiver a menos de 7 dias.

## 2. Alerta de Nota Inferior a 5
- Se o aluno obtiver uma nota inferior a 5 em qualquer avaliação, o sistema deverá recomendá-lo a realizar estudos direcionados.

## 3. Alerta de Frequência Crítica
- Se o aluno estiver perto de atingir 25% de faltas (ex.: 14 faltas em um semestre com 56 aulas), o sistema deverá alertá-lo para comparecer às próximas aulas.

## 4. Alerta de Peso em Avaliações
- O sistema deverá informar o aluno sobre a importância de considerar os pesos das diferentes avaliações (ex.: provas e trabalhos) ao calcular sua média final.

## 5. Alerta de Ausência de Dados
- O sistema deverá alertar o aluno se não houver notas suficientes para calcular a média com precisão (ex.: falta de notas de prova ou trabalho).

---

# Simulador de IRA

Para calcular o IRA:
1. Multiplicar a média final de cada disciplina pelos seus respectivos créditos.
2. Somar os resultados ponderados de todas as disciplinas.
3. Dividir pela soma total de créditos cursados.
4. Exibir o resultado como índice de desempenho do aluno.

---

# Simulador de Menções

O simulador de menções permitirá que o aluno insira notas de avaliações já realizadas e simule:
1. Quanto ainda precisa tirar em avaliações futuras para alcançar as menções SS, MS ou MM.
2. Informar se já não é possível alcançar determinadas menções, considerando as notas obtidas até o momento.

---

# Regras de Causa e Efeito

## Exemplos de Causas e Efeitos:

- **Causa**: A média final do aluno for maior ou igual a 5 e a frequência superior a 75%.
  - **Efeito**: O aluno será considerado aprovado na disciplina.
  
- **Causa**: A nota final do aluno está entre 9,0 e 10,0.
  - **Efeito**: A menção final será SS.

- **Causa**: A nota final do aluno está entre 7,0 e 8,9.
  - **Efeito**: A menção final será MS (Médio Superior).

- **Causa**: A nota final do aluno está entre 5,0 e 6,9.
  - **Efeito**: A menção final será MM (Médio).

- **Causa**: A nota final do aluno está entre 3,0 e 4,9.
  - **Efeito**: A menção final será MI (Médio Inferior).

- **Causa**: A nota final do aluno está entre 0,1 e 2,9.
  - **Efeito**: A menção final será II (Inferior).

- **Causa**: O aluno teve mais de 25% de faltas nas aulas.
  - **Efeito**: A menção final será SR (Sem Rendimento), independentemente da nota.

- **Causa**: A data de uma avaliação esteja próxima (1 semana).
  - **Efeito**: O aluno será alertado sobre a proximidade da avaliação.

- **Causa**: O aluno tiver uma nota inferior a 5 em alguma avaliação.
  - **Efeito**: O sistema recomenda estudos direcionados para melhorar seu desempenho.

---

# Regras de Diretriz

## Exemplos de Alertas:

- **Alerta sobre a nota mínima para aprovação**: Se a média final do aluno for inferior a 5,0, o aluno será informado de que a nota está abaixo da média exigida para aprovação.

- **Alerta sobre a data das avaliações**: Se a data da avaliação estiver próxima (1 semana), o usuário será alertado sobre a avaliação.

- **Alerta sobre a nota necessária para alcançar a menção MS**: Se a nota do aluno estiver entre 7,0 e 9,0, este será informado sobre o que é necessário para tirar MS.

- **Alerta sobre a nota necessária para alcançar a menção SS**: Se a nota do aluno estiver de 9,0 a 10,0, este será informado sobre o que é necessário para tirar SS.

- **Alerta de cálculo de média em disciplinas com diferentes tipos de avaliação**: O aluno será alertado sobre a diferença que os pesos podem implicar na sua média final.

- **Alerta sobre a ausência de avaliações suficientes para a aprovação**: Se o aluno não tiver ao menos duas notas de avaliação, será informado que sua média não pode ser calculada com precisão.

---

# Regras de Restrição

## Exemplos de Restrições:

- **Cadastro de matérias**: Só pode ser realizado por usuários com permissão de administrador ou professor.
- **Simulador do IRA**: Calcula o Índice de Rendimento Acadêmico com base nas notas de cada disciplina cadastrada pelo o aluno.
- **Simulador de Menções**: Permite a inserção de notas para simular as menções SS, MS, MM, MI e II.
- **Google Agendas**: O sistema deve sincronizar com o Google Agendas e permitir a adição de datas diretamente no calendário do usuário.
- **Salvar dados em link**: Os dados devem ser salvos em um banco de dados seguro e acessível apenas por usuários permitidos.
