function adicionarDisciplina() {
  const disciplinaSelecionada = document.getElementById("disciplinas").value;

  if (!disciplinaSelecionada) {
    alert("Por favor, escolha uma disciplina.");
  } else {
    alert(
      "Disciplina adicionada com sucesso! ID da disciplina: " +
        disciplinaSelecionada
    );
  }
}
