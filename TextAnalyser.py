from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    Doc
)


class TextAnalyser:
    def __init__(self, text):
        # Инициализация компонентов Natasha
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        self.emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)
        self.text = text

        # Анализ текста с использованием объекта Doc
        self.doc = Doc(self.text)

        # Обработка текста Natasha
        self.doc.segment(self.segmenter)
        self.doc.tag_morph(self.morph_tagger)
        self.doc.parse_syntax(self.syntax_parser)

    def search_word(self, word):
        count = 0
        # Поиск сочетаний "слово" + прилагательное
        for token in self.doc.tokens:
            if word == token.text:
                for item in self.doc.tokens:
                    if item.head_id == token.id and item.rel == 'amod':
                        adjective = item.text
                        sentence_id = None
                        for i, sentence in enumerate(self.doc.sents):
                            if token in sentence.tokens:
                                sentence_id = i
                                break
                        if sentence_id is not None:
                            sentence_text = self.doc.sents[sentence_id].text
                            print(f"Сочетание {token.text} {adjective}")
                            print(f"Предложение: {sentence_text}\n")
                            count += 1
        return count
