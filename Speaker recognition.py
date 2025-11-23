import sounddevice as sd
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
import time

# --- Configuration ---
ENROLLMENT_FILE = "my_voiceprint.npy"
RECORD_DURATION = 5  # Duration of recording in seconds
SAMPLE_RATE = 16000  # Sample rate for recording

# --- Initialize Voice Encoder ---
try:
    encoder = VoiceEncoder()
    print("VoiceEncoder initialized.")
except Exception as e:
    print(f"Failed to initialize VoiceEncoder: {e}")
    print("This may be due to a download failure. Please check your internet connection.")
    exit()

def record_audio(duration, fs):
    """Records audio from the microphone."""
    print(f"Recording for {duration} seconds... Speak continuously.")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait for recording to complete
    print("Recording complete.")
    return recording.flatten() # Return as a 1D array

def get_embedding(audio_data, fs):
    """Processes audio data and returns a voice embedding."""
    processed_wav = preprocess_wav(audio_data, fs)
    
    # Get the embedding
    embedding = encoder.embed_utterance(processed_wav)
    return embedding

def enroll_user():
    """Records and saves a user's voiceprint."""
    print("\n--- Voice Enrollment ---")
    speak("Please speak clearly to enroll your voice. Start talking when I say 'go'.")
    time.sleep(1)
    
    # Give a countdown
    speak("Ready?")
    speak("3...")
    time.sleep(1)
    speak("2...")
    time.sleep(1)
    speak("1...")
    time.sleep(1)
    speak("Go!")

    audio_data = record_audio(RECORD_DURATION, SAMPLE_RATE)
    
    speak("Processing your voiceprint...")
    embedding = get_embedding(audio_data, SAMPLE_RATE)
    
    # Save the embedding
    np.save(ENROLLMENT_FILE, embedding)
    speak(f"Enrollment complete. Your voiceprint has been saved to {ENROLLMENT_FILE}.")

def verify_user():
    """Records a new sample and verifies it against the saved voiceprint."""
    print("\n--- Voice Verification ---")
    
    enrollment_path = Path(ENROLLMENT_FILE)
    if not enrollment_path.is_file():
        speak("No voiceprint found. Please enroll first.")
        return

    enrolled_embedding = np.load(ENROLLMENT_FILE)
    
    speak("Please speak to verify your identity. Start talking when I say 'go'.")
    
    # Give a countdown
    speak("Ready?")
    speak("3...")
    # --- THIS IS THE FIX ---
    time.sleep(1) 
    # -----------------------
    speak("2...")
    time.sleep(1)
    speak("1...")
    time.sleep(1)
    speak("Go!")

    audio_data = record_audio(RECORD_DURATION, SAMPLE_RATE)
    
    speak("Verifying...")
    
    verification_embedding = get_embedding(audio_data, SAMPLE_RATE)
    
    # Calculate Similarity
    similarity = np.dot(enrolled_embedding, verification_embedding)
    
    print(f"--- Similarity Score: {similarity:.2f} ---")
    
    threshold = 0.60  # You may need to adjust this
    
    if similarity > threshold:
        speak(f"Welcome. Your identity is verified with {similarity:.2f} similarity.")
    else:
        speak(f"Verification failed. Your voice similarity was only {similarity:.2f}.")

# --- Helper 'speak' function (simulation) ---
def speak(text):
    print(f"ASSISTANT: {text}")

# --- Main Program Loop ---
if __name__ == "__main__":
    while True:
        print("\n" + "="*30)
        choice = input("Choose an option:\n1. Enroll new user\n2. Verify user\n3. Exit\nEnter 1, 2, or 3: ")
        
        if choice == '1':
            enroll_user()
        elif choice == '2':
            verify_user()
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")