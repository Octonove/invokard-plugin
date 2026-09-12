#!/usr/bin/env node
// Invokard — SessionStart hook.
// Injects the always-on rules (The Orchestrator and The Workflower) as
// additionalContext when the session starts. No dependencies, cross-platform.

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
    // If the file is missing we do not block the session: exit quietly.
    process.exit(0);
  }

  process.stdout.write(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'SessionStart',
      additionalContext: rules
    }
  }));
}

// The event arrives on stdin as JSON; we do not need to read it, but we drain
// it so the pipe is not left hanging on Windows.
process.stdin.resume();
process.stdin.on('data', () => {});
process.stdin.on('end', main);
process.stdin.on('error', main);
setTimeout(main, 1000).unref();
