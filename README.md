# Работа с тестовыми данными

- txt
- csv
- json
- sqlite

### Чтение из файла

```python
f = open("file_name", "r")
f.read()
f.close()
```

### Использование with
```python
with open("file_name", "r") as f:
    f.read()
```

Python содержит встроенные библиотеки для работы json, csv, sqlite, html данными. А так же может быть использован для чтения любого файла в бинарном формате.

### Генераторы и итераторы

Генераторы создаются путем добавления ключевого слова yield в любую функцию. После этого каждое новое обращение к ней вызывает следующую итерацию цикла или выдачу следующего значения.

```python
def squares(start, stop):
    for i in range(start, stop):
        yield i * i

generator = squares(1, 10)
```

Итераторы это более общее понятние и в общем случае означает объект который явялется наследником класса у которого реализованы методы __next__ и __iter__

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
            
            
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
```
