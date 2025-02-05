let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();
const currentDate = new Date(); // Data atual

const monthNames = [
  "Janeiro",
  "Fevereiro",
  "Março",
  "Abril",
  "Maio",
  "Junho",
  "Julho",
  "Agosto",
  "Setembro",
  "Outubro",
  "Novembro",
  "Dezembro",
];

let tasks = {};

function renderCalendar() {
  const firstDay = new Date(currentYear, currentMonth, 1);
  const lastDay = new Date(currentYear, currentMonth + 1, 0);
  const totalDays = lastDay.getDate();
  const startDay = firstDay.getDay();

  const monthName = monthNames[currentMonth];
  document.getElementById(
    "month-name"
  ).textContent = `${monthName} ${currentYear}`;

  const calendar = document.getElementById("calendar");
  calendar.innerHTML = ""; // Limpar o calendário antes de renderizar

  // Criar células vazias para o início do mês
  for (let i = 0; i < startDay; i++) {
    const emptyDay = document.createElement("div");
    emptyDay.classList.add("calendar-day", "empty");
    calendar.appendChild(emptyDay);
  }

  // Criar os dias do mês
  for (let day = 1; day <= totalDays; day++) {
    const dayElement = document.createElement("div");
    dayElement.classList.add("calendar-day");
    dayElement.innerHTML = `
      <div class="day-number">${day}</div>
      <div class="tasks" id="tasks-${day}"></div>
    `;
    dayElement.setAttribute("data-day", day);

    // Verificar se o dia já passou
    if (isPastDay(day)) {
      dayElement.classList.add("past-day");
    }

    // Adicionar evento para abrir o modal de tarefas
    dayElement.onclick = () => openTaskForm(day);
    calendar.appendChild(dayElement);

    // Exibir as tarefas já adicionadas ao dia
    renderTasksForDay(day);
  }

  document.getElementById("prev-month").disabled = currentMonth === 0;
  document.getElementById("next-month").disabled = currentMonth === 11;
}

function isPastDay(day) {
  if (currentYear < currentDate.getFullYear()) return true;
  if (currentYear > currentDate.getFullYear()) return false;
  if (currentMonth < currentDate.getMonth()) return true;
  if (currentMonth > currentDate.getMonth()) return false;
  return day < currentDate.getDate();
}

function navigateMonth(direction) {
  currentMonth += direction;
  if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  } else if (currentMonth < 0) {
    currentMonth = 11;
    currentYear--;
  }
  renderCalendar();
}

function openTaskForm(day) {
  document.getElementById("task-container").style.display = "block";
  document.getElementById("task-day").textContent = day;
  document.getElementById("task-input").value = "";
}

function addTask(event) {
  event.preventDefault();

  const day = document.getElementById("task-day").textContent;
  const taskInput = document.getElementById("task-input");
  const taskText = taskInput.value.trim();

  if (!taskText) return;

  if (!tasks[day]) {
    tasks[day] = [];
  }
  tasks[day].push(taskText);

  renderCalendar();
  openTaskForm(day);
}

function renderTasksForDay(day) {
  const taskContainer = document.getElementById(`tasks-${day}`);
  if (tasks[day]) {
    taskContainer.innerHTML = tasks[day]
      .map(
        (task) => `
      <div class="task-item">${task}</div>
    `
      )
      .join("");
  }
}

renderCalendar();
