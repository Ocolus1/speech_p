from app import app
from flask import render_template, request, send_file
import pyttsx3
import string
import random



@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        body = request.form["body"]
        lang = request.form["lang"]
        speed = request.form["speed"]
        v = request.form["voice"]
        try:
            def an(length):
                letters_and_digits = string.ascii_letters + string.digits
                result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
                return result_str

            name = str("audio" + an(8))

            def save(text):
                engine = pyttsx3.init()
                if speed == "2":
                    engine.setProperty('rate', 200)
                elif speed == "0":
                    engine.setProperty('rate', 150)
                elif speed == "1":
                    engine.setProperty('rate', 100)

                voices = engine.getProperty("voices")

                if v == "0":
                    engine.setProperty("voice", voices[0].id)
                elif v == "1":
                    engine.setProperty("voice", voices[1].id)

                engine.save_to_file(text , 'upload/{}.mp3'.format(name))
                engine.runAndWait()

            save(body)
            files = "./upload/" 
            file = name + ".mp3"
            path = files + file
            if path:
                return send_file(path , as_attachment=True)
        except Exception as e:
            return render_template("index.htm", e=e)
    return render_template("index.htm")


@app.route("/get", methods=["POST","GET"])
def get():
    if request.method == "POST":
        body = request.form["body"]
        lang = request.form["lang"]
        speed = request.form["speed"]
        v = request.form["voice"]
        try:
            
            def speak(audio):
                engine = pyttsx3.init()
                if speed == "2":
                    engine.setProperty('rate', 200)
                elif speed == "0":
                    engine.setProperty('rate', 150)
                elif speed == "1":
                    engine.setProperty('rate', 100)

                voices = engine.getProperty("voices")

                if v == "0":
                    engine.setProperty("voice", voices[0].id)
                elif v == "1":
                    engine.setProperty("voice", voices[1].id)

                engine.say(audio)
                engine.runAndWait()

            speak(body)
        except Exception as e:
            return render_template("index.htm", e=e)
    return render_template("index.htm", body=body)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.htm'), 404


@app.errorhandler(403)
def page_not_found(e):
    # note that we set the 403 status explicitly
    return render_template('403.htm'), 403


@app.errorhandler(410)
def page_not_found(e):
    # note that we set the 410 status explicitly
    return render_template('410.htm'), 410


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 500 status explicitly
    return render_template('500.htm'), 500
