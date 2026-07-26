# Eksperimen_SML_Ahmad-Raihan

Eksperimen deteksi berita hoax berbahasa Indonesia — dataset IDNHoaxCorpus.


## Cara Menjalankan
```bash
pip install -r requirements.txt
```

**Opsi A — otomatis:**
```bash
cd preprocessing
python automate.py
```

**Opsi B — via notebook (dengan MLflow tracking ke DagsHub):**
1. Buat repo baru di https://dagshub.com (kalau belum ada)
2. Buka `preprocessing/Eksperimen.ipynb`
3. Ganti `DAGSHUB_USERNAME` dan `DAGSHUB_REPO` di cell konfigurasi MLflow
4. Generate token di DagsHub (Settings → Tokens), isi ke `MLFLOW_TRACKING_PASSWORD`
5. Jalankan seluruh cell
6. Cek dashboard DagsHub → tab **Experiments** untuk melihat run yang tercatat

## Sumber Dataset
[9uz/IDNHoaxCorpus](https://github.com/9uz/IDNHoaxCorpus) (MIT License)
