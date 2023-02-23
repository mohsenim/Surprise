# Analyzing Unpredictability and Surprise in Text
To analyze unpredictability and "surprise" in text we calculated two entropy measures:

* Shannon Entropy (ShEn) as a global measure of unpredictability

* Approximate Entropy (ApEn) as a local measure of surprise (unpredictability in a specific context)

This repository contains codes that calculate ShEn and ApEn for texts in the folder _corpus_. Texts should be annotated with POSTags (look at the sample texts). Each subfolder in _corpus_ is considered as a text categoty. 
To run the code set the parameters and run _Main.py_.
Parameters can be set in _parameters.py_. The main parameters are:
* _working_dir_: where the final feature file is saved.
* _corpus_main_dir: the path to the text files
* _text_property_: the entropy measures can be applied to series of sentence length or series of POSTags frequencies in windows of texts. In the latter case, we will have the following parameters as well.
* _pos_tag_segmentation_size_: the size of windows 
* _traget_postag_: the postag(s) that its ferquency is counted. 
* _postag_word_interval_: is the interval between each word and its POSTag.
* _features_file_path_: the name of the file containing ShEn and ApEn values in the end.

Using these two measures, we analyzed texts in three different text categories: canonical/fictional, non-canonical/fictional and  non-fictional texts.
We showed that canonical and non-canonical texts differ in sequential structure, while inter-genre differences (fictional vs. non-fictional) are a matter of the overall distribution of local
frequencies [1].


In another study [2], We showed that unpredictability and surprise analysis can differentiate between preferred and non-preferred texts in different time periods.
We analyzed contemporary texts and texts from the 19th and early 20th centuries. Preferred texts from both periods (contemporary bestsellers and canonical earlier texts) are characterized by higher degrees of unpredictability. However, preference in contemporary texts is reflected in global (text-level) distributions only (as measured with Shannon Entropy), while surprise in local distributions (as measured with Approximate Entropy) does not have an additional discriminating effect.




### References:

[1] Mohseni, M.; Redies, C.; Gast, V. Approximate Entropy in Canonical and Non-Canonical Fiction. Entropy 2022, 24, 278. https://doi.org/10.3390/e24020278 

[2] Mohseni, M.; Redies, C.; Gast, V. Comparative Analysis of Preference in Contemporary and Earlier Texts Using Entropy Measures, (under review).

