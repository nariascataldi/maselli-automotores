/* =============================================
   MASELLI AUTOMOTORES - JavaScript Principal
   ============================================= */

const WHATSAPP_NUMBER = '5493875322496';

// --- Centralizar WhatsApp ---
document.querySelectorAll('[data-whatsapp]').forEach(link => {
  link.href = `https://wa.me/${WHATSAPP_NUMBER}`;
});

// --- Theme Toggle (Day/Night) ---
const themeToggle = document.querySelectorAll('.theme-toggle');
const savedTheme = localStorage.getItem('theme') || 'dark';

function updateThemeColor(theme) {
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta) meta.content = theme === 'dark' ? '#0A1628' : '#ffffff';
}

document.body.setAttribute('data-theme', savedTheme);
updateThemeColor(savedTheme);

function toggleTheme() {
  const current = document.body.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.body.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  updateThemeColor(next);
}

themeToggle.forEach(btn => {
  btn.addEventListener('click', toggleTheme);
});

// --- Intro / Preloader (hide immediately, no delay) ---
const intro = document.querySelector('.intro');
if (intro) {
  intro.classList.add('hidden');
}

// --- Mobile Drawer ---
const hamburger = document.querySelector('.hamburger');
const drawer = document.querySelector('.mobile-drawer');
const drawerClose = document.querySelector('.mobile-drawer__close');
const drawerLinks = document.querySelectorAll('.mobile-drawer__links a');

function openDrawer() {
  drawer.classList.add('open');
  hamburger.setAttribute('aria-expanded', 'true');
  document.body.style.overflow = 'hidden';
  drawerClose?.focus();
}

function closeDrawer() {
  drawer.classList.remove('open');
  hamburger.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
  hamburger.focus();
}

if (hamburger && drawer) {
  hamburger.addEventListener('click', () => {
    if (drawer.classList.contains('open')) {
      closeDrawer();
    } else {
      openDrawer();
    }
  });

  drawerClose?.addEventListener('click', closeDrawer);

  drawerLinks.forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  drawer.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeDrawer();
      return;
    }
    if (e.key !== 'Tab') return;
    const focusable = drawer.querySelectorAll('button, a[href], [tabindex]:not([tabindex="-1"])');
    if (focusable.length === 0) return;
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  });
}

// --- Header scroll effect (throttled with rAF) ---
const header = document.querySelector('.header');
if (header) {
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        header.style.background = window.scrollY > 50
          ? 'var(--color-header-bg-scroll)'
          : 'var(--color-header-bg)';
        ticking = false;
      });
      ticking = true;
    }
  });
}

// --- Smooth scroll para links internos ---
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    try {
      const href = this.getAttribute('href');
      if (!href || href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    } catch (err) {
      // Invalid selector — ignore
    }
  });
});
