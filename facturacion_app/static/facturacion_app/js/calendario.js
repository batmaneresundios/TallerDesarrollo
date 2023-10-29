
document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: [ 'dayGrid' ],
        defaultDate: new Date(),
        header: {
            left: 'prev,next',
            center: 'title',
            right: 'month,basicWeek,basicDay'
        },
        events: function(fetchInfo, successCallback, failureCallback) {
            $.ajax({
                url: 'get_cuotas',  // Asegúrate de cambiar esto por la URL de tu endpoint
                type: 'GET',
                dataType: 'json',
                success: function(data) {
                    // Transforma tus datos si es necesario para que tengan el formato adecuado para FullCalendar
                    var transformedEvents = data.map(function(cuota) {
                        return {
                            title: cuota.monto_cuota,  // Asume que cada cuota tiene un campo 'monto'
                            start: cuota.fecha_cuota   // Asume que cada cuota tiene un campo 'fecha'
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
