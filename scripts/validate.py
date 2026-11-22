
import json
import hashlib
from pathlib import Path
from datetime import datetime

# Menentukan lokasi folder utama proyek
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Lokasi manifest dan laporan
MANIFEST_PATH = PROJECT_ROOT / "manifest.json"
REPORT_PATH = PROJECT_ROOT / "reports" / "validation.json"

# Metadata yang wajib tersedia
REQUIRED_FIELDS = [
    "document_id",
    "title",
    "source",
    "file_path",
    "version",
    "access_level"
]


def calculate_sha256(file_path):
    """Menghitung hash SHA-256 sebuah file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def validate_dataset():
    # Membaca manifest JSON
    with open(MANIFEST_PATH, "r", encoding="utf-8") as file:
        manifest = json.load(file)

    documents = manifest.get("documents", [])

    errors = []
    valid_documents = []
    invalid_documents = []
    used_ids = set()

    # Memeriksa setiap dokumen
    for document in documents:
        document_id = document.get("document_id", "UNKNOWN")
        document_errors = []

        # 1. Memeriksa metadata wajib
        for field in REQUIRED_FIELDS:
            if not document.get(field):
                document_errors.append(
                    f"Metadata {field} belum diisi"
                )

        # 2. Memeriksa ID duplikat
        if document_id in used_ids:
            document_errors.append(
                f"Document ID duplikat: {document_id}"
            )
        else:
            used_ids.add(document_id)

        # 3. Memeriksa lokasi file
        relative_path = Path(document.get("file_path", ""))

        if relative_path.is_absolute() or ".." in relative_path.parts:
            document_errors.append(
                "Path file tidak boleh keluar dari folder proyek"
            )
            file_path = None
        else:
            file_path = PROJECT_ROOT / relative_path

        # 4. Memeriksa keberadaan dan isi file
        if file_path is not None:
            if not file_path.is_file():
                document_errors.append(
                    f"File tidak ditemukan: {relative_path}"
                )
            else:
                try:
                    content = file_path.read_text(encoding="utf-8")

                    if len(content.strip()) < 50:
                        document_errors.append(
                            "Konten dokumen kosong atau kurang dari 50 karakter"
                        )

                    # 5. Menghitung SHA-256
                    file_hash = calculate_sha256(file_path)
                    file_size = file_path.stat().st_size

                except UnicodeDecodeError:
                    document_errors.append(
                        "File tidak menggunakan encoding UTF-8"
                    )
                    file_hash = None
                    file_size = None
        else:
            file_hash = None
            file_size = None

        # Menyimpan hasil pemeriksaan
        result = {
            "document_id": document_id,
            "title": document.get("title", ""),
            "status": "VALID" if not document_errors else "INVALID",
            "sha256": file_hash,
            "size_bytes": file_size,
            "errors": document_errors
        }

        if document_errors:
            invalid_documents.append(result)
            errors.append(result)
        else:
            valid_documents.append(result)

    # Membuat laporan validasi
    report = {
        "project_name": manifest.get("project_name", ""),
        "validation_date": datetime.now().isoformat(),
        "total_documents": len(documents),
        "valid_documents": len(valid_documents),
        "invalid_documents": len(invalid_documents),
        "status": "SUCCESS" if not errors else "FAILED",
        "documents": valid_documents + invalid_documents,
        "errors": errors
    }

    # Menyimpan laporan JSON
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(REPORT_PATH, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    # Menampilkan hasil ke terminal
    print("=== HASIL VALIDASI DATASET TP5 ===")
    print(f"Total dokumen  : {len(documents)}")
    print(f"Dokumen valid  : {len(valid_documents)}")
    print(f"Dokumen invalid: {len(invalid_documents)}")
    print(f"Status         : {report['status']}")
    print(f"Laporan        : {REPORT_PATH}")

    if errors:
        print("\nDaftar kesalahan:")
        for error in errors:
            print(
                f"- {error['document_id']}: "
                f"{', '.join(error['errors'])}"
            )


if __name__ == "__main__":
    validate_dataset()
