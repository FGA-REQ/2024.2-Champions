# Declaração de Requisitos

A **declaração de requisitos** é a especificação detalhada das necessidades e expectativas de um sistema de software, documentada de forma clara e objetiva. Ela descreve **o que o sistema deve fazer**, sem entrar em detalhes sobre como será implementado.

## Declaração de Requisitos Funcionais

| Código | Nome do Requisito      | Descrição do Requisito                                                                                                                                                     | Prioridade do Requisito | Regra de Negócio Associada |
| ------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | -------------------------- |
| RF01   | Cadastro de Usuário    | O sistema deve permitir que o usuário faça cadastro no sistema, com email e senha, em uma tela de cadastro exclusiva                                                       | ALTA                    | [RN01](regras-negocio.md)  |
| RF02   | Login de Usuário       | O sistema deve permitir que o usuário faça login no sistema com email e senha em uma tela de login de usuário exclusiva.                                                   | ALTA                    | [RN01](regras-negocio.md)  |
| RF03   | Mudança de senha       | O sistema deve permitir que o usuário faça alteração de senha, fornecendo seu email, a nova senha e a confirmação da nova senha em uma tela de mudança de senha exclusiva. | ALTA                    | [RN01](regras-negocio.md)  |
| RF04   | Validação de Usuário   | O sistema deve validar o login do usuário, indicando quando os dados inseridos forem incorretos, notificando o usuário com uma frase em vermelho.                          | ALTA                    | [RN01](regras-negocio.md)  |
| RF05   | Página de Menu         | O sistema deve disponibilizar uma tela de menu exclusiva para usuários que efetuaram o login.                                                                              | ALTA                    | [RN02](regras-negocio.md)  |
| RF06   | Adicionar disciplinas  | O usuário na tela de menu poderá acessar uma página exclusiva para adicionar disciplinas.                                                                                  | ALTA                    | [RN03](regras-negocio.md)  |
| RF07   | Ver disciplinas        | O usuário na tela de menu poderá acessar uma página exclusiva para ver suas disciplinas.                                                                                   | ALTA                    | [RN04](regras-negocio.md)  |
| RF08   | Acesso ao Calendário   | O usuário na tela de menu poderá acessar o calendário.                                                                                                                     | ALTA                    | [RN05](regras-negocio.md)  |
| RF09   | Cálculo de Médias      | O sistema deve permitir que o usuário insira notas de avaliações e calcular automaticamente a média final de cada disciplina.                                              | ALTA                    | [RN02](regras-negocio.md)  |
| RF10   | Registro de Avaliações | O sistema deve permitir que o usuário registre avaliações, informando a data e a disciplina correspondente.                                                                | ALTA                    | [RN03](regras-negocio.md)  |
