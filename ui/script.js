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
        
        // Показываем результат
        resultDiv.style.display = 'block';
        
        // Форматируем результат
        let resultText = '';
        let confidenceText = '';
        
        if (result.confidence) {
            confidenceText = ` (уверенность: ${(result.confidence * 100).toFixed(1)}%)`;
        }
        
        // Проверяем что приходит от API
        console.log('API response:', result); // для отладки
        
        // Если приходит строка "Good"/"Standard"/"Poor"
        if (typeof result.credit_score_prediction === 'string') {
            switch(result.credit_score_prediction) {
                case 'Good':
                    resultText = '✅ ОДОБРЕНО';
                    resultDiv.className = 'result-approved';
                    break;
                case 'Standard':
                    resultText = '⚠️ НА РАССМОТРЕНИИ';
                    resultDiv.className = 'result-standard';
                    break;
                case 'Poor':
                    resultText = '❌ ОТКАЗАНО';
                    resultDiv.className = 'result-rejected';
                    break;
                default:
                    resultText = `Результат: ${result.credit_score_prediction}`;
                    resultDiv.className = '';
            }
        } 
        // Если приходит число 0,1,2
        else {
            switch(result.credit_score_prediction) {
                case 2:
                    resultText = '✅ ОДОБРЕНО';
                    resultDiv.className = 'result-approved';
                    break;
                case 1:
                    resultText = '⚠️ НА РАССМОТРЕНИИ';
                    resultDiv.className = 'result-standard';
                    break;
                case 0:
                    resultText = '❌ ОТКАЗАНО';
                    resultDiv.className = 'result-rejected';
                    break;
                default:
                    resultText = `Результат: ${result.credit_score_prediction}`;
                    resultDiv.className = '';
            }
        }
        
        resultDiv.innerText = resultText + confidenceText;
        
    } catch (err) {
        resultDiv.style.display = 'block';
        resultDiv.className = 'result-rejected';
        resultDiv.innerText = '❌ Ошибка соединения: ' + err.message;
    }
});