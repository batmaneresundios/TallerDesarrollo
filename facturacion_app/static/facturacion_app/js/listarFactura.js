function hacerEditable(idFactura) {
    // Ocultar la información estática y mostrar el formulario
    document.getElementById('info-' + idFactura).style.display = 'none';
    document.getElementById('form-' + idFactura).style.display = 'block';
}
