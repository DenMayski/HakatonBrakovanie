import chardet
import os
from wordWrap import wordWrap

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

dd = wordWrap(text)

while (wordSearch := input("Введите слово для поиска ").strip().lower()):
    count = 0
    # Поиск сочетаний "слово" + прилагательное
    for token in dd.doc.tokens:
        if wordSearch == token.text:
            for item in dd.doc.tokens:
                if item.head_id == token.id and item.rel == 'amod':
                    adjective = item.text
                    sentence_id = None
                    for i, sentence in enumerate(dd.doc.sents):
                        if token in sentence.tokens:
                            sentence_id = i
                            break
                    if sentence_id is not None:
                        sentence_text = dd.doc.sents[sentence_id].text
                        print(f"Сочетание {token.text} {adjective}")
                        print(f"Предложение: {sentence_text}\n")
                        count += 1
    if not count:
        print("Это слово не встречается с прилагательными")
    print()
