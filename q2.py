from yt_dlp import YoutubeDL
from contextlib import redirect_stdout
import io
import ffmpeg
import pandas as pd
import numpy as np
import csv
import threading
from tqdm import tqdm
from os.path import exists
import sys, os


def download_audio(YTID: str, path: str) -> None:
    """
    Créez une fonction qui télécharge l'audio de la vidéo Youtube avec un
    identifiant donné et l'enregistre dans le dossier donné par `path`.
    Téléchargez-le en mp3. S'il y a un problème lors du téléchargement du
    fichier, gérez l'exception. Si il y a déjà un fichier à `path`, la fonction
    devrait retourner sans tenter de le télécharger à nouveau.

    ** Utilisez la librairie yt-dlp: https://github.com/yt-dlp/yt-dlp **
    (https://github.com/yt-dlp/yt-dlp#embedding-examples est particulièrement
    utile) Assurez-vous que le fichier est sauvegardé exactement à <path> (et
    qu'il n'y a pas de .mp3 extra ajoutés)

    Arguments : - YTID : Contient l'identifiant youtube, la vidéo youtube
    correspondante peut être trouvée sur 'https://www.youtube.com/watch?v='+YTID
    - path : Le chemin d'accès au fichier où l'audio sera enregistré
    """
    # TODO
    if exists(path) == True:
        return
    if path.endswith(".mp3"):
        path = path[0:-4]
    url = "https://www.youtube.com/watch?v=" + YTID
    ydl_opts = {
        "format": "mp3/bestaudio/best",
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
        "quiet": True,
        "outtmpl": path,
    }
    with YoutubeDL(ydl_opts) as ydl:
        # class HiddenPrints(): # blocking print to stdout
        try:
            ydl.download(url)
        except:
            pass


def cut_audio(in_path: str, out_path: str, start: float, end: float) -> None:
    """
    Créez une fonction qui coupe l'audio de in_path pour n'inclure que le
    segment de start à end et l'enregistre dans out_path.

    ** Utilisez la bibliothèque ffmpeg :
    https://github.com/kkroening/ffmpeg-python Arguments : - in_path : Chemin du
    fichier audio à couper - out_path : Chemin du fichier pour enregistrer
    l'audio coupé - start : Indique le début de la séquence (en secondes) - end
    : Indique la fin de la séquence (en secondes)
    """
    # TODO
    #
    if exists(in_path) == True:
        with HiddenPrints():
            ffmpeg.input(in_path, ss=start, t=end - start).output(
                out_path, loglevel="quiet"
            ).run()


class HiddenPrints:  # blocking print to stdout
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


if __name__ == "__main__":
    id = "dIjUtfSSJ6Q"
    path = "./dirtest/out"
    download_audio(id, path)
    cut_audio(path + ".mp3", "./output/out.mp3", 1, 3)
