#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║  LOCAL INGEST — Gitingest-style tool, nhưng chạy 100% offline  ║
║  Tác giả: AnhKiet's Workspace                                  ║
╚══════════════════════════════════════════════════════════════════╝

Hai chế độ hoạt động:
  1. ingest  — Gom toàn bộ codebase thành 1 file .txt có cấu trúc
  2. package — Đóng gói các file kết quả vào thư mục sạch cho người xem

Cách dùng:
  python local_ingest.py ingest <đường_dẫn...> [tùy chọn]
  python local_ingest.py package <đường_dẫn...> [tùy chọn]

Hỗ trợ kéo thả file/thư mục vào terminal (Windows sẽ tự paste đường dẫn).
"""

import argparse
import os
import sys
import shutil
import fnmatch
import datetime
import textwrap

# ─── Cấu hình mặc định ─────────────────────────────────────────
DEFAULT_EXCLUDE_DIRS = [
    "legacy", "node_modules", ".git", "__pycache__", ".venv", "venv",
    ".idea", ".vscode", "dist", "build", ".next", ".cache",
]
DEFAULT_EXCLUDE_FILES = [
    "*.pyc", "*.pyo", "*.exe", "*.dll", "*.so", "*.dylib",
    "*.zip", "*.tar.gz", "*.rar", "*.7z",
    "*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.ico", "*.svg",
    "*.mp4", "*.avi", "*.mov", "*.mp3", "*.wav",
    "*.woff", "*.woff2", "*.ttf", "*.eot",
    "*.pdf", "*.doc", "*.docx", "*.xls", "*.xlsx",
    ".DS_Store", "Thumbs.db", "desktop.ini",
]

# Giới hạn kích thước file (mặc định 500KB)
MAX_FILE_SIZE_KB = 500

# ─── Tiện ích ────────────────────────────────────────────────────

def clean_path(path: str) -> str:
    """Xóa dấu ngoặc kép bao quanh đường dẫn (do kéo thả trên Windows)."""
    return path.strip().strip('"').strip("'")


def should_exclude_dir(dirname: str, exclude_dirs: list) -> bool:
    """Kiểm tra thư mục có nằm trong danh sách loại trừ không."""
    return any(fnmatch.fnmatch(dirname.lower(), pat.lower()) for pat in exclude_dirs)


def should_exclude_file(filename: str, exclude_files: list) -> bool:
    """Kiểm tra file có nằm trong danh sách loại trừ không."""
    return any(fnmatch.fnmatch(filename.lower(), pat.lower()) for pat in exclude_files)


def collect_files(paths: list, exclude_dirs: list, exclude_files: list,
                  include_extensions: list = None) -> list:
    """
    Thu thập danh sách file từ các đường dẫn đầu vào.
    Hỗ trợ cả file lẻ và thư mục.
    """
    collected = []
    for raw_path in paths:
        path = clean_path(raw_path)
        if not os.path.exists(path):
            print(f"  ⚠️  Bỏ qua (không tồn tại): {path}")
            continue

        if os.path.isfile(path):
            fname = os.path.basename(path)
            if not should_exclude_file(fname, exclude_files):
                if include_extensions:
                    ext = os.path.splitext(fname)[1].lstrip('.').lower()
                    if ext in [e.lower() for e in include_extensions]:
                        collected.append(os.path.abspath(path))
                else:
                    collected.append(os.path.abspath(path))
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                # Loại bỏ thư mục không mong muốn (sửa tại chỗ để os.walk không đi sâu vào)
                dirs[:] = [d for d in dirs if not should_exclude_dir(d, exclude_dirs)]
                for fname in sorted(files):
                    if should_exclude_file(fname, exclude_files):
                        continue
                    if include_extensions:
                        ext = os.path.splitext(fname)[1].lstrip('.').lower()
                        if ext not in [e.lower() for e in include_extensions]:
                            continue
                    collected.append(os.path.abspath(os.path.join(root, fname)))
    return collected


def read_file_safe(filepath: str, max_size_kb: int = MAX_FILE_SIZE_KB) -> str | None:
    """Đọc nội dung file an toàn, bỏ qua file quá lớn hoặc binary."""
    try:
        size_kb = os.path.getsize(filepath) / 1024
        if size_kb > max_size_kb:
            return f"[FILE QUÁ LỚN: {size_kb:.0f}KB > {max_size_kb}KB — đã bỏ qua]"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception as e:
        return f"[LỖI ĐỌC FILE: {e}]"


def build_tree(paths: list, exclude_dirs: list, exclude_files: list) -> str:
    """Xây dựng cây thư mục dạng text (giống lệnh `tree`)."""
    lines = []
    for raw_path in paths:
        path = clean_path(raw_path)
        if not os.path.exists(path):
            continue
        if os.path.isfile(path):
            lines.append(f"📄 {os.path.basename(path)}")
        elif os.path.isdir(path):
            base = os.path.basename(os.path.abspath(path))
            lines.append(f"📁 {base}/")
            _tree_walk(path, "", lines, exclude_dirs, exclude_files)
    return "\n".join(lines)


def _tree_walk(directory: str, prefix: str, lines: list,
               exclude_dirs: list, exclude_files: list):
    """Đệ quy vẽ cây thư mục."""
    entries = sorted(os.listdir(directory))
    dirs = [e for e in entries if os.path.isdir(os.path.join(directory, e))
            and not should_exclude_dir(e, exclude_dirs)]
    files = [e for e in entries if os.path.isfile(os.path.join(directory, e))
             and not should_exclude_file(e, exclude_files)]

    all_items = [(d, True) for d in dirs] + [(f, False) for f in files]
    for i, (name, is_dir) in enumerate(all_items):
        is_last = (i == len(all_items) - 1)
        connector = "└── " if is_last else "├── "
        if is_dir:
            lines.append(f"{prefix}{connector}📁 {name}/")
            extension = "    " if is_last else "│   "
            _tree_walk(os.path.join(directory, name), prefix + extension,
                       lines, exclude_dirs, exclude_files)
        else:
            lines.append(f"{prefix}{connector}{name}")


# ─── Chế độ INGEST ──────────────────────────────────────────────

def cmd_ingest(args):
    """Gom toàn bộ codebase thành 1 file text có cấu trúc."""
    exclude_dirs = DEFAULT_EXCLUDE_DIRS + (args.exclude_dirs or [])
    exclude_files = DEFAULT_EXCLUDE_FILES + (args.exclude_files or [])

    print("\n🔍 LOCAL INGEST — Quét codebase...")
    print(f"   📂 Đầu vào: {', '.join(args.paths)}")
    print(f"   🚫 Loại trừ thư mục: {', '.join(exclude_dirs)}")
    if args.exclude_files:
        print(f"   🚫 Loại trừ file: {', '.join(args.exclude_files)}")

    files = collect_files(args.paths, exclude_dirs, exclude_files,
                          args.extensions)
    if not files:
        print("   ❌ Không tìm thấy file nào phù hợp.")
        return

    print(f"   ✅ Tìm thấy {len(files)} file\n")

    # Xây dựng nội dung
    output_parts = []

    # Header
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = textwrap.dedent(f"""\
    ╔══════════════════════════════════════════════════════════════╗
    ║  LOCAL INGEST — Tổng hợp Codebase                          ║
    ║  Thời gian: {timestamp}                          ║
    ║  Tổng số file: {len(files):<44}║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    output_parts.append(header)

    # Cây thư mục
    output_parts.append("=" * 60)
    output_parts.append("📂 CẤU TRÚC THƯ MỤC (Directory Tree)")
    output_parts.append("=" * 60 + "\n")
    tree = build_tree(args.paths, exclude_dirs, exclude_files)
    output_parts.append(tree)
    output_parts.append("\n")

    # Nội dung từng file
    output_parts.append("=" * 60)
    output_parts.append("📄 NỘI DUNG CÁC FILE")
    output_parts.append("=" * 60 + "\n")

    # Tìm đường dẫn gốc chung để hiển thị relative path
    common = os.path.commonpath(files) if len(files) > 1 else os.path.dirname(files[0])

    for filepath in files:
        rel = os.path.relpath(filepath, common)
        ext = os.path.splitext(filepath)[1].lstrip('.')
        size_kb = os.path.getsize(filepath) / 1024
        
        output_parts.append(f"{'─' * 60}")
        output_parts.append(f"📄 File: {rel}")
        output_parts.append(f"   Kích thước: {size_kb:.1f} KB | Loại: .{ext}")
        output_parts.append(f"{'─' * 60}")

        content = read_file_safe(filepath, args.max_size)
        if content:
            output_parts.append(content)
        output_parts.append("\n")

    # Ghi output
    output_text = "\n".join(output_parts)
    output_path = args.output or "ingest_output.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_text)

    total_size = os.path.getsize(output_path) / 1024
    print(f"✅ Đã xuất bản: {os.path.abspath(output_path)}")
    print(f"   📊 Tổng kích thước: {total_size:.1f} KB | {len(files)} file")


