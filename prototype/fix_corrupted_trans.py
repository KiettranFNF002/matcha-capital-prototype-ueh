import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix the truncated SVG strings
replacements = {
    'btn_submit_blockchain: "<svg class=\'w-4 h-4 inline-block mr-1\' fill=",': 'btn_submit_blockchain: "<svg class=\'w-4 h-4 inline-block mr-1\' fill=\'none\' stroke=\'currentColor\' viewBox=\'0 0 24 24\'><path stroke-linecap=\'round\' stroke-linejoin=\'round\' stroke-width=\'2\' d=\'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z\'></path></svg> REGISTER ON BLOCKCHAIN",',
    'wizard_risk_esg: "<svg class=\'w-4 h-4 inline-block mr-1 text-emerald-500\' fill=",': 'wizard_risk_esg: "<svg class=\'w-4 h-4 inline-block mr-1 text-emerald-500\' fill=\'none\' stroke=\'currentColor\' viewBox=\'0 0 24 24\'><path stroke-linecap=\'round\' stroke-linejoin=\'round\' stroke-width=\'2\' d=\'M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z\'></path></svg> ESG / EUDR Risks",',
    'wizard_risk_legal: "<svg class=\'w-4 h-4 inline-block mr-1 text-slate-500\' fill=",': 'wizard_risk_legal: "<svg class=\'w-4 h-4 inline-block mr-1 text-slate-500\' fill=\'none\' stroke=\'currentColor\' viewBox=\'0 0 24 24\'><path stroke-linecap=\'round\' stroke-linejoin=\'round\' stroke-width=\'2\' d=\'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z\'></path></svg> Legal / Construction Licensing",',
    'vdr_public_badge: "<svg class=\'w-4 h-4 inline-block mr-1 text-emerald-500\' fill=",': 'vdr_public_badge: "<svg class=\'w-4 h-4 inline-block mr-1 text-emerald-500\' fill=\'currentColor\' viewBox=\'0 0 20 20\'><circle cx=\'10\' cy=\'10\' r=\'5\'></circle></svg> PUBLIC",',
    'cv_status_processing: "<svg class=\'w-4 h-4 inline-block mr-1 animate-spin\' fill=",': 'cv_status_processing: "<svg class=\'w-4 h-4 inline-block mr-1 animate-spin\' fill=\'none\' stroke=\'currentColor\' viewBox=\'0 0 24 24\'><path stroke-linecap=\'round\' stroke-linejoin=\'round\' stroke-width=\'2\' d=\'M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z\'></path></svg> RECONCILING...",',
    'status_mismatch: "[<svg class=\'w-4 h-4 inline-block mr-1 text-red-600 font-bold\' fill=",': 'status_mismatch: "[<svg class=\'w-4 h-4 inline-block mr-1 text-red-600 font-bold\' fill=\'none\' stroke=\'currentColor\' viewBox=\'0 0 24 24\'><path stroke-linecap=\'round\' stroke-linejoin=\'round\' stroke-width=\'2\' d=\'M6 18L18 6M6 6l12 12\'></path></svg> Mismatch!]",',
}

for vi, en in replacements.items():
    text = text.replace(vi, en)

# 2. Standardize "B" to "Billion"
# Matches like "125B", "21B", "250B", "45B", "500B", "1250B" followed by optional space and <u>đ</u>
text = re.sub(r'(\d+)B(?=\s*<u>đ</u>)', r'\1 Billion', text)
text = re.sub(r'(\d+)B(?=\s*")', r'\1 Billion', text)
text = re.sub(r'(\d+)B(?=\s*\')', r'\1 Billion', text)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed translations.js SVG strings and standardized Billion.")
