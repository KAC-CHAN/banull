import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "26788480"))
    API_HASH = os.getenv("API_HASH", "858d65155253af8632221240c535c314")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7222795881:AAGvVnHfh2qOcKkPQ18LpS6YAkAT5EbX_WE")
    sudo = os.getenv("SUDO")
    SUDO = [6988231213]
    if sudo:
        SUDO = make_int(sudo)
