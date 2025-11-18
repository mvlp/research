from flask import Flask
from sqlalchemy import text
from Backend.src.infra.controller.Governanca_controller import Governanca_controller
from Backend.src.infra.controller.Indice_controller import Indice_controller
from Backend.src.infra.controller.Indice_grupo_controller import Indice_grupo_controller
from Backend.src.infra.controller.Pergunta_controller import Pergunta_controller
from Backend.src.infra.controller.Pergunta_indice_controller import Pergunta_indice_controller
from src.infra.Database.extensions import db
from src.infra.Database.Models.Governanca import Governanca
from src.infra.Database.Models.Indice import Indice
from src.infra.Database.Models.indice_grupo import Indice_grupo
from src.infra.Database.Models.pergunta import Pergunta
from src.infra.Database.Models.pergunta_indice import Pergunta_indice

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://guilhermedesouzafornaciari:Ga05112002@localhost:5432/research"
db.init_app(app)

controllers = []
controllers.append(Governanca_controller())
controllers.append(Indice_grupo_controller())
controllers.append(Indice_controller())
controllers.append(Pergunta_indice_controller())
controllers.append(Pergunta_controller())

for controller in controllers:
    app.register_blueprint(controller.blueprint)

print(app.url_map)

if __name__ == '__main__':
    with app.app_context():
      db.create_all()
      print("Database is reachable and tables can be created.")
      try:
          db.session.execute(text('SELECT 1'))
          print("Database connection successful!")
      except Exception as e:
          print("Database connection failed:", e)
    app.run(debug=True)
