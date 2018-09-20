 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 23:42:08 2018

@author: ian
"""

# System Resources
import requests
from dateutil.parser import parse
from datetime import date
from json import dumps, loads
from random import sample
# Server Resources 
from flask import request, jsonify, Blueprint, flash, redirect,url_for, render_template, abort 

# Application Local Resources
from main import app, db, api, Resource
#from main.Bq.forms import WallEntryForm

# Create the Estimator Blueprint of the Application
fastestimate = Blueprint('fastestimate', __name__)


    
# a route where we will display a welcome message via an HTML template

class Wall(Resource):
    def get(self, id):
        """clients = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from clients") # This line performs query and returns json result
       
        for i in query.cursor.fetchall():
            clients_data = {'client': i[0]} 
            
            clients.append(clients_data)
        
        """
         
        data_search = dict(
            data_start = id.find('{'),
            data_stop = id.find('}')
        )
        sanitized_data = id[data_search['data_start']:data_search['data_stop']+1]
        data = loads(sanitized_data)

        
        wall_data = dict(
        wid=data.doc_id,
        tag=data.wall_tag,
        length=data.length,
        height=data.height

        )
       
        return wall_data
        
"""
class Clients(Resource):
    def get(self):
        clients = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from clients") # This line performs query and returns json result
       
        for i in query.cursor.fetchall():
            clients_data = {'client': i[0], 'data': loads(i[1])} 
            
            clients.append(clients_data)
       
        return clients

class Client(Resource):
    ''' Client Route sends the clients data, any projects being done 
        for the client, projects income and projects expenditure '''
    
    def get(self, id):
        client = []
        projects = []
        contract_sum = []
        project_uri = 'http://192.168.0.22/projects'
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from clients") # This line performs query and returns json result
        # get projects data from uri
        res = requests.get(project_uri)
        project_data = res.text
        project_data = loads(project_data)

        for i in query.cursor.fetchall():
            clients_data = {'client': i[0], 'data': loads(i[1])} 
            if(id == clients_data["data"]['doc_id']):
                clients_data = clients_data
                
        for item in project_data:
            if item['data']['client_id'] == id:
                client_projects = {
                    "name": item['data']['name'],
                    "address": item['data']['addr'],
                    "contract": item['data']['contractSum'],
                    "project_id": item['data']['doc_id'],
                    "refferal": item['data']['refferal'],
                    "comments": item['data']['comments'],
                    "reg_date": item['data']['registration_date'],
                    "technical": item['data']['technical']
                }
                projects.append(client_projects)
                contract = {'project':item['data']["doc_id"], 'contract_sum': item["data"]["contractSum"] }
                client.append(contract)
                contract_sum.append(item["data"]["contractSum"])
        clients_data['projects'] = projects
        clients_data['projects_contract'] = contract_sum
        clients_data['contracts_sum'] = sum(contract_sum)
        clients_data['contract'] = client
        


                
        return  clients_data#_data[0]['data']["client_id"], 200 
        # else return a user not found message with 404 Not Found.
        #return "Client not found", 400 
        

