document.addEventListener('DOMContentLoaded', function() {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var nome = button.getAttribute('data-nome');
        var telefone = button.getAttribute('data-telefone');
        var email = button.getAttribute('data-email');
        var endereco = button.getAttribute('data-endereco');
        

        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputNome = editModal.querySelector('#fornecedorNome');
        var modalBodyInputTelefone = editModal.querySelector('#fornecedorTel');
        var modalBodyInputEmail = editModal.querySelector('#fornecedorEmail');
        var modalBodyInputEndereco = editModal.querySelector('#fornecedorEndereco');
        var modalBodyInputId = editModal.querySelector('#fornecedorId');
        var modalExcluirId = editModal.querySelector('#fornecedorIdExclusao')

        modalTitle.textContent = 'Editar Fornecedor: ' + nome;
        modalBodyInputNome.value = nome;
        modalBodyInputTelefone.value = telefone;
        modalBodyInputEmail.value = email
        modalBodyInputEndereco.value = endereco
        modalBodyInputId.value = id
        modalExcluirId.value = id
    });
});