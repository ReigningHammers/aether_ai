from fastapi import FastAPI
from .schemas.command import AetherCommand

app = FastAPI(title='Aether', version='0.1.0')

@app.post('/v1/command')
async def command(cmd: AetherCommand):
    return {'status': 'received', 'flow': 'Core → Memory → Router → Executor → Log', 'message': 'Aether is alive on Windows!'}

@app.get('/health')
def health():
    return {'status': 'Aether Core Online - Windows Ready'}