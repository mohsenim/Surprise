import logging
import os
import pandas as pd
import parameters
import Corpus
import Text_Property_Extractor
import Features_Calculator


def run():
    corpus = Corpus.Corpus(parameters.corpus_main_dir)

    records = []
    for fileid in corpus.fileids():
        logging.info('Computing entropy features. Category/Filename: {}'.format(fileid))

        category_filename = fileid.split(os.sep)
        if len(category_filename) > 1:
            category = category_filename[0]
            filename = ''.join(category_filename[1:])
        else:
            category = ''
            filename = fileid

        record = dict()
        record['category'] = category
        record['filename'] = filename

        if parameters.text_property == parameters.TextPropertyNames.SENT_LENGTH:
            sents = corpus.sents(fileid)
            series = Text_Property_Extractor.sentence_length(sents)
        else:
            wordtaglist = corpus.tokens(fileid)
            series = Text_Property_Extractor.pos_tag_counter(wordtaglist)

        record['ap_en'] = Features_Calculator.ApEn(series)
        record['entropy'] = Features_Calculator.Entropy(series)
        records.append(record)
        # df_features = df_features.append(record, ignore_index=True)

    df_features = pd.DataFrame.from_records(records)
    df_features.set_index(['category', 'filename'], inplace=True)
    df_features.to_csv(parameters.features_file_path, sep='\t', float_format='%.5f')


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s')
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Running ....')
    run()

