# PF2E to Daggerheart Converter

A tool for converting Pathfinder 2e adversary stats to Daggerheart equivalents, featuring a user-friendly PyQt5 GUI.

## Features

- Input PF2E stats: Level, Armor Class, Hit Points, Attack Bonus
- Get estimated PF2E stat ranges
- Select Daggerheart adversary type and receive recommended stats
- Data-driven using JSON files for stat ranges

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shavits/pf2e-to-daggerheart-converter.git
   cd pf2e-to-daggerheart-converter
   ```
2. Install dependencies:
   ```bash
   pip install PyQt5
   ```

## Usage

Run the application:
```bash
python ui_main.py
```

## Project Structure

- `ui_main.py`: Main GUI application and entry point
- `Stats/`: Conversion logic and stat modules
- `Data/`: JSON files for PF2E and Daggerheart stats

## License

MIT License
