import cyrtranslit

# insert the dictionary to transliterate to Mongolian Cyrillic
dictionary = {
        "khicheeliin_dugaar": "fffcc1a3964b4ad665fa2f07d7bfd086",
        "khicheeliin_indyeks": "LANG813",
        "mongol_ner": "Эртний франц хэл",
        "angli_ner": "Old French",
        "khariyaalakh_buttsiin_dugaar": "b43d3f04841fc58b6e155df37be8b3f0",
        "khariyaalakh_butets": "Шинжлэх ухааны сургууль",
        "khariyaalakh_tenkhim_dugaar": "2e5a22ad1a6bdea6713db3f508f40a39",
        "khariyaalakh_tenkhim": "Европ судлалын тэнхим",
        "surgaltyn_tuvshin": "Доктор",
        "orokh_uliral": "Улирал харгалзахгүй",
        "zorilgo": "•\tЭртний франц болон латин хэлээрх бичвэрүүдийг уншиж ойлгодог болох \r\n•\tЭртний франц хэлний хэлзүйн анхны мэдэгдэхүүнтэй болох\r\n•\tФранц хэлний үгийн сангаа эртний утгаар баяжуулах \r\n\r\n\r\n",
        "zorilgo_angli": "",
        "tovch_aguulga": "Францын эртний ёгт үлгэр, домог үлгэр, өгүүллэг зэрэг Францын түүх, уран зохиол, гүн ухааны чиглэлийн янз бүрийн агуулгатай олон бүтээлүүдээс түүвэрлэн авсан эртний франц, латин хэл дээрх бичвэрүүдтэй танилцан, тэдгээрийг хөнгөнөөс хүндрүү, богино бичвэрээс урт бичвэр рүү, энгийнээс гүнзгийрүүлэх аргаар уншиж орчуулна. Мөн бичвэрт хэрэглэгдэж буй үг хэллэгүүдийн эртний утга бүрийг мэдэж авахын  зэрэгцээ эртний франц хэлний тархац, түүхэн замналыг судлан мэдэх болно. ",
        "tovch_aguulga_angli": "This course is linguistic approach to French  language history, with emphasis on earlier version of French  language and its derivations as  a way of communication, extension of France culture, cultural values and tradition. ",
        "todorkhoilson_ognoo": 2015,
        "bagts_tsag": 3.0,
        "hicheeliin_tuluwluguunii_helber": "Өдрийн сургалт",
        "lyektsiin_bagts_tsag": "#4 цаг - 12 хоног",
        "syeminaryn_bagts_tsag": "-",
        "laboratoriin_bagts_tsag": "-",
        "biye_daaltyn_bagts_tsag": "-",
        "dadlaga_sudalgaany_bagts_tsag": "-"
    }
# Put the output in google translate to have the translation, minor adjustments may be needed
for k in dictionary:
    print(" ".join(cyrtranslit.to_cyrillic(k, "mn").split("_")))