from yt_dlp import YoutubeDL

import ffmpeg
import pandas as pd
import numpy as np
import csv
import threading
from tqdm import tqdm
from os.path import exists


def download_audio(YTID: str, path: str) -> None:
    """
<<<<<<< HEAD
    Créez une fonction qui télécharge l'audio de la vidéo Youtube avec un identifiant donné
    et l'enregistre dans le dossier donné par `path`. Téléchargez-le en mp3. S'il y a un problème lors du téléchargement du fichier, gérez l'exception. Si il y a déjà un fichier à `path`, la fonction devrait retourner sans tenter de le télécharger à nouveau.

    ** Utilisez la librairie yt-dlp: https://github.com/yt-dlp/yt-dlp **
    (https://github.com/yt-dlp/yt-dlp#embedding-examples est particulièrement utile)
    Assurez-vous que le fichier est sauvegardé exactement à <path> (et qu'il n'y a pas de .mp3 extra ajoutés)

    Arguments :
    - YTID : Contient l'identifiant youtube, la vidéo youtube correspondante peut être trouvée sur
    'https://www.youtube.com/watch?v='+YTID
    - path : Le chemin d'accès au fichier où l'audio sera enregistré
    """
    # TODO
    pass
=======
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

    url = 'https://www.youtube.com/watch?v='+YTID
    ydl_opts = {
        'format': 'mp3',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        res = ydl.download(url)
        f = open(path, "x")
        f.write(res)
        f.close()
>>>>>>> c4aeab0 ("init yeahbadou")


def cut_audio(in_path: str, out_path: str, start: float, end: float) -> None:
    """
    Créez une fonction qui coupe l'audio de in_path pour n'inclure que le segment de start à end et l'enregistre dans out_path.

    ** Utilisez la bibliothèque ffmpeg : https://github.com/kkroening/ffmpeg-python
    Arguments :
    - in_path : Chemin du fichier audio à couper
    - out_path : Chemin du fichier pour enregistrer l'audio coupé
    - start : Indique le début de la séquence (en secondes)
    - end : Indique la fin de la séquence (en secondes)
    """
    # TODO
<<<<<<< HEAD
    pass
=======
    input = ffmpeg.input(in_path)
    input.trim(start = start, end = end)
    with open(out_path, "w") as f:
        f.write()
    pass
>>>>>>> c4aeab0 ("init yeahbadou")
