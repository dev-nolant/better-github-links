from flask import Flask, request, redirect, render_template, g
import webbrowser, markdown.extensions.fenced_code
from werkzeug.urls import url_parse

app = Flask(__name__)

# HOME Default
@app.route('/')
def main():
    readme_file = open("files/README.md", "r")

    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return md_template_string


# MAIN Redirect Process
@app.route("/linkify")
def linkify():
    direct_link = request.args.get('link')
    if len(str(direct_link)) > 0:
        return render_template('redirect.html', direct_link = direct_link)
        
    else:
        return redirect('https://github.com/dev-nolant')


if __name__ == "__main__":
    app.run(debug=True)

# http://127.0.0.1:5000/linkify?myLink=https://github.com/dev-nolant/UCCS-Mimir-Help&gotoLink=https://choosealicense.com/licenses/mit/