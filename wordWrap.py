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


class wordWrap:
    def __init__(self, text):
        # Инициализация компонентов Natasha
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        self.emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)

        # Анализ текста с использованием объекта Doc
        self.doc = Doc(text)

        # Обработка текста Natasha
        self.doc.segment(self.segmenter)
        self.doc.tag_morph(self.morph_tagger)
        self.doc.parse_syntax(self.syntax_parser)
