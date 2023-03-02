#Задание 1
def positive_numbers(func):
    def wrapper(*args):
        if args[1] > args[0]:
            return 0
        else:
            return func(*args)
    return wrapper

@positive_numbers
def sub(a, b):
    return a - b

print(sub(1, 5))

#Задание 2
import requests

def retry(num):
    def decorator(func):
        def wrapper(*args):
            for i in range(num + 1):
                try:
                    return func(*args)
                except Exception:
                    if i == num:
                        raise Exception(f'Определенное количество попыток ({num}) превышено!')
        return wrapper
    return decorator

@retry(num=5)
def get_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

url = "https://example.com"
content = get_url(url)
print(content)