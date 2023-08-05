# Stock Price Prediction App with FastAPI, MongoDB, and LSTM

This is a simple web application built with FastAPI that uses MongoDB for data storage and LSTM (Long Short-Term Memory) for stock price prediction. The app predicts the price of Apple stock based on the last two recorded values.

## Requirements

- Python 3.11
- FastAPI
- pymongo
- keras (TensorFlow backend)
- numpy

## Installation

1. Clone this repository:

```
git clone https://github.com/your-username/fastapi-mongodb-lstm.git
cd fastapi-mongodb-lstm
```

2. Install the required packages:

```
pip install fastapi pymongo keras numpy uvicorn
```

## Usage

1. Start MongoDB:

Ensure that your MongoDB server is running on the default port (27017) or update the connection settings in `app.py` accordingly.

2. Run the FastAPI app:

```
uvicorn app:app --reload
```

3. Make predictions:

- Open your web browser and go to http://localhost:8000/docs.
- Use the provided Swagger UI to make a POST request to the `/predict/` endpoint. Provide the last two recorded values of the Apple stock as input, and the app will return the predicted price.

## Project Structure

The repository includes the following files:

- `app.py`: The main FastAPI app, which handles the prediction endpoint.
- `prediction.py`: Contains the LSTM model to predict stock prices based on historical data.
- `database.py`: Contains the database connection setup and data storage functions using MongoDB.
- `requirements.txt`: Lists the required packages for the app.
- `README.md`: This file, providing information about the app and its usage.

## Note

This app is for educational and demonstration purposes only. The stock price predictions are based on simple LSTM models and may not be accurate for real-world trading decisions. Always exercise caution and consult financial experts before making any investment decisions based on the predictions.

## Acknowledgments

The LSTM model used for stock price prediction is inspired by various online tutorials and resources, including [TensorFlow documentation](https://www.tensorflow.org/guide/keras/rnn) and [Kaggle notebooks](https://www.kaggle.com/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
