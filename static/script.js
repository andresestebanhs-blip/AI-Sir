document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') sendMessage();
});

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();
    if (message === "") return;

    // Display user message
    addMessage(message, 'user');
    userInput.value = '';

    // Show typing indicator (optional placeholder for realism)
    const chatWindow = document.getElementById('chat-window');
    const loadingId = 'loading-' + Date.now();
    const loadingMsg = document.createElement('div');
    loadingMsg.className = 'message bot-message';
    loadingMsg.id = loadingId;
    loadingMsg.innerHTML = `
        <div class="avatar bot-avatar">AI</div>
        <div class="text">Processing...</div>
    `;
    chatWindow.appendChild(loadingMsg);
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // Fetch response from Flask backend
    fetch('/predict', {
        method: 'POST',
        body: JSON.stringify({ message: message }),
        headers: { 'Content-Type': 'application/json' }
    })
        .then(r => r.json())
        .then(r => {
            // Remove loading
            const loadingElement = document.getElementById(loadingId);
            if (loadingElement) loadingElement.remove();

            // Display bot response
            if (r && r.answer) {
                addMessage(r.answer, 'bot');
            } else {
                addMessage("Lo siento, hubo un error interno en el servidor.", 'bot');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            const loadingElement = document.getElementById(loadingId);
            if (loadingElement) loadingElement.remove();
            addMessage("Error de conexión con el núcleo neural.", 'bot');
        });
}

function addMessage(text, sender) {
    if (!text) return; // Prevent crash on null text

    const chatWindow = document.getElementById('chat-window');
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender}-message`;

    // Format text (simple markdown replacement for bold/newlines)
    let formattedText = text.replace(/\n/g, '<br>');
    formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    if (sender === 'bot') {
        msgDiv.innerHTML = `
            <div class="avatar bot-avatar">AI</div>
            <div class="text">${formattedText}</div>
        `;
    } else {
        msgDiv.innerHTML = `
            <div class="text">${formattedText}</div>
            <div class="avatar user-avatar">U</div>
        `;
    }

    chatWindow.appendChild(msgDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
