# main_index

# System & Server Localised Resources
from main import abort,app,Blueprint,date,db,dumps,flash,jsonify,loads,parse,redirect,render_template,requests,request,Resource,sample,url_for,uu_id#,qsrep 

# Application Resources
from main.index.models import Beam,  Opening, Category, Wall
from main.index.forms import  BarTypeForm, BeamEntryForm, BeamCategoryForm, WallEntryForm,  OpeningForm,  WallBarsForm, CategoryForm,  ColumnCategoryForm, WallCategoryForm 
from main.index.qsrep import Walls
from main.Bq import estimator
# initialise once

# Create the Index Blueprint of the Application
index = Blueprint('index', __name__)


@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html', title='Forbidden'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Not Found'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', title='Server Fault'), 500

@index.route('/')
@index.route('/home')
def home():
    """
        Fast estimate Home Page
    """ 
    wall_resource = 'http://localhost:8090/wall/:WA1' 
    res = requests.get(wall_resource)
    wall_ = loads(res.text)
    return render_template('index.html', title='FastEstimate', message="Create Professional Construction Estimates in Seconds.", wall=wall_)

@index.route('/getwall', methods=['GET', 'POST'])
def getwall():
    """
        Fast estimate Wall
    """
    categories = [(c.id, c.name) for c in Category.query.all()]
    w_form = WallEntryForm(request.form)
    o_form = OpeningForm(request.form)
    sb_form = BeamEntryForm(request.form)    
    o_form.category.choices = categories
    w_form.category.choices = categories
    sb_form.category.choices = categories
    

    openings = Opening.query.all() 
    beams = Beam.query.all()     
    return render_template('wall_index.html',
    title='FastEstimate Wall',
    wall_form=w_form,
    opening_form=o_form,
    beam_form=sb_form,
    openings=openings,
    beams=beams
    )

@index.route('/wall_result', methods=['POST'])
def wall_result():
    """
        Fast estimate Wall
    """
    
    data = dict(
    doc_id=uu_id('doc')
    ) 
    if request.method == 'POST':
        data['wall_tag'] = request.form.get('tag')
        data['length'] = request.form.get('length')
        data['height'] = request.form.get('height')
        #data['category'] = Category.query.get_or_404(request.form.get('category'))  
        data['rebar'] = dict(
            hbar=request.form.get('h_bar_type'), 
            hspacing=request.form.get('h_bar_spacing'),
            vbar=request.form.get('v_bar_type'), 
            vspacing=request.form.get('v_bar_spacing') 

        ) 
    #qsr = qsrep.Stuctural  
    #product = Product(name, price, category, uid)
    openings_dict = {}
    openings = Opening.query.filter_by(wall_tag=data['wall_tag']).all()
    
    if openings is not None:
        for opening in openings:
            openings_dict[opening.tag] = {'w':opening.width,'h':opening.height,'amt':opening.amount}
    else:
        openings_dict = None

    
    wall_bq = estimator.Walls(data['length'],data['height'],openings_dict)
    data['estimate'] = wall_bq.wall
    #wall_data = str(data)    
        
    #wall_resource = 'http://localhost:8090/wall/:' +  wall_data  
    #res = requests.get(wall_resource)
    #wall_ = loads(res.text)
    return render_template('wall_result.html', title='FastEstimate Wall', data=data, opening=openings_dict)
    #return jsonify(data)

@index.route('/wall_opening', methods=['GET', 'POST'])
def wall_opening():
    """
        Fast estimate Wall
    """
    data = dict(
    doc_id=uu_id('item')
    ) 
    data['tag'] = request.form.get('tag')
    data['wall_tag'] = request.form.get('wall_tag')
    data['width'] = request.form.get('width')
    data['height'] = request.form.get('height')
    data['amount'] = request.form.get('amount')
    data['category'] = Category.query.get_or_404(request.form.get('category'))  

    opening = Opening(data['tag'], data['wall_tag'], data['width'], data['height'], data['amount'], data['category'], data['doc_id']) 
    
    db.session.add(opening)
    db.session.commit()

    flash('Opening {} added to project!'.format(data['tag']), 'success')
    return redirect(url_for('index.getwall'))

@index.route('/beam_result', methods=['GET', 'POST'])
def beam_result():
    """
        Fast estimate Wall
    """
    data = dict(
    doc_id=uu_id('item')
    ) 
    data['tag'] = request.form.get('tag')
    data['wall_tag'] = request.form.get('wall_tag')
    data['width'] = request.form.get('width')
    data['depth'] = request.form.get('depth')
    data['length'] = request.form.get('length')

    data['amount'] = request.form.get('amount')
    data['category'] = Category.query.get_or_404(request.form.get('category')) 


    data['topbar'] = request.form.get('topbar')
    data['midbar'] = request.form.get('midbar')
    data['botbar'] = request.form.get('botbar')
    data['stirup'] = request.form.get('stirup')

    data['topbar_amt'] = request.form.get('topbar_amt')
    data['midbar_amt'] = request.form.get('midbar_amt')
    data['botbar_amt'] = request.form.get('botbar_amt')
    data['stirup_spacing'] = request.form.get('stirup_spacing')

    beam = Beam(data['doc_id'],data['tag'],data['wall_tag'],data['width'],data['depth'],data['length'],data['amount'],data['category'],data['topbar'], data['midbar'],data['botbar'],data['stirup'],data['stirup_spacing'],data['topbar_amt'],data['midbar_amt'],data['botbar_amt']) 
    
    db.session.add(beam)
    db.session.commit()

    flash('Beam {} added to project!'.format(data['tag']), 'success')
    return redirect(url_for('index.getwall'))

@index.route('/walls')
@index.route('/walls/<int:page>')
def walls(page=1):
    """
        This method returns the list of all products in the database in
         JSON format
    """
    walls = Wall.query.paginate(page, 5)
    return render_template('walls.html', title='Walls', walls=walls)
    

# Categories
@index.route('/create_category', methods=['GET'])
def create_category():
    form = CategoryForm(request.form)
    
        
    return render_template('category_create.html',
         title='Category By Id',
         form=form,
         
         )  

@index.route('/category_create', methods=['POST'])
def category_create():
    
    if request.method == 'POST':
        name = request.form.get('name')
        category = Category(name)
        db.session.add(category)
        db.session.commit()
        flash('Category {} created has been created!'.format(name), 'success')
        return redirect(url_for('index.create_category'))    


@index.route('/category/<id>')
def category(id):
    category = Category.query.get_or_404(id)
    return render_template('category.html', title='Category By Id', category=category)
    
@index.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', title='Categories', categories=categories)



# Streaming 
@index.route("/stream", methods=["POST"])
def demo():
    with open("/tmp/flask-stream-demo", "bw") as f:
        chunk_size = 4096
        while True:
            chunk = request.stream.read(chunk_size)
            if len(chunk) == 0:
                return

            f.write(chunk)