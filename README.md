Приложение Бракованный лингвист создано для поиска сочетания существ. + прилаг.

Для запуска приложения необходимо установить интерпритатор языка python ver 3.9, а также установить следующие библиотеки

``` doctest
>>> pip install -r requirements.txt
```

После установки необходимых библиотек через терминал откройте файл с именем main.py

```doctest
# писать в папке с main.py
>>> python.exe main.py
```

После запуска приложения пользователю будет выведено сообщение в консоль с предложением выбрать действие

```doctest
1) Ввод текста вручную
2) Указать ссылку на файл
>>> 1
```

После выбора действия от пользователя потребуется ввести текст для анализа вручную, либо указать абсолютную ссылку на
файл, если файл не был найден, программа попросит исправить ссылку.

Затем приложение просит указать слово для поиска

```doctest
Введите слово для поиска
>>> кошка
```

В результате всех действий будет проведен анализ текста на наличие сочетания из указанного слова и прилагательного.
```doctest
Сочетание кошка одноглазая
Предложение: Ледяные на ощупь кнопки набора прыгали в глазах и под пальцами, а когда тяжеленная дверь с надсадным стоном впустила его в подъезд, одноглазая грязная кошка, от которой глухо воняло мазутом, принялась с мучительной дрожью тереться, оплела протезы и трость.

Сочетание кошка грязная
Предложение: Ледяные на ощупь кнопки набора прыгали в глазах и под пальцами, а когда тяжеленная дверь с надсадным стоном впустила его в подъезд, одноглазая грязная кошка, от которой глухо воняло мазутом, принялась с мучительной дрожью тереться, оплела протезы и трость.

Сочетание кошка Мягкая
Предложение: Мягкая кошка так бархатной лапой погладит: погладит и оцарапает.

```

Если пользователь желает продолжить анализ в тексте, то ему следует указать следующее слово. Для выхода из приложения следует просто нажать Enter

```doctest
Введите слово для поиска
>>> 

```
