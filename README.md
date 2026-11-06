# Indic Language Stop Words for NLP

A beginner-friendly Python project that provides stopword lists for four Indian languages (Bengali, Gujarati, Hindi and Tamil), each with a small example of removing stopwords from a sentence.

**Course:** DH Lab 2, Monsoon Semester 2026
**Department:** Department of Humanities and Social Sciences, IIT (ISM) Dhanbad
**Author:** [Your Name]

---

## 1. Project overview

Each language has its own Python file containing a list named `<language>_stopwords` and a function `remove_stopwords(text, stopwords)`. The files use only Python's standard library, so there is nothing to install. Every file has comments explaining what stopwords are, where its list comes from, and what the list cannot do.

## 2. What are stopwords?

Stopwords are very common, mostly grammatical words (words meaning "and", "is", "of", "this" and so on). On their own they say little about what a text is *about*.

## 3. Why are stopwords useful in NLP?

In tasks such as word-frequency counts, keyword extraction, document search and topic modelling, the most frequent words are usually stopwords, and they can hide the content words a researcher cares about. Removing them can make results easier to read and can reduce the size of the data. This is a choice that depends on the task (see Limitations).

## 4. Languages covered

| Language | Script | Variable | Words in list | Source |
|---|---|---|---|---|
| Bengali | বাংলা | `bengali_stopwords` | 398 | NLTK stopwords corpus (identical to stopwords-iso `bn`) |
| Gujarati | ગુજરાતી | `gujarati_stopwords` | 224 | stopwords-iso `gu` |
| Hindi | हिन्दी | `hindi_stopwords` | 225 | stopwords-iso `hi` |
| Tamil | தமிழ் | `tamil_stopwords` | 125 | NLTK stopwords corpus |

## 5. Repository file descriptions

```
indic-language-stopwords/
|-- README.md               This file
|-- bengali_stopwords.py    Bengali list + remove_stopwords() + demo
|-- gujarati_stopwords.py   Gujarati list + remove_stopwords() + demo
|-- hindi_stopwords.py      Hindi list + remove_stopwords() + demo
`-- tamil_stopwords.py      Tamil list + remove_stopwords() + demo
```

Each `.py` file contains, in order: a header comment, explanatory comments and source attribution, the stopword list, the `remove_stopwords()` function, and a demo that runs only when the file is executed directly. All files are saved as UTF-8.

## 6. Installation and usage

**Requirements:** Python 3.8 or newer. No external packages.

```bash
# 1. Check Python
python --version          # on some systems: python3 --version

# 2. Get the files (after you upload them to GitHub)
git clone https://github.com/YOUR-USERNAME/indic-language-stopwords.git
cd indic-language-stopwords

