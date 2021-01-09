from flask import Flask, redirect, request, render_template, Markup,send_file,url_for
from math import prod,floor

def gcd(a,b):
    if a<b:
        return gcd(b, a)

    if abs(b)<0.001:
        return a
    else:
        return gcd(b, a - floor(a/b)*b)


def lcm(l):
    l1=(l[0]*l[1])/gcd(l[0],l[1])
    for i in l[2:]:
        l1=(l1*i)/gcd(l1,i)
    return l1

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nav')
def nav():
    return render_template('nav.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/home1')
def home1():
    return redirect(url_for('home'))


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/default',methods=["POST"])
def default():
    return render_template("default.html")

@app.route('/default.html')
def default_htm():
    return render_template("default.html")

@app.route('/custom',methods=["POST"])
def custom():
    return render_template("custom.html")

@app.route('/custom.html')
def custom_htm():
    return render_template("custom.html")

@app.route('/default/chaturasram',methods=["POST"])
def chaturasram():
    return render_template("chaturasram.html")

@app.route('/default/trisram',methods=["POST"])
def trisram():
    return render_template("trisram.html")

@app.route('/default/khandam',methods=["POST"])
def khandam():
    return render_template("khandam.html")

@app.route('/default/misram',methods=["POST"])
def misram():
    return render_template("misram.html")

@app.route('/default/2t1c',methods=["POST"])
def t2c1():
    return render_template("2t1c.html")

@app.route('/custom/simple',methods=["POST"])
def simple_pt():
    return render_template("simple.html")

@app.route('/custom/complex',methods=["POST"])
def complex_pt():
    return render_template("complex.html")

@app.route('/default/chaturasram/patterns',methods=["POST"])
def default4_patterns():
    ta = float(request.form['num1'])
    j = float(request.form['num2'])
    c_l=[[] for i in range(4)]
    if(ta*4>=j):
        result="<b><h4>Chaturasram patterns with their Korvai(Mukthai) aksharas</b><h4><br><h6>Place the cursor on a paritcular pattern to get the detailed description about it.<br>Scroll down to view all results</h6><br>"
        for i in range(1,101):
            c1=(24/23)*((((ta*4)*i)+j)/4)
            c2=(24/13)*((((ta*4)*i)+j)/4)
            c3=(24/19)*((((ta*4)*i)+j)/4)
            c4=(((ta*4)*i)+j)/3
            if ((23*c1)/6-j)%ta==0 and c1-int(c1)==0:
                c_l[2].append(str(" 1 2 3 pattern: "+str(c1)))
            if ((13*c2)/6-j)%ta==0 and c2-int(c2)==0:
                c_l[1].append(" 1 1 1 pattern: "+str(c2))
            if ((19*c3)/6-j)%ta==0 and c3-int(c3)==0:
                c_l[3].append(" 1 1 3 pattern: "+str(c3))
            if c4-int(c4)==0 and c4>j:
                c_l[0].append(" 3 times chaturasram: "+str(c4))
    else:
        result="Jaga is exceeding the avruthaksharas!!!"
    if not any(c_l) and ta*4>=j:
        result="There is no possibility of making a Korvai(Mukthai) of these pattern.<br><br>Hint:You can check with any other default patterns or can check Custom patterns i.e pattern definied on your own!!!<br>Else there may be a possibility of making a Korvai(Mukthai) with progressive incremental pattern(i.e the uttarangam increases with each time of Korvai(Mukthai))!!<br>"
    else:
        result+="<br>"
        for i in range(4):
            if i==0:
                result+="<div class='gist' title=' This pattern is 3 times chaturasram(4) '>"+"<br>".join(c_l[i])+"</div>"
            elif i==1:
                result+="<br><div class='gist' title=' This pattern is 1 time chaturasram(4) 1 time trisram 2nd speed(6) 1 time chaturasram 2nd speed(8) '>"+"<br>".join(c_l[i])+"</div>"
            elif i==2:
                result+="<br><div class='gist' title=' This pattern is 1 time chaturasram(4) 2 times trisram 2nd speed(6) 3 times chaturasram 2nd speed(8) '>"+"<br>".join(c_l[i])+"</div>"
            else:
                result+="<br><div class='gist' title=' This pattern is 1 time chaturasram(4) 1 time trisram 2nd speed(6) 3 times chaturasram 2nd speed(8) '>"+"<br>".join(c_l[i])+"</div>"
    return render_template("result.html",result = Markup("<h4>"+result+"</h4>"))

