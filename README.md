## Описание папок

1) test_app - скрипт для теста всех функций pioneer mini
   * testPioneer.py - скрипт теста всех функций pioneer mini
   * testSetup.py - сборка тестового скрипта в exe приложение
2) joy_control - скрипт управления pioneer mini с помощью джойстиков от PS4 и XBox
   * Joystick.py - библиотека обработки джойстиков
   * joy_control.py - скрипт для управления пионером с джойстика
3) pioneer_sdk - библиотека необходимая для работы всех скриптов
   * piosdk.py - библиотека управления коптером
   
## Подготовка
Необходимо обновить прошивку и параметры автопилота для pioneer mini. Также обновить прошивку модуля wifi.
Сделать это можно с помощью программы Pioneer Station. Инструкции по обновлению Пионера имеются на сайте Геоскан.
   
[Ссылка на обновление прошивки автопилота](https://pioneer-doc.readthedocs.io/ru/master/instructions/pioneer-mini/settings/firmware_upgrade.html)

[Ссылка на обновление модуля wifi](https://pioneer-doc.readthedocs.io/ru/master/instructions/pioneer-mini/settings/esp32-update.html)

Также нужно скачать необходимое программное обеспечение для программирования pioneer mini на языке Python.

[Ссылка на ПО]( https://pioneer-doc.readthedocs.io/ru/master/programming/python/python-sdk-main.html )

После обновления Пионера и установки всех необходимых программ, можно запустить PyCharm.
При первом включениивам нужно будет открыть проект в виртуальной среде: File-Open-указываете путь до скачанного репозитория.
![рис.1-Открытие файла](image\1.png)
Далее проект начнет собираться и на экран выведется окно "Creating Virtual Environment". Это окно заполняется по умолчанию,
нажимаете "Ок" и автоматически начнутся загрузки необходимых компонентов. 
![рис.2-Открытие виртуальной среды](image\2.jpg)
После чего среда разработки выведет ряд ошибок, связанных с отсутствием необходимых библиотек.
Чтобы установить эти компоненты, в нижней части окна найдите "Terminal" и последовательно вводите команды:
 * pip install pymavlink
 * python -m pip install -r requirements.txt

После каждой команды ожидете установки соответствующего пакета. В случае возникновения какой-либо ошибки в терминале
наведите курсор на описание ошибки, скорее всего среда разработки подскажет, какой компонент дополнительно нобходимо установить,
чтобы избежать подобных ошибок.   

Также PyCharm, возможно, выведет ошибки, связанные с другими бибилотеками. Для их установки наведите в коде на ошибку
(подчеркнутая красным курсивом строка), после чего появится значок подсказок (оранжевая лампочка), в которой можно выбрать установку библиотек.
В Терминале ничего вводить не нужно, они установятся автоматически, после чего ошибки исчезнут.

## Тестирование с помощью testPioneer.py
Для запуска программ тестирования необходимо подключить pioneer mini по wifi к компьютеру (инструкция выше) и запустить скрипт из папки testPioneer.py.
В нижней части экрана в окне "Python Console" будут выводится результаты тестирования того или иного компонента квадрокоптера, там же вы можете вводить ответы на вопросы.

Перед каждым тестом выводится название теста:
 * Проверка моторов
 * Проверка светодиодов
 * Проверка камеры
 * Проверка оптического потока, взлета и посадки
 * Проверка полета в точку
 * Проверка запуска луа скрипта
 * Проверка управления с помощью каналов
 * Проверка работы сенсора дистанции

В конце каждого теста вопрос с проверкой результата: 
 * Для положительного ответа нажмите введите "+" и нажмите enter

По окончанит тестирования появится надпись: 
 * Для завершения тестирования нажмите любую клавишу

Результаты тестирования будут сформированы в таблицу Excel в папку test_app.

## Управление с помощью joy_control.py
Для запуска программы управления pioneer mini с помощью
джойстика необходимо подключить ваш джойстик к компьютеру.
А также подключить Пионер по wifi (инструкция выше) и подготовить его к полету. Запустить скрипт из папки joy_control.py.

На данный момент возможно подключение 5 видов:
 * PS4 Controller
 * Defender COBRA M5 USB Joystick
 * Xbox 360 Controller
 * Controller (Rumble Gamepad F510)
 * Logitech Rumblepad 2 USB

В нижней части экрана в окне "Python Console" будут выводится результаты с левого и правого стиков подключенного джойстика.
Левый отвечает за полет вверх/вниз и повороты, а правый за полет вперед/назад и влево/вправо.
