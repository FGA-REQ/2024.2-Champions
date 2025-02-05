
# Definition of Done (DoR)

## DoR -> Interação -> DoD

## US01 - Cadastro no Sistema

### Desenvolvimento:

Código do formulário de cadastro implementado com validação de e-mail (regex string@email.com) e senha (letras + números).

Integração com banco de dados para armazenar e-mails únicos.

### Testes:

Testes unitários para validação de campos (sucesso, e-mail duplicado, campos inválidos).

Teste de integração com o banco de dados.

### Validação:

Aprovado pelo Product Owner (PO) após revisão da UI/UX.

## US02 - Seleção de Disciplinas

### Desenvolvimento:

Interface de busca por nome/código implementada.

Integração com a base de dados de disciplinas (atualizada semestralmente).

### Testes:

Testes de busca (casos: disciplina encontrada, não encontrada, múltiplas seleções).

Teste de carregamento da lista de disciplinas.

### Validação:

PO confirma que a UI corresponde ao design aprovado.

## US03 - Cálculo de Menção

### Desenvolvimento:

Lógica de cálculo (simples, ponderada, personalizada) implementada.

Interface para input de notas e pesos (se aplicável).

### Testes:

Testes unitários para cada fórmula (ex: SS ≥ 9,0).

Testes de cenários extremos (notas zeradas, máximas).

### Validação:

Validação das fórmulas pela instituição (ex: coordenador acadêmico).

## US05 - Gerar Calendário de Provas e Avaliações

### Desenvolvimento:

Importação automática de datas via API do calendário acadêmico.

Funcionalidade de edição manual de datas implementada.

### Testes:

Teste de importação de datas (sucesso/falha).

Teste de adição/edição manual de datas.

### Validação:

PO confirma que as notificações de datas próximas funcionam.

## US04 - Cálculo do IRA (Não prioritário para MVP)

### Desenvolvimento:

Implementação da fórmula validada da instituição.

### Testes:

Teste de cálculo com dados reais (ex: disciplinas aprovadas).

Teste de tratamento para dados incompletos.

## US06 - Integração com Google Calendar (Não prioritário para MVP)

### Desenvolvimento:

Integração das datas.

Automatização de confirmação por e-mail com o link.

### Testes:

Teste de integração (sucesso/falha de permissões).

Teste de envio de e-mail de confirmação.


## US07 - Gerar Link para Salvar Dados (Não prioritário para MVP)

### Desenvolvimento:

Geração de link único e criptografado.

Funcionalidade de restauração de dados via link.

### Testes:

Teste de acesso ao link em diferentes dispositivos.

Teste de segurança (ex: token inválido).
