import os
import re

base_dir = r"d:\Downloads\UX_UI_Design_EN_only\prototype"

print("1. Updating shared/styles.css")
css_path = os.path.join(base_dir, "shared", "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("width: 120px;", "width: 160px;").replace("margin-bottom: 1rem;", "margin-bottom: 2rem;")
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("2. Updating index.html")
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

idx = idx.replace('bg-slate-50', 'bg-[#0a2d2f]')
idx = idx.replace('<img src="shared/logo.png" alt="Matcha Capital" class="h-16 mx-auto mb-6">', '<img src="shared/logo.png" alt="Matcha Capital" class="h-24 mx-auto mb-4">')
idx = re.sub(r'<h1 class="text-4xl[^>]*>MATCHA CAPITAL</h1>\s*', '', idx)
idx = idx.replace('text-slate-500 font-medium', 'text-teal-100/80 font-medium')
idx = idx.replace('text-xs font-black text-slate-400 uppercase tracking-[0.3em]', 'text-xs font-black text-teal-400/80 uppercase tracking-[0.3em]')
idx = idx.replace('border-b pb-2', 'border-b border-teal-800/50 pb-2')
idx = idx.replace('border-t border-slate-200', 'border-t border-teal-900/60')
idx = idx.replace('text-[10px] font-bold text-slate-400 uppercase tracking-widest', 'text-[10px] font-bold text-teal-600/70 uppercase tracking-widest')

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

print("3. Updating other HTML files")
for fname in os.listdir(base_dir):
    if fname.endswith('.html'):
        path = os.path.join(base_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        nc = content
        
        # Remove h2 matcha capital
        nc = re.sub(r'<h2 class="text-xl font-bold tracking-tight[^>]*>\s*Matcha Capital\s*</h2>\s*', '', nc)
        
        # Specific updates for login
        if fname == 'login.html':
            nc = nc.replace('h-16 mx-auto mb-6', 'h-24 mx-auto mb-6')
            
        if nc != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(nc)
            print(f"Updated {fname}")

print("Done.")
