from flask import Flask,render_template,url_for,redirect,flash,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from form import LoginForm, Wellsform, Wellboreform, Wellborecoreform,Categoryform
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from flask_bcrypt import Bcrypt
import pymysql



app = Flask(__name__)
app.config['SECRET_KEY'] ='kalenzo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://edward:edward1234@localhost/database2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =SQLAlchemy(app)
bcrypt =Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key =True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role     = db.Column(db.String(15))

    def __repr__(self):
        return '<User %r>' % self.password

class Wellbore(db.Model):
    wellboreid = db.Column(db.Integer,primary_key =True)
    wellboreofficialname = db.Column(db.String(150), nullable=False)
    wellborelocalname = db.Column(db.String(100), nullable=False)
    wellborealiasname = db.Column(db.String(100), nullable=False)
    spudyear= db.Column(db.String(100), nullable=False)
    wellboretypeid= db.Column(db.Float, nullable=False)
    initialwellborepurposeid= db.Column(db.Float,nullable=False)
    
    wellborespuddate= db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Wellbore %r>' % self.wellboreofficialname

class Wells(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    sampletype = db.Column(db.String(150), nullable=False)
    wellname = db.Column(db.String(100), nullable=False)
    layer = db.Column(db.String(150), nullable=False)
    initialdepth = db.Column(db.Float, nullable=False)
    terminationdepth = db.Column(db.Float, nullable=False)
    samplebucket= db.Column(db.String(100), nullable=False)
    uploaddate = db.Column(db.DateTime,default =datetime.now())

    def __repr__(self):
        return '<Wells %r>' % self.sampletype

class Wellborecore(db.Model):
    wellborecoreid = db.Column(db.Integer,primary_key =True)
    corenumber= db.Column(db.Float, nullable=False)
    coredate= db.Column(db.String(100), nullable=False)
    wellborename = db.Column(db.String(200), nullable=False)
    coringcontractor = db.Column(db.String(200), nullable=False)
    coretopmdrt= db.Column(db.Float, nullable=False)
    corebottommdrt= db.Column(db.Float, nullable=False)
    coretoptvd= db.Column(db.Float, nullable=False)
    corebottomtvd= db.Column(db.Float, nullable=False)
    cutlength= db.Column(db.Float, nullable=False)
    cutlengthtvd= db.Column(db.Float, nullable=True)
    recoveredlength= db.Column(db.Float, nullable=True)
    corerecovery= db.Column(db.Float, nullable=True)
    topformation= db.Column(db.String(200), nullable=False)
    bottomformation = db.Column(db.String(100), nullable=True)
    wellborecorename = db.Column(db.String(100), nullable=True)
    corepicturesoftcopypath = db.Column(db.String(100), nullable=True)
    corepicturehyperlink= db.Column(db.String(200), nullable=True)
    corereportsoftcopypath= db.Column(db.String(100), nullable=True)
    corereporthyperlink= db.Column(db.String(200), nullable=True)
    documentformat = db.Column(db.String(100), nullable=True)
    filesize= db.Column(db.String(20), nullable=True)
    securitygrade = db.Column(db.String(100), nullable=True)
    openduedate= db.Column(db.String(20), nullable=True)
    comments= db.Column(db.String(100), nullable=True)
    documenttitle= db.Column(db.String(200), nullable=True)
    receivedate= db.Column(db.String(100), nullable=True)
    documentdate= db.Column(db.String(100), nullable=True)
    documentname= db.Column(db.String(200), nullable=True)
    cored= db.Column(db.String(100), nullable=True)
    
    createdby = db.Column(db.String(100), nullable=True)
    datecreated= db.Column(db.String(20), nullable=True)
    modifiedon = db.Column(db.String(100), nullable=True)
    modifiedby= db.Column(db.String(200), nullable=True)
    pictureuploaddate= db.Column(db.String(100), nullable=True)
    reportuploaddate= db.Column(db.String(200), nullable=True)
    recorddate = db.Column(db.DateTime,default =datetime.now())

    def __repr__(self):
        return '<Wellborecore%r>' % self.corenumber

class Category(db.Model):
    corecatalogid = db.Column(db.Integer,primary_key =True)
    wasanalysed= db.Column(db.String(50), nullable=True)
    coretype= db.Column(db.String(100), nullable=False)
    storeidentifier = db.Column(db.String(100), nullable=False)
    catalogcorefromdepth= db.Column(db.Float, nullable=False)
    catalogcoretodepth= db.Column(db.Float, nullable=False)
    coresecurityflag= db.Column(db.String(200), nullable=False)
    catalogcorelength= db.Column(db.Float, nullable=True)
    hascorephotos= db.Column(db.String(20), nullable=True)
    wellborecorename = db.Column(db.String(100), nullable=True)
    topcoreformation= db.Column(db.String(20), nullable=True)
    bottomcoreformation = db.Column(db.String(100), nullable=True)
    cataloguepicturename= db.Column(db.String(20), nullable=True)
    cataloguepicturesoftcopypath = db.Column(db.String(100), nullable=True)
    cataloguepicturehyperlink= db.Column(db.String(200), nullable=True)
    cataloguereportsoftcopypath= db.Column(db.String(100), nullable=True)
    cataloguereporthyperlink= db.Column(db.String(200), nullable=True)
    documentformat = db.Column(db.String(100), nullable=True)
    filesize= db.Column(db.String(20), nullable=True)
    securitygrade = db.Column(db.String(100), nullable=True)
    openduedate= db.Column(db.String(20), nullable=True)
    comments= db.Column(db.String(100), nullable=True)
    corecatalogname= db.Column(db.String(200), nullable=True)
    welloperator= db.Column(db.String(100), nullable=True)
    wellbore= db.Column(db.String(200), nullable=True)
    spuddate= db.Column(db.String(100), nullable=True)
    corename= db.Column(db.String(200), nullable=True)
    coredate= db.Column(db.String(100), nullable=True)
    comment= db.Column(db.String(200), nullable=True)
    createdby = db.Column(db.String(100), nullable=True)
    datecreated= db.Column(db.String(20), nullable=True)
    modifiedon = db.Column(db.String(100), nullable=True)
    modifiedby= db.Column(db.String(200), nullable=True)
    pictureuploaddate= db.Column(db.String(100), nullable=True)
    reportuploaddate= db.Column(db.String(200), nullable=True)
    recorddate = db.Column(db.DateTime,default =datetime.now())

    def __repr__(self):
        return '<Category %r>' % self.storeidentifier

@app.route('/dashbord',)
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/',methods =['GET'])
def signin():
    form = LoginForm()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()
    if request.method == 'POST' :
            user= User.query.filter_by(email=form.email.data).first()
            if user:
                if bcrypt.check_password_hash(user.password,form.password.data) :
                    login_user(user)
                    flash('You are Welcome','success')
                    return redirect(url_for('dashboard'))

                else:
                    flash('login Unsuccessful','danger')
                    return redirect(url_for('signin'))

            else:
                 flash('invalid credentials','danger')
                 return redirect(url_for('signin'))
             
    return render_template('login.html',title='login', form=form)


@app.route('/wellbore/new', methods=['GET','POST'])
def new_wellbore():

    form = Wellboreform()
    if request.method == 'POST':
        oilsample=Wellbore(wellboreofficialname=form.wellboreofficialname.data,wellborelocalname=form.wellborelocalname.data,
        wellborealiasname=form.wellborealiasname.data,wellborespuddate=form.wellborespuddate.data,spudyear=form.spudyear.data,
        wellboretypeid=form.wellboretypeid.data,initialwellborepurposeid=form.initialwellborepurposeid.data)
        db.session.add(oilsample)
        db.session.commit()

        flash('Data successfully Added','success')
        return redirect(url_for('wellbore'))

    return render_template('create_wellbore.html',form=form)

@app.route('/wells/new', methods=['GET','POST'])
def new_wells():

    form = Wellsform()
    if request.method == 'POST':
        oilinfo= Wells(wellname=form.wellname.data,sampletype=form.sampletype.data,layer=form.layer.data,
        initialdepth=form.initialdepth.data,terminationdepth=form.terminationdepth.data,samplebucket=form.samplebucket.data)
        db.session.add(oilinfo)
        db.session.commit()

        flash('Data successfully Added','success')
        return redirect(url_for('wells'))

    return render_template('create_wells.html',form=form)


@app.route('/wellborecore/new', methods=['GET','POST'])
def new_wellborecore():

    form = Wellborecoreform()
    if request.method == 'POST':
        corebase=Wellborecore(wellborename=form.wellborename.data,corenumber=form.corenumber.data,coredate=form.coredate.data
        ,coringcontractor=form.coringcontractor.data,coretopmdrt=form.coretopmdrt.data,corebottommdrt=form.corebottommdrt.data,coretoptvd=form.coretoptvd.data,
        corebottomtvd=form.corebottomtvd.data,cutlength=form.cutlength.data,cutlengthtvd=form.cutlengthtvd.data,recoveredlength=form.recoveredlength.data,
        corerecovery=form.corerecovery.data,topformation=form.topformation.data,bottomformation=form.bottomformation.data,wellborecorename=form.wellborecorename.data,
        corepicturesoftcopypath=form.corepicturesoftcopypath.data,corepicturehyperlink=form.corepicturehyperlink.data,corereportsoftcopypath=form.corereportsoftcopypath.data,
        corereporthyperlink=form.corereporthyperlink.data,documentformat=form.documentformat.data,filesize=form.filesize.data,securitygrade=form.securitygrade.data,openduedate=form.openduedate.data,
        comments=form.comments.data,documenttitle=form.documenttitle.data,receivedate=form.receivedate.data,documentdate=form.documentdate.data,documentname=form.documentname.data,
        cored=form.cored.data,createdby=form.createdby.data,datecreated=form.datecreated.data,modifiedon=form.modifiedon.data,modifiedby=form.modifiedby.data,
        pictureuploaddate=form.pictureuploaddate.data,reportuploaddate=form.reportuploaddate.data)
        db.session.add(corebase)
        db.session.commit()

        flash('Data successfully Added','success')
        return redirect(url_for('wellborecore'))

    return render_template('create_wellborecore.html',form=form)

@app.route('/category/new', methods=['GET','POST'])
def new_category():

    form = Categoryform()
    if request.method == 'POST':
        cat=Category(coretype=form.coretype.data,storeidentifier=form.storeidentifier.data,catalogcorefromdepth=form.catalogcorefromdepth.data,catalogcoretodepth=form.catalogcoretodepth.data,
        coresecurityflag=form.coresecurityflag.data,catalogcorelength=form.catalogcorelength.data,topcoreformation=form.topcoreformation.data,bottomcoreformation=form.bottomcoreformation.data,wellborecorename=form.wellborecorename.data,
        cataloguepicturesoftcopypath=form.cataloguepicturesoftcopypath.data,cataloguepicturehyperlink=form.cataloguepicturehyperlink.data,cataloguereportsoftcopypath=form.cataloguereportsoftcopypath.data,
        cataloguereporthyperlink=form.cataloguereporthyperlink.data,documentformat=form.documentformat.data,filesize=form.filesize.data,securitygrade=form.securitygrade.data,openduedate=form.openduedate.data,
        comments=form.comments.data,cataloguepicturename=form.cataloguepicturename.data,corecatalogname=form.corecatalogname.data,welloperator=form.welloperator.data,wellbore=form.wellbore.data,
        spuddate=form.spuddate.data,createdby=form.createdby.data,datecreated=form.datecreated.data,modifiedon=form.modifiedon.data,modifiedby=form.modifiedby.data,
        pictureuploaddate=form.pictureuploaddate.data,reportuploaddate=form.reportuploaddate.data,wasanalysed=form.wasanalysed.data,hascorephotos=form.hascorephotos.data,
        corename=form.corename.data,coredate=form.coredate.data,comment=form.comment.data)
        db.session.add(cat)
        db.session.commit()

        flash('Data successfully Added','success')
        return redirect(url_for('category'))

    return render_template('create_category.html',form=form)

@app.route('/wells')
@login_required
def wells():
    infos = Wells.query.all()

    return render_template('wells.html',infos=infos)

@app.route('/wellbore')
@login_required
def wellbore():
    infos = Wellbore.query.all()

    return render_template('wellbore.html',infos=infos)

@app.route('/wellborecore')
@login_required
def wellborecore():
    infos = Wellborecore.query.all()

    return render_template('wellborecore.html',infos=infos)

@app.route('/category')
@login_required
def category():
    infos = Category.query.all()

    return render_template('category.html',infos=infos)

@app.route('/navigation')
@login_required
def navigation():
    return render_template('navigation.html')

@app.route('/logout')
@login_required
def logout():

    logout_user()
    flash('login to continue','danger')
    return redirect(url_for('login'))

@app.route('/wellborecore/<id>/update', methods=['GET','POST'])
def wellborecoreupdate(id):
    corebase1 = Wellborecore.query.get_or_404(id)
    
    if request.method == 'POST':
        
        corebase1.corenumber = request.form['corenumber']
        corebase1.coredate = request.form['coredate']
        corebase1.coringcontractor = request.form['coringcontractor']
        corebase1.coretopmdrt = request.form['coretopmdrt']
        corebase1.corebottommdrt = request.form['corebottommdrt']
        corebase1.coretoptvd = request.form['coretoptvd']
        corebase1.corebottomtvd = request.form['corebottomtvd']
        corebase1.cutlength= request.form['cutlength']
        corebase1.cutlengthtvd= request.form['cutlengthtvd']
        corebase1.recoveredlength= request.form['recoveredlength']
        corebase1.corerecovery = request.form['corerecovery']
        corebase1.topformation= request.form['topformation']
        corebase1.bottomformation = request.form['bottomformation']
        corebase1.wellborename = request.form['wellborename']
        corebase1.corepicturesoftcopypath = request.form['corepicturesoftcopypath']
        corebase1.corepicturehyperlink = request.form['corepicturehyperlink']
        corebase1.corereportsoftcopypath = request.form['corereportsoftcopypath']
        corebase1.corereporthyperlink = request.form['corereporthyperlink']
        corebase1.documentformat = request.form['documentformat']
        corebase1.filesize = request.form['filesize']
        corebase1.securitygrade = request.form['securitygrade']
        corebase1.openduedate = request.form['openduedate']
        corebase1.comments = request.form['comments']
        corebase1.documenttitle = request.form['documenttitle']
        corebase1.receivedate = request.form['receivedate']
        corebase1.documentdate = request.form['documentdate']
        corebase1.documentname = request.form['documentname']
        corebase1.cored = request.form['cored']
        corebase1.createdby = request.form['createdby']
        corebase1.datecreated = request.form['datecreated']
        corebase1.modifiedon = request.form['modifiedon']
        corebase1.modifiedby = request.form['modifiedby']
        corebase1.pictureuploaddate = request.form['pictureuploaddate']
        corebase1.reportuploaddate = request.form['reportuploaddate']

        try:
            db.session.commit()

            flash('wellbore core data has been successfully updated','success')
            return redirect(url_for('wellborecore'))
        
        except:
            return 'there is an issue updating the info'

    else:
        return render_template('wellborecore_update.html',corebase1=corebase1)

@app.route('/wells/<id>/update', methods=['GET','POST'])
def wellsupdate(id):
    oilinfo1 = Wells.query.get_or_404(id)
    
    if request.method == 'POST':
        
        oilinfo1.sampletype = request.form['sampletype']
        oilinfo1.wellname = request.form['wellname']
        oilinfo1.layer = request.form['layer']
        oilinfo1.initialdepth = request.form['initialdepth']
        oilinfo1.terminationdepth = request.form['terminationdepth']
        oilinfo1.samplebucket = request.form['samplebucket']
        

        try:
            db.session.commit()

            flash('Wells data has been successfully updated','success')
            return redirect(url_for('wells'))
        
        except:
            return 'there is an issue updating the info'

    else:
        return render_template('wells_update.html',oilinfo1 = oilinfo1)

@app.route('/wellbore/<id>/update', methods=['GET','POST'])
def wellboreupdate(id):
    oilsample1 = Wellbore.query.get_or_404(id)
    
    if request.method == 'POST':
        
        oilsample1.wellboreofficialname= request.form['wellboreofficialname']
        oilsample1.wellborelocalname = request.form['wellborelocalname']
        oilsample1.wellborealiasname= request.form['wellborealiasname']
        oilsample1.wellborespuddate = request.form['wellborespuddate']
        oilsample1.spudyear = request.form['spudyear']
        oilsample1.wellboretypeid = request.form['wellboretypeid']
        oilsample1.initialwellborepurposeid = request.form['initialwellborepurposeid']
      

        try:
            db.session.commit()

            flash('Wellbore data has been successfully updated','success')
            return redirect(url_for('wellbore'))
        
        except:
            return 'there is an issue updating the info'

    else:
        return render_template('wellbore_update.html',oilsample1 = oilsample1)

@app.route('/category/<id>/update', methods=['GET','POST'])
def categoryupdate(id):
    category1 = Category.query.get_or_404(id)
    
    if request.method == 'POST':
        
        category1.wasanalysed= request.form['wasanalysed']
        category1.coretype= request.form['coretype']
        category1.storeidentifier= request.form['storeidentifier']
        category1.catalogcorefromdepth = request.form['catalogcorefromdepth']
        category1.catalogcoretodepth= request.form['catalogcoretodepth']
        category1.coresecurityflag= request.form['coresecurityflag']
        category1.catalogcorelength = request.form['catalogcorelength']
        category1.hascorephotos = request.form['hascorephotos']
        category1.corecatalogname = request.form['corecatalogname']
        category1.welloperator = request.form['welloperator']
        category1.wellbore = request.form['wellbore']
        category1.spuddate = request.form['spuddate']
        category1.topcoreformation= request.form['topcoreformation']
        category1.bottomcoreformation = request.form['bottomcoreformation']
        category1.wellborecorename = request.form['wellborecorename']
        category1.cataloguepicturesoftcopypath = request.form['cataloguepicturesoftcopypath']
        category1.cataloguepicturehyperlink = request.form['cataloguepicturehyperlink']
        category1.cataloguereportsoftcopypath = request.form['cataloguereportsoftcopypath']
        category1.cataloguereporthyperlink = request.form['cataloguereporthyperlink']
        category1.documentformat = request.form['documentformat']
        category1.filesize = request.form['filesize']
        category1.securitygrade = request.form['securitygrade']
        category1.openduedate = request.form['openduedate']
        category1.comments = request.form['comments']
        category1.corename = request.form['corename']
        category1.coredate = request.form['coredate']
        category1.comment = request.form['comment']
        category1.cataloguepicturename = request.form['cataloguepicturename']
        
        category1.createdby = request.form['createdby']
        category1.datecreated = request.form['datecreated']
        category1.modifiedon = request.form['modifiedon']
        category1.modifiedby = request.form['modifiedby']
        category1.pictureuploaddate = request.form['pictureuploaddate']
        category1.reportuploaddate = request.form['reportuploaddate']
        
        try:
            db.session.commit()

            flash('Category data has been successfully updated','success')
            return redirect(url_for('category'))
        
        except:
            return 'there is an issue updating the info'

    else:
        return render_template('category_update.html',category1 = category1)



@app.route('/wellborecore/delete/<int:id>')
def deletewellborecore(id):

    item_to_delete = Wellborecore.query.get_or_404(id)
    try:
        flash('item Successfully deleted','success')
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect(url_for('wellborecore'))
    
    except:
        flash('Unable to delete ','danger')
        return redirect(url_for('wellborecore'))

@app.route('/wells/delete/<int:id>')
def deletewells(id):

    item_to_delete = Wells.query.get_or_404(id)
    try:
        flash('item Successfully deleted','success')
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect(url_for('Wells'))
    
    except:
        flash('Unable to delete ','danger')
        return redirect(url_for('wells'))

@app.route('/wellbore/delete/<int:id>')
def deletewellbore(id):

    item_to_delete = Wellbore.query.get_or_404(id)
    try:
        flash('item Successfully deleted','success')
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect(url_for('wellbore'))
    
    except:
        flash('Unable to delete ','danger')
        return redirect(url_for('navigation'))

@app.route('/category/delete/<int:id>')
def deletecategory(id):

    item_to_delete = Category.query.get_or_404(id)
    try:
        flash('item Successfully deleted','success')
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect(url_for('category'))
    
    except:
        flash('Unable to delete ','danger')
        return redirect(url_for('category'))



















if __name__ == '__main__':
    app.run(debug=True)





