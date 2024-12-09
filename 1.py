def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

inner_function() # выдаст ошибку, что функция inner_function не была найдена в глобальной области видимости.
                # Т.к. каждая функция имеет свою собственную область видимости, а функция inner_function доступна только внутри функции test_function.

test_function() # на экране появится сообщение "Я в области видимости функции test_function".
                # Это значит, что функция inner_function успешно вызвана внутри функции test_function.
