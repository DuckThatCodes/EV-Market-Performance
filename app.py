from flask import Flask, render_template

app = Flask(__name__)

TABLEAU_STORY_URL = (
    "https://public.tableau.com/views/EV_Market_Performance_Dashboard_17932037663110/Story1"
    "?:showVizHome=no&:embed=true"
)
TABLEAU_PUBLIC_URL = (
    "https://public.tableau.com/app/profile/tanish.jain5883/viz/"
    "EV_Market_Performance_Dashboard_17932037663110/Story1?publish=yes"
)

@app.route("/")
def home():
    return render_template(
        "index.html",
        tableau_story_url=TABLEAU_STORY_URL,
        tableau_public_url=TABLEAU_PUBLIC_URL,
    )

@app.route("/methodology")
def methodology():
    return render_template(
        "index.html",
        tableau_story_url=TABLEAU_STORY_URL,
        tableau_public_url=TABLEAU_PUBLIC_URL,
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
