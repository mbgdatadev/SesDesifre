import whisper
from pydub import AudioSegment
from tkinter import Tk, filedialog
from pathlib import Path
import os

def format_time(seconds: float) -> str:
    minutes = int(seconds) // 60
    secs = int(seconds) % 60
    ms = int((seconds - int(seconds)) * 1000)
    return f"{minutes}:{secs:02d}.{ms:03d}"

# 🎧 Ses dosyasını seç
Tk().withdraw()
print("📂 Lütfen bir ses ya da video dosyası seçin (mp3, mp4, wav...)")
file_path = filedialog.askopenfilename(filetypes=[("Media files", "*.mp3 *.mp4 *.wav *.m4a *.mov")])
if not file_path:
    print("❌ Dosya seçilmedi.")
    exit()
print(f"🎧 Seçilen dosya: {file_path}")

# Ses dosyasını yükle ve mono + 16000Hz olarak ayarla
sound = AudioSegment.from_file(file_path)
sound = sound.set_frame_rate(16000).set_channels(1)

# Süre bilgisi
duration_ms = len(sound)
segment_ms = 3000  # 3 saniyelik segment
total_segments = duration_ms // segment_ms + (1 if duration_ms % segment_ms != 0 else 0)
print(f"🔍 Toplam {total_segments} adet 3 saniyelik segment işlenecek.")

# Whisper model
model = whisper.load_model("large")

# Çıktı dosyası
output_file = Path("transkript_3saniye.txt")
with output_file.open("w", encoding="utf-8") as f:
    for i in range(total_segments):
        start_ms = i * segment_ms
        end_ms = min(start_ms + segment_ms, duration_ms)

        segment_audio = sound[start_ms:end_ms]
        temp_path = f"segment_{i}.wav"
        segment_audio.export(temp_path, format="wav")

        result = model.transcribe(temp_path, language="tr")
        text = result.get("text", "").strip()

        start_sec = start_ms / 1000
        end_sec = end_ms / 1000
        f.write(f"[{format_time(start_sec)} - {format_time(end_sec)}] {text}\n")

        os.remove(temp_path)

print("✅ Transkript tamamlandı: transkript_3saniye.txt")
