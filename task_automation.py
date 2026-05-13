# ============================================================
# Task Automation with Python Scripts
# CodeAlpha Python Programming Internship
# All 3 sub-tasks included — user picks one at runtime
# ============================================================

import os
import re
import shutil

# ─────────────────────────────────────────────────────────────
# SUB-TASK A: Move all .jpg files from source to destination
# ─────────────────────────────────────────────────────────────

def move_jpg_files():
    """Move all .jpg files from a source folder to a new destination folder."""
    print("\n📁 JPG FILE MOVER")
    source = input("Enter source folder path: ").strip()

    if not os.path.isdir(source):
        print(f"⚠  Source folder '{source}' does not exist.")
        return

    destination = input("Enter destination folder path (will be created if absent): ").strip()
    os.makedirs(destination, exist_ok=True)

    jpg_files = [f for f in os.listdir(source)
                 if f.lower().endswith((".jpg", ".jpeg"))]

    if not jpg_files:
        print("⚠  No .jpg files found in the source folder.")
        return

    moved = 0
    for filename in jpg_files:
        src_path  = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)

        # Avoid overwriting: rename if file exists at destination
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            dest_path = os.path.join(destination, f"{base}_copy{ext}")

        shutil.move(src_path, dest_path)
        print(f"  ✅ Moved: {filename}")
        moved += 1

    print(f"\n🎉 Done! {moved} file(s) moved to '{destination}'")


# ─────────────────────────────────────────────────────────────
# SUB-TASK B: Extract email addresses from a .txt file
# ─────────────────────────────────────────────────────────────

def extract_emails():
    """Extract all email addresses from a .txt file and save them."""
    print("\n📧 EMAIL EXTRACTOR")
    input_file = input("Enter path to input .txt file: ").strip()

    if not os.path.isfile(input_file):
        print(f"⚠  File '{input_file}' does not exist.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex pattern to match standard email addresses
    email_pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    emails = list(set(re.findall(email_pattern, content)))  # unique emails

    if not emails:
        print("⚠  No email addresses found in the file.")
        return

    print(f"\n✅ Found {len(emails)} unique email(s):")
    for email in sorted(emails):
        print(f"   • {email}")

    output_file = input("\nEnter output file path to save emails (e.g. emails.txt): ").strip()
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Extracted Emails ({len(emails)} found)\n")
        f.write("=" * 40 + "\n")
        for email in sorted(emails):
            f.write(email + "\n")

    print(f"💾 Emails saved to '{output_file}'")


# ─────────────────────────────────────────────────────────────
# SUB-TASK C: Scrape the title of a webpage and save it
# ─────────────────────────────────────────────────────────────

def scrape_webpage_title():
    """Fetch and save the <title> of a given webpage."""
    try:
        import urllib.request
        from html.parser import HTMLParser
    except ImportError:
        print("⚠  Required modules not available.")
        return

    class TitleParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self._in_title = False
            self.title = None

        def handle_starttag(self, tag, attrs):
            if tag.lower() == "title":
                self._in_title = True

        def handle_data(self, data):
            if self._in_title and self.title is None:
                self.title = data.strip()

        def handle_endtag(self, tag):
            if tag.lower() == "title":
                self._in_title = False

    print("\n🌐 WEBPAGE TITLE SCRAPER")
    url = input("Enter the full URL (e.g. https://www.python.org): ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"⚠  Could not fetch the page: {e}")
        return

    parser = TitleParser()
    parser.feed(html)

    if parser.title:
        print(f"\n✅ Page Title: {parser.title}")
        output_file = input("Save to file? Enter filename (or press Enter to skip): ").strip()
        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"URL   : {url}\n")
                f.write(f"Title : {parser.title}\n")
            print(f"💾 Saved to '{output_file}'")
    else:
        print("⚠  Could not find a title tag on the page.")


# ─────────────────────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("   🤖 TASK AUTOMATION — CodeAlpha")
    print("=" * 50)
    print("\nChoose a sub-task:")
    print("  1. Move .jpg files to a new folder")
    print("  2. Extract emails from a .txt file")
    print("  3. Scrape and save a webpage title")
    print("  0. Exit")

    choice = input("\nEnter choice (0-3): ").strip()

    if choice == "1":
        move_jpg_files()
    elif choice == "2":
        extract_emails()
    elif choice == "3":
        scrape_webpage_title()
    elif choice == "0":
        print("Goodbye! 👋")
    else:
        print("⚠  Invalid choice.")

if __name__ == "__main__":
    main()
