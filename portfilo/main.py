from flask import Flask,render_template,request,url_for
import csv

app=Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
     return render_template(page_name)

def write_to_File(data):
    with open("database.txt",newline='',mode="+a") as f:
        email=data['email']
        sub=data['subject']
        mess=data['message']
        result=f.write(f'\nEmail:{email} subject:{sub} Message:{mess}')
        return result
    
def write_to_csv(data):
    with open("database2.csv","+a") as f2:
        email=data['email']
        sub=data['subject']
        mess=data['message']
        result1=csv.writer(f2,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL )
        result1.writerow([email,sub,mess])

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return render_template("thankyou.html")
        except:
            return 'Something went wrong!.Please do correctly.'
    else:
        return 'Error'

if __name__=='__main__':
    app.run(debug=True)