let count = 0;

const result = document.getElementById("result");
const plus = document.getElementById("plus");
const minus = document.getElementById("minus");
const message = document.getElementById("message");

function updateCounter() {
    result.textContent = count;

    if (count > 0) {
        result.style.background = "yellow";
    } else if (count < 0) {
        result.style.background = "green";
    } else {
        result.style.background = "red";
    }

    plus.disabled = count === 10;
    minus.disabled = count === -10;

    if (count === 10 || count === -10) {
        message.textContent = "Вы достигли экстремального значения";
    } else {
        message.textContent = "";
    }
}

plus.addEventListener("click", function () {
    count++;
    updateCounter();
});

minus.addEventListener("click", function () {
    count--;
    updateCounter();
});