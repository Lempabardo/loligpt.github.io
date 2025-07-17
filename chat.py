import requests

# Ваш API-токен
API_TOKEN = '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'

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_response(prompt):
    json_data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,   # Максимальное количество новых токенов в ответе
            "temperature": 0.7,      # Размытие генерации (чем выше — тем более разнообразный ответ)
            "top_p": 0.9,
            "top_k": 50,
            "do_sample": True
        }
    }
    response = requests.post(
        "https://api-inference.huggingface.co/models/EleutherAI/gpt-j-6B",
        headers=headers,
        json=json_data
    )
    if response.status_code == 200:
        result = response.json()
        # Ответ модели — первый элемент в списке
        return result[0]['generated_text']
    else:
        return f"Ошибка: {response.status_code} - {response.text}"

# Цикл для постоянного ввода текста
while True:
    prompt = input("Введите ваш текст (или 'выход' для завершения): ")
    if prompt.lower() == 'выход':
        break
    answer = get_response(prompt)
    print("Ответ:\n", answer)