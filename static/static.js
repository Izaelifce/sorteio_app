document.addEventListener("DOMContentLoaded", () => {
    // Atualiza o número sorteado e o histórico
    function sortear() {
    const qtd = parseInt(document.getElementById("quantidade").value);
    if (isNaN(qtd) || qtd <= 0) {
        alert("Digite uma quantidade válida!");
        return;
    }

    let numeros = [];
    while (numeros.length < qtd) {
        let n = Math.floor(Math.random() * (qtd * 2)) + 1;
        if (!numeros.includes(n)) {
            numeros.push(n);
        }
    }

    // Aqui usamos os IDs que você já tem no HTML
    document.getElementById("numero-sorteado").textContent = "Números sorteados:";
    document.getElementById("numeros-sorteados").textContent = numeros.join(", ");
}

    

    // Limpa o número sorteado e histórico
    window.resetNumeros = function() {
        document.getElementById("numeroSorteado").textContent = "Nenhum número ainda";
        document.getElementById("numerosSorteados").innerHTML = "";
    };
});