# ─── Chế độ PACKAGE ──────────────────────────────────────────────

def cmd_package(args):
    """Đóng gói các file kết quả vào thư mục sạch."""
    exclude_dirs = DEFAULT_EXCLUDE_DIRS + (args.exclude_dirs or [])
    exclude_files = (args.exclude_files or [])

    print("\n📦 LOCAL PACKAGE — Đóng gói file kết quả...")
    print(f"   📂 Đầu vào: {', '.join(args.paths)}")

    # Mặc định chỉ lấy file kết quả (HTML, PDF...) trừ khi có --extensions
    include_ext = args.extensions or ["html", "pdf", "csv", "json", "md"]
    print(f"   📋 Chỉ lấy file: {', '.join(['.' + e for e in include_ext])}")

    files = collect_files(args.paths, exclude_dirs, exclude_files, include_ext)
    if not files:
        print("   ❌ Không tìm thấy file nào phù hợp.")
        return

    # Tạo thư mục đầu ra
    output_dir = args.output_dir or "CRN_Package"
    os.makedirs(output_dir, exist_ok=True)

    print(f"   ✅ Tìm thấy {len(files)} file")
    print(f"   📁 Đóng gói vào: {os.path.abspath(output_dir)}\n")

    copied = 0
    for filepath in files:
        fname = os.path.basename(filepath)
        dest = os.path.join(output_dir, fname)
        
        # Tránh ghi đè file trùng tên
        if os.path.exists(dest):
            base, ext = os.path.splitext(fname)
            counter = 1
            while os.path.exists(dest):
                dest = os.path.join(output_dir, f"{base}_{counter}{ext}")
                counter += 1

        shutil.copy2(filepath, dest)
        print(f"   ✔ {fname}")
        copied += 1

    print(f"\n✅ Đóng gói hoàn tất: {copied} file → {os.path.abspath(output_dir)}")
    print(f"   💡 Gửi thư mục '{output_dir}' này cho người xem là xong!")


