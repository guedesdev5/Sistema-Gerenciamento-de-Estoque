document.addEventListener('DOMContentLoaded', function() {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var qtd = button.getAttribute('data-qtd');
        var id_vendedor = button.getAttribute('data-idVendedor');
        var id_produto = button.getAttribute('data-idProduto');
        var iDP = button.getAttribute('data-idP')
        
        

        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputID = editModal.querySelector('#IDVenda');
        var modalBodyInputNome = editModal.querySelector('#quantidadeVendas');
        var modalBodyInputTelefone = editModal.querySelector('#codVendedor');
        var modalBodyInputEmail = editModal.querySelector('#codProduto');
        var modalBodyInputIdExcluir = editModal.querySelector('#vendasIdExclusao');
        var modalBodyInputprodutoExcluir = editModal.querySelector('#codProdutoEx');
        var modalBodyInputqttdExcluir = editModal.querySelector('#quantidadeVendasEX');
        var IDP = editModal.querySelector('#idProduto');



        modalTitle.textContent = 'Editar Venda: ' ;
        modalBodyInputNome.value = qtd;
        modalBodyInputTelefone.value = id_vendedor;
        modalBodyInputEmail.value = id_produto
        modalBodyInputID.value = id
        modalBodyInputIdExcluir.value = id
        modalBodyInputprodutoExcluir.value = iDP
        modalBodyInputqttdExcluir.value = qtd
        IDP.value = iDP
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