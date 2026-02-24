/* Shared navigation, theme toggle, and mobile menu */
(function () {
  function initTheme() {
    const stored = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const theme = stored || (prefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
    return theme;
  }

  function setThemeIcon(theme) {
    const icon = document.getElementById('theme-icon');
    if (!icon) return;
    icon.className = theme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    setThemeIcon(next);
  }

  document.addEventListener('DOMContentLoaded', function () {
    const theme = initTheme();
    setThemeIcon(theme);

    const toggleBtn = document.getElementById('btn-theme-toggle');
    if (toggleBtn) toggleBtn.addEventListener('click', toggleTheme);

    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');
    if (hamburger && navLinks) {
      hamburger.addEventListener('click', function () {
        navLinks.classList.toggle('open');
        const expanded = navLinks.classList.contains('open');
        hamburger.setAttribute('aria-expanded', expanded);
      });
    }
  });
})();
