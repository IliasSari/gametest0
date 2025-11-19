import random

def play_game():
    """Παίζει μια παρτίδα Πέτρα, Ψαλίδι, Χαρτί."""
    
    # 1. Ορίζουμε τις διαθέσιμες επιλογές
    choices = ["πετρα", "ψαλιδι", "χαρτι"]
    
    # 2. Ζητάμε την επιλογή του χρήστη
    print("Παρακαλώ διάλεξε: πετρα, ψαλιδι, ή χαρτι;")
    user_choice = input("> ").lower()
    
    # Ελέγχουμε την εγκυρότητα της εισόδου του χρήστη
    while user_choice not in choices:
        print("Μη έγκυρη επιλογή. Διάλεξε ξανά: πετρα, ψαλιδι, ή χαρτι.")
        user_choice = input("> ").lower()
        
    # 3. Ο υπολογιστής διαλέγει τυχαία
    computer_choice = random.choice(choices)
    
    print(f"\nΗ επιλογή σου: **{user_choice.capitalize()}**")
    print(f"Η επιλογή του υπολογιστή: **{computer_choice.capitalize()}**\n")
    
    # 4. Ελέγχουμε τον νικητή
    
    # Περίπτωση Ι: Ισοπαλία
    if user_choice == computer_choice:
        print("🤝 Ισοπαλία!")
        
    # Περίπτωση ΙΙ: Ο χρήστης κερδίζει (3 πιθανές νίκες)
    elif (user_choice == "πετρα" and computer_choice == "ψαλιδι") or \
         (user_choice == "ψαλιδι" and computer_choice == "χαρτι") or \
         (user_choice == "χαρτι" and computer_choice == "πετρα"):
        print("🎉 Συγχαρητήρια! **Κέρδισες!**")
        
    # Περίπτωση ΙΙΙ: Ο υπολογιστής κερδίζει (Όλες οι άλλες περιπτώσεις)
    else:
        print("😞 Δυστυχώς **έχασε** ο παίκτης.")

# Εκκίνηση του παιχνιδιού
if __name__ == "__main__":
    while True:
        play_game()
        
        # Ρωτάμε αν θέλει να ξαναπαίξει
        play_again = input("\nΘέλεις να ξαναπαίξεις; (ναι/οχι): ").lower()
        if play_again != 'ναι':
            print("Ευχαριστούμε που έπαιξες! Αντίο!")
            break