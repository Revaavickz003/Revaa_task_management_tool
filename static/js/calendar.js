$(document).ready(function () {
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];
    const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    let today = new Date();
    let currentMonth = today.getMonth();
    let currentYear = today.getFullYear();

    // Assuming eventsData is already parsed JSON from the template script tag
    let events = eventsData;

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function generateCalendar(month, year, events) {
        $("#month-year").text(monthNames[month] + " " + year);
        const calendar = $("#calendar");
        calendar.empty();

        // Days of the week header
        daysOfWeek.forEach(day => {
            calendar.append(`<div class="day-header">${day}</div>`);
        });

        let firstDay = new Date(year, month, 1).getDay();
        let daysInMonth = new Date(year, month + 1, 0).getDate();

        // Blank days before the first day of the month
        for (let i = 0; i < firstDay; i++) {
            calendar.append('<div class="day"></div>');
        }

        // Actual days of the month
        for (let i = 1; i <= daysInMonth; i++) {
            let dayElement = $(`<div class="day" data-date="${year}-${(month + 1).toString().padStart(2, '0')}-${i.toString().padStart(2, '0')}">
                <div class="day-header">${i}</div>
            </div>`);

            // Add class for today's date
            if (year === today.getFullYear() && month === today.getMonth() && i === today.getDate()) {
                dayElement.addClass('today-border');
            }

            // Ensure that the day-header element is clickable
            dayElement.find('.day-header').on('click', function (e) {
                e.stopPropagation();
                $("#eventStartDate").val($(this).parent().data('date'));
                $("#eventEndDate").val($(this).parent().data('date'));
                $("#eventModal").modal('show');
            });

            calendar.append(dayElement);
        }

        // Append events to days
        if (events && events.length > 0) {
            events.forEach(event => {
                let startDate = new Date(event.fields.start_date);
                let endDate = new Date(event.fields.end_date);
                let bgColor = event.fields.color || '#007bff'; // Default to primary color if no bgColor is specified

                let current = new Date(startDate);

                while (current <= endDate) {
                    let dayDate = current.toISOString().split('T')[0];
                    let dayElement = calendar.find(`.day[data-date="${dayDate}"]`);

                    if (dayElement.length > 0) {
                        // Generate a unique ID for each modal
                        let modalId = `update-${event.pk}-${dayDate.replace(/-/g, '')}`;
                        let epk = `${event.pk}`;
                        let icon;

                        // Determine the correct icon based on the typeOfEvent
                        switch (event.fields.typeOfEvent) {
                            case 'Call':
                                icon = '<i class="bx bx-phone-call text-light"></i>';
                                break;
                            case 'Event':
                                icon = '<i class="bx bxs-megaphone text-light"></i>';
                                break;
                            case 'Meeting':
                                icon = '<i class="bx bx-group text-light"></i>';
                                break;
                            default:
                                icon = '<i class="bx bx-group text-light"></i>'; // Default icon if typeOfEvent is not matched
                        }

                        let eventElement = $(`
                            <div class="event text-truncate" style="background-color:${bgColor};">
                                <button type="button" class="border-0 rounded-1" data-bs-toggle="modal" data-bs-target="#${modalId}" style="background-color: rgba(236, 236, 236, .2);">
                                    ${icon}
                                </button> ${event.fields.name}
                                <div class="modal fade" id="${modalId}" tabindex="-1" aria-labelledby="${modalId}Label" aria-hidden="true">
                                    <div class="modal-dialog" style="height: 83vh; width: 350px;">
                                        <div class="modal-content rounded-4 border-0 h-100 bg-none bg-transparent">
                                            <div class="container rounded-top-4 modal-header d-flex dlex-column align-items-start justify-content-end text-start" style="height: 180px; background-color:${bgColor}; flex-direction: column;">
                                                <h1 class="modal-title fs-5 fw-bold text-light mb-1 text-wrap" id="${modalId}Label">${event.fields.name} ( ${event.fields.typeOfEvent} )</h1>
                                                <p class="text-light m-0 p-0 fs-6"><i class='bx bx-time text-light'></i> ${formatDate(new Date(event.fields.start_date))}</p>
                                                <p class="text-light m-0 p-0 fs-6"><i class='bx bx-time text-light'></i> ${formatDate(new Date(event.fields.end_date))}</p>
                                            </div>
                                            <div class="modal-body rounded-bottom-4 bg-light">
                                                <div class="mb-5 rounded-bottom-4">
                                                    <p class="fs-6">Description:</p>
                                                    <div style="height:6.4rem; overflow-y:auto;">
                                                        <p class="text-wrap fs-6">${event.fields.description || 'No description available.'}</p>
                                                    </div>
                                                    <hr style="border-top: 1px dotted;">
                                                    ${event.fields.meeting_url ? `<a href="${event.fields.meeting_url}" class="btn btn-sm btn-primary px-3">Join Meeting</a>` : ''}
                                                </div>
                                            </div>
                                            <div class="d-flex align-items-center justify-content-center gap-2 mt-3">
                                                <a href="/calendar/update_event/${epk}/" class="btn bg-light" id="update-event">
                                                    <i class='bx bxs-edit text-success fs-5' style="padding: 8.7px 3.5px;"></i>
                                                </a>
                                                <button type="button" class="btn bg-light delete-event" data-epk="${epk}">
                                                    <i class='bx bx-trash fs-5 text-danger' style="padding: 8.7px 3.5px;"></i>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `);

                        dayElement.append(eventElement);
                    }

                    current.setDate(current.getDate() + 1);
                }
            });

            // Attach click event for delete buttons
            $(".delete-event").on('click', function () {
                let epk = $(this).data('epk');
                if (confirm('Are you sure you want to delete this event?')) {
                    $.ajax({
                        url: `/calendar/delete_event/${epk}/`,
                        type: 'POST',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        success: function (response) {
                            location.reload(); 
                        },
                        error: function (xhr, status, error) {
                            console.error('Error deleting event:', status, error);
                        }
                    });
                }
            });
        }
    }

    function formatDate(date) {
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        return date.toLocaleDateString(undefined, options);
    }

    // Initialize the calendar
    generateCalendar(currentMonth, currentYear, events);

    // Event listeners for navigation buttons
    $("#prev-month").click(function () {
        currentMonth = (currentMonth - 1 + 12) % 12;
        if (currentMonth === 11) {
            currentYear--;
        }
        generateCalendar(currentMonth, currentYear, events);
    });

    $("#next-month").click(function () {
        currentMonth = (currentMonth + 1) % 12;
        if (currentMonth === 0) {
            currentYear++;
        }
        generateCalendar(currentMonth, currentYear, events);
    });
});
