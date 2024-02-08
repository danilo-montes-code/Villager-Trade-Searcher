from flask import Flask, request

###########################################
###                Setup                ###
###########################################

app = Flask(__name__)



###########################################
###                Routes               ###
###########################################

@app.route("/")
def hello_world():
    return "Hello, World!"







# ###########################################
# ###              Run Server             ###
# ###########################################

# if __name__=='__main__':
#     app.run(host="0.0.0.0", port=3000)