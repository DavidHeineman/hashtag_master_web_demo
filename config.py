"""Paths to all the resources needed to calculate features.

"""

LM_KN = [
    "static/data/small_kn.bin"
]

LM_GT = [
    "static/data/small_gt.bin" 
]

RESOURCES = {
    "lm_gt": LM_GT,
    "lm_kn": LM_KN,
    "wiki": "static/data/wiki_titles.txt",
    "urban": "static/data/urban_dict_words_A_Z.txt",
    "twitter": "static/data/twitter_counts.tsv",
    "google":  "static/data/google_counts.tsv",
}


def get_resources():
    return RESOURCES
