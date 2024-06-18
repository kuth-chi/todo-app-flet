# Todo Application
This is a simple todo application build from Flet this project has no Database to store yet.


### How to test this project
Before you can test this project, you need to install:
1. Python3 (https://www.python.org/downloads/)
2. Flutter SDK (https://flutter.dev/docs/get-started/install)


### How to run this project

```bash
git clone https://github.com/kuth-chi/todo-app-flet.git
```

1. Open your terminal and change directory to `todo-app-flet`
   ```bash
   cd todo-app-flet
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app
   ```bash
   flet run todo.py
   ```

dist folder is created for web and you can run as web app below.

### How to run web in dist
1. On terminal, 
   ```bash
   python -m http.server --directory dist
   ```

2. Visit http://127.0.0.1:8000 in your browser.

If you have any issues, please open an issue on GitHub: https://github.com/kuth-chi/todo-app-flet/issues
