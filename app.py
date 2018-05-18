from flask import Flask, request
from sklearn.externals import joblib
import json
import jieba

app = Flask(__name__)
model_clone = joblib.load('./honestbee_department_clf.pkl')
jieba.set_dictionary('./dict.txt')
tags = json.load(open('tags.json'))


@app.route("/predict")
def predict():
    title = request.args.get('title')
    words = ' '.join([x for x in jieba.cut(title)])
    predicted_tag = model_clone.predict([words])[0]
    predicted_tag_name = tags[str(predicted_tag)]
    return predicted_tag_name
