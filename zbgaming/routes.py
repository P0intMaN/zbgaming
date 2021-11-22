from zbgaming import app

@app.route('/')
def home():
    return "<h1> This is the beginning of something <strong> BIG </strong> </h1>"

