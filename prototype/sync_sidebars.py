import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != 'login.html']

internal_files = [
    'dashboard.html', 'company-verify.html', 'create-room.html', 
    'upload-docs.html', 'distribution.html', 'deal-pipeline.html', 'permission.html'
]
lender_files = [
    'deal-discovery.html', 'investor-profile.html', 'verification-center.html', 
    'deal-room.html', 'lender-view.html', 'indicative-offer.html', 'pricing.html'
]
admin_files = [
    'admin-dashboard.html', 'blockchain-monitor.html', 'audit-trail.html', 'blockchain-ledger.html'
]

internal_nav = """    <nav class="mt-4">
      <a href="index.html" class="text-xs opacity-50 mb-4 hover:opacity-100" data-i18n="nav_hub">← Back to Hub</a>
      <a href="dashboard.html" data-i18n="nav_dashboard">Dashboard</a>
      <a href="company-verify.html" data-i18n="nav_verify">Company Verify</a>
      <a href="create-room.html" data-i18n="nav_initiate">Initiate Project</a>
      <a href="upload-docs.html" data-i18n="nav_vault">Document Vault</a>
      <a href="distribution.html" data-i18n="nav_distribution">Distribution</a>
      <a href="deal-pipeline.html" data-i18n="nav_pipeline">Deal Pipeline</a>
      <a href="permission.html" data-i18n="nav_permission">Permissions</a>
    </nav>"""

lender_nav = """    <nav class="mt-4">
      <a href="index.html" class="text-xs opacity-50 mb-4 hover:opacity-100" data-i18n="nav_hub">← Back to Hub</a>
      <a href="deal-discovery.html" data-i18n="nav_marketplace">Browse Marketplace</a>
      <a href="investor-profile.html" data-i18n="nav_profile">Investor Profile</a>
      <a href="verification-center.html" data-i18n="nav_verification">Verification Center</a>
      <a href="deal-room.html" data-i18n="nav_vault">Deal Room</a>
      <a href="lender-view.html" data-i18n="nav_my_deals">My Deals</a>
      <a href="indicative-offer.html" data-i18n="nav_indicative">Indicative Offer</a>
      <a href="pricing.html" data-i18n="nav_pricing">Pricing Plan</a>
    </nav>"""

admin_nav = """    <nav class="mt-4">
      <a href="index.html" class="text-xs opacity-50 mb-4 hover:opacity-100" data-i18n="nav_hub">← Back to Hub</a>
      <a href="admin-dashboard.html" data-i18n="nav_admin_global">Global Dashboard</a>
      <a href="blockchain-monitor.html" data-i18n="nav_integrity">Integrity Monitor</a>
      <a href="audit-trail.html" data-i18n="nav_audit">Audit Trail</a>
      <a href="blockchain-ledger.html" data-i18n="nav_ledger">Blockchain Ledger</a>
    </nav>"""

def sync_file(filename, nav_content):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace nav block
    content = re.sub(r'<nav class="mt-4">.*?</nav>', nav_content, content, flags=re.DOTALL)
    
    # Set active class
    content = content.replace(f'href="{filename}"', f'href="{filename}" class="active"')
    
    # Remove redundant Matcha Capital H2 if exists below logo
    content = re.sub(r'<h2 class="[^"]*">Matcha Capital</h2>', '', content)
    
    # Ensure logo sizing and no double Matcha text
    content = re.sub(r'<div class="px-6 py-8 text-center border-b border-white/10">.*?</div>', 
                     f'<div class="px-6 py-8 text-center border-b border-white/10">\\n      <img src="shared/logo.png?v=3" alt="Matcha Capital" class="sidebar-logo mx-auto">\\n      <p class="text-[10px] text-teal-300 mt-1 uppercase tracking-widest opacity-70">{"INTERNAL" if filename in internal_files else "LENDER" if filename in lender_files else "ADMIN"} VIEW</p>\\n    </div>', 
                     content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Synced {filename}")

for f in internal_files: sync_file(f, internal_nav)
for f in lender_files: sync_file(f, lender_nav)
for f in admin_files: sync_file(f, admin_nav)
