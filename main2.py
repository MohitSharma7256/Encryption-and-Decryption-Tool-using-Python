from tkinter import *
from tkinter import messagebox
import base64

# Function to encode a message using base64
def encrypt_message():
    message = entry.get()
    encoded_message = base64.b64encode(message.encode()).decode()
    result_label.config(text="Encrypted Message: " + encoded_message)

# Function to decode an encoded message
def decrypt_message():
    encoded_message = entry.get()
    try:
        decoded_message = base64.b64decode(encoded_message).decode()
        result_label.config(text="Decrypted Message: " + decoded_message)
    except Exception as e:
        result_label.config(text="Error: Invalid encoded message")

# Create the main screen
def main_screen():
    screen = Tk()
    screen.geometry("500x500")  # Fixed the geometry format
    screen.title("Vision Endec")

    global entry
    entry = Entry(screen, width=40)
    entry.pack(pady=20)

    encrypt_button = Button(screen, text="Encrypt", command=encrypt_message)
    encrypt_button.pack()

    decrypt_button = Button(screen, text="Decrypt", command=decrypt_message)
    decrypt_button.pack()

    global result_label
    result_label = Label(screen, text="", wraplength=400)
    result_label.pack()

    screen.mainloop()

main_screen()
