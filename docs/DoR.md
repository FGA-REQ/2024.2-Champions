# Definition of Ready (DoR)

## DoR -> Interação -> DoD

## US01

### Critérios de Aceitação definidos:

- Campos obrigatórios: e-mail, senha.

- Validação de e-mail (formato válido = string@email.com).

- Criação de senha (letras e números).

- Mensagens de erro para campos inválidos ou incompletos.

### Design cadastro:

Design da tela com opção de inserção de e-mail e senha.

### Testes básicos definidos:

- Casos de teste para sucesso, falha de validação e duplicidade de e-mail.

## US02 - Seleção de Disciplinas

### Critérios de Aceitação definidos:

- O usuário pode selecionar 1 ou mais disciplinas.

- Busca por nome ou código da disciplina.

- Lista de disciplinas disponíveis atualizada semestralmente.

### Dados das disciplinas disponíveis:

- Integração com sistema acadêmico ou base de dados das disciplinas.

### UI/UX aprovado:

- Design da interface de busca e seleção de disciplinas validado.

### Tratamento de erros:

- Mensagens para disciplinas não encontradas ou indisponíveis.

## US03 - Cálculo de Menção

### Critérios de Aceitação definidos:

- Opções de cálculo: média simples, ponderada ou personalizada.

- Menções disponíveis: MM, MS, SS.

- Fórmulas de cálculo validadas com a instituição.

### Regras de negócio claras:

- Peso de cada prova (se for ponderada).

- Notas mínimas por menção (ex: SS ≥ 9,0).

### Interface de entrada de notas:

- Design da tela de input de notas aprovado.

### Testes de cenários extremos:

- Exemplo: cálculo com notas zeradas ou máximas.

## US04 - Cálculo do Índice de Rendimento Acadêmico (IRA)

### Critérios de Aceitação definidos:

- Cálculo baseado apenas em disciplinas cursadas e aprovadas.

- Fórmula do IRA validada com a instituição.

### Integração com histórico acadêmico:

- Acesso às notas e disciplinas concluídas do usuário.

### UI de exibição do IRA:

- Design do dashboard ou tela de resultados aprovado.

### Tratamento de dados incompletos:

- Mensagem se o usuário não tiver disciplinas concluídas.

## US05 - Gerar Calendário de Provas e Avaliações

### Critérios de Aceitação definidos:

- Importação automática de datas do calendário acadêmico.

- Edição manual de datas pelo usuário.

- Suporte a provas de reposição.

### Fonte de dados definida:

- API ou arquivo (ex: CSV) do calendário acadêmico.

### UI do calendário:

- Design da visualização mensal/semanal aprovado.

### Notificações:

- Lógica para alertas de datas próximas definida.

## US06 - Integração com Google Calendar

### Critérios de Aceitação definidos:

- Integração das datas do calendário acadêmico no Google Calendar.

- Confirmação por e-mail com link do Google Calendar.

### Autenticação OAuth com Google:

- Configuração de credenciais da API do Google Calendar.

### Tratamento de erros:

- Mensagens para falha na sincronização (ex: permissões negadas).

### Testes de integração:

- Cenários de sucesso e falha na sincronização.

## US07 - Gerar Link para Salvar Dados

### Critérios de Aceitação definidos:

- Dados incluídos: perfil, disciplinas, notas, IRA, calendário.

- Link acessível em qualquer dispositivo.

- Opção de compartilhamento.

### Estrutura de dados:

- Formato do link (ex: JSON criptografado ou URL curta).

### Segurança:

- Proteção contra acesso não autorizado (ex: token único).

### UI de geração do link:

- Design do botão/interface para gerar e compartilhar o link aprovado.