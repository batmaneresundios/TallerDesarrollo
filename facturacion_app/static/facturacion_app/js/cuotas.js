window.onload = function() {
    var selectCuotas = document.getElementById("numero_cuotas");
    
    for (var i = 1; i <= 24; i++) {
        var option = document.createElement("option");
        option.value = i;
        option.text = i + (i === 1 ? " cuota" : " cuotas");
        selectCuotas.appendChild(option);
    }
};

function calcularCuotas() {
    var totalMonto = document.getElementById("monto_plan_hidden").value;  // Nota este cambio
    var numCuotas = document.getElementById("numero_cuotas").value;
    var montoCuota = totalMonto / numCuotas;
    document.getElementById("monto_por_cuota").innerHTML = "Monto por cuota: " + montoCuota;
}

document.getElementById("numero_cuotas").addEventListener("change", function() {
    var numCuotas = this.value;
    var contenedorFechas = document.getElementById("fechas_facturacion");
    contenedorFechas.innerHTML = "";  // Limpiar fechas previas

    for(var i = 0; i < numCuotas; i++) {
        var inputFecha = document.createElement("input");
        inputFecha.type = "date";
        inputFecha.name = "fecha_" + (i+1);  // Para tener nombres únicos
        contenedorFechas.appendChild(inputFecha);
        calcularCuotas();
    }
});
