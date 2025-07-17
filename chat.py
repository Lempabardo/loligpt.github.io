import os
import requests

# Получаем токен из переменной окружения
API_TOKEN = os.getenv('HF_API_TOKEN')

if not API_TOKEN:
    raise ValueError("Пожалуйста, установите переменную окружения HF_API_TOKEN")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_response(prompt):
    json_data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
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
        # В зависимости от модели структура ответа может отличаться
        return result[0]['generated_text']
    else:
        return f"Ошибка: {response.status_code} - {response.text}"

# Основной цикл или вызов функции
if __name__ == "__main__":
    prompt = input("Введите ваш текст: ")
    print(get_response(prompt))