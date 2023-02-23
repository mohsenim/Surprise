from enum import Enum
import os

working_dir = "./working_dir/"

corpus_main_dir = os.path.join(working_dir, 'corpus')
corpus_lowercase = True


class TextPropertyNames(Enum):
    POSTAG = 'postag'
    SENT_LENGTH = 'sentlength'


text_property = TextPropertyNames.SENT_LENGTH  # or TextPropertyNames.SENT_LENGTH
pos_tag_segmentation_size = 25  # size of boxes/windows
target_postag = 'NN'  # We use a regext matching, meaning that nn counts nn and nnp and so on.
pos_word_tag_interval = '_$$_'

# name of the features file
feature_filename_extention = TextPropertyNames.SENT_LENGTH.value if text_property == TextPropertyNames.SENT_LENGTH \
    else 'segmentsize-{}-{}'.format(str(pos_tag_segmentation_size), target_postag)
features_file_path = os.path.join(working_dir,
                                  'features-{}.csv'.format(feature_filename_extention))
