document.addEventListener("DOMContentLoaded", function() {
    let fechaHoy = new Date().toISOString().substr(0, 10);
    document.getElementById("fecha_emision").value = fechaHoy;
});
