// project Status 

document.addEventListener('DOMContentLoaded', function () {
    // Initialize Flatpickr
    const startDatePicker = flatpickr("#start-date", {
        dateFormat: "Y-m-d",
        onChange: function (selectedDates, dateStr, instance) {
            document.getElementById('start-date-display').innerText = dateStr;
            document.getElementById('start-date').classList.add('d-none');
        }
    });

    const targetDatePicker = flatpickr("#target-date", {
        dateFormat: "Y-m-d",
        onChange: function (selectedDates, dateStr, instance) {
            document.getElementById('target-date-display').innerText = dateStr;
            document.getElementById('target-date').classList.add('d-none');
        }
    });

    // Show the datepicker when the date display is clicked
    document.getElementById('start-date-display').addEventListener('click', function () {
        document.getElementById('start-date').classList.remove('d-none');
        startDatePicker.open();
    });

    document.getElementById('target-date-display').addEventListener('click', function () {
        document.getElementById('target-date').classList.remove('d-none');
        targetDatePicker.open();
    });

    // Toggle status options visibility
    document.getElementById('current-status-display').addEventListener('click', function () {
        document.getElementById('status-options').style.display = 'block';
    });

    // Update status when an option is clicked
    const statusOptions = document.querySelectorAll('.status-option');
    statusOptions.forEach(option => {
        option.addEventListener('click', function () {
            document.getElementById('current-status-display').innerText = this.innerText;
            document.getElementById('status-options').style.display = 'none';
        });
    });
});


// Project details

function execCmd(command) {
    if (command === 'createLink') {
        let url = prompt('Enter the link here: ', 'http://');
        document.execCommand(command, false, url);
    } else {
        document.execCommand(command, false, null);
    }
}

function saveEdit() {
    const content = document.getElementById('editor').innerHTML;
    console.log('Saved content:', content);
}

function cancelEdit() {
    document.getElementById('editor').innerHTML = '';
}