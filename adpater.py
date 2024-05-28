from transformers import pipeline

class adapter :
    def translateFrenchToEnglish(sentence):
      translateToEnglish = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
      return translateToEnglish(sentence).translation_text

    def toFrench(sentence):
      translateToFrench = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
      return translateToFrench(sentence).translation_text