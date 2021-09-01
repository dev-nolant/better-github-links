from flask import Flask, request, redirect
import webbrowser, markdown.extensions.fenced_code

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
    github_link = request.args.get('myLink')
    direct_link = request.args.get('gotoLink')
    webbrowser.open_new_tab('{}'.format(direct_link))
    return redirect(github_link)


if __name__ == "__main__":
    app.run(debug=True)