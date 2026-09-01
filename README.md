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

## Personalización

1. Agregar imágenes reales en `image/`
2. Reemplazar placeholder de foto en `sections/05-about.html`
3. Actualizar testimonios en `sections/07-testimonios.html`
4. Colores: editar variables CSS en `css/style.css`
