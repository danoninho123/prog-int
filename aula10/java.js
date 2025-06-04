$(document).ready(function () {
    $('#buscar').click(function () {
        const cidade = $('#cidade').val().trim();
        if (cidade === '') {
            alert('Por favor, digite o nome de uma cidade.');
            return;
        }

        const url = `https://wttr.in/${cidade}?format=j1`;

        $.getJSON(url, function (data) {
            const tempAtual = data.current_condition[0].temp_C;
            const condicao = data.current_condition[0].weatherDesc[0].value;
           

            $('#resultado').removeClass('d-none').html(`
                <h4>Clima em <strong>${cidade}</strong>:</h4>
                <p>Temperatura atual: <strong>${tempAtual}°C</strong></p>
                <p>Condição: <strong>${condicao}</strong></p>
               
            `);
        }).fail(function () {
            $('#resultado').removeClass('d-none').addClass('alert-danger').html('Erro ao buscar os dados do clima.');
        });
    });
});