# ─── CLI Parser ──────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="local_ingest",
        description="🔧 Local Ingest — Gitingest chạy offline, tùy biến cao",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
        ─────────────────────────────────────────────────
        VÍ DỤ SỬ DỤNG:
        
          # Gom toàn bộ project thành 1 file text:
          python local_ingest.py ingest . --output project.txt
          
          # Gom chỉ file Python, loại bỏ thư mục legacy:
          python local_ingest.py ingest . --ext py --exclude-dirs legacy test
          
          # Kéo thả file vào terminal:
          python local_ingest.py ingest "D:\\path\\file1.py" "D:\\path\\file2.py"
          
          # Đóng gói file HTML cho người xem:
          python local_ingest.py package . --ext html --output-dir BanGiao
          
          # Đóng gói file HTML và PDF:
          python local_ingest.py package . --ext html pdf --output-dir BanGiao
        ─────────────────────────────────────────────────
        """)
    )

    subparsers = parser.add_subparsers(dest="command", help="Chế độ hoạt động")

    # ── Subcommand: ingest ──
    p_ingest = subparsers.add_parser("ingest", help="Gom codebase thành 1 file text")
    p_ingest.add_argument("paths", nargs="+",
                          help="Đường dẫn file hoặc thư mục (hỗ trợ kéo thả)")
    p_ingest.add_argument("-o", "--output", default="ingest_output.txt",
                          help="Tên file đầu ra (mặc định: ingest_output.txt)")
    p_ingest.add_argument("--exclude-dirs", nargs="*", default=[],
                          help="Thư mục cần loại trừ (thêm vào danh sách mặc định)")
    p_ingest.add_argument("--exclude-files", nargs="*", default=[],
                          help="Pattern file cần loại trừ (ví dụ: *.log *.tmp)")
    p_ingest.add_argument("--ext", dest="extensions", nargs="*", default=None,
                          help="Chỉ lấy file có đuôi cụ thể (ví dụ: py html js)")
    p_ingest.add_argument("--max-size", type=int, default=MAX_FILE_SIZE_KB,
                          help=f"Bỏ qua file lớn hơn N KB (mặc định: {MAX_FILE_SIZE_KB})")
    p_ingest.set_defaults(func=cmd_ingest)

    # ── Subcommand: package ──
    p_package = subparsers.add_parser("package", help="Đóng gói file kết quả")
    p_package.add_argument("paths", nargs="+",
                           help="Đường dẫn file hoặc thư mục (hỗ trợ kéo thả)")
    p_package.add_argument("-d", "--output-dir", default="CRN_Package",
                           help="Thư mục đầu ra (mặc định: CRN_Package)")
    p_package.add_argument("--exclude-dirs", nargs="*", default=[],
                           help="Thư mục cần loại trừ")
    p_package.add_argument("--exclude-files", nargs="*", default=[],
                           help="Pattern file cần loại trừ")
    p_package.add_argument("--ext", dest="extensions", nargs="*", default=None,
                           help="Chỉ lấy file có đuôi cụ thể (mặc định: html pdf csv json md)")
    p_package.set_defaults(func=cmd_package)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
