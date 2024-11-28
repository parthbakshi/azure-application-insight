import os

from fastapi import FastAPI


app = FastAPI()


from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace
from opentelemetry.trace import (
    get_tracer_provider,
)
from opentelemetry.propagate import extract
from logging import getLogger, INFO

if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
    configure_azure_monitor()

tracer = trace.get_tracer(__name__,
                          tracer_provider=get_tracer_provider())

logger = getLogger(__name__)

app = FastAPI()

FastAPIInstrumentor.instrument_app(app)


@app.get("/")
async def root():
    return "todooo"

@app.post("/todo")
async def create_todo():
    return "create todo item"

@app.get("/todo/{id}")
async def read_todo(id: int):
    return "read todo item with id {id}"

@app.put("/todo/{id}")
async def update_todo(id: int):
    return "update todo item with id {id}"

@app.delete("/todo/{id}")
async def delete_todo(id: int):
    return "delete todo item with id {id}"

@app.get("/todo")
async def read_todo_list():
    return "read todo list"

