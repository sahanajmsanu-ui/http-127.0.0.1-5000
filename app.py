from flask import Flask, render_template, request

app = Flask(__name__)

properties = [
    {
        "id": 1,
        "name": "Modern Villa",
        "location": "Bangalore",
        "price": "₹85 Lakh",
        "beds": 3,
        "baths": 2
    },
    {
        "id": 2,
        "name": "City Apartment",
        "location": "Mysore",
        "price": "₹55 Lakh",
        "beds": 2,
        "baths": 2
    },
    {
        "id": 3,
        "name": "Green Farmhouse",
        "location": "Coorg",
        "price": "₹1.2 Crore",
        "beds": 4,
        "baths": 3
    }
]


@app.route("/")
def home():
    search = request.args.get("search", "").lower()

    if search:
        result = [
            p for p in properties
            if search in p["name"].lower()
            or search in p["location"].lower()
        ]
    else:
        result = properties

    return render_template("index.html", properties=result)


@app.route("/property/<int:id>")
def property_details(id):
    property = next(
        (p for p in properties if p["id"] == id),
        None
    )

    return render_template(
        "details.html",
        p=property
    )


if __name__ == "__main__":
    app.run(debug=True)