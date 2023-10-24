document.addEventListener("DOMContentLoaded", function() {
  var btnPreencher = document.querySelector('.btn_preencher');
  var btnBaixar = document.querySelector('.btn_baixar');
  var containerNota = document.getElementById("containerNota");

  btnBaixar.disabled = true;

  btnPreencher.addEventListener('click', function() {
    var nomeCliente = prompt('Digite o nome do cliente:');
    var formaPagamento = prompt('Digite a forma de pagamento:');
    var total = prompt('Digite o total:');

    if (nomeCliente && formaPagamento && !isNaN(total)) {
      btnBaixar.disabled = false;

      var pontos = " ";
      document.getElementById('nomeCliente').textContent = 'Nome Cliente: '  + pontos + nomeCliente;
      document.getElementById('formaPagamento').textContent = 'Forma Pagamento: ' + pontos + formaPagamento;
      document.getElementById('total').textContent = 'Total: ' + pontos + total + "R$";
    } else {
      btnBaixar.disabled = true;
    }
  });

  btnBaixar.addEventListener('click', function() {
    // Aplica um zoom à captura (ajuste conforme necessário)
    var scale = 2; // Ajuste o valor conforme necessário

    // Usa html2canvas para renderizar a seção no canvas com zoom
    html2canvas(containerNota, {
      scale: scale
    }).then(function(canvas) {
      var dataURL = canvas.toDataURL("image/png");

      var linkDownload = document.createElement("a");
      linkDownload.href = dataURL;
      linkDownload.download = "cupom.png";

      document.body.appendChild(linkDownload);
      linkDownload.click();

      document.body.removeChild(linkDownload);
    });
  });
});
