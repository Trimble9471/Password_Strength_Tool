# Password Checker

A Python tool that evaluates password strength and provides recommendations for improvement.

## Features

- **Password Strength Scoring**: Rates passwords on a 5-point scale
- **Common Password Detection**: Identifies weak, commonly-used passwords
- **Security Recommendations**: Provides specific suggestions to strengthen weak passwords
- **Interactive Loop**: Keeps prompting until a strong password is entered
- **Visual Feedback**: Uses Unicode emojis to display password strength status

## How It Works

The tool evaluates passwords based on 5 security criteria:

1. **Length**: Password must be at least 8 characters long
2. **Uppercase Letters**: Must contain at least 1 uppercase letter (A-Z)
3. **Lowercase Letters**: Must contain at least 1 lowercase letter (a-z)
4. **Numbers**: Must contain at least 1 digit (0-9)
5. **Special Characters**: Must contain at least 1 special character (`!@#$%^&*(),./":{}|<>`)

### Strength Ratings

- **Weak** (❌): 0-2 points - Does not meet most criteria
- **Medium** (⚠️): 3-4 points - Meets most criteria
- **Strong** (✅): 5 points - Meets all criteria

## Installation

No external dependencies required. Simply ensure you have Python 3 installed.

```bash
python3 --version
```

## Usage

Run the script from the command line:

```bash
python3 Password_Checker.py
```

You will be prompted to enter a password. The tool will evaluate it and display:
- The strength rating
- Your score (e.g., "score: 3/5")
- Recommendations for improvement (if applicable)

The script will continue prompting you until you enter a strong password.

### Example

```
Enter a password to check: password
Password strength: ❌ Weak Password - Common Password!!
Try again.

Enter a password to check: Pass123
Password strength: ⚠️ Medium Password (score: 4/5)
Recommendations:
 - Use atleast 1 special character.
Try again.

Enter a password to check: Pass123!@#
Password strength: ✅ Strong Password (score: 5/5)
🎉 Congratulations! Your password is strong!!
```

## Common Weak Passwords

The tool flags the following as weak passwords:
- `password`
- `123456`
- `password123`
- `qwerty`
- `123password`

## Tips for Strong Passwords

✓ Use at least 8 characters (longer is better)  
✓ Mix uppercase and lowercase letters  
✓ Include numbers  
✓ Add special characters  
✓ Avoid common words and simple patterns  
✓ Don't reuse passwords across multiple accounts  

## Requirements

- Python 3.x

