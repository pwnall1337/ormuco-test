from flask import Flask, render_template, request, url_for
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define our sqlite query method
def sql_query(query_data, data=None):
    con=sqlite3.connect('ormuco.db')
    cur=con.cursor()
    cur.execute(query_data)
    print query_data
    if 'select' in query_data:
        data=cur.fetchall()
    if 'insert' in query_data:
        con.commit()
    return data
 
# Define a route for capturing POST data and gathing it.
@app.route('/done/', methods=['POST'])
def done():
    name=request.form['name']
    color=request.form['color']
    catdog=request.form['catdog']
    query_name=("select name from data where name='%s'" % name)
    name_result=sql_query(query_name)
    if len(name_result) >0:
        return render_template('bad_name.html', name=name)
    else:
        query_string=("insert into data('name','color','animal') values ('%s','%s','%s')" 
                      % (name,color,catdog))
        sql_query(query_string)
        return render_template('form_action.html', name=name, color=color, catdog=catdog)


# Run the app
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("5000"),
        debug=True
  )

