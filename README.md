# Invokard — plugin para Claude

Instala de una vez las **55 cartas** de Invokard, las **reglas permanentes** que hacen que
Claude enrute bien y no se disperse, y la **memoria persistente CRBRO** que recuerda de una
sesión a otra.

---

## Qué instala exactamente

**1. Las 55 cartas** (`skills/`)
Cada carta es un especialista: El Arquitecto, El Copywriter, El Analista de Datos, El
Políglota, El Manitas… Claude las carga solo cuando hacen falta, así que no te ocupan
contexto mientras no las uses.

- **9 cartas gratuitas** vienen con el texto completo dentro del plugin y funcionan sin
  cuenta ni conexión: `zero-protocol`, `zero-crbro`, `core-orchestrator`,
  `mkt-copywriter`, `strategy-business`, `data-analyst`, `dev-vibecoder`,
  `creator-aimedia`, `nexus-polymath`.
- **46 cartas de pago** están instaladas como lanzaderas: el fichero local no contiene el
  texto de la carta, solo la instrucción de pedírsela al servidor de Invokard. El texto
  llega en el momento y solo si tu cuenta la tiene desbloqueada.

**2. Las reglas permanentes** (`hooks/`)
Un hook `SessionStart` inyecta al arrancar cada sesión una versión condensada (menos de
2.500 caracteres) de **El Orquestador** —quién responde a qué y cómo firma— y de
**El Workflower** —detectar repetición y ofrecer automatizarla al final, nunca a mitad—.
No tienes que invocarlas: están puestas desde el primer mensaje.

**3. Dos servidores MCP** (`.mcp.json`)

| Servidor | Qué hace |
|---|---|
| `crbro` | Memoria persistente en disco (`npx -y crbro-memory`). Contexto al empezar, decisiones guardadas, consolidación al cerrar. |
| `invokard` | Entrega el texto de las cartas de pago y gestiona la sesión de tu cuenta (`npx -y invokard-mcp`). |

Ambos se arrancan solos al activar el plugin. Necesitas **Node.js** instalado (es lo que
provee `npx`).

---

## Cómo se instala, paso a paso, sin terminal

Desde Claude Desktop o Claude Code, escribiendo en el chat:

1. **Añade el marketplace.** Escribe:

   ```
   /plugin marketplace add Octonove/invokard-plugin
   ```

2. **Instala el plugin.** Escribe:

   ```
   /plugin install invokard@invokard
   ```

3. **Rellena tus datos si te los pide.** Al activarlo, Claude te preguntará por el email y
   la contraseña de tu cuenta de Invokard. Son **opcionales**: déjalos vacíos si solo vas a
   usar las 9 cartas gratuitas. La contraseña se guarda en el almacén seguro de Claude, no
   en un fichero de texto.

4. **Recarga.** Escribe:

   ```
   /reload-plugins
   ```

5. **Compruébalo.** Abre una conversación nueva y pídele algo, por ejemplo *"escríbeme el
   headline de mi landing"*. Debería contestarte firmando `▸ El Copywriter`.

Si prefieres el menú, `/plugin` abre el gestor y puedes hacer los pasos 1, 2 y 3 pinchando.

---

## Qué hace falta para las cartas de pago

Las 46 cartas restantes se sirven desde Invokard y requieren **cuenta con Pase activo** (o
esa carta comprada suelta) en <https://invokard.web.app>.

1. Crea tu cuenta en <https://invokard.web.app> con email y contraseña.
2. Activa el Pase o compra las cartas que quieras.
3. Conecta el plugin con tu cuenta, de una de estas dos formas:
   - **Al instalar:** rellena "Email de Invokard" y "Contraseña de Invokard" en el diálogo
     de configuración del plugin (paso 3 de arriba). Puedes volver a él cuando quieras
     desde `/plugin`.
   - **Desde el chat:** dile a Claude *"usa `invokard_login` con mi email y mi contraseña
     de Invokard"* y dáselos ahí.

A partir de ese momento, cuando invoques una carta de pago, Claude se la pide al servidor y
trabaja con ella. Si no tienes esa carta desbloqueada te lo dirá y te señalará el Pase; no
se inventará el contenido.

**Las 9 cartas gratuitas siguen funcionando siempre**, con cuenta o sin ella.

---

## Preguntas rápidas

**¿Se me va a llenar el contexto con 55 cartas?**
No. Claude solo tiene en contexto el nombre y una descripción corta de cada carta (unos
13 KB en total) y carga el texto completo únicamente de la que va a usar.

**¿Dónde está el texto de las cartas de pago?**
En el servidor de Invokard, nunca en tu disco. Por eso el fichero local es de unas pocas
líneas.

**¿Puedo usar solo la memoria y no las cartas?**
Sí: instala el plugin y usa CRBRO. Las cartas no molestan si no las llamas.

**¿Cómo lo desinstalo?**
`/plugin uninstall invokard@invokard`.

---

MIT · [Octonove](https://github.com/Octonove) · <https://invokard.web.app>
