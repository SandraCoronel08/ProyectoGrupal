from app import app
from app.controllers.users import *
from app.controllers.dealz import *

if __name__ == "__main__":
    app.run(debug=True)