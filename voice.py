import outetts

# Function to initialize the TTS system
def initialize_tts_system():
    model_config = outetts.HFModelConfig_v1(
        model_path="OuteAI/OuteTTS-0.2-500M",
        language="en",
    )
    interface = outetts.InterfaceHF(model_version="0.2", cfg=model_config)
    return interface

# Function to read content from a file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Function to generate and play speech
def generate_speech(interface, text, speaker_name="male_1"):
    speaker = interface.load_default_speaker(name=speaker_name)
    output = interface.generate(
        text=text,
        temperature=0.1,
        repetition_penalty=1.1,
        max_length=4096,
        speaker=speaker,
    )
    output.save("response.wav")
    output.play()

# Main function
def main():
    # Ask user for the file path
    file_path = input("Enter the path to the text file you want to read: ")

    # Read content from the file
    content = read_file(file_path)
    
    if content:
        print(f"Reading content from {file_path} aloud...")
        
        # Initialize TTS system
        interface = initialize_tts_system()
        
        # Generate speech for the file content
        generate_speech(interface, content)

if __name__ == "__main__":
    main()
