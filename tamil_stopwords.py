# =============================================================================
# Project Title : Indic Language Stop Words for NLP
# Author        : [Your Name]
# Description   : A beginner-friendly Tamil (தமிழ்) stopword list with a small
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
#   NLTK stopwords corpus, language file 'tamil' (125 words).
#     Access in Python: nltk.download('stopwords'); stopwords.words('tamil')
#     Project page: https://www.nltk.org/ ; data: https://github.com/nltk/nltk_data
#   Tamil is not in the stopwords-iso combined collection I checked.
#   Not verified: the NLTK corpus README does not say who compiled the Tamil
#     list, so its original authorship and method are not stated here.
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
tamil_stopwords = [
    "அங்கு", "அங்கே", "அடுத்த", "அதனால்", "அதன்", "அதற்கு",
    "அதிக", "அதில்", "அது", "அதே", "அதை", "அந்த",
    "அந்தக்", "அந்தப்", "அன்று", "அல்லது", "அவன்", "அவரது",
    "அவர்", "அவர்கள்", "அவள்", "அவை", "ஆகிய", "ஆகியோர்",
    "ஆகும்", "இங்கு", "இங்கே", "இடத்தில்", "இடம்", "இதனால்",
    "இதனை", "இதன்", "இதற்கு", "இதில்", "இது", "இதை",
    "இந்த", "இந்தக்", "இந்தத்", "இந்தப்", "இன்னும்", "இப்போது",
    "இரு", "இருக்கும்", "இருந்த", "இருந்தது", "இருந்து", "இவர்",
    "இவை", "உன்", "உள்ள", "உள்ளது", "உள்ளன", "எந்த",
    "என", "எனக்", "எனக்கு", "எனப்படும்", "எனவும்", "எனவே",
    "எனினும்", "எனும்", "என்", "என்ன", "என்னும்", "என்பது",
    "என்பதை", "என்ற", "என்று", "என்றும்", "எல்லாம்", "ஏன்",
    "ஒரு", "ஒரே", "ஓர்", "கொண்ட", "கொண்டு", "கொள்ள",
    "சற்று", "சிறு", "சில", "சேர்ந்த", "தனது", "தன்",
    "தவிர", "தான்", "நான்", "நாம்", "நீ", "பற்றி",
    "பற்றிய", "பல", "பலரும்", "பல்வேறு", "பின்", "பின்னர்",
    "பிற", "பிறகு", "பெரும்", "பேர்", "போது", "போன்ற",
    "போல", "போல்", "மட்டுமே", "மட்டும்", "மற்ற", "மற்றும்",
    "மிக", "மிகவும்", "மீது", "முதல்", "முறை", "மேலும்",
    "மேல்", "யார்", "வந்த", "வந்து", "வரும்", "வரை",
    "வரையில்", "விட", "விட்டு", "வேண்டும்", "வேறு",
]

# Punctuation to strip from the edges of each word. It includes the danda (।)
# and double danda (॥), which are used as full stops in Indic scripts.
PUNCTUATION = ".,;:!?\"'()[]{}-\u2013\u2014\u2026\u0964\u0965"


def remove_stopwords(text, stopwords=tamil_stopwords):
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
# (python tamil_stopwords.py). It does not run when the file is imported.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Some Windows terminals do not print Indic scripts unless output is UTF-8.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    # Illustrative sentence written for this project (not taken from any text).
    # Approximate English meaning (my own gloss): This book is very good, and there are many stories in it.
    sentence = "இந்த புத்தகம் மிகவும் நல்லது மற்றும் அதில் பல கதைகள் உள்ளன."

    words_before = sentence.split()
    words_after = remove_stopwords(sentence)

    print("Tamil stopwords in list:", len(tamil_stopwords))
    print("Original sentence :", sentence)
    print("Words before      :", len(words_before))
    print("After removal     :", " ".join(words_after))
    print("Words after       :", len(words_after))
