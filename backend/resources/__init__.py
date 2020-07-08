from flask_restful import Resource, reqparse
from classifier.classifier.logistic_regression_classifier import LogisticRegressionClassifier


class MovieReviewPredict(Resource):

    attr = reqparse.RequestParser()
    attr.add_argument('review', type=str, required=True, help='Users Review')

    def post(self):
        data = self.attr.parse_args()

        classification = LogisticRegressionClassifier().load(
            regressor_path='models/sklearn-logistc-regressor-model.joblib',
            vectorizer_path='models/vectorizer.pickle'
        ).predict(data['review'])

        return {
            'msg': 'Sucess',
            'classification': classification
        }
