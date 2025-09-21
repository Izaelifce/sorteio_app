document.addEventListener("DOMContentLoaded", () => {
    // Atualiza o número sorteado e o histórico
    window.updateNumero = function(numero) {
        const numeroDiv = document.getElementById("numeroSorteado"); // ID deve ser igual ao HTML
        numeroDiv.textContent = numero || "Nenhum número ainda";

        const historico = document.getElementById("numerosSorteados"); // ID igual ao HTML
        if (numero) {
            const novoSpan = document.createElement("span");
            novoSpan.textContent = numero;
            historico.appendChild(novoSpan);
        }
    };

    // Limpa o número sorteado e histórico
    window.resetNumeros = function() {
        document.getElementById("numeroSorteado").textContent = "Nenhum número ainda";
        document.getElementById("numerosSorteados").innerHTML = "";
    };
});
