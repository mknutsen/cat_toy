from flask import Flask, render_template, request
from gpiozero import LED

app = Flask(__name__)
led_r = LED(17)
led_l = LED(18)

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('left') == 'left':
            led_r.off()
            led_l.on()
        elif  request.form.get('right') == 'right':
            # pass # do something else
            led_r.on()
            led_l.off()

        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call??")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)