class StaffList(Resource):
    def get(self):
        #staff = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from staff") # This line performs query and returns json result
        return {'staff': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    

class Staff(Resource):
    def get(self):
        staff = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from staff") # This line performs query and returns json result
       
        for i in query.cursor.fetchall():
            staff_data = {'staff': i[0], 'data': loads(i[1])} 
            
            staff.append(staff_data)
        return staff
    
    
class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Employee(Resource):
    def get(self, id):
        self.id = id
        employee = []
        employee_paybills = []
        contract_sum = []
        paybill_uri = 'http://192.168.0.22/paybill'
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        employee_data = [loads(i[1]) for i in query.cursor.fetchall()]
        # get projects paybills data from uri
        res = requests.get(paybill_uri)
        paybills = res.text
        # load paybills data
        paybills = loads(paybills)
        # load employee data
       
              
        # search through employee data for requested employee
        for item in employee_data:
            if self.id == item['doc_id']:
                # if found assign it 
                employee_data = item
        # search through paybills for employee paybills
        for paybill in paybills:
            if self.id == paybill['data']['info']['workerId']:
                # if found enlist 
                employee_paybills.append(paybill)

        '''{
                    "name": item['data']['name'],
                    "address": item['data']['addr'],
                    "contract": item['data']['contractSum'],
                    "project_id": item['data']['doc_id'],
                    "refferal": item['data']['refferal'],
                    "comments": item['data']['comments'],
                    "reg_date": item['data']['registration_date'],
                    "technical": item['data']['technical']
                }
                projects.append(client_projects)
                contract = {'project':item['data']["doc_id"], 'contract_sum': item["data"]["contractSum"] }
                client.append(contract)
                contract_sum.append(item["data"]["contractSum"])
                clients_data['projects'] = projects
                clients_data['projects_contract'] = contract_sum
                clients_data['contracts_sum'] = sum(contract_sum)
                clients_data['contract'] = client
        '''
        # assign the employee paybills 
        employee_data['paybills'] = employee_paybills
        


        return employee_data, 200
        
    
class SubsList(Resource):
    def get(self):
        #subs = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from subs") # This line performs query and returns json result
        return {'subs': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    

class Subs(Resource):
    def get(self):
        subs = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from subs") # This line performs query and returns json result
       
        for i in query.cursor.fetchall():
            subs_data = {'subs': i[0], 'data': loads(i[1])} 
            
            subs.append(subs_data)
        return subs
    
    
class ProjectsList(Resource):
    def get(self):
        #project = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from projects") # This line performs query and returns json result
        return {'projects': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    
class Projects(Resource):
    def get(self):
        '''  projectsReport = {}, generalReport = {};

        numProjects, activeProjects, expiredProjects, projectedContractSum, activeContractSum, 
        '''
        
        projects = []
        expired_projects = []
        expired_contracts_sum = []
        contracts_sum = []
        all_projects = []
        active_projects = []
        active_projects_sum = []
        active_projects_contracts = []

        active_projects_chart_list = []
        expired_projects_chart_list = []


        status = 'in time'
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from projects") # This line performs query and returns json result       
        for i in query.cursor.fetchall():
            pdata = {'project': i[0], 'data': loads(i[1])}  
            project_start = parse(pdata['data']['technical']['start'])
            project_end = parse(pdata['data']['technical']['completion'])
            time_delta = project_end.date() - project_start.date()
            duration = time_delta.days
            overrun = date.today() - project_end.date()
            expired = date.today() > project_end.date()
            active_projects.append(pdata['data']['doc_id'])
            active_projects_contracts.append(pdata['data']['contractSum'])
            # Active Project Charts
            # get the expired project , contract, registration date
            active_projects_chart = { 
                     'project': pdata['data']['doc_id'],
                     'contract': pdata['data']['contractSum'],
                     'date': (pdata['data']['registration_date'])
                }
            active_projects_chart_list.append(active_projects_chart)
            # Filtering expired projects
            if expired:
                status = 'expired'
                expired_projects.append(pdata['data']['doc_id'])
                expired_contracts_sum.append(pdata['data']['contractSum'])
                active_projects.remove(pdata['data']['doc_id'])
                active_projects_chart_list.remove(active_projects_chart)
                active_projects_contracts.remove(pdata['data']['contractSum'])
                # get the expired project , contract, registration date as chart data
                expired_projects_chart = { 
                     'project': pdata['data']['doc_id'],
                     'contract': pdata['data']['contractSum'],
                     'date': (pdata['data']['registration_date'])
                 }
                # enlist chart data 
                expired_projects_chart_list.append(expired_projects_chart)

       
                
            pdata['data']['technical']['duration'] = duration
            pdata['data']['technical']['status'] = status
            pdata['data']['technical']['overrun'] = overrun.days
           
            contracts_sum.append(pdata['data']['contractSum'])
            all_projects.append(pdata['data']['doc_id'])
            
            projects.append(pdata)
        num_projects = len(projects)
        num_expired_projects = len(expired_projects)
        expired_contracts = sum(expired_contracts_sum)
        contracts_sum_total = sum(contracts_sum)
        active_projects_sum = sum(active_projects_contracts)
       

                
        report = {
                'active_projects': active_projects,
                'active_projects_sum': active_projects_sum,
                'active_projects_chart_list':  active_projects_chart_list,
                'all_projects': all_projects,
                'contracts_sum': contracts_sum,
                'contracts_sum_total': contracts_sum_total,

                'expired_contracts': expired_contracts,                
                'expired_contracts_sum': expired_contracts_sum,
                'expired_projects': expired_projects,
                'expired_projects_chart_data':  expired_projects_chart_list,

                'num_active_projects': num_projects - num_expired_projects,                
                'num_expired_projects': num_expired_projects,
                'num_projects': num_projects

                          
               
                
                }
               
 
       
        
        
        projects.append(report)
        return projects


class ProjectExpenditure(Resource):
    def get(self):
        spends = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from expenditure") # This line performs query and returns json result
        
        for i in query.cursor.fetchall():
            spends_data = {'spend_id': i[0], 'data': loads(i[2])} 
            
            spends.append(spends_data)
            
        return spends
        
       # return {'spending': [i[0] for i in query.cursor.fetchall()]} 

class ProjectIncome(Resource):
    def get(self):
        income = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from project_income") # This line performs query and returns json result
        
        for i in query.cursor.fetchall():
            income_data = {'income_id': i[0], 'data': loads(i[1])} 
            
            income.append(income_data)
            
        return income

class ProjectInvoice(Resource):
    def get(self):
        invoice = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from project_invoice") # This line performs query and returns json result
        
        for i in query.cursor.fetchall():
            invoice_data = {'invoice_id': i[0], 'data': loads(i[1])} 
            
            invoice.append(invoice_data)
            
        return invoice

class ProjectPaybill(Resource):
    def get(self):
        paybill = []
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from project_paybill") # This line performs query and returns json result
        
        for i in query.cursor.fetchall():
            paybill_data = {'paybill_id': i[0], 'data': loads(i[2])} 
            
            paybill.append(paybill_data)
            
        return paybill
"""                

"""
@app.route("/dview")
def dataview():
    
    
    name = request.args.get("name")
    if name == None:
        name = "No tag specified"        
    data = {
    'name': name,
    "message": "Hello "}

    

    #if data['name'] == 'list':
     #   data['message'] = 'projects[0]'
    return render_template('dview.html', data=data)

@app.route("/data")
def data():
    jdata = {
        'apples': sample(range(1,10), 7),
        'oranges': [2, 29, 5, 5, 2, 3, 10]
    }
    return jsonify(jdata)
"""
todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

#api.add_resource(TodoSimple, '/do/<int:todo_id>', endpoint='todo_ep')
    


#api.add_resource(Home, '/home') # Route_1
#api.add_resource(Home, '/home') # Route_1
api.add_resource(Wall, '/wall/<string:id>') # Route_2
"""
api.add_resource(Employee, '/employee/<string:id>') # Route_1
api.add_resource(StaffList, '/stafflist') # Route_4
api.add_resource(Staff, '/staff') # Route_4
api.add_resource(SubsList, '/subslist') # Route_4
api.add_resource(Subs, '/subs') # Route_4
api.add_resource(ProjectsList, '/projectlist') # Route_2
api.add_resource(Projects, '/projects') # Route_3
api.add_resource(ClientsList, '/clientlist') # Route_4
api.add_resource(Clients, '/clients') # Route_5
api.add_resource(Client, '/client/<string:id>') # Route_5
api.add_resource(ProjectExpenditure, '/spends') # Route_6
api.add_resource(ProjectIncome, '/income') # Route_7
api.add_resource(ProjectInvoice, '/invoice') # Route_8
api.add_resource(ProjectPaybill, '/paybill') # Route_9

"""

