from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsNERTagger,
    NewsSyntaxParser,
    PER,
    Doc
)

with open(r"Bulgakov.txt") as fp:
    text = '. '.join(i.replace('\n', '') for i in fp.readlines() if i.replace('\n', ''))

while ".." in text:
    text = text.replace("..", ". ")

# Инициализация компонентов Natasha
segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

# Анализ текста с использованием объекта Doc
doc = Doc(text)

# Обработка текста Natasha
doc.segment(segmenter)
doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)

while (wordSearch := input("Введите слово для поиска ").strip().lower()):
    count = 0
    # Поиск сочетаний "кошка" + прилагательное
    for token in doc.tokens:
        if wordSearch == token.text:
            for item in doc.tokens:
                if item.head_id == token.id and item.rel == 'amod':
                    adjective = item.text
                    sentence_id = None
                    for i, sentence in enumerate(doc.sents):
                        if token in sentence.tokens:
                            sentence_id = i
                            break
                    if sentence_id is not None:
                        sentence_text = doc.sents[sentence_id].text
                        print(f"Сочетание {token.text} {adjective}")
                        print(f"Предложение: {sentence_text}\n")
                        count+=1
    if not count:
        print("Это слово не встречается с прилагательными")
    print()