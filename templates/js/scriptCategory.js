
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.open-window-btn');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            openTableInNewWindow();
        });
    });
});

function openTableInNewWindow() {
    const tableHTML = document.getElementById('table-container').innerHTML;
    const newWindow = window.open('', '_blank', 'width=800,height=600');
    console.log("teste ettstet");
    newWindow.document.write(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Nova Janela com Tabela</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    margin: 0;
                    padding: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                    font-size: 18px;
                    text-align: left;
                }
                table th, table td {
                    padding: 12px;
                    border-bottom: 1px solid #ddd;
                }
                table th {
                    background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
            ${tableHTML}
        </body>
        </html>
    `);
    newWindow.document.close();
}
