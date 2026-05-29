from flask import Flask, render_template, request, redirect

app = Flask(__name__)

inventory = [
    {   "id": 1,
        "name": "Green Sweater",
        "category": "Sweaters",
        "icon": "fa-shirt",
        "on_hand": 50,
        "counted": 50,
        "image": "/static/item1.jpg"},
    {
        "id": 2,
        "name": "Blue T-Shirt",
        "category": "T-Shirts",
        "icon": "fa-tshirt",
        "on_hand": 50,
        "counted": 55,
        "image": "/static/item2.jpg"},
        
    {"id": 3,
        "name": "White Casual Shirt",
        "category": "Shirts",
        "icon": "fa-shirt",
        "on_hand": 25,
        "counted": 26,
        "difference": 1,
        "image": "/static/item3.jpg"},
    {"id": 4, "name": "Pink Sweater", "on_hand": 50, "counted": 50,"image": "/static/item4.jpg"},
    {"id": 5, "name": "Jeans", "on_hand": 50, "counted": 50, "image": "/static/item5.jpg"},
    {"id": 6, "name": "Warm Winter Sweater", "on_hand": 12, "counted": 10,"image": "/static/item6.jpg"},
]

@app.route("/")
def home():
    profile = {"name": "Admin"}

    for item in inventory:
        item["difference"] = item["counted"] - item["on_hand"]

    return render_template("inventory.html", inventory=inventory, profile=profile)

@app.route("/update", methods=["POST"])
def update():
    for item in inventory:
        field_name = f"counted_{item['id']}"
        if field_name in request.form:
            item["counted"] = int(request.form[field_name])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)