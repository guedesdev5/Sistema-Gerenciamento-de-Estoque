document.addEventListener('DOMContentLoaded', function() {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var date = button.getAttribute('data-data')
        var qtd = button.getAttribute('data-qtd');
        var id_vendedor = button.getAttribute('data-idFornecedor');
        var id_produto = button.getAttribute('data-idProduto');
        var idP = button.getAttribute('data-idP');
        var preco = button.getAttribute('data-preco');
        

        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputID = editModal.querySelector('#idEntrada');
        var modalBodyInputData = editModal.querySelector('#data');
        var modalBodyInputNome = editModal.querySelector('#quantidadeEntrada');
        var modalBodyInpupreco = editModal.querySelector('#precoEntrada');
        var modalBodyInputEmail = editModal.querySelector('#codProduto');
        var modalBodyInputIDP = editModal.querySelector('#idProduto');

        var modalBodyInputIdExcluir = editModal.querySelector('#identrada');
        var modalBodyInputprodutoExcluir = editModal.querySelector('#ProdutoIdExclusao');
        var modalBodyInputqttdExcluir = editModal.querySelector('#quantidadeEntradasEX');
        


        modalTitle.textContent = 'Editar Entrada:' ;
        modalBodyInputID.value = id;
        modalBodyInputNome.value = qtd;
        modalBodyInputData.value = date;
        modalBodyInpupreco.value = preco
        modalBodyInputEmail.value = id_produto
        modalBodyInputIDP.value = idP;
        
        modalBodyInputIdExcluir.value = id
        modalBodyInputprodutoExcluir.value = idP
        modalBodyInputqttdExcluir.value = qtd
        
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
        message.style.display = 'block'; 
        setTimeout(function() {
            message.style.opacity = '0'; 
            setTimeout(function() {
                message.style.display = 'none'; 
            }, 500); 
        }, 1500); 
    });
});


function filtrarProdutos() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const select = document.getElementById('codP');
    
    for (let i = 0; i < select.options.length; i++) {
        const option = select.options[i];
        const optionText = option.text.toLowerCase();

        if (optionText.includes(input)) {
            option.style.display = ""; 
        } else {
            option.style.display = "none"; 
        }
    }
}