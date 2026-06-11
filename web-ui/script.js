document.addEventListener('DOMContentLoaded', () => {
    const demoBtn = document.getElementById('demoBtn');
    const modal = document.getElementById('demoModal');
    const closeBtn = document.getElementById('closeBtn');
    const classifyBtn = document.getElementById('classifyBtn');
    const textInput = document.getElementById('textInput');
    const resultBox = document.getElementById('resultBox');
    
    const toxicProgress = document.getElementById('toxicProgress');
    const toxicValue = document.getElementById('toxicValue');
    const nontoxicProgress = document.getElementById('nontoxicProgress');
    const nontoxicValue = document.getElementById('nontoxicValue');

    
    demoBtn.addEventListener('click', () => {
        modal.classList.add('show');
    });

    
    closeBtn.addEventListener('click', () => {
        modal.classList.remove('show');
        resetModal();
    });

    
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('show');
            resetModal();
        }
    });

    
    classifyBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();
        if (!text) return;

        
        toxicProgress.style.width = '0%';
        nontoxicProgress.style.width = '0%';
        resultBox.classList.remove('hidden');

        classifyBtn.textContent = 'Analyzing...';
        classifyBtn.disabled = true;

        try {
            
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            if (data.error) {
                alert("Error: " + data.error);
                return;
            }

            const toxicScore = data.toxic_percentage;
            const nontoxicScore = data.nontoxic_percentage;

            toxicProgress.style.width = `${toxicScore}%`;
            nontoxicProgress.style.width = `${nontoxicScore}%`;
            
            toxicValue.textContent = `${toxicScore}%`;
            nontoxicValue.textContent = `${nontoxicScore}%`;

        } catch (error) {
            console.error('Error during classification:', error);
            alert("Failed to connect to backend. Make sure app.py is running!");
        } finally {
            classifyBtn.textContent = 'Classify Text';
            classifyBtn.disabled = false;
        }
    });

    function resetModal() {
        textInput.value = '';
        resultBox.classList.add('hidden');
        toxicProgress.style.width = '0%';
        nontoxicProgress.style.width = '0%';
    }
});
