#!/usr/bin/env node
// Invokard — hook SessionStart.
// Inyecta las reglas permanentes (El Orquestador y El Workflower) como
// additionalContext al arrancar la sesion. Sin dependencias, multiplataforma.

const fs = require('fs');
const path = require('path');

let done = false;

function main() {
  if (done) return;
  done = true;
  const file = path.join(__dirname, 'invokard-rules.txt');
  let rules;
  try {
    rules = fs.readFileSync(file, 'utf8').trim();
  } catch (err) {
    // Si el fichero no esta, no bloqueamos la sesion: salimos en silencio.
    process.exit(0);
  }

  process.stdout.write(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'SessionStart',
      additionalContext: rules
    }
  }));
}

// El evento llega por stdin como JSON; no necesitamos leerlo, pero lo drenamos
// para no dejar la tuberia colgada en Windows.
process.stdin.resume();
process.stdin.on('data', () => {});
process.stdin.on('end', main);
process.stdin.on('error', main);
setTimeout(main, 1000).unref();
