# Guía de Identidad de Marca — Maselli Automotores

## Paleta de colores

| Color | Hex | Uso |
|-------|-----|-----|
| Azul Corporativo | #0A1628 | Fondo principal, headers |
| Gris Antracita | #2D3748 | Secciones alternas, cards |
| Plata Acero | #8C9BAB | Texto secundario, iconos |
| Dorado Acento | #C9A84C | CTAs, highlights, links activos |
| Blanco Puro | #FFFFFF | Texto principal |
| WhatsApp Verde | #15803d | Botón WhatsApp (contraste 4.5:1 con blanco) |

## Tipografía

- **Headings:** Montserrat (700, 800, 900)
- **Body:** Inter (400, 500)

## BEM Naming

```
 bloque__elemento--modificador
 .hero__title
 .servicio-card__icon
 .header__whatsapp
```

## Modo día/noche

- Dark: fondo azul corporativo, texto blanco
- Light: fondo blanco, texto negro
- Toggle con localStorage
- Variable `data-theme` en `<body>`

## Spacing

- Secciones: `padding: 5rem 2rem`
- Cards: `padding: 2rem`
- Gap grid: `2rem`
- Border radius: `12px` (cards), `25px` (botones), `50%` (iconos circulares)

## Breakpoints

- Desktop: > 768px (nav horizontal)
- Mobile: ≤ 768px (hamburger + drawer)

## Accesibilidad

- **Skip-link** visible al hacer Tab desde el inicio de la página
- **Focus visible** en todos los elementos interactivos
- **Contraste mínimo:** ratio 4.5:1 para texto normal (WCAG AA)
- **Landmarks:** `<header>`, `<nav>`, `<main>`, `<footer>`, `<aside>` (drawer)
- **SVGs decorativos** marcados con `aria-hidden="true"`
- **Drawer móvil:** `role="dialog"`, `aria-modal`, focus trap con Escape para cerrar
- **Hamburger:** `aria-expanded` + `aria-controls` vinculados al drawer
