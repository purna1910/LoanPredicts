const API_URL = 'http://localhost:5000';  // Change to your Heroku URL when deployed

// Handle loan form submission
document.getElementById('loanForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    
    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        const resultDiv = document.getElementById('result');
        
        if (result.status === 'success') {
            resultDiv.textContent = result.message;
            resultDiv.style.background = result.loan_status === 'Approved' ? '#4CAF50' : '#f44336';
            resultDiv.style.color = 'white';
        } else {
            resultDiv.textContent = 'Error: ' + result.message;
            resultDiv.style.background = '#ff9800';
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Network error. Please try again.';
    }
});

// Chatbot functionality
function sendMessage() {
    const input = document.getElementById('chatInput');
    const message = input.value.trim();
    
    if (!message) return;
    
    const chatbox = document.getElementById('chatbox');
    chatbox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    
    fetch(`${API_URL}/chatbot`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch(error => {
        chatbox.innerHTML += `<p><strong>Bot:</strong> Error connecting to server.</p>`;
    });
    
    input.value = '';
}

// Allow Enter key to send message
document.getElementById('chatInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
