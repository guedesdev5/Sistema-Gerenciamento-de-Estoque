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
        

        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputID = editModal.querySelector('#ID');
        var modalBodyInputData = editModal.querySelector('#data');
        var modalBodyInputNome = editModal.querySelector('#quantidadeEntrada');
        var modalBodyInputTelefone = editModal.querySelector('#codFornecedor');
        var modalBodyInputEmail = editModal.querySelector('#codProduto');
        var modalBodyInputIDP = editModal.querySelector('#idProduto');
        var modalBodyInputIdExcluir = editModal.querySelector('#idEntrada');
        var modalBodyInputprodutoExcluir = editModal.querySelector('#ProdutoIdExclusao');
        var modalBodyInputqttdExcluir = editModal.querySelector('#quantidadeEntradasEX');



        modalTitle.textContent = 'Editar Entrada:' ;
        modalBodyInputNome.value = qtd;
        modalBodyInputData.value = date;
        modalBodyInputTelefone.value = id_vendedor;
        modalBodyInputEmail.value = id_produto
        modalBodyInputIDP.value = idP;
        modalBodyInputID.value = id
        modalBodyInputIdExcluir.value = id
        modalBodyInputprodutoExcluir.value = idP
        modalBodyInputqttdExcluir.value = qtd
    });
});