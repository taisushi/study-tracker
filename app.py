from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 学習記録（メモリ上に保存）
study_records = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        subject = request.form.get("subject")
        hours = request.form.get("hours")

        if subject and hours:
            study_records.append({
                "subject": subject,
                "hours": int(hours)
            })

        return redirect(url_for("index"))

    total_hours = sum(record["hours"] for record in study_records)

    return render_template(
        "index.html",
        records=study_records,
        total_hours=total_hours
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)