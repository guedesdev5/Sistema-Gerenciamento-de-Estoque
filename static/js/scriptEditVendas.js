document.addEventListener('DOMContentLoaded', function() {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var qtd = button.getAttribute('data-qtd');
        var id_vendedor = button.getAttribute('data-idVendedor');
        var id_produto = button.getAttribute('data-idProduto');
        

        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputID = editModal.querySelector('#IDVenda');
        var modalBodyInputNome = editModal.querySelector('#quantidadeVendas');
        var modalBodyInputTelefone = editModal.querySelector('#codVendedor');
        var modalBodyInputEmail = editModal.querySelector('#codProduto');
        var modalBodyInputId = editModal.querySelector('#deleteForm');


        modalTitle.textContent = 'Editar Venda: ' ;
        modalBodyInputNome.value = qtd;
        modalBodyInputTelefone.value = id_vendedor;
        modalBodyInputEmail.value = id_produto
        modalBodyInputID.value = id
    });
});