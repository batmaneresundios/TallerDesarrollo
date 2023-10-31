import { Calendar } from '@fullcalendar/core'
import dayGridPlugin from '@fullcalendar/daygrid'
const calendar = new Calendar(calendarEl, {
    plugins: [dayGridPlugin],
    initialView: 'dayGridMonth'
  });

const urlParams = new URLSearchParams(window.location.search);
const colegioRBD = urlParams.get('colegio_rbd');

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        headerToolbar: {
            left: 'prev,next',
            center: 'title',
            right: 'dayGridMonth,dayGridWeek,dayGridDay'
        },
        events: function(fetchInfo, successCallback, failureCallback) {
            $.ajax({
                url: '/lista_colegios/get_cuotas/' + colegioRBD + '/',
                type: 'GET',
                dataType: 'json',
                success: function(data) {
                    // Transforma tus datos si es necesario para que tengan el formato adecuado para FullCalendar
                    var transformedEvents = data.map(function(cuota) {
                        return {
                            title: cuota.title,  // Asume que cada cuota tiene un campo 'monto'
                            start: cuota.start   // Asume que cada cuota tiene un campo 'fecha'
                        };
                    });
                    successCallback(transformedEvents);
                },
                error: function() {
                    failureCallback();
                }
            });
        }
    });

    calendar.render();
});
