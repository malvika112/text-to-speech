# Text-to-Speech (TTS) Project

This project provides a simple Python application to convert text content from a file into speech using the `outetts` library. The application reads the content of a file, initializes the TTS system, and generates speech from the text.

## Features

- **File Reading**: The program reads the text content from a specified file.
- **Speech Generation**: The text is converted into speech using a TTS model.
- **Custom Speaker**: The speech is generated using a specified speaker, defaulting to a male voice (`male_1`).
- **Audio Output**: The generated speech is saved as a `.wav` file and played aloud.

## Requirements

- Python 3.x
- `outetts` library (version 0.2 or higher)
- A TTS model (`OuteTTS-0.2-500M`)

## Installation

1. Install Python 3.x if you don't have it already.
2. Install the required dependencies using `pip`:

```bash
pip install outetts
```

3. Ensure you have the correct TTS model (`OuteTTS-0.2-500M`) available in the `OuteAI` directory.

## How to Use

1. Clone or download this repository to your local machine.
2. Ensure the `outetts` library and TTS model are correctly set up.
3. Run the script:

```bash
python tts_script.py
```

4. The program will prompt you to enter the file path of the text file you want to read aloud.

5. After entering the file path, the application will:
   - Read the content from the specified file.
   - Convert the text into speech.
   - Save the generated speech as `response.wav`.
   - Play the generated speech aloud.

## Example

If the content of your file (`example.txt`) is:

```
Hello! This is an example of text-to-speech conversion.
```

Upon running the program, it will read the file aloud and play the speech.

## Code Explanation

- **initialize_tts_system()**: Initializes the TTS system with a model configuration.
- **read_file(file_path)**: Reads the content from the specified file.
- **generate_speech(interface, text, speaker_name)**: Generates speech from the text and plays it aloud.
- **main()**: Main function that ties everything together.

## Troubleshooting

- **FileNotFoundError**: Ensure the file path you entered is correct and the file exists.
- **Model Initialization Issues**: Make sure the TTS model (`OuteTTS-0.2-500M`) is correctly placed in the `OuteAI` directory.
