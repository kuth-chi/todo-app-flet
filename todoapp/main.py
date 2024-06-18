
"""
This is the server file of main.py to run serve uvicorn server with FastAPI
"""
import flet as ft
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from module.todo import TodoApp


app = FastAPI()


@app.get("/")
async def read_root():
    """ Function to handle root"""
    return {"message": "Hello, this is Root page by default of FastAPI"}


# Create Todo App instance 
def main(page: ft.Page):
    """ Main page handle of application """
    page.title = "Todo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    todo_app = TodoApp()

    # add application's root control to the page
    page.add(todo_app)

flet_wsgi_app = ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

app.mount("/app", WSGIMiddleware(flet_wsgi_app))

# Handle Server run python main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
