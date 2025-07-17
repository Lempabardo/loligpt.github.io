const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

sendBtn.addEventListener('click', () => {
	const message = userInput.value.trim();
	if (message === '') return;

	// Добавляем сообщение пользователя
	addMessage(message, 'user');

	// Очистка поля ввода
	userInput.value = '';

	// Генерируем ответ бота (заглушка)
	setTimeout(() => {
		const reply = generateReply(message);
		addMessage(reply, 'bot');
	}, 500);
});

function addMessage(text, sender) {
	const msgDiv = document.createElement('div');
	msgDiv.className = 'message ' + sender;
	msgDiv.innerText = text;

	chatBox.appendChild(msgDiv);
	chatBox.scrollTop = chatBox.scrollHeight; // автоматическая прокрутка
}

function generateReply(userMsg) {
	// Простая заглушка - можно расширить или подключить API позже
	return "Это ответ от loli-gpt.";
}