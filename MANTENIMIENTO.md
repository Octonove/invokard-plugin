# Mantenimiento

Qué hay que tocar cuando cambia algo. Escrito porque las piezas están en
cuatro sitios y la que se olvida siempre es la última.

## Cuando sale la carta nueva del mes

1. **synthetica-decks**: `skills/<slug>.md` en castellano y sus cuatro
   traducciones en `skills/{en,fr,de,it}/`, más la entrada en
   `data/catalog.json`.
2. **Firestore**: el documento `skills/<slug>` con `prompt_es`, `prompt_en`,
   `prompt_fr`, `prompt_de`, `prompt_it`. Es de donde el conector sirve el
   texto, así que sin esto la carta no se abre aunque exista en todo lo demás.
3. **Este repo**: una carpeta nueva en `skills/<slug>/SKILL.md`. Si la carta
   es de pago, copia una lanzadera existente y cambia el slug y la
   descripción; **no pegues nunca el texto de una carta de pago aquí**, este
   repositorio es público.
4. **La Bóveda** (`invokard-comic`): copia `data/catalog.json` desde
   synthetica-decks y despliega. El conector lee ese fichero para saber qué
   cartas existen, y si se queda viejo la carta nueva no aparece en la lista
   aunque se pueda abrir por su nombre.

Sin el paso 4 no se rompe nada: el conector cae a la copia que lleva
empaquetada y sigue funcionando. Solo se ve desactualizada la lista.

## Cuando cambia el texto de una carta

Firestore manda. Actualiza el documento `skills/<slug>` y ya está: el
conector sirve siempre lo que hay ahí, no una copia. Las nueve gratuitas son
la excepción, porque su texto vive dentro de este repositorio: hay que
actualizarlo aquí también.

## Cuando se publica versión de CRBRO

Nada que hacer aquí. `.mcp.json` llama a `npx -y crbro-memory`, que siempre
sirve la última. El fichero `.mcpb` de Claude Desktop sí hay que regenerarlo
en cada versión, pero eso vive en el repositorio de CRBRO.

## Cuando cambia el conector

`invokard-mcp` se publica en npm y `.mcp.json` lo llama con `npx -y`, así que
los clientes reciben la versión nueva sin tocar nada. Solo hay que publicar.
