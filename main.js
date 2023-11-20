function submitForm(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Coletar dados do formulário
    const formData = new FormData(document.getElementById('contractForm'));

    // Enviar os dados para o backend
    fetch('http://localhost:5000/submit_form', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Manipular a resposta da API (por exemplo, exibir um link para download)
        alert('Contrato gerado com sucesso! Faça o download do contrato.');
    })
    .catch(error => {
        console.error('Erro ao gerar contrato:', error);
    });
}
