// ui/script.js
const form = document.getElementById('prediction-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // Преобразуем числовые поля
    ['Age', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_of_Loan', 'Total_EMI_per_month'].forEach(field => {
        data[field] = parseFloat(data[field]);
    });

    try {
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        resultDiv.innerText = `Prediction: ${result.credit_score_prediction} (Confidence: ${result.confidence.toFixed(2)})`;
    } catch (err) {
        resultDiv.innerText = 'Error: ' + err.message;
    }
});