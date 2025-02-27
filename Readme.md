# Character Guessing Game

This is a Python-based character guessing game where the user answers Yes/No questions, and the program tries to determine the character they are thinking of based on predefined attributes. This is inspired by Akinator.

## Features
- Interactive question-answer format
- Input validation to ensure correct responses
- Efficient filtering to narrow down possible characters
- Handles cases where no match is found
- Displays possible matches if multiple characters fit the criteria

## Installation
### Prerequisites
- Python 3.x

### Steps
1. Clone this repository:
   ```sh
   https://github.com/vharishcse/Character_Guessing_Game.git
   cd Character_Guessing_Game
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

## Usage
Run the script using:
```sh
python Hackinator.py
```
Answer the Yes/No questions, and the program will try to guess the character you are thinking of!

## Requirements
- Python 3.x

## Connect
- [LinkedIn](https://www.linkedin.com/in/harish-yadav-b2bb52241)

## Contributing
Feel free to fork the repository and submit pull requests if you have improvements or new features to add!

## License
This project is licensed under the MIT License.

---

### Character Database Table
| Character          | Human | Male | Famous | Indian | Movie | Cricketer | Scientist | Politics |
|--------------------|-------|------|--------|--------|-------|-----------|-----------|----------|
| Virat Kohli       | Yes   | Yes  | Yes    | Yes    | No    | Yes       | No        | No       |
| AB De Villiers    | Yes   | Yes  | Yes    | No     | No    | Yes       | No        | No       |
| Smriti Mandhana   | Yes   | No   | Yes    | Yes    | No    | Yes       | No        | No       |
| Ellyse Perry      | Yes   | No   | Yes    | No     | No    | Yes       | No        | No       |
| Narendra Modi     | Yes   | Yes  | Yes    | Yes    | No    | No        | No        | Yes      |
| Droupadi Murmu    | Yes   | No   | Yes    | Yes    | No    | No        | No        | Yes      |
| Donald Trump      | Yes   | Yes  | Yes    | No     | No    | No        | No        | Yes      |
| Jacinda Ardern    | Yes   | No   | Yes    | No     | No    | No        | No        | Yes      |
| Yash             | Yes   | Yes  | Yes    | Yes    | Yes   | No        | No        | No       |
| Sridevi          | Yes   | No   | Yes    | Yes    | Yes   | No        | No        | No       |
| Johnny Depp      | Yes   | Yes  | Yes    | No     | Yes   | No        | No        | No       |
| Angelina Jolie   | Yes   | No   | Yes    | No     | Yes   | No        | No        | No       |
| Sir C V Raman    | Yes   | Yes  | Yes    | Yes    | No    | No        | Yes       | No       |
| B Vijayalakshmi  | Yes   | No   | Yes    | Yes    | No    | No        | Yes       | No       |
| Nikola Tesla     | Yes   | Yes  | Yes    | No     | No    | No        | Yes       | No       |
| Marie Curie      | Yes   | No   | Yes    | No     | No    | No        | Yes       | No       |

---

### Example Gameplay
```
Is your character a human (y/n)? y
Is your character male (y/n)? y
Is your character famous (y/n)? y
Is your character an Indian (y/n)? y
Is your character a cricketer (y/n)? y
Your character is Virat Kohli!
```
