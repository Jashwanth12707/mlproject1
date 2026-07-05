from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/predict_data', methods=['GET', 'POST'])
def predict_data():

    if request.method == "GET":
        return render_template("home.html")

    data = CustomData(
        gender=request.form.get("gender"),
        race_ethnicity=request.form.get("race_ethnicity"),
        parental_level_of_education=request.form.get("parental_level_of_education"),
        lunch=request.form.get("lunch"),
        test_preparation_course=request.form.get("test_preparation_course"),
        reading_score=float(request.form.get("reading_score")),
        writing_score=float(request.form.get("writing_score"))
    )

    pred_df = data.get_data_as_dataframe()

    predict_pipeline = PredictPipeline()

    results = predict_pipeline.predict(pred_df)

    return render_template("home.html", results=results[0])


if __name__ == "__main__":
    app.run(debug=True)