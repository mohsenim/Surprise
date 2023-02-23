import logging
import parameters
import re
import numpy as np


def sentence_length(sentences):
    output = np.zeros(len(sentences))
    for i, sent in enumerate(sentences):
        output[i] = len(sent)
    return output


def pos_tag_counter(wordtaglist):

    def _counter(wordtaglist, target_postag):
        count = 0
        for wordtag in wordtaglist:
            postag_split = wordtag.split(parameters.pos_word_tag_interval)
            if len(postag_split) < 2:
                logging.warning('An error in POS-tagged file!', wordtaglist)
                continue
            postag = postag_split[1]
            if re.match(target_postag, postag, re.IGNORECASE):
                count += 1
        return count

    counts = np.zeros(len(wordtaglist) // parameters.pos_tag_segmentation_size)
    for i in range(counts.size):
        segment = wordtaglist[i * parameters.pos_tag_segmentation_size: (i + 1) * parameters.pos_tag_segmentation_size]
        c = _counter(segment, parameters.target_postag)
        counts[i] = c
    return counts

