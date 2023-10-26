from wordWrap import wordWrap

with open(r"Bulgakov.txt") as fp:
    text = '. '.join(i.replace('\n', '') for i in fp.readlines() if i.replace('\n', ''))

while ".." in text:
    text = text.replace("..", ". ")
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
