# 📝 Ses Deşifre
Bu proje, ses dosyalarını yazılı metne dönüştüren bir Python uygulamasıdır. Özellikle ses kayıtlarının dökümünü otomatikleştirmek için tasarlanmıştır.


## 🛠️ Geliştirme Ortamı Kurulumu

Projeyi çalıştırmak için önce Visual Studio Code ve Python 3.10.0 kurulumu yapılmalıdır.

---

### 1️⃣ Visual Studio Code Kurulumu

1. [Visual Studio Code'un resmi web sitesine gidin](https://code.visualstudio.com/)
2. İşletim sisteminize uygun olan sürümü indirin (Windows, macOS, Linux).
3. Kurulumu tamamlayın ve **VS Code**'u açın.
4. Sol menüde yer alan **Extensions (Eklentiler)** bölümüne tıklayın.
5. Arama kısmına `Python` yazın ve **Microsoft tarafından geliştirilen Python uzantısını** yükleyin.

---

### 2️⃣ Python 3.10.0 Kurulumu

1. [Python 3.10.0 sürümünü indirmek için buraya tıklayın](https://www.python.org/downloads/release/python-3100/)
2. İşletim sisteminize uygun olan kurulum dosyasını indirin.
3. Kurulum sırasında mutlaka şu seçeneği işaretleyin:  
   ✅ **Add Python to PATH**
4. Kurulum tamamlandıktan sonra terminal veya komut satırına aşağıdaki komutlardan birini yazın:


```bash
python --version
```

veya

```bash
python3 --version
```




## 📦 Gereksinimler

Proje bağımlılıkları `requirements.txt` dosyasında listelenmiştir. Gerekli kütüphaneleri tek komutla kurabilirsiniz.

## 📚 Kullanılan Kütüphaneler

Bu projede kullanılan başlıca Python kütüphaneleri şunlardır:

- **`openai-whisper`**: Ses dosyalarını metne dönüştürmek için kullanılan transkripsiyon modeli  
- **`ffmpeg-python`**: Ses ve video dosyalarını dönüştürmek ve işlemek için  
- **`torch`**: Whisper modelinin çalışması için gerekli derin öğrenme kütüphanesi  
- **`pydub`**: Ses dosyalarını kesmek, birleştirmek ve dönüştürmek için  
- **`noisereduce`**: Arka plan gürültüsünü azaltmak için kullanılan kütüphane

> 💡 Tüm bağımlılıkların tam listesi ve sürüm bilgileri `requirements.txt` dosyasında yer almaktadır.



---

## 🚀 Kurulum Adımları

### 1. Sanal Ortam Oluştur

```bash
py -3.10 -m venv env
```

### 2. Ortamı Aktif Et

**Windows:**

```bash
.\env\Scripts\activate
```

**macOS / Linux:**

```bash
source env/bin/activate
```

### 3. Gerekli Paketleri Kur

```bash
pip install -r requirements.txt
```

---

## ▶️ Kullanım

Kurulum işlemi tamamlandıktan sonra aşağıdaki komutu çalıştırarak transkripsiyon işlemine başlayabilirsiniz:

```bash
python transkriptor_3sn.py
```
Veya

```bash
python  transkriptor_full.py

```


- `transkriptor_3sn.py` : Ses dosyasını 3 saniyelik segmentlere ayırarak her bir parçayı Whisper ile işler. Zaman damgalı, bölünmüş transkript çıktısı verir.
- `transkriptor_full.py`: ffmpeg ile sesi ayrıştırır ve dosyanın tamamını Whisper ile işleyerek bütünsel bir transkript oluşturur.


## 🧾 Çıktılar (Output)

### 📄 1. `transkriptor_full.py` Scripti

Bu script, seçilen ses veya video dosyasını `ffmpeg` kullanarak işledikten sonra, **Whisper modeli ile tamamını tek seferde** transkribe eder.

✅ Oluşan çıktı dosyası: transkript.txt


-[00:00 - 00:07] Merhaba, bu bir test kaydıdır.

-[00:08 - 00:15] Whisper modeli ile transkript işlemi yapılmaktadır.



🧠 Açıklamalar:
- Tüm transkript tek parça olarak işlenir.
- Her satırda başlangıç ve bitiş zamanları ile birlikte transkripte edilen metin yer alır.
- Dil: Türkçe (`language="tr"` parametresi kullanılmıştır)


---

### 🧩 2. `transkriptor_3sn.py` Scripti

Bu script, ses dosyasını **3 saniyelik segmentlere böler** ve her segmenti ayrı ayrı Whisper modeli ile işler. Her segmentin zamanı ve metni dosyaya yazılır.

✅ Oluşan çıktı dosyası:transkript_3saniye.txt

📄 Örnek içerik:

-[0:00.000 - 0:03.000] Merhaba, bu bir test kaydıdır.

-[0:03.000 - 0:06.000] Bu kayıt parça parça analiz edilmektedir.



🧠 Açıklamalar:
- Her satır 3 saniyelik bir parçanın transkriptini temsil eder.
- Zaman aralıkları milisaniye cinsindedir (`0:03.000` gibi).
- Kayıt uzunluğuna göre yüzlerce segment oluşabilir.
- Arka arkaya düzgün konuşmaların zaman damgalı dökümü alınır.

---

📁 Her iki dosya da çalıştırıldığında `.txt` formatında çıktı üretir ve çalıştırıldığı dizine kaydeder.




---

## 📁 Dosya Yapısı

```
.
├── env/                   # Sanal ortam klasörü
├── requirements.txt       # Gerekli Python kütüphaneleri
├── transkriptor_3sn.py    # Segment bazlı (3 saniyelik) transkripsiyon scripti
├── transkriptor_full.py   # Tam ses dosyasını işleyen bütünsel transkripsiyon scripti
└── README.md              # Proje açıklamaları ve kurulum dokümantasyonu

```

---

## ℹ️ Ek Bilgi

- Python sürümü: `3.10.0`
- Örnek ses dosyaları `.wav`, `.mp3`, `.mp4`,`.mov` gibi formatlarda desteklenebilir (kullandığınız kütüphaneye göre).
- Script içerisinde kullanılan kütüphaneler arasında `speechrecognition`, `pydub`, `openai`, vs. olabilir. Detaylar `requirements.txt` içerisinde yer alır.

---


