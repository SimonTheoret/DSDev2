import re
import os
import pandas as pd
from tqdm import tqdm
from q2 import download_audio, cut_audio
from typing import List


def filter_df(csv_path: str, label: str) -> pd.DataFrame:
    """
    Écrivez une fonction qui prend le path vers le csv traité (dans la partie
    notebook de q1) et renvoie un df avec seulement les rangées qui contiennent
    l'étiquette `label`.

    Par exemple: get_ids("audio_segments_clean.csv", "Speech") ne doit renvoyer
    que les lignes où l'un des libellés est "Speech"
    """
    # TODO
    df = pd.read_csv(csv_path)
    index = df["label_names"].map(lambda x: label in x.split("|"))
    return df[index]


def data_pipeline(csv_path: str, label: str) -> None:
    """
    En utilisant vos fonctions précédemment créées, écrivez une fonction qui
    prend un csv traité et pour chaque vidéo avec l'étiquette donnée: 1. Le
    télécharge à <label>_raw/<ID>.mp3 2. Le coupe au segment approprié 3.
    L'enregistre dans <label>_cut/<ID>.mp3 (n'oubliez pas de créer le dossier
    audio/ et le dossier label associé !).

    Il est recommandé d'itérer sur les rangées de filter_df().  Utilisez tqdm
    pour suivre la progression du processus de téléchargement
    (https://tqdm.github.io/)

    Malheureusement, il est possible que certaines vidéos ne peuvent pas être
    téléchargées. Dans de tels cas, votre pipeline doit gérer l'échec en passant
    à la vidéo suivante avec l'étiquette.
    """

    # TODO
    def go(serie: pd.Series) -> None:
        serie = serie.T
        YTID = serie["# YTID"]
        download_audio(serie["# YTID"], f"./{label}_raw/{ YTID }")
        start = serie[" start_seconds"]
        end = serie[" end_seconds"]
        in_path = f"./{label}_raw/{YTID}.mp3"
        out_path = f"./{label}_cut/{YTID}.mp3"
        out_dir = f"./{label}_cut/"
        try:
            os.mkdir(out_dir)
        except:
            pass
        cut_audio(in_path, out_path, start, end)
    tqdm.pandas(desc = "Advancement")
    filter_df(csv_path, label).progress_apply(go, axis =1)

def rename_files(path_cut: str, csv_path: str) -> None:
    """
    Supposons que nous voulons maintenant renommer les fichiers que nous avons
    téléchargés dans `path_cut` pour inclure les heures de début et de fin ainsi
    que la longueur du segment. Alors que cela aurait pu être fait dans la
    fonction data_pipeline(), supposons que nous avons oublié et que nous ne
    voulons pas tout télécharger à nouveau.

    Écrivez une fonction qui, en utilisant regex (c'est-à-dire la bibliothèque
    `re`), renomme les fichiers existants de "<ID>.mp3" ->
    "<ID>_<start_seconds_int>_<end_seconds_int>_<length_int>.mp3" dans path_cut.
    csv_path est le chemin vers le csv traité à partir de q1. `path_cut` est un
    chemin vers le dossier avec l'audio coupé.

    Par exemple "--BfvyPmVMo.mp3" -> "--BfvyPmVMo_20_30_10.mp3"

    ## ATTENTION : supposez que l'YTID peut contenir des caractères spéciaux
    ## tels que '.' ou même '.mp3' ##
    """
    # TODO
    df = pd.read_csv(csv_path)
    df = df.set_index('# YTID')
    print(df.head())
    regex = r'^(.*?)\.([^\.]+)$'
    for file in os.listdir(path_cut):
        splitted = re.split(regex, file)
        id, ext = [val for val in splitted if val]
        print(id, ext)
        rows = df.loc[id]
        start = int(rows[' start_seconds'])
        end = int( rows[' end_seconds'] )
        duration = int(end-start)
        e = "_"
        new_file = id + e + str(start) + e + str( end ) +e + str( duration ) + ".mp3"
        actual_path = os.path.join(path_cut, file)
        print(actual_path)
        new_file_path = os.path.join(path_cut, new_file)
        print(new_file_path)
        os.rename(actual_path, new_file_path)

if __name__ == "__main__":
    print(filter_df("test.csv", "Laughter"))
    data_pipeline("test.csv", "Laughter")
    rename_files("Laughter_cut", "test.csv")
