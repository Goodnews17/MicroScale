from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    if request.method == "POST":

        try:
            image_size = float(request.form["image_size"])
            magnification = float(request.form["magnification"])
            unit = request.form["unit"]

            if image_size <= 0 or magnification <= 0:
                error = "Values must be greater than zero."

            else:
                # Formula:
                # Actual Size = Image Size / Magnification
                actual_size = image_size / magnification

                # Unit Conversion
                if unit == "um":
                    actual_size *= 1000
                    unit_label = "μm"

                elif unit == "nm":
                    actual_size *= 1000000
                    unit_label = "nm"

                else:
                    unit_label = "mm"

                result = f"{actual_size:.4f} {unit_label}"

        except:
            error = "Please enter valid numbers."

    return render_template(
        "index.html",
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
