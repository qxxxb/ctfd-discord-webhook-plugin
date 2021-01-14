from os import environ


def config(app):
    """
    Discord webhook URL to send data to. Set to None to disable plugin
    entirely.
    """
    app.config['DISCORD_WEBHOOK_URL'] = environ.get('DISCORD_WEBHOOK_URL')

    """
    Limit on number of solves for challenge to trigger webhook for. Set to None
    to send a message for every solve.
    """
    app.config["DISCORD_WEBHOOK_FIRST_SOLVES"] = environ.get("DISCORD_WEBHOOK_FIRST_SOLVES", "5")

    """
    Webhook message format string. Valid vars: user, solves, fsolves (formatted
    solves), challenge, category, points
    """
    app.config["DISCORD_WEBHOOK_MESSAGE"] = environ.get(
        "DISCORD_WEBHOOK_MESSAGE",
        "Congratulations to **{user}** for the **{fsolves}** solve on challenge **{challenge}** ({points} points)!",
    )
