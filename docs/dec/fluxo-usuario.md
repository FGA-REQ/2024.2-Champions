# Fluxo de Usuário - MediaMestre

Este documento descreve o fluxo de usuário para o site MediaMestre, desde o acesso até a integração com o Google Calendar.

## 1. Acesso à Interface do Site

O usuário acessa a interface do site, onde verá o layout inicial.

## 2. Sistema de Login

### Passos para o Login:

1. O usuário clica no botão **Login**.
2. Se o usuário já tem um cadastro, ele pode fazer login com e-mail e senha.
3. Se não tiver um cadastro, será redirecionado para um link de cadastro com a mensagem **"Cadastre-se agora"**.

## 3. Sistema de Cadastro de Usuário (CRUD)

### Passos para o Cadastro:

1. O usuário clica em **Cadastre-se** e acessa o formulário de cadastro.
2. O formulário de cadastro contém os seguintes campos:

   - Nome completo
   - Idade
   - Curso
   - E-mail
   - Senha

3. Após preencher, o usuário clica em **Finalizar** e o sistema exibe a mensagem **"Cadastro concluído com sucesso!"**.

## 4. Escolher Disciplinas

### Passos para Seleção de Disciplinas:

1. O usuário, após fazer login, vai para a tela de **usuário** e clica em **Adicionar Disciplinas**.
2. O sistema permite que o usuário busque disciplinas pelo **código ou nome**.
3. As disciplinas filtradas aparecem com seus respectivos dados (código, nome, turma, professor).
4. O usuário escolhe a **turma** desejada e a adiciona ao campo **Disciplinas escolhidas**.
   - O usuário pode continuar escolhendo disciplinas ou clicar em **Adicionar disciplina(s)** para finalizar.

## 5. Calcular Notas Mínimas (Média)

### Passos para Cálculo das Notas:

1. O usuário clica na disciplina desejada e acessa o modal de **Cálculo de Notas**.
2. O sistema oferece as opções de cálculo:
   - **Média Simples**: Exibe as notas mínimas para as menções MM, MS e SS.
   - **Média Ponderada**: O usuário define o número de provas e os pesos, e o sistema exibe as notas mínimas.
   - **Outro**: O usuário define as avaliações e pesos personalizados.

## 6. Calcular o Índice de Rendimento Acadêmico (IRA)

### Passos para o Cálculo do IRA:

1. O usuário, após login, vê o **IRA** exibido ao lado do semestre atual, com base nas disciplinas que já cursou.

## 7. Gerar Google Calendar com Datas de Provas

### Passos para a Integração com Google Calendar:

1. O usuário entra na tela de **Agenda**.
2. O sistema exibe um **calendário** com as datas das provas das disciplinas cadastradas.
3. O usuário clica em **Integrar com Google Calendar**.
4. Se a integração for bem-sucedida, o usuário recebe um e-mail de confirmação com o link para a agenda integrada.
