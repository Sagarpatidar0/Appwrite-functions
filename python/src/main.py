from appwrite.client import Client
import os


def main(context):
    if context.req.method == "GET":
        return context.res.send("Hello, Python!")

    
    code = context.req.body
    if not code:
        return context.res.json({"status": "error", "error": "No code provided"})

    output = ""
    console_output = ""

    
    try:
        exec_globals = {}
        exec_locals = {}
        exec(code, exec_globals, exec_locals)
        context.log(exec_locals);
        output = exec_locals.get('output', '')
        console_output = exec_locals.get('console_output', '')
    except Exception as e:
        return context.res.json({"status": "error", "error": str(e), "consoleOutput": console_output})

    return context.res.json({"status": "success", "output": output, "consoleOutput": console_output})
