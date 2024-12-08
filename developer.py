import requests
import urllib.parse
import os

def ai():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    print("Selamat datang di chat Meta AI!")
    print("Ketik 'exit' atau 'x' untuk keluar.")
    
    while True:
        text = input("Prompt:~$ ").strip()
        try:
            if not text:  # Jika input kosong
                print("Meta AI: Hai, saya adalah Meta AI. Ada yang bisa saya bantu?")
            elif text.lower() in ["exit", "x"]:  # Exit command
                print("Meta AI: Sampai jumpa!")
                break
            else:
                params = {
                    "text": text,
                    "prompt": (
                        "kamu adalah ai buatan ZulXDev. ZulXDev punya nama asli Zulkarnaen dan berumur 14 tahun. "
                        "Pembuat awalmu adalah Meta Inc. dan model ai didukung oleh Together AI. "
                        "Jika ditanya siapa pembuatmu, jawablah ZulXDev sambil memperkenalkan siapa ZulXDev itu."
                        "Jangan terus-terusan memberikan jawaban yang sama seperti developernya siapa,jawab ketika user bertanya saja."
                    ),
                }
                url = "https://api.ryzendesu.vip/api/ai/meta-llama"
                r = requests.get(url, params=params)
                r.raise_for_status()  
                response = r.json().get("response", "Meta AI tidak memberikan respons.")
                print(f"Meta AI: {response}")
        except requests.ConnectionError:
            print("Meta AI: Tidak dapat terhubung ke server. Periksa koneksi internet Anda.")
        except requests.HTTPError as e:
            print(f"Meta AI: Terjadi kesalahan pada server: {e}")
        except KeyError:
            print("Meta AI: Respons dari server tidak sesuai.")
        except Exception as e:
            print(f"Meta AI: Terjadi kesalahan: {e}")

ai()
