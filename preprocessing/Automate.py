"""
automate_Ahmad-Raihan.py
[Kriteria Skilled - opsional] Otomatisasi preprocessing dataset.

Mengunduh dataset asli IDNHoaxCorpus, membersihkannya (drop label ambigu '?',
drop teks kosong, mapping label ke biner), lalu menyimpan hasilnya ke
preprocessing/namadataset_preprocessing/hoax_preprocessing.csv.

Jalankan: python automate_Ahmad-Raihan.py
"""

import os
import pandas as pd
import urllib.request

RAW_URL = "https://raw.githubusercontent.com/9uz/IDNHoaxCorpus/main/dataset/datasetUMPOHoax.csv"
RAW_DEST = "namadataset_raw/hoax_raw.csv"
OUT_DEST = "preprocessing/namadataset_preprocessing/hoax_preprocessing.csv"


def download_raw(url: str = RAW_URL, dest: str = RAW_DEST) -> str:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    urllib.request.urlretrieve(url, dest)
    print(f"Dataset mentah diunduh -> {dest}")
    return dest


def preprocess(raw_path: str = RAW_DEST, out_path: str = OUT_DEST) -> pd.DataFrame:
    df = pd.read_csv(raw_path)

    # Buang baris tanpa teks, dan label ambigu "?"
    df = df.dropna(subset=["tweet"])
    df = df[df["label"].isin(["hoax", "valid"])].copy()

    df["text"] = df["tweet"]
    df["label"] = (df["label"] == "hoax").astype(int)  # 1 = hoax, 0 = valid

    df = df[["text", "label"]].drop_duplicates(subset=["text"]).reset_index(drop=True)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Preprocessing selesai: {len(df)} baris -> {out_path}")
    print(df["label"].value_counts().rename({1: "hoax", 0: "valid"}))
    return df


if __name__ == "__main__":
    download_raw()
    preprocess()
