import os
import time
import hashlib
from celery import Celery

app = Celery(
    "watcher",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

processed_files = {}

def get_file_hash(filepath):
    stat = os.stat(filepath)
    return hashlib.md5(f"{filepath}-{stat.st_mtime}-{stat.st_size}".encode()).hexdigest()

@app.task
def process_file(filepath):
    print(f"📄 Processing: {filepath}")

    # ONLY ingest once (not full re-run)
    os.system("python3 ingest.py")

    print(f"✅ Done: {filepath}")

def watch_folder(folder="data"):
    print("👀 Watching PDFs...")

    while True:
        for file in os.listdir(folder):
            if file.endswith(".pdf"):
                path = os.path.join(folder, file)

                file_hash = get_file_hash(path)

                if processed_files.get(path) != file_hash:
                    processed_files[path] = file_hash
                    print(f"🚀 New/Updated file: {file}")
                    process_file.delay(path)

        time.sleep(5)

if __name__ == "__main__":
    watch_folder()