# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# A simple HTML template with Bootstrap and a nav bar
def bootstrap_page(title: str, content: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <title>{title}</title>
        <!-- Bootstrap 5 CDN -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" 
              rel="stylesheet">
    </head>
    <body style="margin:0; padding:0;">
        <!-- NAVBAR -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">My Web App</a>
                <button class="navbar-toggler" type="button" 
                        data-bs-toggle="collapse" 
                        data-bs-target="#navbarSupportedContent" 
                        aria-controls="navbarSupportedContent" 
                        aria-expanded="false" 
                        aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link" href="/">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/data">Data</a>
                        </li>
                        <li class="nav-item">
                            <!-- Link to the Jupyter server -->
                            <a class="nav-link" href="http://localhost:8888" target="_blank">
                                Jupyter Notebook
                            </a>
                        </li>
                        <li class="nav-item">
                            <!-- Alternatively, an iframe version -->
                            <a class="nav-link" href="/jupyter_iframe">
                                Jupyter in Iframe
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- PAGE CONTENT -->
        <div class="container mt-4">
            {content}
        </div>

        <!-- Bootstrap 5 JS (needed for some nav functionality) -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
def home():
    page_content = """
    <h1 class="display-4">Welcome to the Home Page, Siobhan Barton</h1>
    <p class="lead">Use the nav bar above to explore the site. Hi This is an update</p>
    <hr/>
    <p>This is a sample FastAPI app with three pages and an embedded Jupyter notebook.</p>
    """
    return bootstrap_page("Home", page_content)

@app.get("/data", response_class=HTMLResponse)
def data():
    page_content = """
    <h1>Data Page</h1>
    <p>This is where you'd display or process data.</p>
    <hr/>
    <p>Maybe show some charts or data tables here in the future.</p>
    """
    return bootstrap_page("Data", page_content)

@app.get("/jupyter_iframe", response_class=HTMLResponse)
def jupyter_iframe():
    """
    Show the running Jupyter server in an iframe.
    This requires that you're running the Jupyter Notebook server
    at http://localhost:8888 in a separate terminal.
    """
    page_content = """
    <h1>Jupyter Notebook (Iframe) not working</h1>
    <p>
        If you prefer, you can open the notebook directly in a new tab:
        <a href="http://localhost:8888" target="_blank">http://localhost:8888</a>
    </p>
    <div class="ratio ratio-16x9" style="height: 800px;">
      <iframe src="http://localhost:8888" 
              style="border:1px solid #ccc; width:100%; height:100%;">
      </iframe>
    </div>
    """
    return bootstrap_page("Jupyter Iframe", page_content)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
