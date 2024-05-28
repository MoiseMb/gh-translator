from transformers import  MarianMTModel, AutoTokenizer

class Adapter:
   
    def translateFrenchToEnglish(sentence):
        try:
            model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
            tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")

            batch = tokenizer([sentence], return_tensors="pt")
            generated_ids = model.generate(**batch, max_new_tokens=50)
            translation = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            print(f"\nvoici la traduction: {translation}\n")
        except Exception as e:
            print(f"Erreur lors de la traduction : {e}")

   
    def translateEnglishToFrench(sentence):
        try:
            model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
            tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")

            batch = tokenizer([sentence], return_tensors="pt")
            generated_ids = model.generate(**batch, max_new_tokens=50)
            translation = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            print(f"\nHere is the translation: {translation}\n")
        except Exception as e:
            print(f"Error during translation: {e}")


    


