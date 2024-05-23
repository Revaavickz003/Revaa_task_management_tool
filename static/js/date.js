
let currentDate = new Date();

function updateCalendar(date) {
  const currentMonthYearElement = document.getElementById('currentMonthYear');
  const weekDatesContainer = document.getElementById('weekDates');

  // Clear previous dates
  weekDatesContainer.innerHTML = '';

  // Get current month and year
  const currentMonth = date.toLocaleString('default', { month: 'long' });
  const currentYear = date.getFullYear();
  currentMonthYearElement.textContent = `${currentMonth} ${currentYear}`;

  // Move to the start of the current week
  const firstDayOfWeek = date.getDate() - date.getDay() + 1;
  date.setDate(firstDayOfWeek);

  // Calculate and display dates for the current week
  for (let i = 0; i < 7; i++) {
    const day = date.getDate();
    const dayOfWeek = date.toLocaleString('default', { weekday: 'short' });
    const dateElement = document.createElement('div');
    dateElement.classList.add('small', 'date-container');

    // Dynamically generate the URL using the current date
    const url = `/home/${currentYear}-${date.getMonth() + 1}-${day}/`;
    dateElement.innerHTML = `<div>${dayOfWeek}</div><div class="one"><a href="${url}" class=" text-decoration-none text-black">${day}</a></div>`;

    if (isToday(date)) {
      dateElement.classList.add('today');
    }

    weekDatesContainer.appendChild(dateElement);
    date.setDate(day + 1); // Move to the next day
  }
}

function isToday(date) {
  const today = new Date();
  return date.getDate() === today.getDate() &&
    date.getMonth() === today.getMonth() &&
    date.getFullYear() === today.getFullYear();
}

document.getElementById('gotoprevWeek').addEventListener('click', () => {
  currentDate.setDate(currentDate.getDate() - 7);
  updateCalendar(new Date(currentDate));
});

document.getElementById('gotonextWeek').addEventListener('click', () => {
  currentDate.setDate(currentDate.getDate() + 7);
  updateCalendar(new Date(currentDate));
});

// Initialize calendar with current date
updateCalendar(new Date());

// Pikaday date picker
const picker = new Pikaday({
  field: document.getElementById('currentMonthYear'), // Change this to the appropriate input field
  format: 'MMMM YYYY',
  onSelect: function(date) {
    currentDate = date;
    updateCalendar(new Date(currentDate));
  }
});

// ----------------------------------------------------------
google.charts.load('current', {'packages':['timeline']});
    google.charts.setOnLoadCallback(drawChart);

    let originalData = [
        ['RDS023', 'Frontend for RDS tool login page', new Date(2024, 4, 17, 9, 0, 0), new Date(2024, 4, 17, 11, 0, 0), 'Assigned By: John Doe'],
        ['RDS023', 'Task 2', new Date(2024, 4, 17, 11, 30, 0), new Date(2024, 4, 17, 13, 0, 0), 'Assigned By: Jane Doe'],
        ['RDS023', 'Task 3', new Date(2024, 4, 17, 14, 0, 0), new Date(2024, 4, 17, 16, 0, 0), 'Assigned By: John Doe'],
        ['RDS023', 'Task 4', new Date(2024, 4, 17, 16, 0, 0), new Date(2024, 4, 17, 18, 0, 0), 'Assigned By: Jane Doe'],
        ['RDS023', 'Task 5', new Date(2024, 4, 17, 18, 0, 0), new Date(2024, 4, 17, 20, 0, 0), 'Assigned By: John Doe'],
        ['User-2', 'Task 1', new Date(2024, 4, 17, 9, 0, 0), new Date(2024, 4, 17, 11, 0, 0), 'Assigned By: Jane Doe'],
        ['User-2', 'Task 2', new Date(2024, 4, 17, 11, 30, 0), new Date(2024, 4, 17, 13, 0, 0), 'Assigned By: John Doe'],
        ['User-1', 'Task 3', new Date(2024, 4, 17, 14, 0, 0), new Date(2024, 4, 17, 16, 0, 0), 'Assigned By: Jane Doe'],
        ['User-2', 'Task 4', new Date(2024, 4, 17, 16, 0, 0), new Date(2024, 4, 17, 18, 0, 0), 'Assigned By: John Doe'],
        ['User-8', 'Task 5', new Date(2024, 4, 17, 18, 0, 0), new Date(2024, 4, 17, 20, 0, 0), 'Assigned By: Jane Doe'],
        ['User-5', 'Task 1', new Date(2024, 4, 17, 9, 0, 0), new Date(2024, 4, 17, 11, 0, 0), 'Assigned By: John Doe'],
        ['User-5', 'Task 2', new Date(2024, 4, 17, 11, 30, 0), new Date(2024, 4, 17, 13, 0, 0), 'Assigned By: Jane Doe'],
        ['User-4', 'Task 3', new Date(2024, 4, 17, 14, 0, 0), new Date(2024, 4, 17, 16, 0, 0), 'Assigned By: John Doe']
    ];

    function drawChart(filteredData = originalData) {
        var container = document.getElementById('taskChart');
        var chart = new google.visualization.Timeline(container);
        var dataTable = new google.visualization.DataTable();

        dataTable.addColumn({ type: 'string', id: 'User' });
        dataTable.addColumn({ type: 'string', id: 'Task' });
        dataTable.addColumn({ type: 'date', id: 'Start' });
        dataTable.addColumn({ type: 'date', id: 'End' });
        dataTable.addColumn({ type: 'string', role: 'tooltip', p: { html: true } });

        var rows = filteredData.map(function(row) {
            return [
                row[0], 
                row[1], 
                row[2], 
                row[3], 
                createCustomTooltip(row[1], row[2], row[3], row[4])
            ];
        });

        dataTable.addRows(rows);

        var options = {
            timeline: {
                singleColor: false, // Enable different colors for each row
                barLabelStyle: { fontSize: 14 }, // Adjust font size if needed
            },
            backgroundColor: 'transparent', // Remove chart background color
            height: 300, // Set minimum height of the chart
            tooltip: { isHtml: true }, // Use custom HTML tooltips
        };

        google.visualization.events.addListener(chart, 'ready', function () {
            var svg = container.getElementsByTagName('svg')[0];
            var paths = svg.getElementsByTagName('path');
            for (var i = 0; i < paths.length; i++) {
                paths[i].setAttribute('stroke', 'none');
            }
        });

        chart.draw(dataTable, options);
    }
    function createCustomTooltip(task, start, end, assignedBy) {
        var startTime = start.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
        var endTime = end.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
        return `
            <div style="padding:10px;">
                <strong>Task:</strong> ${task}<br>
                <strong>Start Time:</strong> ${startTime}<br>
                <strong>End Time:</strong> ${endTime}<br>
                <strong>${assignedBy}</strong>
            </div>
        `;
    }

    document.getElementById('employeeSearch').addEventListener('input', function() {
        var searchValue = this.value.toLowerCase();
        var filteredData = originalData.filter(function(row) {
            return row[0].toLowerCase().includes(searchValue);
        });
        drawChart(filteredData);
    });