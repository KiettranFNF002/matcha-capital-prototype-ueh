content = open('prototype/deal-discovery.html', 'r', encoding='utf-8').read()

# Find and remove the junk orphan text on its own line
bad_lines = [
    '\u1ed0N L\u01af \u0110\u1ed8NG CAO SU</h2>',
    '          <p class="text-sm text-slate-500 mb-8 line-clamp-2" data-i18n="market_proj_rubber_desc">T\u00e0i tr\u1ee3 thu mua m\u1ee7 cao su cho m\u00f9a v\u1ee5 2026. \u0110\u1ea3m b\u1ea3o b\u1eb1ng kho h\u00e0ng v\u00e0 ph\u1ea3i thu.</p>',
]

lines = content.split('\n')
cleaned = []
for line in lines:
    skip = False
    for bad in bad_lines:
        if bad in line:
            skip = True
            break
    if not skip:
        cleaned.append(line)

result = '\n'.join(cleaned)
open('prototype/deal-discovery.html', 'w', encoding='utf-8').write(result)
print(f"Done. Removed {len(lines) - len(cleaned)} junk lines.")
