# Analyzing Unpredictability and Surprise in Text
This repository contains codes that calculate Shannon Entropy (ShEn) and Approximate Entropy (ApEn) for texts in the folder _corpus_. Texts should be annotated with POSTags (look at the sample texts). Each subfolder in _corpus_ is considered as a text categoty. 
To run the code, set the parameters in _parameters.py_ and run _Main.py_.
The main parameters are:
* _working\_dir_: where the final feature file is saved.
* _corpus\_main\_dir: the path to the text files
* _text\_property_: the entropy measures can be applied to series of sentence lengths or to series of POSTags frequencies in windows of texts. In the latter case, you should set the following parameters as well.
* _postag\_segmentation\_size_: the size of windows 
* _target\_postag_: the postag(s) that its ferquency is counted. 
* _postag\_word\_interval_: is the interval between each word and its POSTag.
* _features\_file\_path_: the name of the file containing ShEn and ApEn values in the end.


ShEn is a global measure of unpredictability and ApEn a local measure of surprise (unpredictability in a specific context). Using these two measures, we analyzed texts in three different text categories: canonical/fictional, non-canonical/fictional and  non-fictional texts.
We showed that canonical and non-canonical texts differ in sequential structure, while inter-genre differences (fictional vs. non-fictional) are a matter of the overall distribution of local
frequencies [1].


In another study [2], We showed that unpredictability and surprise analysis can differentiate between preferred and non-preferred texts in different time periods.
We analyzed contemporary texts and texts from the 19th and early 20th centuries. Preferred texts from both periods (contemporary bestsellers and canonical earlier texts) are characterized by higher degrees of unpredictability. However, preference in contemporary texts is reflected in global (text-level) distributions only (as measured with Shannon Entropy), while surprise in local distributions (as measured with Approximate Entropy) does not have an additional discriminating effect.




### References:

[1] Mohseni, M.; Redies, C.; Gast, V. Approximate Entropy in Canonical and Non-Canonical Fiction. Entropy 2022, 24, 278. https://doi.org/10.3390/e24020278 

[2] Mohseni, M.; Redies, C.; Gast, V. Comparative Analysis of Preference in Contemporary and Earlier Texts Using Entropy Measures, (under review).

