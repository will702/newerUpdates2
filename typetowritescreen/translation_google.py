from google_trans_new import google_translator
def translating(isi):
    try:
        translator = google_translator()
        translate_text = translator.translate(isi, lang_src='id',
                                              lang_tgt='en')
        return translate_text
    except:
        pass