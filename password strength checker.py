import re


class PasswordChecker:
    def check_strength(self, password):
        score = 0

        # Length check
        if len(password) >= 8:
            score += 1

        # Uppercase check
        if re.search(r"[A-Z]", password):
            score += 1

        # Lowercase check
        if re.search(r"[a-z]", password):
            score += 1

        # Digit check
        if re.search(r"[0-9]", password):
            score += 1

        # Special character check
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1

        # Strength result
        if score <= 2:
            return "Weak"
        elif score == 3 or score == 4:
            return "Medium"
        else:
            return "Strong"

    def run(self):
        print("\n--- Password Strength Checker ---")

        while True:
            password = input("\nEnter password (or type 'exit' to quit): ")

            if password.lower() == "exit":
                print("Program closed.")
                break

            strength = self.check_strength(password)
            print(f"Password Strength: {strength}")


if __name__ == "__main__":
    app = PasswordChecker()
    app.run()
    