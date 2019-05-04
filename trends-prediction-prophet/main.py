from matplotlib import pyplot as plt
import pandas as pd
from fbprophet import Prophet


def run_prophet(data: pd.DataFrame, periods: int) -> [Prophet, pd.DataFrame]:
    """
    Creates forecasting for time-series data for a specified period of time

    :param data: time-series data frame in with column 'y' for data and 'ds' for timestamps
    :param periods: future prediction timescale in days
    :return: Prophet model and forecasting data frame
    """
    m = Prophet(daily_seasonality=False, yearly_seasonality=False)
    m.fit(data)
    f = m.make_future_dataframe(periods=periods)
    return [m, m.predict(f)]


if __name__ == "__main__":
    plt.style.use('ggplot')

    # Load csv info data frame
    df = pd.read_csv('./data/nodejs_trends.csv')

    print(df.head())

    # Forecast data
    model, forecast = run_prophet(df, periods=365 * 10)

    # Plot predicted time-series data
    model.plot(forecast)
    # Save chart into PNG file
    plt.savefig('charts/nodejs_trends.png')
    # Show chart
    plt.show()
