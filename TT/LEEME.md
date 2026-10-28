# LATTICCE TT · Trayectoria Trazada (respaldo)

Corte: 28 de octubre de 2026. Uso interno: trae información de clientes y prospectos, no publicar abierto.

- `tt.html`: versión independiente. Se abre con doble clic en cualquier navegador, sin internet ni Claude. Datos, logos y gráficas van dentro. Instagram de Design es un corte fijo (en el tablero de Claude es en vivo).
- Tablero en vivo (claude.ai): https://claude.ai/artifact/5JPkHDbctqsuNSDufvQrMZ
- `fuente/`: lo necesario para regenerar.
  - `build_data.py`: genera los JSON junto a sí mismo (copia de referencia en `datos/`; lee también `../dash/hitos.json`, los hitos del reporte 2026) (frentes, hitos, etapas, capacidad, nodos, redes, rumbo, Book, blog, madurez).
  - `index.src.html`: la página; `index.html` es la misma con el logotipo insertado (`wordmark.txt`).
  - `logos.js`: sellos y logos oficiales de los 6 nodos (desde Documents/LOGO).
  - `standalone.py`: arma `tt.html` (uso: `python3 standalone.py d3.v7.9.0.min.js '<respuesta de Metricool>'`, con los JSON junto al script).

Siguiente paso propuesto: subir esta carpeta a un repositorio privado de GitHub y, cuando exista el portal, publicarla en UROBOROS con acceso controlado.
