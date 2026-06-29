from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "cientifica_key_secreta"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/reservar", methods=["POST"])
def reservar():
    if request.method == "POST":
        plato_elegido = request.form.get("platillo")
        print(f"--- PYTHON [RESERVAS]: El alumno reservó: {plato_elegido} ---")
        flash(f"¡Reserva confirmada con éxito! Reservaste: {plato_elegido}")
        return redirect(url_for("inicio"))

@app.route("/feedback", methods=["POST"])
def feedback():
    if request.method == "POST":
        puntuacion = request.form.get("puntuacion")
        comentario = request.form.get("comentario")
        print(f"--- PYTHON [FEEDBACK]: Calificación: {puntuacion} estrellas. Comentario: {comentario} ---")
        flash("¡Gracias por tu feedback! Tus comentarios nos ayudan a mejorar.")
        return redirect(url_for("inicio"))

@app.route("/encuesta", methods=["POST"])
def encuesta():
    if request.method == "POST":
        voto_plato = request.form.get("voto")
        print(f"--- PYTHON [ENCUESTA]: Voto registrado para el plato: {voto_plato} ---")
        flash(f"¡Voto registrado! Has votado por: {voto_plato}")
        return redirect(url_for("inicio"))

import os

if __name__ == '__main__':
    # Lee el puerto dinámico de Render o usa el 5000 por defecto de forma local
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)