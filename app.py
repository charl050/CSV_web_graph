from flask import Flask, Markup, render_template
from read_data import total_death, valid_dates

app = Flask(__name__)
labels = valid_dates("data.csv")
values = []

for i in labels:
        try:
            values.append(total_death("data.csv",i))
        except:
            pass


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('index.html', title='Covid-19 Total Deaths', max=(max(values)*1.1), labels=bar_labels, values=bar_values)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
