# import
from elezioni import app

# config file
app.config.from_envvar('SETTINGS')

# app run
app.run(host=app.config['HOST'], port=app.config['PORTA']) 
