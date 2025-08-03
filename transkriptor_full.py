import whisper
import ffmpeg
from tkinter import Tk, filedialog
from pathlib import Path

# Zamanı dakika:saniye olarak biçimlendir
def format_time(seconds: float) -> str:
    minutes = int(seconds) // 60
    secs = int(seconds) % 60
    return f"{minutes}:{secs:02d}"

# Tkinter dosya seçici penceresi aç
Tk().withdraw()  # GUI penceresini gizle
print("Lütfen bir ses ya da video dosyası seçin (mp3, mp4, wav...)")
file_path = filedialog.askopenfilename(filetypes=[("Media files", "*.mp3 *.mp4 *.wav *.m4a *.mov")])

if not file_path:
    print("❌ Hiçbir dosya seçilmedi. Çıkılıyor.")
    exit()

print(f"✅ Seçilen dosya: {file_path}")

# Geçici ses dosyası
audio_path = "temp_audio.wav"

# ffmpeg ile ses ayıklama ve dönüştürme
ffmpeg.input(file_path).output(audio_path, ac=1, ar='16000').run(overwrite_output=True)

# Whisper modelini yükle
model = whisper.load_model("base")

# Transkripsiyon işlemi
result = model.transcribe(audio_path, language="tr")

# TXT çıktısı yaz
output_file = Path("transkript.txt")
with output_file.open("w", encoding="utf-8") as f:
    for seg in result['segments']:
        start = format_time(seg['start'])
        end = format_time(seg['end'])
        text = seg['text'].strip()
        f.write(f"[{start} - {end}] {text}\n")

print("📄 Transkript başarıyla oluşturuldu: transkript.txt")
