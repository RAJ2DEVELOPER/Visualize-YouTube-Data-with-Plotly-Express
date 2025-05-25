from google.colab import files
import plotly.express as px

uploaded = files.upload()
import pandas as pd
import io

df = pd.read_csv(io.BytesIO(uploaded['most_subscribed_youtube_channels.csv']))
display(df)
import plotly.express as px

fig = px.pie(df, values='subscribers', names='category', title='YouTube Categories')
fig.show()

