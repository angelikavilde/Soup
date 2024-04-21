""""""


from flask import Flask, jsonify, request, send_from_directory, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/select_ingredients", methods=["GET"])
def selected_ingredients_page():
    """"""
    return render_template("select_ingredient.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/recipes", methods=["GET"])
def selected_ingredients_recipes():
    """"""
    ingredients = request.args.get("ingredients")

    if ingredients:
        ingredient_list = ingredients.split(",")
        recipes = ingredient_list #! here
        return render_template("recipes.html", recipes=recipes)

    else:
        # "No ingredients selected"
        pass


if __name__=="__main__":
    app.run(port = 5040, debug = True, host = "0.0.0.0")