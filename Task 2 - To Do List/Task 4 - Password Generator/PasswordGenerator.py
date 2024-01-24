import random
import string

class PasswordGenerator:

    def generate_password(self, complexity):
        simple = string.ascii_letters + string.digits
        moderate = simple + string.punctuation
        complex_chars = moderate + string.ascii_letters

        if complexity == 1:
            return "".join(random.choice(simple) for _ in range(4))
        elif complexity == 2:
            return "".join(random.choice(moderate) for _ in range(6))
        elif complexity == 3:
            return "".join(random.choice(complex_chars) for _ in range(8))


password_generator = PasswordGenerator()
        
complexity_choice = int(input('Enter Password Level\n1. Simple Level Password\n2. Moderate Level Password\n3. Complex Level Password\n# Your Choice - '))
        
generated_password = password_generator.generate_password(complexity_choice)
        
print("Generated Password:", generated_password)
