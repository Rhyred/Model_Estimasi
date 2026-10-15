<div align="center">

# Implementasi Regresi Linear untuk Estimasi Gaji Berdasarkan Pengalaman Kerja

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Data Mining](https://img.shields.io/badge/Data-Mining-red.svg?style=for-the-badge&logo=lightningreplace)

</div>

## 📑 Table of Contents

- [📋 Describe](#-deskripsi-proyek)
- [✨ Main](#-tujuan-pembelajaran)
- [🛠️ Tech to stack](#-teknologi-dan-library)
- [📁 Struktur Project](#-struktur-proyek)
- [🔍 Alur Kerja](#-alur-kerja-program)
- [📊 Dataset](#-dataset)
- [💡 Kesimpulan](#-kesimpulan)
- [👤 Author](#-author)

## Deskripsi Proyek

Proyek ini mendemonstrasikan penggunaan algoritma **Regresi Linear** (*Linear Regression*) untuk memperkirakan gaji berdasarkan pengalaman kerja dalam tahun. Program membangun model dari dataset dummy yang didefinisikan langsung di dalam kode, kemudian menggunakan model tersebut untuk mengestimasi gaji seseorang dengan pengalaman kerja baru.

Regresi Linear mencari hubungan linear antara pengalaman kerja sebagai variabel masukan dan gaji sebagai variabel keluaran. Hubungan tersebut kemudian digunakan untuk menghasilkan estimasi gaji.

## Tujuan Pembelajaran

Program ini mendemonstrasikan:

- pengolahan data menggunakan Pandas;
- pemisahan data latih dan data uji menggunakan `train_test_split`;
- pelatihan model menggunakan `LinearRegression`;
- pengambilan konstanta dan koefisien model; dan
- prediksi gaji menggunakan data pengalaman kerja baru.
- Pelengkap Tugas 1 IFB-307 Data Mining PEMBUATAN MODEL ESTIMASI

## Teknologi dan Library

Program menggunakan Python dengan library berikut:

| Library          | Fungsi dalam program                                                                                            |
| ---------------- | --------------------------------------------------------------------------------------------------------------- |
| `pandas`       | Membuat dan mengelola `DataFrame` dari dataset dummy.                                                         |
| `scikit-learn` | Menyediakan `train_test_split` untuk membagi data serta `LinearRegression` untuk membuat dan melatih model. |
| `numpy`        | Membuat array dua dimensi yang berisi nilai pengalaman kerja baru untuk prediksi.                               |

Instalasi library:

```powershell
python -m pip install pandas scikit-learn numpy
```

## Struktur Proyek

```text
Tugas1/
├── main.py
└── README.md
```

## Dataset

Dataset dibuat langsung di dalam `main.py` melalui dictionary `data`, sehingga program tidak membaca dataset dari file eksternal. Dataset memiliki dua variabel:

- `Pengalaman`: pengalaman kerja dalam tahun.
- `Gaji`: gaji dalam Rupiah.

Dataset berisi 10 observasi, dengan pengalaman kerja dari 1 hingga 10 tahun.

| No. | Pengalaman (tahun) | Gaji (Rupiah) |
| --: | -----------------: | ------------: |
|   1 |                  1 |     4.000.000 |
|   2 |                  2 |     4.500.000 |
|   3 |                  3 |     5.200.000 |
|   4 |                  4 |     6.000.000 |
|   5 |                  5 |     7.100.000 |
|   6 |                  6 |     7.500.000 |
|   7 |                  7 |     8.300.000 |
|   8 |                  8 |     9.000.000 |
|   9 |                  9 |    10.500.000 |
|  10 |                 10 |    11.000.000 |

Data tersebut merupakan **data dummy**, bukan data hasil survei dan bukan dataset eksternal.

## Alur Kerja Program

Program berjalan melalui tahapan berikut.

### 1. Mengimpor library

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
```

### 2. Membuat `DataFrame`

Dictionary `data` diubah menjadi `DataFrame` bernama `df`:

```python
df = pd.DataFrame(data)
```

### 3. Menentukan variabel

Kolom `Pengalaman` digunakan sebagai variabel independen (`X`), sedangkan kolom `Gaji` digunakan sebagai variabel dependen (`y`):

```python
X = df[['Pengalaman']]
y = df['Gaji']
```

`X` ditulis dengan dua tanda kurung siku agar berbentuk array dua dimensi, sesuai kebutuhan model scikit-learn.

### 4. Membagi data latih dan data uji

Dataset dibagi menggunakan `test_size=0.2` dan `random_state=42`:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

Sebanyak 20% data digunakan sebagai data uji, sedangkan sisanya digunakan sebagai data latih. `random_state=42` membuat pembagian data dapat direproduksi.

### 5. Membuat dan melatih model

Model dibuat menggunakan `LinearRegression`, kemudian dilatih menggunakan data latih:

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

### 6. Menampilkan konstanta dan koefisien

Program mengambil konstanta dari `model.intercept_` dan koefisien pengalaman kerja dari `model.coef_[0]`:

```python
konstanta = model.intercept_
koefisien = model.coef_[0]
print(f"Persamaan Model Estimasi: Y = {konstanta:.2f} + {koefisien:.2f}X")
```

### 7. Melakukan prediksi

Nilai pengalaman kerja baru ditetapkan sebesar 4,5 tahun. Nilai tersebut dibuat sebagai array NumPy dua dimensi dan diberikan kepada model:

```python
pengalaman_baru = np.array([[4.5]])
prediksi_gaji = model.predict(pengalaman_baru)
```

Hasil prediksi kemudian ditampilkan dalam Rupiah.

## Konsep Regresi Linear

Persamaan umum Regresi Linear adalah:

```text
Y = a + bX
```

Keterangan:

- `Y`: estimasi gaji.
- `X`: pengalaman kerja.
- `a`: konstanta atau *intercept*, yaitu nilai dasar pada persamaan model.
- `b`: koefisien regresi, yaitu perubahan estimasi gaji untuk setiap kenaikan satu tahun pengalaman kerja.

Dalam program:

- `a` direpresentasikan oleh `model.intercept_` dan disimpan dalam variabel `konstanta`.
- `b` direpresentasikan oleh `model.coef_[0]` dan disimpan dalam variabel `koefisien`.

Dengan demikian, model menghasilkan estimasi gaji menggunakan bentuk `konstanta + koefisien * pengalaman`.

## Cara Instalasi dan Menjalankan Program

Buka terminal VS Code atau PowerShell pada direktori proyek, kemudian jalankan:

```powershell
python -m pip install pandas scikit-learn numpy
python .\main.py
```

Perintah pertama memasang library yang dibutuhkan. Perintah kedua menjalankan file `main.py`.

## Output Program

Program menghasilkan dua keluaran utama:

1. persamaan model estimasi; dan
2. estimasi gaji untuk pengalaman kerja 4,5 tahun.

Dengan pembagian data yang ditentukan oleh `test_size=0.2` dan `random_state=42`, output dari dataset pada program adalah:

```text
Persamaan Model Estimasi: Y = 3028448.28 + 769827.59X
Estimasi gaji untuk pengalaman 4.5 tahun: Rp 6,492,672.41
```

Format angka pada output mengikuti format string di `main.py`: konstanta, koefisien, dan prediksi ditampilkan dengan dua angka di belakang koma, sedangkan prediksi juga menggunakan pemisah ribuan.

## Analisis dan Interpretasi

Konstanta menunjukkan nilai dasar yang dihasilkan persamaan ketika `X` bernilai nol. Koefisien menunjukkan arah dan besarnya perubahan estimasi gaji untuk setiap tambahan satu tahun pengalaman kerja. Pada program ini, koefisien bernilai positif, sehingga persamaan menghasilkan estimasi gaji yang meningkat ketika pengalaman kerja bertambah.

Untuk pengalaman kerja 4,5 tahun, model memasukkan nilai tersebut ke dalam persamaan:

```text
Y = konstanta + (koefisien × 4,5)
```

Hasilnya adalah estimasi berdasarkan pola pada dataset dummy. Nilai tersebut bukan jaminan gaji aktual seseorang. Program juga belum menghitung metrik evaluasi, sehingga dokumentasi ini tidak menyatakan tingkat akurasi atau performa tertentu.

## Keterbatasan Program

- Dataset hanya terdiri dari 10 data dummy.
- Model hanya menggunakan satu variabel independen, yaitu pengalaman kerja.
- Belum ada pengukuran performa menggunakan MAE, MSE, RMSE, atau R².
- Data belum dibaca dari file CSV eksternal.
- Hasil estimasi tidak otomatis menggambarkan kondisi gaji di dunia nyata.

## Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dipertimbangkan adalah:

- menggunakan dataset gaji yang nyata dan lebih besar;
- menambahkan visualisasi data dan garis regresi;
- menghitung metrik evaluasi seperti MAE, MSE, RMSE, dan R²;
- menguji model dengan beberapa nilai pengalaman kerja; dan
- membaca data dari file CSV eksternal.

Semua poin tersebut merupakan saran pengembangan dan belum menjadi fitur yang diterapkan dalam program saat ini.

## Kesimpulan

Program ini menunjukkan alur dasar penerapan Regresi Linear untuk mengestimasi gaji berdasarkan pengalaman kerja. Data dummy diubah menjadi `DataFrame`, dibagi menjadi data latih dan data uji, lalu digunakan untuk melatih `LinearRegression`. Konstanta dan koefisien model membentuk persamaan estimasi, yang kemudian digunakan untuk memprediksi gaji berdasarkan pengalaman kerja baru sebesar 4,5 tahun. Karena menggunakan data dummy dan belum memiliki evaluasi performa, hasilnya perlu dipahami sebagai contoh pembelajaran, bukan sebagai prediksi gaji aktual.

## 👤 Author

<div align="center">

### 🎓 Student Information

**Robi Rizki Permana**
 NIM: `152024141`

**Aditya Luthfi**
 NIM: `152024139`

---

<table>
<tr>
<td align="center">
<img src="https://img.icons8.com/color/96/000000/python.png" width="60px"/><br/>
<sub><b>Python Developer</b></sub>
</td>
<td align="center">
<img src="https://img.icons8.com/color/96/000000/parallel-tasks.png" width="60px"/><br/>
<sub><b>Data Mining</b></sub>
</td>
<td align="center">
<img src="https://img.icons8.com/color/96/000000/code.png" width="60px"/><br/>
<sub><b>Algorithm Design</b></sub>
</td>
</tr>
</table>

---

### 📬 Connect

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)](https://github.com/rhyred)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:robigold9@gmail.com)

</div>

---

<div align="center">

---

```
┌────────────────────────────────────────────┐
│  © 2026 Data Mining & Information Retrival │
│       Systems - Informatika ITENAS         │
└────────────────────────────────────────────┘
```

</div>