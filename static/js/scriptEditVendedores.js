document.addEventListener('DOMContentLoaded', function() {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var nome = button.getAttribute('data-nome');
        var username = button.getAttribute('data-username');
        var email = button.getAttribute('data-email');
        var senha = button.getAttribute('data-senha');
        var permissao = button.getAttribute('data-permissao');
       
        var modalTitle = editModal.querySelector('.modal-title');
        var modalBodyInputNome = editModal.querySelector('#vendedorNome');
        var modalBodyInputUsername = editModal.querySelector('#vendedorUsername');
        var modalBodyInputEmail = editModal.querySelector('#vendedorEmail');
        var modalBodyInputSenha = editModal.querySelector('#vendedorSenha');
        var modalBodyInputPermissao = editModal.querySelector('#vendedorPermissao');
        var modalBodyInputId = editModal.querySelector('#vendedorId');
        var modalExcluirId = editModal.querySelector('#vendedorIdExclusao')

        modalTitle.textContent = 'Editar Produto: ' + nome;
        modalBodyInputNome.value = nome;
        modalBodyInputUsername.value = username;
        modalBodyInputId.value = id
        modalBodyInputEmail.value = email;
        modalBodyInputSenha.value = senha;
        modalBodyInputPermissao.value = permissao
        modalExcluirId.value = id
    });
});