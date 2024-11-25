import cyrtranslit

mappings = {
    "бутциин": "бүтцийн"
}

# insert the dictionary to transliterate to Mongolian Cyrillic
dictionary = {
        "khutulburiin_dugaar": "7f33f3cf57028703a831717b633393df",
        "khutulburiin_indyeks": "E 011436",
        "khutulburiin_mongol_ner": "Гадаад хэлний боловсрол",
        "khutulburiin_angli_ner": "Foreign Language Education",
        "akadyemik_tuvshin": "Магистр",
        "suraltsakh_khelber": "Өдрийн сургалт",
        "khariyaalakh_negjiin_dugaar": "d8b895cde1c2fac83b938cd1ae057f72",
        "khariyaalakh_negjiin_ner": "Баруун бүсийн сургууль",
        "batlagdsan_on": 2024
    }
# Put the output in google translate to have the translation, minor adjustments may be needed
for k in dictionary:
    text = " ".join(cyrtranslit.to_cyrillic(k, "mn").split("_"))
    for r, t in mappings.items():
        text = text.replace(r, t)
    print(text)