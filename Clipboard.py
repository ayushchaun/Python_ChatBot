import pyautogui
import pyperclip
import time
from openai import OpenAI

def is_last_message_from_sender(chat_log, sender_name="Sis"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]

    if sender_name in messages:
        return True
    return False

pyautogui.click(1230,1041)
time.sleep(1)
while True:

    pyautogui.moveTo(1677,293)
    pyautogui.dragTo(1844,889,duration=1.0,button='left')

    pyautogui.hotkey('ctrl','c')
    pyautogui.click(904,854)
    time.sleep(1)

    text = pyperclip.paste()

    print(text)

    if is_last_message_from_sender(text):

        reply = "HAR HAR MAHADEV"

        pyperclip.copy(reply)

        pyautogui.click(1108,957)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pyautogui.press('enter')