from flask import Flask, request
import requests
import base64
import os

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


@app.route("/", methods=["GET", "POST"])
def home():

    image_html = ""

    if request.method == "POST":

        name = request.form["name"]
        character_class = request.form["class"]
        trait = request.form["trait"]
        weapon = request.form["weapon"]

        prompt = (
            f"fantasy character named {name}, "
            f"{trait} {character_class}, "
            f"holding a {weapon}, "
            f"highly detailed fantasy art, "
            f"character portrait, cinematic lighting, "
            f"professional digital painting"
        )

        try:
            response = requests.post(
                API_URL,
                headers=headers,
                json={"inputs": prompt},
                timeout=120
            )

            if response.status_code == 200:

                image_base64 = base64.b64encode(
                    response.content
                ).decode("utf-8")

                image_html = f"""
                <h2>{name}</h2>
                <img
                    src="data:image/png;base64,{image_base64}"
                    width="512"
                    style="border-radius:15px;"
                >
                """

            else:
                image_html = f"""
                <p>
                    Image generation failed.
                    Status: {response.status_code}
                </p>
                """

        except Exception as e:
            image_html = f"<p>Error: {e}</p>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Character Creator</title>

        <style>

        body {{
            background:#111;
            color:white;
            text-align:center;
            font-family:Arial;
            padding:30px;
        }}

        .container {{
            max-width:800px;
            margin:auto;
            background:#222;
            padding:20px;
            border-radius:15px;
        }}

        input, select {{
            width:80%;
            padding:10px;
            margin:8px;
            border-radius:8px;
            border:none;
        }}

        button {{
            background:red;
            color:white;
            padding:12px 20px;
            border:none;
            border-radius:10px;
            cursor:pointer;
        }}

        img {{
            margin-top:20px;
            max-width:100%;
        }}

        </style>
    </head>

    <body>

        <div class="container">

            <h1>AI Character Creator</h1>

            <form method="post">

                <input
                    name="name"
                    placeholder="Character Name"
                    required
                >

                <br>

                <select name="class">
                    <option>Warrior</option>
                    <option>Mage</option>
                    <option>Ranger</option>
                    <option>Paladin</option>
                    <option>Assassin</option>
                </select>

                <br>

                <select name="trait">
                    <option>Brave</option>
                    <option>Wise</option>
                    <option>Mysterious</option>
                    <option>Loyal</option>
                    <option>Fearless</option>
                </select>

                <br>

                <select name="weapon">
                    <option>Sword</option>
                    <option>Bow</option>
                    <option>Staff</option>
                    <option>Dagger</option>
                    <option>Hammer</option>
                </select>

                <br><br>

                <button type="submit">
                    Generate Character
                </button>

            </form>

            {image_html}

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
