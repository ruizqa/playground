from flask import Flask, render_template

app = Flask(__name__)   

@app.route('/play', defaults={'x':3, 'color':'#9fc5f8'})          
@app.route('/play/<int:x>', defaults = {'color': '#9fc5f8'})
@app.route('/play/<int:x>/<string:color>')
def show_boxes(x,color):
    return render_template("index.html",x=x, color=color)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.