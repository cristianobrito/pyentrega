from flask import Flask, render_template, request
app = Flask(__name__,template_folder='./src/view')

@app.route('/',methods=['GET','POST'])
def home():
    if(request.method=='GET'): 
        return render_template('index.html')
    else:
        if(request.form['input1']!='' and request.form['input2']!=''):
            input1=request.form['input1']
            input2=request.form['input2']
            operadores=request.form['condicionais']
            #calculos
            soma=int(input1)+int(input2)
            sub=int(input1)-int(input2)
            mult=int(input1)*int(input2)
            div=int(input1)/int(input2)

            if(operadores=='soma'):
                return str(soma)
            elif(operadores=='subt'):
                return str(sub)
            elif(operadores=='multi'):
                return str(mult)
            else:
                return str(div)
        else:
            return '<h1> preencha os campos vazios</h1>'
app.run(port=3000, debug =True)    