@app.route('/default/trisram/patterns', methods=['POST'])
def default3_patterns():
    ta = float(request.form['num1'])
    j = float(request.form['num2'])
    t_l=[[] for i in range(3)]
    if(ta*4>=j):
        result="<h3><b>Trisram patterns with their Korvai(Mukthai) aksharas</h3></b><br><br><h6>Place the cursor on a paritcular pattern to get the detailed description about it.<br>Scroll down to view all results</h6><br>"
        for i in range(1,101):
            t1=(18*(ta*4*i+j)/4)/23
            t2=(18*(ta*4*i+j)/4)/13
            t3=(18*(ta*4*i+j)/4)/19
            if ((46*t1)/9-j)%ta==0 and t1-int(t1)==0:
                t_l[1].append(str(" 1 2 3 pattern:"+str(t1)))
            if ((26*t2)/9-j)%ta==0 and t2-int(t2)==0:
                t_l[0].append(" 1 1 1 pattern: "+str(t2))
            if ((38*t3)/9-j)%ta==0 and t3-int(t3)==0:
                t_l[2].append(" 1 1 3 pattern: "+str(t3))
    else:
        result="Jaga is exceeding the avruthaksharas!!!"
    if not any(t_l) and ta*4>=j:
        result="There is no possibility of making a Korvai(Mukthai) of these patterns.<br><br>Hint:You can check with any other default patterns or can check Custom patterns i.e pattern definied on your own!!!<br>Else there may be a possibility of making a Korvai(Mukthai) with progressive incremental pattern(i.e the uttarangam increases with each time of Korvai(Mukthai))!!<br>"
    else:
        result+="<br>"
        for i in range(3):
            if i==0:
                result+="<br><div class='gist' title=' This pattern is 1 time trisram(3) 1 time sankeernam slow speed(9 letters in 2 beats) 1 time trisram 2nd speed(6) '>"+"<br>".join(t_l[i])+"</div>"
            elif i==1:
                result+="<br><div class='gist' title=' This pattern is 1 time trisram(3) 2 times sankeernam slow speed(9 letters in 2 beats) 3 times trisram 2nd speed(6) '>"+"<br>".join(t_l[i])+"</div>"
            else:
                result+="<br><div class='gist' title=' This pattern is 1 time trisram(3) 1 time sankeernam slow speed(9 letters in 2 beats) 3 times trisram 2nd speed(6) '>"+"<br>".join(t_l[i])+"</div>"
    return render_template("result.html",result = Markup("<h4>"+result+"</h4>"))

@app.route('/default/khandam/patterns', methods=['POST'])
def default5_patterns():
    ta = float(request.form['num1'])
    j = float(request.form['num2'])
    k_l=[[] for i in range(3)]
    if(ta*4>=j):
        result="<h3><b>Khandam patterns with their Korvai(Mukthai) aksharas</b></h3><br><br><p>Place the cursor on a paritcular pattern to get the detailed description about it.<br>Scroll down to view all results</p><br>"
        for i in range(1,101):
            k1=(5*(ta*4*i+j)/4)/6
            k2=(ta*4*i+j)/4
            k3=(15*(ta*4*i+j)/4)/11
            if ((24*k1)/5-j)%ta==0 and k1-int(k1)==0 and k1%5==0:
                k_l[1].append(str(" 1 2 3 pattern:"+str(k1)))
            if ((4*k2)-j)%ta==0 and k2-int(k2)==0 and k2%5==0:
                k_l[2].append(" khandam 3 3 or 1 1 3 pattern: "+str(k2))
            if ((44*k3)/15-j)%ta==0 and k3-int(k3)==0 and k3%5==0:
                k_l[0].append(" 1 1 1 pattern: "+str(k3))
    else:
        result="Edupu(Jaga) is exceeding the avruthaksharas!!!"
    if not any(k_l) and ta*4>=j:
        result="There is no possibility of making a Korvai(Mukthai) of these pattern.<br><br>Hint:You can check with any other default patterns or can check Custom patterns i.e pattern definied on your own!!!<br>Else there may be a possibility of making a Korvai(Mukthai) with progressive incremental pattern(i.e the uttarangam increases with each time of Korvai(Mukthai))!!<br>"
    else:
        for i in range(3):
            if i==0:
                result+="<br><div class='gist' title=' This pattern is 1 time khandam slow speed(5 letters in 2 beats) 1 time khandam(5) 1 time khandatrisram(15 letters in 2 beats) '>"+"<br>".join(k_l[i])+"</div>"
            elif i==1:
                result+="<br><div class='gist' title=' This pattern is 1 time khandam slow speed(5 letters in 2 beats) 2 times khandam(5) 3 times khandatrisram(15 letters in 2 beats) '>"+"<br>".join(k_l[i])+"</div>"
            else:
                result+="<br><div class='gist' title=' This pattern is 1 time khandam slow speed(5 letters in 2 beats) 1 time khandam(5) 3 times khandatrisram(15 letters in 2 beats) or 3 times khandam(5) 3 times khandatrisram(15 letters in 2 beats) '>"+"<br>".join(k_l[i])+"</div>"
    return render_template("result.html",result = Markup("<h4>"+result+"</h4>"))

