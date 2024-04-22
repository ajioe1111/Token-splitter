### Сортировщик и разделитель данных для работы с Discord токенами

**Функционал:**
- Работает из папки.
- Принимает файл `input.txt`, который содержит данные в формате `LOGIN:PASS:TOKEN`.
- Создаёт директорию `output`, внутри которой:
  - Создаётся папка с текущей датой.
  - Создаются два файла `.txt`:
    - `input_copy.txt` — полная копия `input.txt`.
    - `tokens.txt` — файл, содержащий только токены.

**Дополнительные возможности:**
- Скрипт выводит количество обработанных токенов.
- Файл `input.txt` очищается после выполнения скрипта.

**Пример использования:**

```bash
python main.py
```

