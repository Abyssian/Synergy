let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let result = document.getElementById("result");

document.getElementById("sumBtn").addEventListener("click", function () {
    calculate("+");
});

document.getElementById("subBtn").addEventListener("click", function () {
    calculate("-");
});

document.getElementById("mulBtn").addEventListener("click", function () {
    calculate("*");
});

document.getElementById("divBtn").addEventListener("click", function () {
    calculate("/");
});

function calculate(operator) {
    let a = Number(num1.value);
    let b = Number(num2.value);

    if (num1.value === "" || num2.value === "" || isNaN(a) || isNaN(b)) {
        result.innerText = "Ошибка: введите числа";
        return;
    }

    if (operator === "+") {
        result.innerText = a + b;
    } else if (operator === "-") {
        result.innerText = a - b;
    } else if (operator === "*") {
        result.innerText = a * b;
    } else if (operator === "/") {
        if (b === 0) {
            result.innerText = "Ошибка: деление на 0";
        } else {
            result.innerText = a / b;
        }
    }
}