@app.route('/default/misram/patterns', methods=['POST'])
def default7_patterns():
    ta = float(request.form['num1'])
    j = float(request.form['num2'])
    m_l=[[] for i in range(3)]
    if(ta*4>=j):
        result="<h3><b>Misram patterns with their Korvai(Mukthai) aksharas</b></h3><br><br><h6>Place the cursor on a paritcular pattern to get the detailed description about it.<br>Scroll down to view all results</h6><br>"
        for i in range(1,101):
            m1=(7*(ta*4*i+j)/4)/6
            m2=(7*(ta*4*i+j)/4)/5
            m3=(21*(ta*4*i+j)/4)/11
            if ((24*m1)/7-j)%ta==0 and m1-int(m1)==0 and m1%7==0:
                m_l[1].append(str(" 1 2 3 pattern:"+str(m1)))
            if ((20*m2)/7-j)%ta==0 and m2-int(m2)==0 and m2%7==0:
                m_l[2].append(" misram 3 3 pattern or 1 1 3 pattern: "+str(m2))
            if ((44*m3)/21-j)%ta==0 and m3-int(m3)==0 and m3%7==0:
                m_l[0].append(" 1 1 1 pattern: "+str(m3))
    else:
        result="Edupu(Jaga) is exceeding the avruthaksharas!!!"
    if not any(m_l) and ta*4>=j:
        result="There is no possibility of making a Korvai(Mukthai) of these patterns.<br><br>Hint:You can check with any other default patterns or can check Custom patterns i.e pattern definied on your own!!!<br>Else there may be a possibility of making a Korvai(Mukthai) with progressive incremental pattern(i.e the uttarangam increases with each time of Korvai(Mukthai))!!<br>"
    else:
        for i in range(3):
            if i==0:
                result+="<br><div class='gist' title=' This pattern is 1 time misram slow speed(7 letters in 2 beats) 1 time misram(7) 1 time misratrisram(21 letters in 2 beats) '>"+"<br>".join(m_l[i])+"</div>"
            elif i==1:
                result+="<br><div class='gist' title=' This pattern is 1 time misram slow speed(7 letters in 2 beats) 2 times misram(7) 3 times misratrisram(21 letters in 2 beats) '>"+"<br>".join(m_l[i])+"</div>"
            else:
                result+="<br><div class='gist' title=' This pattern is 1 time misram slow speed(7 letters in 2 beats) 1 time misram(7) 3 times misratrisram(21 letters in 2 beats) or 3 times misram(7) 3 times misratrisram(21 letters in 2 beats) '>"+"<br>".join(m_l[i])+"</div>"
    return render_template("result.html",result = Markup("<h4>"+result+"</h4>"))

