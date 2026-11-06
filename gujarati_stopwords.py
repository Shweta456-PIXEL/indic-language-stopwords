# =============================================================================
# Project Title : Indic Language Stop Words for NLP
# Author        : [Your Name]
# Description   : A beginner-friendly Gujarati (ગુજરાતી) stopword list with a small
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
#   stopwords-iso Gujarati list, 'stopwords-gu' (224 words).
#     https://github.com/stopwords-iso/stopwords-gu  (MIT licence)
#   Gujarati is not included in the NLTK stopwords corpus (checked 6 November 2026).
#   Not verified: the repository README does not say how the list was compiled or
#     by whom, so its original authorship and method are not stated here.
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
gujarati_stopwords = [
    "અંગે", "અંદર", "અથવા", "અને", "અમને", "અમારું",
    "અમે", "અહીં", "આ", "આગળ", "આથી", "આનું",
    "આને", "આપણને", "આપણું", "આપણે", "આપી", "આર",
    "આવી", "આવે", "ઉપર", "ઉભા", "ઊંચે", "ઊભું",
    "એ", "એક", "એન", "એના", "એનાં", "એની",
    "એનું", "એને", "એનો", "એમ", "એવા", "એવાં",
    "એવી", "એવું", "એવો", "ઓછું", "કંઈક", "કઈ",
    "કયું", "કયો", "કરતાં", "કરવું", "કરી", "કરીએ",
    "કરું", "કરે", "કરેલું", "કર્યા", "કર્યાં", "કર્યું",
    "કર્યો", "કાંઈ", "કે", "કેટલું", "કેમ", "કેવી",
    "કેવું", "કોઈ", "કોઈક", "કોણ", "કોણે", "કોને",
    "ક્યાં", "ક્યારે", "ખૂબ", "ગઈ", "ગયા", "ગયાં",
    "ગયું", "ગયો", "ઘણું", "છ", "છતાં", "છીએ",
    "છું", "છે", "છેક", "છો", "જ", "જાય",
    "જી", "જે", "જેટલું", "જેને", "જેમ", "જેવી",
    "જેવું", "જેવો", "જો", "જોઈએ", "જ્યાં", "જ્યારે",
    "ઝાઝું", "તને", "તમને", "તમારું", "તમે", "તા",
    "તારાથી", "તારામાં", "તારું", "તું", "તે", "તેં",
    "તેઓ", "તેણે", "તેથી", "તેના", "તેની", "તેનું",
    "તેને", "તેમ", "તેમનું", "તેમને", "તેવી", "તેવું",
    "તો", "ત્યાં", "ત્યારે", "થઇ", "થઈ", "થઈએ",
    "થતા", "થતાં", "થતી", "થતું", "થતો", "થયા",
    "થયાં", "થયું", "થયેલું", "થયો", "થવું", "થાઉં",
    "થાઓ", "થાય", "થી", "થોડું", "દરેક", "ન",
    "નં", "નં.", "નથી", "નહિ", "નહી", "નહીં",
    "ના", "ની", "નીચે", "નું", "ને", "નો",
    "પછી", "પણ", "પર", "પરંતુ", "પહેલાં", "પાછળ",
    "પાસે", "પોતાનું", "પ્રત્યેક", "ફક્ત", "ફરી", "ફરીથી",
    "બંને", "બધા", "બધું", "બની", "બહાર", "બહુ",
    "બાદ", "બે", "મને", "મા", "માં", "માટે",
    "માત્ર", "મારું", "મી", "મૂકવું", "મૂકી", "મૂક્યા",
    "મૂક્યાં", "મૂક્યું", "મેં", "રહી", "રહે", "રહેવું",
    "રહ્યા", "રહ્યાં", "રહ્યો", "રીતે", "રૂ.", "રૂા",
    "લેતા", "લેતું", "લેવા", "વગેરે", "વધુ", "શકે",
    "શા", "શું", "સરખું", "સામે", "સુધી", "હતા",
    "હતાં", "હતી", "હતું", "હવે", "હશે", "હશો",
    "હા", "હું", "હો", "હોઈ", "હોઈશ", "હોઈશું",
    "હોય", "હોવા",
]

# Punctuation to strip from the edges of each word. It includes the danda (।)
# and double danda (॥), which are used as full stops in Indic scripts.
PUNCTUATION = ".,;:!?\"'()[]{}-\u2013\u2014\u2026\u0964\u0965"


def remove_stopwords(text, stopwords=gujarati_stopwords):
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
# (python gujarati_stopwords.py). It does not run when the file is imported.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Some Windows terminals do not print Indic scripts unless output is UTF-8.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    # Illustrative sentence written for this project (not taken from any text).
    # Approximate English meaning (my own gloss): This book is very good and there are many stories in it.
    sentence = "આ પુસ્તક ખૂબ સારું છે અને તેમાં ઘણી વાર્તાઓ છે."

    words_before = sentence.split()
    words_after = remove_stopwords(sentence)

    print("Gujarati stopwords in list:", len(gujarati_stopwords))
    print("Original sentence :", sentence)
    print("Words before      :", len(words_before))
    print("After removal     :", " ".join(words_after))
    print("Words after       :", len(words_after))
