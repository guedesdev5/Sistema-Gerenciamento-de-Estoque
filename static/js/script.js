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