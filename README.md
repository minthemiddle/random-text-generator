# Dummy Text Generator

This project provides a Python script that generates dummy text data for various purposes, such as testing or placeholder content. It uses the Faker library to create realistic-looking text with customizable length and structure.

## Features

- Generates company descriptions, contact sections, image titles, video titles, and document titles
- Supports both randomized and maximized length text generation
- Outputs results in JSON format

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/dummy-text-generator.git
   cd dummy-text-generator
   ```

3. Install the required dependencies:
   ```
   pip install faker
   ```

## Usage

Run the script using Python:

```
python main.py
```

This will generate two sets of dummy text data:
1. Randomized Length: Text with varying lengths within the specified limits
2. Maximized Length: Text that attempts to reach the maximum allowed length for each field

The output will be displayed in JSON format in the console.

## Customization

You can modify the `main.py` file to adjust the text generation parameters, such as the maximum length for different fields or the number of items in each category.

## License

This project is open-source and available under the MIT License.
