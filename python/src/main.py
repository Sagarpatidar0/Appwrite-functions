from appwrite.client import Client
import os
import io
from contextlib import redirect_stdout


def main(context):
    if context.req.method == "GET":
        return context.res.send("Hello, Python!")

    
    code = context.req.body
    if not code:
        return context.res.json({"status": "error", "error": "No code provided"})

    out = ""

    
    try:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exec(func_str)

        out = stdout.getvalue()
    except Exception as e:
        return context.res.json({"status": "error", "error": out, "consoleOutput": out})

    return context.res.json({"status": "success", "output": out, "consoleOutput": out})
