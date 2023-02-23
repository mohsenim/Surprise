from nltk import corpus
from nltk.tokenize.regexp import RegexpTokenizer, WhitespaceTokenizer
import parameters
import logging
import os


class Corpus(corpus.PlaintextCorpusReader):
    def __init__(self, path):

        class LowercaseTokenizer:
            def __init__(self, tokenizer):
                self.tokenizer = tokenizer

            def tokenize(self, text):
                return self.tokenizer.tokenize(str.lower(text))

        class LineTokenizer(RegexpTokenizer):
            def __init__(self):
                RegexpTokenizer.__init__(self, '[^\n]+')

        if parameters.corpus_lowercase:
            logging.info('Building corpuse -- Texts are lowercased!')
            corpus.PlaintextCorpusReader.__init__(self, root=path, fileids='.*',
                                                      word_tokenizer=LowercaseTokenizer(WhitespaceTokenizer()),
                                                      sent_tokenizer=LowercaseTokenizer(LineTokenizer()))
        else:
            logging.info('Building corpuse -- Texts are NOT lowercased!')
            corpus.PlaintextCorpusReader.__init__(self, root=path, fileids='.*',
                                                      word_tokenizer=WhitespaceTokenizer(),
                                                      sent_tokenizer=LineTokenizer())

    def word(self, id):
        return list(super(Corpus, self).words(id))

    def tokens(self, id):
        return self.word(id)

    def sents(self, id):
        ss = []
        for s in super(Corpus, self).sents(id):
            ss.append([w for w in s])
        return ss


if __name__=='__main__':
    c = Corpus(parameters.corpus_main_dir)
    print('Corpus in path "{}" with {} files!'.format(c.root, len(c.fileids())))
