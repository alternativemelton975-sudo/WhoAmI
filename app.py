from flask import Flask, request
import requests
import base64
import os

app = Flask(__name__)

HF_TOKEN = os.environ.get("HF_TOKEN", "")

API_URL = (
    "https://api-inference.huggingface.co/models/"
    "stabilityai/stable-diffusion-xl-base-1.0"
)

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


@app.route("/", methods=["GET", "POST"])
def home():

    image = ""

    if request.method == "POST":

        name = request.form.get("name")
        character_class = request.form.get("class")
        trait = request.form.get("trait")
        weapon = request.form.get("weapon")

        prompt = (
            f"{name}, "
            f"{trait} fantasy {character_class}, "
            f"holding a {weapon}, "
            f"highly detailed fantasy character, "
            f"character portrait, cinematic lighting, "
            f"epic fantasy art, masterpiece"
        )

        try:
            response = requests.post(
                API_URL,
                headers=HEADERS,
                json={"inputs": prompt},
                timeout=180
            )

            if response.status_code == 200:

                img_base64 = base64.b64encode(
                    response.content
                ).decode("utf-8")

                image = f"""
                <h2>{name}</h2>
                <img src="data:image/png;base64,{img_base64}"
                     style="max-width:600px;
                            width:100%;
                            border-radius:15px;">
                """

            else:
                image = (
                    f"<p>Generation failed. "
                    f"Status: {response.status_code}</p>"
                )

        except Exception as e:
            image = f"<p>Error: {str(e)}</p>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Character Creator</title>

        <style>

        body {{
            background:#111;
            color:white;
            font-family:Arial;
            text-align:center;
            padding:30px;
        }}

        .container {{
            max-width:900px;
            margin:auto;
            background:#222;
            padding:25px;
            border-radius:15px;
        }}

        input, select {{
            width:80%;
            padding:12px;
            margin:8px;
            border-radius:8px;
            border:none;
        }}

        button {{
            background:#ff3333;
            color:white;
            border:none;
            padding:12px 20px;
            border-radius:8px;
            cursor:pointer;
        }}

        button:hover {{
            background:#ff5555;
        }}

        img {{
            margin-top:20px;
        }}

        </style>
    </head>

    <body>

        <div class="container">

            <h1>AI Character Creator</h1>

            <form method="POST">

                <input
                    type="text"
                    name="name"
                    placeholder="Character Name"
                    required
                >

                <br>

                <select name="class">
                    <option>Warrior</option>
                    <option
