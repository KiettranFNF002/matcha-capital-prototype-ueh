(function() {
  // --- Initialization ---
  let currentLang = 'en'; // Force English only
  
  function updateUI() {
    if (!window.translations || !window.translations[currentLang]) return;
    const dict = window.translations[currentLang];
    
    // 1. Translate elements with data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const attrValue = el.getAttribute('data-i18n');
      
      // Support [attr]key syntax
      const match = attrValue.match(/^\[(.+?)\](.+)$/);
      
      if (match) {
        const attrName = match[1];
        const key = match[2];
        if (dict[key]) {
          el.setAttribute(attrName, dict[key]);
        }
      } else {
        if (dict[attrValue]) {
          el.innerHTML = dict[attrValue];
        }
      }
    });

    // 2. Legacy support for data-i18n-placeholder
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (key && dict[key]) {
        el.placeholder = dict[key];
      }
    });

    // 3. Update body class
    document.body.classList.remove('lang-vi', 'lang-en');
    document.body.classList.add('lang-' + currentLang);
  }

  // Run on load
  document.addEventListener('DOMContentLoaded', () => {
    if (!window.translations) {
      setTimeout(() => { if(window.translations) updateUI(); }, 100);
      return;
    }
    updateUI();
  });

  // Export minimal API
  window.matchai18n = { setLanguage: () => {}, currentLang: () => currentLang };

})();
