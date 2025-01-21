document.addEventListener('DOMContentLoaded', function() {
    const incomeForm = document.getElementById('income-form');
    const expenseForm = document.getElementById('expense-form');
    const resultDiv = document.getElementById('result');

    incomeForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const incomeSource = document.getElementById('income-source').value;
        const incomeAmount = parseFloat(document.getElementById('income-amount').value);
        displayResult(incomeSource, incomeAmount, 'income');
    });

    expenseForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const expenseSource = document.getElementById('expense-source').value;
        const expenseAmount = parseFloat(document.getElementById('expense-amount').value);
        displayResult(expenseSource, expenseAmount, 'expense');
    });

    function displayResult(source, amount, type) {
        const typeText = type === 'income' ? 'Gelir' : 'Gider';
        resultDiv.innerHTML += `<p>${typeText}: ${amount} (${source})</p>`;
    }
});