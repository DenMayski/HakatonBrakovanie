import chardet
import os
from TextAnalyser import TextAnalyser

while True:
    choose = input("1) Ввод текста вручную\n2) Указать ссылку на файл\n").strip()
    if choose in ['1', '2']:
        break
    else:
        print("Такого действия нет")
if choose == '1':
    text = input("Введите текст\n")
else:
    while True:
        file = input("Введите абсолютную ссылку на файл\n")
        if os.path.exists(file):
            # Определение кодировки файла
            with open(file, 'rb') as fp:
                result = chardet.detect(fp.read())
            with open(file, encoding=result['encoding']) as fp:
                text = '. '.join(i.replace('\n', '') for i in fp.readlines() if i.replace('\n', ''))
            while ".." in text:
                text = text.replace("..", ". ")
            break
        else:
            print("Файл не найден")

dd = TextAnalyser(text)
while wordSearch := input("Введите слово для поиска ").strip().lower():
    if not dd.search_word(wordSearch):
        print(f"Слово {wordSearch} не встречается с прилагательным в тексте")
    print()
