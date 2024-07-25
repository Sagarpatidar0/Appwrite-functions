import { VM } from 'vm2';

export default async ({ req, res,log }) => {
  if (req.method === 'GET') {
    return res.send('Hello, node!');
  }

  const code  = req.body;
  log(req.body)
  log(code)
  if (req.body === "") {
    return res.json({ status: 'error', error: 'No code provided' });
  }

  let output = '';
  let consoleOutput = '';

  const vm = new VM({
    sandbox: {
      console: {
        log: (...args) => {
          consoleOutput += args.join(' ') + '\n';
        },
        error: (...args) => {
          consoleOutput += args.join(' ') + '\n';
        }
      }
    }
  });

  try {
    output = vm.run(code);
  } catch (err) {
    return res.json({ status: 'error', error: err.message, consoleOutput });
  }

  return res.json({ status: 'success', output, consoleOutput });
};
