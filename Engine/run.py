from src import app
import asyncio


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)