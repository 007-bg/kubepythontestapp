# Random Quote Service (Python)

A minimal Python HTTP server that returns a random quote as JSON on a GET request to `/quote` (also works on `/`). Uses only the Python standard library (`http.server`).

## Run (Windows)

```powershell
# From the project root
cd c:\Projects\kubepythontestapp

# Start the server (Python 3)
python app.py
# or, if the Python launcher is available
py -3 app.py
```

Then visit:

- http://127.0.0.1:8000/quote

You should see a JSON response like:

```json
{
  "quote": "In the middle of difficulty lies opportunity.",
  "author": "Albert Einstein"
}
```

## Configuration

- Port: set `PORT` environment variable to change the port.
  - Example: `set PORT=8080` then run `python app.py`.

## Docker

```powershell
# Build the image (from project root)
docker build -t kubepythontestapp .

# Run the container, mapping host port 8000
docker run --rm -p 8000:8000 --name kubepythontestapp kubepythontestapp

# Optional: override port or host via env vars
docker run --rm -p 9000:9000 -e PORT=9000 -e HOST=0.0.0.0 kubepythontestapp
```

Then visit:

- http://localhost:8000/quote

### Notes

- The server binds to `0.0.0.0` by default inside the container for external access.
- No external dependencies; `requirements.txt` is present for future additions.

## Notes

- No external dependencies; easy to containerize or deploy.
- If you prefer a framework (Flask/FastAPI) for more routes, I can add that.
