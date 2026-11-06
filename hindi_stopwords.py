# =============================================================================
# Project Title : Indic Language Stop Words for NLP
# Author        : [Your Name]
# Description   : A beginner-friendly Hindi (हिन्दी) stopword list with a small
#                 function that removes stopwords from a sentence.
# Semester      : Monsoon Semester 2026
# Department    : Department of Humanities and Social Sciences
# Institution   : IIT (ISM) Dhanbad
# =============================================================================
#
# WHAT ARE STOPWORDS?
# Stopwords are very common, mostly grammatical words (for example words that
# mean "and", "is", "of", "this"). They carry little topical meaning by
# themselves.
#
# WHY ARE THEY USED IN NLP?
# In tasks such as word-frequency counts, keyword extraction, search and topic
# modelling, stopwords can dominate the results. Removing them lets the more
# content-bearing words stand out. Stopword removal is a choice, not a rule:
# for some tasks (for example sentiment analysis, authorship studies or
# translation) stopwords matter and should be kept.
#
# SOURCE OF THIS LIST (transparent attribution)
#   stopwords-iso Hindi list, 'stopwords-hi' (225 words).
#     https://github.com/stopwords-iso/stopwords-hi  (MIT licence)
#   Hindi is not included in the NLTK stopwords corpus (checked 6 November 2026).
#   Not verified: the repository README does not say how the list was compiled or
#     by whom, so its original authorship and method are not stated here.
#   Note on encoding: 2 entries (काफ़ी, वग़ैरह) use precomposed nukta characters.
#     The helper function normalises text to Unicode NFC before comparing.
#
# LIMITATIONS
# - This list is not exhaustive and is not claimed to be universally correct.
# - Matching is exact. Inflected forms and attached suffixes (for example
#   case markers joined to a noun) will not match unless they are in the list.
# - Check the list against your own corpus and task before relying on it.
# =============================================================================

import sys
import unicodedata

# The stopword list, kept in the same order as the source.
hindi_stopwords = [
    "अंदर", "अत", "अदि", "अप", "अपना", "अपनि",
    "अपनी", "अपने", "अभि", "अभी", "आदि", "आप",
    "इंहिं", "इंहें", "इंहों", "इतयादि", "इत्यादि", "इन",
    "इनका", "इन्हीं", "इन्हें", "इन्हों", "इस", "इसका",
    "इसकि", "इसकी", "इसके", "इसमें", "इसि", "इसी",
    "इसे", "उंहिं", "उंहें", "उंहों", "उन", "उनका",
    "उनकि", "उनकी", "उनके", "उनको", "उन्हीं", "उन्हें",
    "उन्हों", "उस", "उसके", "उसि", "उसी", "उसे",
    "एक", "एवं", "एस", "एसे", "ऐसे", "ओर",
    "और", "कइ", "कई", "कर", "करता", "करते",
    "करना", "करने", "करें", "कहते", "कहा", "का",
    "काफि", "काफ़ी", "कि", "किंहें", "किंहों", "कितना",
    "किन्हें", "किन्हों", "किया", "किर", "किस", "किसि",
    "किसी", "किसे", "की", "कुछ", "कुल", "के",
    "को", "कोइ", "कोई", "कोन", "कोनसा", "कौन",
    "कौनसा", "गया", "घर", "जब", "जहाँ", "जहां",
    "जा", "जिंहें", "जिंहों", "जितना", "जिधर", "जिन",
    "जिन्हें", "जिन्हों", "जिस", "जिसे", "जीधर", "जेसा",
    "जेसे", "जैसा", "जैसे", "जो", "तक", "तब",
    "तरह", "तिंहें", "तिंहों", "तिन", "तिन्हें", "तिन्हों",
    "तिस", "तिसे", "तो", "था", "थि", "थी",
    "थे", "दबारा", "दवारा", "दिया", "दुसरा", "दुसरे",
    "दूसरे", "दो", "द्वारा", "न", "नहिं", "नहीं",
    "ना", "निचे", "निहायत", "नीचे", "ने", "पर",
    "पहले", "पुरा", "पूरा", "पे", "फिर", "बनि",
    "बनी", "बहि", "बही", "बहुत", "बाद", "बाला",
    "बिलकुल", "भि", "भितर", "भी", "भीतर", "मगर",
    "मानो", "मे", "में", "यदि", "यह", "यहाँ",
    "यहां", "यहि", "यही", "या", "यिह", "ये",
    "रखें", "रवासा", "रहा", "रहे", "ऱ्वासा", "लिए",
    "लिये", "लेकिन", "व", "वगेरह", "वरग", "वर्ग",
    "वह", "वहाँ", "वहां", "वहिं", "वहीं", "वाले",
    "वुह", "वे", "वग़ैरह", "संग", "सकता", "सकते",
    "सबसे", "सभि", "सभी", "साथ", "साबुत", "साभ",
    "सारा", "से", "सो", "हि", "ही", "हुअ",
    "हुआ", "हुइ", "हुई", "हुए", "हे", "हें",
    "है", "हैं", "हो", "होता", "होति", "होती",
    "होते", "होना", "होने",
]

# Punctuation to strip from the edges of each word. It includes the danda (।)
# and double danda (॥), which are used as full stops in Indic scripts.
PUNCTUATION = ".,;:!?\"'()[]{}-\u2013\u2014\u2026\u0964\u0965"


def remove_stopwords(text, stopwords=hindi_stopwords):
    """Return a list of the words in `text` that are NOT stopwords.

    Steps: (1) split the text on spaces, (2) strip punctuation from each word,
    (3) normalise to Unicode NFC so that look-alike character sequences match,
    (4) keep the word only if it is not in the stopword set.
    """
    stopword_set = {unicodedata.normalize("NFC", w) for w in stopwords}
    kept_words = []
    for word in text.split():
        cleaned = unicodedata.normalize("NFC", word.strip(PUNCTUATION))
        if cleaned and cleaned not in stopword_set:
            kept_words.append(cleaned)
    return kept_words


# -----------------------------------------------------------------------------
# Example: runs only when you execute this file directly
# (python hindi_stopwords.py). It does not run when the file is imported.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Some Windows terminals do not print Indic scripts unless output is UTF-8.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    # Illustrative sentence written for this project (not taken from any text).
    # Approximate English meaning (my own gloss): This book is very good and there are many stories in it.
    sentence = "यह किताब बहुत अच्छी है और इसमें कई कहानियाँ हैं।"

    words_before = sentence.split()
    words_after = remove_stopwords(sentence)

    print("Hindi stopwords in list:", len(hindi_stopwords))
    print("Original sentence :", sentence)
    print("Words before      :", len(words_before))
    print("After removal     :", " ".join(words_after))
    print("Words after       :", len(words_after))
