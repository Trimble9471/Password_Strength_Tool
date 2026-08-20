def load_common_passwords(common_passwords.txt):
    with open(common_passwords.txt, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f)

common_passwords = load_common_passwords("common_passwords.txt")

print("Loaded", len(common_passwords), "passwords")
