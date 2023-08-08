#API that can run every 24 hours
import time

while True:
    import time
    import sqlite3
    from flask import Flask, render_template
    import pandas as pd
    import json
    import plotly
    import plotly.express as px

    conn = sqlite3.connect('athletes_database')

    df = pd.read_sql_query("SELECT * from medals", conn)

    app = Flask(__name__)

    @app.route('/')
    def index():
        return = render_template('index.html')

    @app.route('/chart1')
    def chart1():
        fig = px.bar(df1, x='country', y='num_medals', color='country',title='Top 5 Countries with highest number of medals')

    @app.route('/chart2')
    def chart2():
        #Number of athelets from top 30 countries
        df2 = pd.read_sql_query("SELECT country, COUNT(*) AS num_athletes FROM medals GROUP BY country ORDER BY num_athletes DESC LIMIT 30", conn)
        raphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('graphs.html', graphJSON=graphJSON)

    @app.route('/chart3')
    def chart3():

        fig = px.line(df3, x='discipline', y='avg_age',title='Average Age of athletes by discipline for female athletes')
        fig.update_layout(
            xaxis_title="Discipline",
            yaxis_title="Average Age",
            showlegend=True,
            #plot_bgcolor="Beige"  # Background color of the chart
        )
        fig.update_traces(textposition="top center")  # Position of data labels

    @app.route('/chart4')
    def chart4():

        fig = px.line(df4, x='discipline', y='avg_age',title='Average Age of athletes by discipline for Male athletes')
        fig.update_layout(
            xaxis_title="Discipline",
            yaxis_title="Average Age",
            showlegend=True,
            #plot_bgcolor="Beige"  # Background color of the chart
        )
        fig.update_traces(textposition="top center")  # Position of data labels

    @app.route('/chart5')
    def chart5():

        fig = px.scatter(df5, x="month", y="num_athletes", size="num_athletes", title="Bubble Chart")

    @app.route('/chart6')
    def chart6():

        fig = px.pie(df6, values="num_athletes", names="decade", title="Number of Athletes Born in Each Decade")

    if __name__ == "__main__":
        app.run()



    time.sleep(20) # 86400 Seconds mean 24 Hours of time
