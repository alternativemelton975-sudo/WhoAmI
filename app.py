@app.route("/heroes")
def heroes_page():

    output = """
    <html>
    <body style="
        background:#0d1117;
        color:white;
        font-family:Arial;
        text-align:center;
        padding:20px;
    ">

    <h1>⚔ Hero Registry ⚔</h1>

    <a href="/">Home</a>

    <hr>
    """

    if not characters:
        output += "<h3>No heroes created yet.</h3>"

    for character in characters.values():

        output += f"""
        <div style="
            background:#21262d;
            padding:15px;
            margin:15px auto;
            border-radius:12px;
            border:1px solid #444;
            max-width:700px;
        ">
            <h2>{character.name}</h2>

            <p>Power: {character.power}</p>

            <p>Level: {character.level}</p>

            <p>Total Power: {character.total_power()}</p>

        </div>
        """

    output += "</body></html>"

    return output


@app.route("/battle")
def battle():

    names = list(characters.keys())

    if len(names) < 2:

        return """
        <h1>Create at least two heroes first.</h1>
        <a href="/">Home</a>
        """

    char1 = characters[names[0]]
    char2 = characters[names[1]]

    power1 = char1.total_power()
    power2 = char2.total_power()

    winner = char1 if power1 >= power2 else char2

    return f"""
    <html>

    <body style="
        background:#020617;
        color:white;
        font-family:Arial;
        text-align:center;
        padding:20px;
    ">

    <h1>⚔ Battle Arena ⚔</h1>

    <h2>{char1.name} VS {char2.name}</h2>

    <p>{char1.name}: {power1}</p>

    <p>{char2.name}: {power2}</p>

    <h2 style="color:#22c55e;">
        Winner: {winner.name}
    </h2>

    <a href="/">Home</a>

    </body>

    </html>
    """


@app.route("/tournament")
def tournament():

    if len(characters) < 2:

        return """
        <html>
        <body style="
            background:#020617;
            color:white;
            text-align:center;
            font-family:Arial;
        ">
            <h1>Create at least two heroes first.</h1>
            <a href="/">Home</a>
        </body>
        </html>
        """

    contestants = [
        character.to_dict()
        for character in characters.values()
    ]

    random.shuffle(contestants)

    output = """
    <html>

    <body style="
        background:#020617;
        color:white;
        font-family:Arial;
        text-align:center;
        padding:20px;
    ">

    <h1 style="color:#38bdf8;">
        ⚔ HERO TOURNAMENT ⚔
    </h1>

    <a href="/" style="color:gold;">
        Home
    </a>

    <hr>
    """

    while len(contestants) > 1:

        hero1 = contestants.pop(0)
        hero2 = contestants.pop(0)

        winner = (
            hero1
            if hero1["total_power"] >= hero2["total_power"]
            else hero2
        )

        output += f"""
        <div style="
            background:#1e293b;
            color:#f8fafc;
            margin:15px auto;
            padding:15px;
            border-radius:12px;
            border:2px solid #38bdf8;
            box-shadow:0 0 10px #38bdf8;
            max-width:700px;
        ">

            <h3>
                {hero1['name']} VS {hero2['name']}
            </h3>

            <p>
                {hero1['name']} Power:
                {hero1['total_power']}
            </p>

            <p>
                {hero2['name']} Power:
                {hero2['total_power']}
            </p>

            <p>
                Winner:
                <span style="
                    color:#22c55e;
                    font-weight:bold;
                ">
                    {winner['name']}
                </span>
            </p>

        </div>
        """

        contestants.append(winner)

    champion = contestants[0]

    output += f"""
    <div style="
        background:#451a03;
        color:white;
        margin:25px auto;
        padding:25px;
        border-radius:15px;
        border:3px solid gold;
        max-width:700px;
    ">

        <h1 style="color:gold;">
            🏆 Tournament Champion 🏆
        </h1>

        <h2>{champion['name']}</h2>

        <p>Total Power: {champion['total_power']}</p>

    </div>

    </body>
    </html>
    """

    return output


@app.route("/logs")
def logs():

    try:

        with open("hero_logs.txt", "r") as file:

            return f"""
            <html>

            <body style="
                background:#000814;
                color:#7dd3fc;
                font-family:Consolas;
                padding:20px;
            ">

            <h1 style="color:gold;">
                📜 Hero Logs
            </h1>

            <pre>
{file.read()}
            </pre>

            <a href="/" style="color:gold;">
                Home
            </a>

            </body>

            </html>
            """

    except FileNotFoundError:

        return """
        <h1>No logs found.</h1>
        <a href="/">Home</a>
        """
