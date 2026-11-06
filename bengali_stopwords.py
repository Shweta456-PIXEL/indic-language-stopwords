# =============================================================================
# Project Title : Indic Language Stop Words for NLP
# Author        : [Your Name]
# Description   : A beginner-friendly Bengali (বাংলা) stopword list with a small
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
#   NLTK stopwords corpus, language file 'bengali' (398 words).
#     Access in Python: nltk.download('stopwords'); stopwords.words('bengali')
#     Project page: https://www.nltk.org/ ; data: https://github.com/nltk/nltk_data
#   Cross-check: the same 398 words appear in the stopwords-iso Bengali list
#     (https://github.com/stopwords-iso/stopwords-bn, MIT licence). I compared
#     the two lists on 6 November 2026 and the sets of words are identical.
#   Not verified: the NLTK corpus README does not say who compiled the Bengali
#     list, so its original authorship is not stated here.
#   Note on encoding: 10 entries use the single character U+09DF (য়), and 9 of them
#     also appear in the list as the two-character form U+09AF + U+09BC. They look
#     identical on screen. The list is kept exactly as published; the helper function
#     below normalises text to Unicode NFC so that both forms are matched.
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
bengali_stopwords = [
    "অতএব", "অথচ", "অথবা", "অনুযায়ী", "অনেক", "অনেকে",
    "অনেকেই", "অন্তত", "অন্য", "অবধি", "অবশ্য", "অর্থাত",
    "আই", "আগামী", "আগে", "আগেই", "আছে", "আজ",
    "আদ্যভাগে", "আপনার", "আপনি", "আবার", "আমরা", "আমাকে",
    "আমাদের", "আমার", "আমি", "আর", "আরও", "ই",
    "ইত্যাদি", "ইহা", "উচিত", "উত্তর", "উনি", "উপর",
    "উপরে", "এ", "এঁদের", "এঁরা", "এই", "একই",
    "একটি", "একবার", "একে", "এক্", "এখন", "এখনও",
    "এখানে", "এখানেই", "এটা", "এটাই", "এটি", "এত",
    "এতটাই", "এতে", "এদের", "এব", "এবং", "এবার",
    "এমন", "এমনকী", "এমনি", "এর", "এরা", "এল",
    "এস", "এসে", "ঐ", "ও", "ওঁদের", "ওঁর",
    "ওঁরা", "ওই", "ওকে", "ওখানে", "ওদের", "ওর",
    "ওরা", "কখনও", "কত", "কবে", "কমনে", "কয়েক",
    "কয়েকটি", "করছে", "করছেন", "করতে", "করবে", "করবেন",
    "করলে", "করলেন", "করা", "করাই", "করায়", "করার",
    "করি", "করিতে", "করিয়া", "করিয়ে", "করে", "করেই",
    "করেছিলেন", "করেছে", "করেছেন", "করেন", "কাউকে", "কাছ",
    "কাছে", "কাজ", "কাজে", "কারও", "কারণ", "কি",
    "কিংবা", "কিছু", "কিছুই", "কিন্তু", "কী", "কে",
    "কেউ", "কেউই", "কেখা", "কেন", "কোটি", "কোন",
    "কোনও", "কোনো", "ক্ষেত্রে", "কয়েক", "খুব", "গিয়ে",
    "গিয়েছে", "গিয়ে", "গুলি", "গেছে", "গেল", "গেলে",
    "গোটা", "চলে", "চান", "চায়", "চার", "চালু",
    "চেয়ে", "চেষ্টা", "ছাড়া", "ছাড়াও", "ছিল", "ছিলেন",
    "জন", "জনকে", "জনের", "জন্য", "জন্যওজে", "জানতে",
    "জানা", "জানানো", "জানায়", "জানিয়ে", "জানিয়েছে", "জে",
    "জ্নজন", "টি", "ঠিক", "তখন", "তত", "তথা",
    "তবু", "তবে", "তা", "তাঁকে", "তাঁদের", "তাঁর",
    "তাঁরা", "তাঁাহারা", "তাই", "তাও", "তাকে", "তাতে",
    "তাদের", "তার", "তারপর", "তারা", "তারৈ", "তাহলে",
    "তাহা", "তাহাতে", "তাহার", "তিনঐ", "তিনি", "তিনিও",
    "তুমি", "তুলে", "তেমন", "তো", "তোমার", "থাকবে",
    "থাকবেন", "থাকা", "থাকায়", "থাকে", "থাকেন", "থেকে",
    "থেকেই", "থেকেও", "দিকে", "দিতে", "দিন", "দিয়ে",
    "দিয়েছে", "দিয়েছেন", "দিলেন", "দু", "দুই", "দুটি",
    "দুটো", "দেওয়া", "দেওয়ার", "দেওয়া", "দেখতে", "দেখা",
    "দেখে", "দেন", "দেয়", "দ্বারা", "ধরা", "ধরে",
    "ধামার", "নতুন", "নয়", "না", "নাই", "নাকি",
    "নাগাদ", "নানা", "নিজে", "নিজেই", "নিজেদের", "নিজের",
    "নিতে", "নিয়ে", "নিয়ে", "নেই", "নেওয়া", "নেওয়ার",
    "নেওয়া", "নয়", "পক্ষে", "পর", "পরে", "পরেই",
    "পরেও", "পর্যন্ত", "পাওয়া", "পাচ", "পারি", "পারে",
    "পারেন", "পি", "পেয়ে", "পেয়্র্", "প্রতি", "প্রথম",
    "প্রভৃতি", "প্রযন্ত", "প্রাথমিক", "প্রায়", "প্রায়", "ফলে",
    "ফিরে", "ফের", "বক্তব্য", "বদলে", "বন", "বরং",
    "বলতে", "বলল", "বললেন", "বলা", "বলে", "বলেছেন",
    "বলেন", "বসে", "বহু", "বা", "বাদে", "বার",
    "বি", "বিনা", "বিভিন্ন", "বিশেষ", "বিষয়টি", "বেশ",
    "বেশি", "ব্যবহার", "ব্যাপারে", "ভাবে", "ভাবেই", "মতো",
    "মতোই", "মধ্যভাগে", "মধ্যে", "মধ্যেই", "মধ্যেও", "মনে",
    "মাত্র", "মাধ্যমে", "মোট", "মোটেই", "যখন", "যত",
    "যতটা", "যথেষ্ট", "যদি", "যদিও", "যা", "যাঁর",
    "যাঁরা", "যাওয়া", "যাওয়ার", "যাওয়া", "যাকে", "যাচ্ছে",
    "যাতে", "যাদের", "যান", "যাবে", "যায়", "যার",
    "যারা", "যিনি", "যে", "যেখানে", "যেতে", "যেন",
    "যেমন", "র", "রকম", "রয়েছে", "রাখা", "রেখে",
    "লক্ষ", "শুধু", "শুরু", "সঙ্গে", "সঙ্গেও", "সব",
    "সবার", "সমস্ত", "সম্প্রতি", "সহ", "সহিত", "সাধারণ",
    "সামনে", "সি", "সুতরাং", "সে", "সেই", "সেখান",
    "সেখানে", "সেটা", "সেটাই", "সেটাও", "সেটি", "স্পষ্ট",
    "স্বয়ং", "হইতে", "হইবে", "হইয়া", "হওয়া", "হওয়ায়",
    "হওয়ার", "হচ্ছে", "হত", "হতে", "হতেই", "হন",
    "হবে", "হবেন", "হয়", "হয়তো", "হয়নি", "হয়ে",
    "হয়েই", "হয়েছিল", "হয়েছে", "হয়েছেন", "হল", "হলে",
    "হলেই", "হলেও", "হলো", "হাজার", "হিসাবে", "হৈলে",
    "হোক", "হয়",
]

# Punctuation to strip from the edges of each word. It includes the danda (।)
# and double danda (॥), which are used as full stops in Indic scripts.
PUNCTUATION = ".,;:!?\"'()[]{}-\u2013\u2014\u2026\u0964\u0965"


def remove_stopwords(text, stopwords=bengali_stopwords):
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
# (python bengali_stopwords.py). It does not run when the file is imported.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Some Windows terminals do not print Indic scripts unless output is UTF-8.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    # Illustrative sentence written for this project (not taken from any text).
    # Approximate English meaning (my own gloss): This book is very good and there are many stories in it.
    sentence = "এই বইটি খুব ভালো এবং এর মধ্যে অনেক গল্প আছে।"

    words_before = sentence.split()
    words_after = remove_stopwords(sentence)

    print("Bengali stopwords in list:", len(bengali_stopwords))
    print("Original sentence :", sentence)
    print("Words before      :", len(words_before))
    print("After removal     :", " ".join(words_after))
    print("Words after       :", len(words_after))
