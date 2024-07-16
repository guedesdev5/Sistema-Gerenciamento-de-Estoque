document.addEventListener('DOMContentLoaded', function() {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var nome = button.getAttribute('data-nome');
        var descricao = button.getAttribute('data-descricao');

        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputNome = editModal.querySelector('#categoriaNome');
        var modalBodyInputDescricao = editModal.querySelector('#categoriaDescricao');
        var modalBodyInputId = editModal.querySelector('#categoriaId');
        var modalExcluirId = editModal.querySelector('#categoriaIdExclusao')

        modalTitle.textContent = 'Editar Categoria: ' + nome;
        modalBodyInputNome.value = nome;
        modalBodyInputDescricao.value = descricao;
        modalBodyInputId.value = id
        modalExcluirId.value = id
    });
});