document.addEventListener('DOMContentLoaded', function() {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var nome = button.getAttribute('data-nome');
        var descricao = button.getAttribute('data-descricao');
        var preco = button.getAttribute('data-preco');
        var quantidade = button.getAttribute('data-quantidade');
        var id_categoria = button.getAttribute('data-id_categoria');
        var id_fornecedor = button.getAttribute('data-id_fornecedor');

        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputNome = editModal.querySelector('#produtoNome');
        var modalBodyInputDescricao = editModal.querySelector('#produtoDescricao');
        var modalBodyInputPreco = editModal.querySelector('#produtoPreco');
        var modalBodyInputQuantidade = editModal.querySelector('#produtoQuantidade');
        var modalBodyInputIdCategoria = editModal.querySelector('#produtoIdCategoria');
        var modalBodyInputIdFornecedor = editModal.querySelector('#produtoIdFornecedor');
        var modalBodyInputId = editModal.querySelector('#produtoId');
        var modalExcluirId = editModal.querySelector('#produtoIdExclusao')

        modalTitle.textContent = 'Editar Produto: ' + nome;
        modalBodyInputNome.value = nome;
        modalBodyInputDescricao.value = descricao;
        modalBodyInputId.value = id
        modalBodyInputPreco.value = preco;
        modalBodyInputQuantidade.value = quantidade;
        modalBodyInputIdCategoria.value = id_categoria
        modalBodyInputIdFornecedor.value = id_fornecedor
        modalExcluirId.value = id
    });
});