@app.route('/default/2t1c/patterns', methods=['POST'])
def default23_pattern():
    ta = float(request.form['num1'])
    j = float(request.form['num2'])
    tc_l=[[] for i in range(2)]
    if(ta*4>=j):
        result="<h3><b>2 times trisram 1 time chaturasram with their Korvai(Mukthai) aksharas</b></h3><br><br><h6>Place the cursor on a paritcular pattern to get the detailed description about it.<br>Scroll down to view all results</h6><br>"
        for i in range(1,101):
            tc1=(12*(ta*4*i+j)/4)/7
            tc2=(24*(ta*4*i+j)/4)/11
            if ((7*tc1)/3-j)%ta==0 and tc1-int(tc1)==0:
                tc_l[0].append("2 trisram(6) and 1 chaturasram : "+ str(tc1))
            if ((11*tc2)/6-j)%ta==0 and tc2-int(tc2)==0:
                tc_l[1].append("2 trisram(6) and 1 chaturasram(8) : "+ str(tc2))
    else:
        result="Edupu(Jaga) is exceeding the avruthaksharas!!!"
    if not any(tc_l) and ta*4>=j:
        result+="There is no possibility of making a Korvai(Mukthai) of these patterns.<br><br>Hint:You can check with any other default patterns or can check Custom patterns i.e pattern definied on your own!!!<br>Else there may be a possibility of making a Korvai(Mukthai) with progressive incremental pattern(i.e the uttarangam increases with each time of Korvai(Mukthai))!!<br>"
    else:
        for i in range(2):
            if i==0:
                result+="<br><div class='gist' title=' 2 times trisram 2nd speed(6) and 1 time chaturasram(4) '>"+"<br>".join(tc_l[i])+"</div>"
            else:
                result+="<br><div class='gist' title=' 2 times trisram 2nd speed(6) and 1 time chaturasram 2nd speed(8) '>"+"<br>".join(tc_l[i])+"</div>"
    return render_template("result.html",result = Markup("<h4>"+result+"</h4>"))

@app.route('/custom/simple/patterns',methods=['POST'])
def simple():
    p=str(request.form['pt'])
    ta = float(request.form['num1'])
    j = float(request.form['num2'])
    if(ta*4>=j):
        l=[float(k) for i in p.split('-') for k in i.split(',')]
        result="<h3><b>Custom pattern results</b></h3>"
        x,y=0,lcm(l)
        for m in range(len(l)):
            x=(x+(y/l[m]))
        g=gcd(x,y)
        x,y=x/g,y/g
        s_l=[]
        for i in range(200):
            p1=(y*(ta*4*i+j)/4)/x
            if ((4*x*p1/y)-j)%ta==0 and p1-int(p1)==0 and p1>10 and p1%lcm(l)==0:
                s_l.append("Korvai(Mukthai) aksharas for the above pattern:"+str(p1))
    else:
        result="Edupu(Jaga) is exceeding the avruthaksharas!!!"
    if len(s_l)==0 and ta*4>=j:
        result+= "There is no possibility of making a Korvai(Mukthai) of this pattern.You can check with another pattern."
    else:
        result+="<br>".join(s_l)
    return render_template("result.html",result = Markup("<h4>"+result+"</h4>"))

@app.route('/custom/complex/patterns',methods=['POST'])
def complex():
    p=str(request.form['pt'])
    ta = float(request.form['num1'])
    j = float(request.form['num2'])
    cmp_l=[]
    if ta*4>=j:
        a0=p.split('-')
        a1=[float(k.split('*')[0]) for i in a0 for k in i.split(',')]
        a2=[float(k.split('*')[1]) for i in a0 for k in i.split(',')]
        c_r=dict()
        result="<h3><b>Custom pattern results</b></h3>"
        x1,y1=0,0
        x2,y2=lcm(a1),lcm(a2)
        for i in range(len(a1)):
            x1,y1=(x1+(x2/a1[i])),(y1+(y2/a2[i]))
        gcd1,gcd2=gcd(x1,x2),gcd(y1,y2)
        x1,x2=x1/gcd1,x2/gcd1
        y1,y2=y1/gcd2,y2/gcd2
        for m in range(200):
            n=(ta*4*m+j)/4
            x=x2
            while x<4*int(n)+1:
                y=y2
                while y<2*x+1:
                    f1,f2=0,0
                    if (x*x1*y2)+(y*x2*y1)==(n*x2*y2) and x-y<=y:
                        if x%x2==0:
                            f1=1
                        if y%y2==0:
                            f2=1
                        if f1==1 and f2==1:
                            if x+y in c_r:
                                c_r[x+y].append((x,y))
                            else:
                                c_r[x+y]=[(x,y)]
                    y+=x2
                x+=y2
    else:
        result="Edupu(Jaga) is exceeding the avruthaksharas!!!"
    if len(c_r)==0 and ta*4>=j:
        result+= "There is no possibility of making a Korvai(Mukthai) of this pattern.You can check with another pattern."
    else:
        for k,v in c_r.items():
            cmp_l.append("Korvai(Mukthai) aksharas for purvangam and uttarangam: "+str(k)+" [ "+str(v)+" ] ")
        result+="<br>".join(cmp_l)
    return render_template("result.html",result = Markup("<h4>"+result+"</h4>"))


if __name__ == "__main__":
    app.debug = True
    app.run()
