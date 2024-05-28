from Adapter import Adapter

def main(): 
    print("\n")
    print("+---------------------------------------------------------------------+")
    print("|                            sen Translator                           |")
    print("+---------------------------------------------------------------------+")
    print("|                  1 ->       Français -----> Anglais                 |")
    print("|                  2 ->       Anglais  -----> Français                |")
    print("|                  3 ->       Quitter                                 |")
    print("+---------------------------------------------------------------------+")

    while True:
        try:
            choice = int(input("\nVeuillez choisir une option : "))
            if choice == 1:
                sentence = input("Veuillez entrer une phrase en français : ")
                Adapter.translateFrenchToEnglish(sentence)
            elif choice == 2:
                sentence = input("Veuillez entrer une phrase en anglais : ")
                Adapter.translateEnglishToFrench(sentence)
            elif choice == 3:
                print("\nMerci d'avoir utilisé le traducteur. Au revoir!")
                print("\nBYEE !!")
                break
            else:
                print("Veuillez choisir une option valide (1, 2, ou 3).")
        except ValueError:
            print("Erreur lors de la saisie. Veuillez entrer un nombre (1, 2, ou 3).")

if __name__ == "__main__":
    main()
