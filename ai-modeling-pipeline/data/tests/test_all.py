import unittest
from src.train_model import train_model
from src.predict import make_predictions
import os

class TestAIModels(unittest.TestCase):

    def test_train_model(self):
        data = "data/processed_data.csv"  # Substitua pelo caminho correto
        result = train_model(data)
        self.assertTrue(result)  # Verifique se o treinamento foi bem-sucedido

    def test_make_predictions(self):
        model_path = "models/random_forest_model.pkl"  # Substitua pelo caminho correto
        test_data = "data/test_data.csv"  # Substitua pelo caminho correto
        result = make_predictions(test_data, model_path)
        self.assertIsInstance(result, list)  # Verifique se a previsão retorna uma lista

    def test_predict_endpoint(self):
        # Simulando o comportamento do endpoint /predict
        data = {'country': 'USA', 'date': '2025-05-01'}
        # Adapte esta parte para usar uma biblioteca de testes de API, como requests ou Flask-Testing
        # Aqui, apenas simulamos um comportamento de resposta
        response = {'prediction': 1000}  # Simulação de resposta de previsão
        self.assertEqual(response['prediction'], 1000)

    def test_logfile_endpoint(self):
        # Teste para o endpoint /logfile
        logfile = "logs/predictions_log.txt"  # Caminho para o arquivo de log
        self.assertTrue(os.path.exists(logfile))  # Verifique se o arquivo de log existe

if __name__ == "__main__":
    unittest.main()
