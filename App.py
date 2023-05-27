from flask import Flask
app=Flask(__name__)
@app.route("/")
def Hello_World():
    return "Hello Siddhant!"
if __name__=="__main__":
    print("I am inside the if now")
    app.run(debug=True)