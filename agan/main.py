# Import library yang dibutuhkan
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Siapkan Data Dummy (Bisa diganti dengan membaca file CSV)
# X: Pengalaman Kerja (tahun), y: Gaji (Rupiah)
data = {
    'Pengalaman': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Gaji': [4000000, 4500000, 5200000, 6000000, 7100000, 7500000, 8300000, 9000000, 10500000, 11000000]
}
df = pd.DataFrame(data)

X = df[['Pengalaman']] # Variabel Independen (harus 2D array)
y = df['Gaji']         # Variabel Dependen

# 2. Bagi data menjadi Data Latih (Training) dan Data Uji (Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Buat dan Latih Model Regresi Linear
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Tampilkan Formula Model (Nilai a dan b)
konstanta = model.intercept_
koefisien = model.coef_[0]
print(f"Persamaan Model Estimasi: Y = {konstanta:.2f} + {koefisien:.2f}X")

# 5. Lakukan Prediksi Baru (Contoh: Pengalaman 4.5 tahun)
pengalaman_baru = np.array([[4.5]])
prediksi_gaji = model.predict(pengalaman_baru)
print(f"Estimasi gaji untuk pengalaman 4.5 tahun: Rp {prediksi_gaji[0]:,.2f}")

#kelompok 8 maker