from flask import render_template, request
import json

def init_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            language = request.form.get("language")
            with open(f"app/translations/{language}.json", "r") as f:
                translations = json.load(f)
            income_source = request.form.get("income_source")
            income_amount = request.form.get("income_amount")
            expense_source = request.form.get("expense_source")
            expense_amount = request.form.get("expense_amount")
            remaining_amount = float(income_amount) - float(expense_amount)
            return render_template("index.html", translations=translations, income_source=income_source, income_amount=income_amount, expense_source=expense_source, expense_amount=expense_amount, remaining_amount=remaining_amount)
        else:
            with open("app/translations/en.json", "r") as f:
                translations = json.load(f)
            return render_template("index.html", translations=translations)