import os

base_dir = r"d:\Downloads\UX_UI_Design_EN_only\prototype"

print("1. Refining index.html logo size and card contrast")
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# Logo increase
idx = idx.replace('class="h-24 mx-auto mb-4"', 'class="h-32 mx-auto mb-4"')

# Remove ribbons from .map-card styles
idx = idx.replace('border-left: 4px solid transparent; ', '')
idx = idx.replace('border-left-color: #0d7377; ', '')

# Fix Initiate Project card
idx = idx.replace('class="card map-card p-4 border-l-teal-500 bg-teal-50/20"', 'class="card map-card p-4"')

# Fix Marketplace card
idx = idx.replace('class="card map-card p-4 bg-emerald-50/20 border-l-emerald-500"', 'class="card map-card p-4"')

# Fix Global Dashboard card
idx = idx.replace('class="card map-card p-4 bg-rose-50/20 border-l-rose-500"', 'class="card map-card p-4"')

# Fix Permissions card
idx = idx.replace('class="card map-card p-4 opacity-50"', 'class="card map-card p-4"')

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

print("2. Refining login.html logo size")
login_path = os.path.join(base_dir, "login.html")
with open(login_path, "r", encoding="utf-8") as f:
    login = f.read()

# Logo increase
login = login.replace('h-24 mx-auto mb-6', 'h-32 mx-auto mb-6')

with open(login_path, "w", encoding="utf-8") as f:
    f.write(login)

print("Done.")
