document.addEventListener('DOMContentLoaded', function() {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var qtd = button.getAttribute('data-qtd');
        var id_vendedor = button.getAttribute('data-idFornecedor');
        var id_produto = button.getAttribute('data-idProduto');
        

        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputID = editModal.querySelector('#IDVenda');
        var modalBodyInputNome = editModal.querySelector('#quantidadeEntrada');
        var modalBodyInputTelefone = editModal.querySelector('#codFornecedor');
        var modalBodyInputEmail = editModal.querySelector('#codProduto');
        var modalBodyInputIdExcluir = editModal.querySelector('#vendasIdExclusao');
        var modalBodyInputprodutoExcluir = editModal.querySelector('#codProdutoEx');
        var modalBodyInputqttdExcluir = editModal.querySelector('#quantidadeEntradasEX');



        modalTitle.textContent = 'Editar Venda: ' ;
        modalBodyInputNome.value = qtd;
        modalBodyInputTelefone.value = id_vendedor;
        modalBodyInputEmail.value = id_produto
        modalBodyInputID.value = id
        modalBodyInputIdExcluir.value = id
        modalBodyInputprodutoExcluir.value = id_produto
        modalBodyInputqttdExcluir.value = qtd
    });
});