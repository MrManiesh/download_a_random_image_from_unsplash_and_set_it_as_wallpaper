from requests import get
import os
import ctypes
import sys

url = "https://source.unsplash.com/random"
fileName = "random.jpg"

def is64bit():
    return sys.maxsize > 2 ** 32

def download(url, fileName):
    with open(fileName, "wb") as file:
        resp = get(url)
        file.write(resp.content)

def setup(pathtofile):
    name_of_file = pathtofile
    path_to_file = os.path.join(os.getcwd(), name_of_file)
    SPI_SETDESKWALLPAPER = 20
    if is64bit():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)


if __name__ == "__main__":
    try:
        download(url, fileName)
        setup(fileName)
    except Exception as e:
        print(f"Error {e}")
        raise NotImplementedError
