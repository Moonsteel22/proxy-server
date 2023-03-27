from concurrent.futures import ThreadPoolExecutor
import requests

URLS = [
    "https://google.com",
    "https://ya.ru",
    "https://avito.ru",
    "https://python.org",
    "https://youtube.com",
    "https://ozon.ru",
]


def get_code(url):
    result = requests.get(url)
    return url, result.content


if __name__ == "__main__":
    """
    Так как тут I/O bound операция, то нужно использовать потоки, чтобы не блокироваться из-за ожидания ответа по сети.
    """
    # Создаем пул из 6-и потоков
    with ThreadPoolExecutor(max_workers=6) as pool:
        res = pool.map(get_code, URLS)
        # Открываем файл, записываем
        with open("codes.txt", mode="w") as file:
            for url, content in res:
                file.write(f"{url}\n{content}\n")
