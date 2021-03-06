from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,DecimalField,DateField
from wtforms.validators import DataRequired,Email


class LoginForm(FlaskForm):
       
       password = PasswordField('password',validators=[DataRequired()])
       email    =StringField('email',validators=[DataRequired(),Email()])
       submit =SubmitField('login')

class Wellboreform(FlaskForm):
       wellboreofficialname= StringField('wellboreofficialname',validators=[DataRequired()])
       wellborelocalname = StringField('wellborelocalname',validators=[DataRequired()])
       wellborespuddate = StringField('wellborespuddate',validators=[DataRequired()])
       wellborealiasname = StringField('wellborealiasname',validators=[DataRequired()])
       spudyear = StringField('spudyear',validators=[DataRequired()])
       wellboretypeid= DecimalField('wellboretypeid',validators=[DataRequired()])
       initialwellborepurposeid= DecimalField('initialwellborepurposeid',validators=[DataRequired()])
    

       submit =SubmitField('submit')


class Wellsform(FlaskForm):
       sampletype= StringField('sampletype',validators=[DataRequired()])
       layer= StringField('layer',validators=[DataRequired()])
       wellname = StringField('wellname',validators=[DataRequired()])
       initialdepth = DecimalField('initialdepth',validators=[DataRequired()])
       terminationdepth  = DecimalField('terminationdepth',validators=[DataRequired()])
       samplebucket = StringField('samplebucket',validators=[DataRequired()])
       
       submit =SubmitField('submit')

class Wellborecoreform(FlaskForm):
       wellboreid =DecimalField('wellboreid',validators=[DataRequired()])
       corenumber= DecimalField('corenumber',validators=[DataRequired()])
       coredate= StringField('coredate',validators=[DataRequired()])
       coringcontractor= StringField('coringcontractor',validators=[DataRequired()])
       wellborename= StringField('wellborename',validators=[DataRequired()])
       coretopmdrt=StringField('coretopmdrt',validators=[DataRequired()])
       corebottommdrt = StringField('corebottommdrt',validators=[DataRequired()])
       coretoptvd= StringField('corettoptvd',validators=[DataRequired()])
       corebottomtvd= StringField('corebottomtvd',validators=[DataRequired()])
       cutlength= StringField('cutlength',validators=[DataRequired()])
       cutlengthtvd= StringField('cutlengthtvd')
       recoveredlength= StringField('recoveredlength')
       corerecovery= StringField('corerecovery')
       topformation= StringField('topformation')
       bottomformation= StringField('bottomformation')
       corepicturesoftcopypath= StringField('corepicturesoftcopypath')
       corepicturehyperlink= StringField('corepicturehyperlink')
       createdby= StringField('createdby')
       datecreated= StringField('datecreated')
       modifiedon= StringField('modifiedon')
       modifiedby= StringField('modifiedby')
       wellborecorename= StringField('wellborecorename')
       cored= StringField('cored')
       corereportsoftcopypath= StringField('corereportsoftcopypath')
       corereporthyperlink= StringField('corereporthyperlink')
       documentformat= StringField('documentformat')
       filesize= StringField('filesize')
       securitygrade= StringField('securitygrade')
       openduedate= StringField('openduedate')
       documenttitle= StringField('documenttitle')
       receivedate= StringField('receivedate')
       documentdate= StringField('documentdate')
       documentname= StringField('documentname')
       comments= StringField('comments')
       pictureuploaddate= StringField('pictureuploaddate')
       reportuploaddate= StringField('reportuploaddate')
       submit =SubmitField('submit')

class Categoryform(FlaskForm):
      
       hascorephotos= StringField('hascorephotos',validators=[DataRequired()])
       storeidentifier= StringField('storeidentifier',validators=[DataRequired()])
       catalogcorefromdepth= StringField('catalogcorefromdepth',validators=[DataRequired()])
       wellborecorename= StringField('wellborecorename',validators=[DataRequired()])
       catalogcoretodepth= StringField('catalogcoretodepth',validators=[DataRequired()])
       catalogcorelength= StringField('catalogcorelength')
       coretype= StringField('coretype',validators=[DataRequired()])
       hascorephotos= StringField('hascorephotos')
       wasanalysed= StringField('wasanalysed')
       coresecurityflag= StringField('coresecurityflag')
       topcoreformation= StringField('topcoreformation')
       bottomcoreformation= StringField('bottomcoreformation')
       cataloguepicturename= StringField('cataloguepicturename')
       cataloguepicturesoftcopypath= StringField('cataloguepicturesoftcopypath')
       cataloguereportsoftcopypath= StringField('cataloguereportsoftcopypath')
       cataloguepicturehyperlink= StringField('cataloguepicturehyperlink')
       cataloguereporthyperlink= StringField('cataloguereporthyperlink')
       documentformat= StringField('documentformat')
       filesize= StringField('filesize')
       securitygrade= StringField('securitygrade')
       openduedate= StringField('openduedate')
       comments= StringField('comments')
       corecatalogname= StringField('corecatalogname')
       welloperator= StringField('welloperator')
       wellbore= StringField('wellbore')
       spuddate= StringField('spuddate')
       corename= StringField('corename')
       coredate= StringField('coredate')
       comment= StringField('comment')
       pictureuploaddate= StringField('pictureuploaddate')
       reportuploaddate= StringField('reportuploaddate')
       createdby= StringField('createdby')
       datecreated= StringField('datecreated')
       modifiedon= StringField('modifiedon')
       modifiedby= StringField('modifiedby')
       submit =SubmitField('submit')
