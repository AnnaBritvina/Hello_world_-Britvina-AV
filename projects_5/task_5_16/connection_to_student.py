import psycopg2

try:
    # Устанавливаем соединение
    connection = psycopg2.connect(
        host="localhost",  # База в контейнере, доступна через localhost
        port="5434",  # Порт из docker-compose.yml (5433:5432)
        user="postgres_task",  # POSTGRES_USER из docker-compose.yml
        password="student",  # POSTGRES_PASSWORD из docker-compose.yml
        database="student"  # POSTGRES_DB из docker-compose.yml
    )
    print("Подключение к базе данных прошло успешно!")

    # Закрываем соединение
    connection.close()
    print("Соединение закрыто.")

except psycopg2.Error as e:
    print(f"Ошибка подключения к базе данных: {e}")