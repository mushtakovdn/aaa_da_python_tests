# Решение заданий по инструментам тестирвоания в python

## issue 1
Тестирование функции encode с помощью doctest. Результаты теста сохраняются в файле tst_results/issue_01.txt

Для запуска теста находясь в корне репозитория запустите в терминале команду:
```
python -m doctest -o NORMALIZE_WHITESPACE src/morse.py -v > tst_results/issue_01.txt
```

## issue 2
Тестирование функции decode с помощью pytest с применением параметризации.

Результаты теста сохраняются в файле tst_results/issue_01.txt

Для запуска теста находясь в корне репозитория запустите в терминале команду:

```
python -m pytest tests/test_issue_02.py -v > tst_results/issue_02.txt
```

## issue 3
Тестирование one hot encoder с помощью unittest

Для запуска теста находясь в корне репозитория запустите в терминале команду:
```
python -m unittest tests/test_issue_03.py -v > tst_results/issue_03.txt
```

## issue 4
Тестирование one hot encoder с помощью pytest

Для запуска теста находясь в корне репозитория запустите в терминале команду:
```
python -m pytest tests/test_issue_04.py -v > tst_results/issue_04.txt
```

## issue 5
Тестирование функции what_is_year_now с генерацией отчета в coverage.

Для запуска теста находясь в корне репозитория запустите в терминале команду:
```
python -m pytest tests/test_issue_05_pytest.py --cov=what_is_year_now --cov-report html > tst_results/issue_05_pytest.txt
```
Результат тестирования сохранится в :
- ./tst_results/issue_05_pytest.txt (в текстовом виде)
- ./htmlcov (html report)

*Отчет показывает, что модуль what_is_year_now покрыт всего лишь на 83%. Однако при этом сама тестируемая функция покрыта на 100%.Не покрыт код из \_\_main__*