# 3. Run a demo
python hindi_stopwords.py
```

Replace `hindi` with `bengali`, `gujarati` or `tamil` to run the other demos. If Indic characters appear as boxes or question marks in a Windows terminal, the font or terminal encoding is the cause, not the file; each demo already switches output to UTF-8 where possible.

**Expected output (Hindi demo):**

```
Hindi stopwords in list: 225
Original sentence : यह किताब बहुत अच्छी है और इसमें कई कहानियाँ हैं।
Words before      : 10
After removal     : किताब अच्छी कहानियाँ
Words after       : 3
```

How `remove_stopwords()` works: it splits the text on spaces, strips punctuation (including the danda `।`) from each word, normalises the word to Unicode NFC so look-alike character sequences match, and keeps only words that are not in the list. It returns a list of words.

## 7. Importing and using each list

Run these from the project folder (the folder that contains the `.py` files).

```python
# Hindi
from hindi_stopwords import hindi_stopwords, remove_stopwords
print(len(hindi_stopwords))
print(remove_stopwords("यह किताब बहुत अच्छी है।"))        # ['किताब', 'अच्छी']
```

```python
# Bengali
from bengali_stopwords import bengali_stopwords, remove_stopwords
print(remove_stopwords("এই বইটি খুব ভালো।"))              # ['বইটি', 'ভালো']
```

```python
# Gujarati
from gujarati_stopwords import gujarati_stopwords, remove_stopwords
print(remove_stopwords("આ પુસ્તક ખૂબ સારું છે."))          # ['પુસ્તક', 'સારું']
```

```python
# Tamil
from tamil_stopwords import tamil_stopwords, remove_stopwords
print(remove_stopwords("இந்த புத்தகம் மிகவும் நல்லது."))   # ['புத்தகம்', 'நல்லது']
```

Using your own extra words or a shorter list:

```python
from hindi_stopwords import hindi_stopwords, remove_stopwords
my_list = hindi_stopwords + ["किताब"]          # add a word
print(remove_stopwords("यह किताब अच्छी है", my_list))
```

## 8. Sources and acknowledgements

I checked the lists below against their published sources on 6 November 2026. The Python files contain the same words, in the same order as the sources, with no changes. The demo sentences were written for this project and are not taken from any text; the English glosses are my own.

| Language | Source | Notes |
|---|---|---|
| Bengali | **NLTK stopwords corpus**, file `bengali`. NLTK: https://www.nltk.org/ ; data: https://github.com/nltk/nltk_data | The same 398 words appear in stopwords-iso `bn` (https://github.com/stopwords-iso/stopwords-bn); I compared the two lists. |
| Gujarati | **stopwords-iso**, `stopwords-gu`: https://github.com/stopwords-iso/stopwords-gu | MIT licence. Gujarati is not in the NLTK stopwords corpus. |
| Hindi | **stopwords-iso**, `stopwords-hi`: https://github.com/stopwords-iso/stopwords-hi | MIT licence. Hindi is not in the NLTK stopwords corpus. |
| Tamil | **NLTK stopwords corpus**, file `tamil`. | I did not find a Tamil list in the stopwords-iso collection I checked. |

**What I could not verify.** The NLTK corpus README and the stopwords-iso repository READMEs do not say who compiled these four lists or how. I therefore make no claim about their original authors, methods or linguistic coverage. If your assignment needs fuller provenance, contact the maintainers or consult the repositories' histories.

**Licence notices.** The Hindi and Gujarati lists come from stopwords-iso repositories published under the MIT licence (copyright lines: Hindi, "Copyright (c) 2016 Gene Diaz"; Gujarati, "Copyright (c) 2020 Stopwords ISO"). The Bengali list was taken from NLTK; the stopwords-iso Bengali repository (also MIT, "Copyright (c) 2016 Gene Diaz") contains the same words. The MIT licence requires its notice to accompany copies of the material, so the licence text from the Hindi repository is reproduced here:

```
Copyright (c) 2016 Gene Diaz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

I did not locate a licence statement for the NLTK Bengali and Tamil lists specifically within the files I inspected; check the NLTK data repository (https://github.com/nltk/nltk_data) before reuse beyond coursework. No licence file has been added to this repository; add one of your choice if you want others to reuse your own code.

**Optional cross-check with NLTK** (needs `pip install nltk`; not required by this project):

```python
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
print(len(stopwords.words("bengali")), len(stopwords.words("tamil")))   # 398 125 when checked
```

## 9. Limitations

- **Stopword lists are task-dependent.** A word that is noise in one task can be meaningful in another. Removing stopwords can hurt sentiment analysis, stylometry and authorship work, translation, parsing and phrase search (for example negation words or question words).
- **Meaningful words may be removed.** Some entries are ordinary words with content in certain contexts. Review the list against your own corpus before using it.
- **The lists are not exhaustive or universally correct.** They are fixed word lists from third-party sources, not complete accounts of the grammar of any language, and I make no claim of linguistic coverage.
- **Exact matching only.** In these languages, case markers, postpositions and verb endings are often written attached to or inflected with other words. Such forms are not matched unless they appear in the list. For example, in the Gujarati demo the words `તેમાં` and `ઘણી` are not in the list and are kept.
- **Simple tokenisation.** Splitting on spaces and stripping edge punctuation is sufficient for the demos but does not handle all cases (compound words, hyphenation, mixed scripts, numerals). Use a proper tokeniser for serious work.
- **Variant spellings.** The lists include some spelling variants but cannot cover every spelling in real text.
- **Bengali encoding detail.** 9 Bengali entries are visually identical to another entry but encoded with different Unicode characters (precomposed `য়` versus `য` + nukta). They are kept as published; `remove_stopwords()` normalises to NFC, which treats them as the same word.
- **Coursework scope.** This is a learning project and has not been evaluated on any benchmark.
