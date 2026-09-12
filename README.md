# Maselli Automotores — Web Oficial

Página web de presentación para Maselli Automotores, agencia de compra y venta de vehículos usados en Salta Capital, Argentina.

## Estructura del proyecto

```
├── css/           # Estilos principales
├── js/            # JavaScript
├── sections/      # Secciones HTML separadas
├── image/         # Imágenes
├── build.py       # Script de build
├── vercel.json    # Configuración Vercel
└── estilos.md     # Guía de identidad de marca
```

## Desarrollo local

```bash
python3 build.py
```

Esto genera `index.html` desde las secciones de `sections/`.

## Deploy

1. Crear repo en GitHub
2. `git init && git add . && git commit -m "init"`
3. `git remote add origin <URL>`
4. `git push -u origin main`
5. Conectar repo en Vercel → deploy automático

## Accesibilidad (A11Y)

El sitio cumple con **WCAG 2.1 nivel AA**. Puntajes Lighthouse (desktop):

| Auditoría | Puntaje |
|-----------|---------|
| Accessibility | 100 |
| Best Practices | 100 |
| SEO | 83 |

### Features implementadas

- **Skip-link** (`Saltar al contenido`) para navegación por teclado
- **`<main>` landmark** envolviendo el contenido principal
- **`aria-expanded` / `aria-controls`** en el hamburger del menú móvil
- **`role="dialog"` + focus trap** en el drawer móvil (Escape para cerrar)
- **`aria-hidden="true"`** en SVGs decorativos (sol/luna del theme toggle)
- **`aria-label`** en estrellas de testimonios, links WhatsApp, y landmarks de nav
- **Contraste** botón WhatsApp: `#15803d` sobre `#ffffff` (ratio 4.5:1+)

## Personalización

1. Agregar imágenes reales en `image/`
2. Reemplazar placeholder de foto en `sections/05-about.html`
3. Actualizar testimonios en `sections/07-testimonios.html`
4. Colores: editar variables CSS en `css/style.css`

## Número de WhatsApp

El número está centralizado en **una sola ubicación**:

```js
// js/main.js, línea 5
const WHATSAPP_NUMBER = '5493875322496';
```

En `sections/*.html` los links usan `href="#"` con atributo `data-whatsapp`. Al cargar la página, `js/main.js` reemplaza automáticamente todos los `href` con `https://wa.me/{WHATSAPP_NUMBER}`.

**Para cambiar el número:** editar solo `js/main.js` y ejecutar `python3 build.py`.
