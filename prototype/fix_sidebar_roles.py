import os
import re

# Master Sidebar Template (Dynamic Active Class handled below)
# We use classes to hide/show sections based on the body role class
SIDEBAR_BODY = """
    <div class="px-6 py-8 text-center border-b border-white/10">
      <img src="shared/logo.png?v=3" alt="Matcha Capital" class="sidebar-logo mx-auto">
      <div class="sidebar-section internal-only">
        <p class="text-[10px] text-teal-400 mt-1 uppercase tracking-widest opacity-70" data-i18n="role_internal">Internal View</p>
      </div>
      <div class="sidebar-section lender-only">
        <p class="text-[10px] text-emerald-300 mt-1 uppercase tracking-widest opacity-70" data-i18n="role_lender">Lender View</p>
      </div>
      <div class="sidebar-section admin-only">
        <p class="text-[10px] text-rose-300 mt-1 uppercase tracking-widest opacity-70" data-i18n="role_admin">Admin View</p>
      </div>
    </div>
    <nav class="mt-4 space-y-2 pb-12">
      <div class="px-6 mb-4">
        <a href="index.html" class="p-0 text-[10px] font-bold opacity-50 hover:opacity-100 transition-all uppercase tracking-widest" data-i18n="nav_hub">← Back to Hub</a>
      </div>
      
      <!-- Internal Section -->
      <div class="sidebar-section internal-only">
        <a href="dashboard.html" {active_dashboard} data-i18n="nav_dashboard">Dashboard</a>
        <a href="company-verify.html" {active_company_verify} data-i18n="nav_verify">Company Verify</a>
        <a href="create-room.html" {active_create_room} data-i18n="nav_initiate">Initiate Project</a>
        <a href="upload-docs.html" {active_upload_docs} data-i18n="nav_vault">Document Vault</a>
        <a href="distribution.html" {active_distribution} data-i18n="nav_distribution">Distribution</a>
        <a href="deal-pipeline.html" {active_deal_pipeline} data-i18n="nav_pipeline">Deal Pipeline</a>
        <a href="permission.html" {active_permission} data-i18n="nav_permission">Permissions</a>
      </div>

      <!-- Lender Section -->
      <div class="sidebar-section lender-only">
        <a href="deal-discovery.html" {active_deal_discovery} data-i18n="nav_marketplace">Marketplace</a>
        <a href="investor-profile.html" {active_investor_profile} data-i18n="nav_profile">Investor Profile</a>
        <a href="verification-center.html" {active_verification_center} data-i18n="nav_verification">Verification Center</a>
        <a href="deal-room.html" {active_deal_room} data-i18n="nav_vault">Deal Room</a>
        <a href="lender-view.html" {active_lender_view} data-i18n="nav_my_deals">My Deals</a>
        <a href="indicative-offer.html" {active_indicative_offer} data-i18n="nav_indicative">Indicative Offer</a>
      </div>

      <!-- Admin Section -->
      <div class="sidebar-section admin-only">
        <a href="admin-dashboard.html" {active_admin_dashboard} data-i18n="nav_admin_global">Admin Dashboard</a>
        <a href="blockchain-monitor.html" {active_blockchain_monitor} data-i18n="nav_integrity">Integrity Monitor</a>
        <a href="audit-trail.html" {active_audit_trail} data-i18n="nav_audit">Audit Trail</a>
        <a href="blockchain-ledger.html" {active_blockchain_ledger} data-i18n="nav_ledger">Blockchain Ledger</a>
      </div>
    </nav>
"""

def process_file(filepath):
    filename = os.path.basename(filepath)
    if not filename.endswith('.html') or filename == 'login.html' or filename == 'index.html':
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return

    sidebar_pattern = re.compile(r'<aside class="sidebar">.*?</aside>', re.DOTALL)
    
    active_map = {
        'dashboard.html': 'active_dashboard',
        'company-verify.html': 'active_company_verify',
        'create-room.html': 'active_create_room',
        'upload-docs.html': 'active_upload_docs',
        'distribution.html': 'active_distribution',
        'deal-pipeline.html': 'active_deal_pipeline',
        'permission.html': 'active_permission',
        'deal-discovery.html': 'active_deal_discovery',
        'investor-profile.html': 'active_investor_profile',
        'verification-center.html': 'active_verification_center',
        'deal-room.html': 'active_deal_room',
        'lender-view.html': 'active_lender_view',
        'indicative-offer.html': 'active_indicative_offer',
        'admin-dashboard.html': 'active_admin_dashboard',
        'blockchain-monitor.html': 'active_blockchain_monitor',
        'audit-trail.html': 'active_audit_trail',
        'blockchain-ledger.html': 'active_blockchain_ledger',
        'pricing.html': 'active_pricing_placeholder' # Pricing usually leads back to Marketplace
    }
    
    current_active_key = active_map.get(filename, '')
    
    ready_sidebar = SIDEBAR_BODY
    for key in active_map.values():
        if key == current_active_key:
            ready_sidebar = ready_sidebar.replace('{' + key + '}', 'class="active"')
        else:
            ready_sidebar = ready_sidebar.replace('{' + key + '}', '')

    if sidebar_pattern.search(content):
        content = sidebar_pattern.sub(f'<aside class="sidebar">{ready_sidebar}</aside>', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Restored role-based sidebar for {filename}")

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    process_file(f)
