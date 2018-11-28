# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table as dt
import csv

users=[] #Main users array which contains data for all users taken from testUser.csv
with open('Datasets/testUSER.csv') as csvfile: 
    reader = csv.reader(csvfile, delimiter=',') 
    for row in reader:
        users.append(row)
print(users)

#Getting all the datasets from CSV files
BMI=pd.read_csv('Datasets/Male/Bmi.csv',sep=',')
BMIF=pd.read_csv('Datasets/Female/BmiF.csv',sep=',')
BMIA=pd.read_csv('Datasets/All/BMIA.csv',sep=',')
VIT=pd.read_csv('Datasets/Male/Vit.csv',sep=',')
VITF=pd.read_csv('Datasets/Female/VitF.csv',sep=',')
VITA=pd.read_csv('Datasets/All/VITA.csv',sep=',')
VEG=pd.read_csv('Datasets/Male/Veg.csv',sep=',')
VEGF=pd.read_csv('Datasets/Female/VegF.csv',sep=',')
VEGA=pd.read_csv('Datasets/All/VEGA.csv',sep=',')
AS=pd.read_csv('Datasets/Male/AS.csv',sep=',')
ASF=pd.read_csv('Datasets/Female/ASF.csv',sep=',')
ASA=pd.read_csv('Datasets/All/ASA.csv',sep=',')
SA=pd.read_csv('Datasets/Male/SA.csv',sep=',')
SAF=pd.read_csv('Datasets/Female/SAF.csv',sep=',')
C=pd.read_csv('Datasets/Male/C.csv',sep=',')
CF=pd.read_csv('Datasets/Female/CF.csv',sep=',')
CA=pd.read_csv('Datasets/All/CA.csv',sep=',')
EC=pd.read_csv('Datasets/Male/EC.csv',sep=',')
ECF=pd.read_csv('Datasets/Female/ECF.csv',sep=',')
ECA=pd.read_csv('Datasets/All/ECA.csv',sep=',')
DA=pd.read_csv('Datasets/Male/DA.csv',sep=';')
DAF=pd.read_csv('Datasets/Female/DAF.csv',sep=';')
AL=pd.read_csv('Datasets/Male/AL.csv',sep=',')
ALF=pd.read_csv('Datasets/Female/ALF.csv',sep=',')
ALA=pd.read_csv('Datasets/All/ALA.csv',sep=',')
SAA=pd.read_csv('Datasets/All/SAA.csv',sep=',')
USER=pd.read_csv('Datasets/testUSER.csv',sep=',')
vsZain=pd.read_csv('Datasets/zainAll.csv',sep=',')
usersFile = pd.read_csv('Datasets/leaderboard.csv',sep=',')
df=pd.read_csv('Datasets/parks.csv',sep=';')

#This function gets the index of user and returns the complete data of that user
def returnUserArray(num):
    result = []
    index = 1
    while (index < len(users)):
        result.append(users[index][num])
        index = index + 1
    return result

#Test Case User for the prototype, The first user of the  'users' array
testCase_User = {
        'name' : 'Zain',
        'currentData' : [], #currentData from csv file
        'targetData': [], #targetData which will be changed as we change the BMI or activity level slider
        'x': ['Age','BMI','Fruit Consumption','Vitamins','Self Assessment','Activity Summary','Alcohol Consumption','Cigarettes Consumption','E-Cigarettes Consumption','Water Consumption']
        }
testCase_User['currentData'] = returnUserArray(1)
testCase_User['targetData'] = testCase_User['currentData'].copy() #At Start both current and target are same!
print (testCase_User['currentData'])
print (testCase_User['x'])

#Initializing the application
app = dash.Dash()

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'}) 

#Setting the layout of the application
app.layout = html.Div(style={'background-image': 'url(https://i.ibb.co/dKzDrWS/Improving-Healthcare-Programs.png)','background-size': 'cover','background-position': 'center','hight':'100%'},
        children=[
        html.Div([
        html.Div(
            [ 
                html.H1(children='Health Visualisation', className='seven columns',style={'margin-left': 50, 'margin-top': 25,'font-family':'Oldtown','text-align':'center','color':'#000000'}),
                html.Img(src='https://i.ibb.co/42kLmGz/download-1.png',className='three columns',
                         style={
                        'height': '7%',
                        'width': '7%',
                        'float': 'right',
                        'position': 'center',
                        'margin-top': 25,
                        'margin-right': 5,
                    }),
                html.H4("Hi " + testCase_User['name'],className='two columns',style={'margin-top': 40,'color':'#000000','font-family':'Oldtown'})],className='row'),
   
    html.Div([dcc.Tabs(id="tabs", style={"height":"30","verticalAlign":"middle","horizontalAlign":"middle"},
                children=[
                    dcc.Tab(label="Scottish health survey 2017", value="SH"),
                    dcc.Tab(id="input",label="Health", value="R"),
                ],value="SH") ],className ='row tabs_div',style={'position': 'center','text-align':'justify'}),
    
    html.Div(id='SHtab',children=[
    html.Div(id='DD',children=[
                    html.Div(
                    [dcc.Dropdown(
                                    id='ind',
                                    options=[
{'label':'All','value':'ALL'},
                                            {'label': 'BMI', 'value': 'B'},
                                            {'label': 'Vit & Min Supplements', 'value': 'V'},
                                            {'label': 'Fruit & Veg Consumption', 'value': 'F'},
                                            {'label': 'Alcohol Consumption', 'value': 'AL'},
                                            {'label': 'Cigrattes', 'value': 'C'},
                                            {'label': 'E-Cigrattes', 'value': 'EC'},
                                            {'label': 'Self Assessed General Health', 'value': 'S'},
                                            {'label': 'Detailed Activity', 'value': 'D'},
                                            {'label': 'Activity Summary (MVPA)', 'value': 'A'}
                                                                            ],
                                            value='All',
                                            placeholder= 'Select category'),],
                        className='row tabs_div',
                        style={'margin-top': '10', 'text-align': 'center','verticalAlign' : "middle",}
                    ),], className="row "),
            html.Div(id='G',children=[dcc.Graph(id='graph3')]),
            html.Div(id='S',children=[
            html.P('Choose Age Group:'),
            dcc.Slider(
                    id='ageSlider',
                    min=1,
                    max=8,
                    marks={
                        1: '16-24',
                        2: '25-34',
                        3: '35-44',
                        4: '45-54',
                        5: '55-64',
                        6: '65-74',
                        7: '75+',
                        8: 'Avg',
                        },
                    value=8,
                        ),
                ], className= 'row tabs_div',style={'margin-left': 30, 'text-align': 'center'}),
          ])]),
    
       
  html.Div(id='rectab',style={'margin-top': '40', 'text-align': 'center','verticalAlign' : "middle"},className='twelve columns',children=[
    html.Div([
            html.Div([html.P("Change BMI")],style={'color':'#742e26','font-weight': 'bold'}),
              dcc.Slider(
                    id='bmiSlider',
                    min=1,
                    max=5,
                    marks={
                        1: {'label': '<18.5', 'style': {'color': '#000000'}}, #20
                        2: {'label': '18.5 to 24', 'style': {'color': '#000000'}}, #30
                        3: {'label': '25 to 29 (current)', 'style': {'color': '#000000'}}, #25
                        4: {'label': '30 to 40', 'style': {'color': '#000000'}}, #15
                        5: {'label': '40+', 'style': {'color': '#000000'}} #10
                        },
                    value=3,
                        )],className='seven columns', style={'text-align':'center','margin-left': '20','margin-top': '40'}),
    html.Div([
            html.Div([html.P("Change Activity")],style={'color':'#742e26','text-align':'center','font-weight': 'bold'}) ,
            dcc.Slider(
                    id='activitySlider',
                    min=1,
                    max=4,
                    marks={
                        1: {'label': 'MVPA (current)', 'style': {'color': '#000000'}},
                        2: {'label': 'Some Activity', 'style': {'color': '#000000'}},
                        3: {'label': 'Low Activity', 'style': {'color': '#000000'}},
                        4: {'label': 'Very Low Activity', 'style': {'color': '#000000'}},
                        },
                    value=1,
                        )],className="six columns", style={'text-align':'center','margin-top':'20','margin-left': '60'}),
            
    html.Div([dcc.RadioItems(
                    id = 'options',
                    options=[{'label': 'MyData', 'value': 'mD'},
                             {'label': 'vs Competitors', 'value': 'vC'},
                             {'label': 'vs All', 'value': 'vA'}],
                    value='mD',
                    labelStyle={'display': 'inline-block'}
                    ),
   dcc.Dropdown(
                    id = 'usersList',
                    options=[{'label': users[0][2],'value': users[0][2]},
                             {'label':users[0][3],'value': users[0][3]},
                             {'label':users[0][4],'value': users[0][4]},
                             {'label':users[0][5],'value': users[0][5]},
                             {'label':users[0][6],'value': users[0][6]},
                             {'label':users[0][7],'value': users[0][7]},
                             {'label':users[0][8],'value': users[0][8]}
                            ],
                    value = [],
                    multi=True
                    ),
],className="six columns", style={'text-align':'center','margin-top': '20','margin-left': '7'}),
   html.Div(
            [
            html.Div([
            html.Div([
                dcc.Graph(
                    id='graph1'
                )
                ], className= 'six columns',
                    style={ 'text-align': 'center','margin-left':10},
                ),
            html.Div(html.P("--Leaderboard--"),style={'color':'#742e26','text-align':'center','font-weight': 'bold'},),
            html.Div([ 
            dt.DataTable(
                    id="table",
                    columns=[{"name": i, "id": i} for i in usersFile.columns],
                    data = usersFile.to_dict("rows"),
                    style_cell={
                    'text-align':'center',
                        },
                    style_data_conditional=[{
                            "if": {"row_index": 0},
                            "backgroundColor": "#699FC3",
                            'color': 'white',
                            }]
                    ),], style={
                        'height': '45%',
                        'width': '45%',
                        'float': 'right',
                        'position': 'center',
                        'margin-right':25,}
                    ,className='four columns',),
         html.Div(
        id='map',
        className="nine columns",
        style={'margin-left':150},
        children=[
                dcc.Graph(
            id='graph',
            figure={
                'data': [
                    {'lat': df.lat, 'lon': df.log, 'type': 'scattermapbox' ,'text':df.Park,'name': 'Parks' },
                    {'lat': df.glat, 'lon': df.glog, 'type': 'scattermapbox' ,'text':df.Gym,'name': 'Gyms'}],
                'marker':{ 
                },
                'layout' :{
                    'title':'Nearest Parks/Gyms',
                    'font':{'color':'#742e26'},
                    'autosize':True,
                    'hovermode':'closest',
                    'bearing':0,
                    'mapbox': {
                        'center': {'lat':55.8597181, 'lon':-4.254425},
                        'zoom':12,
                    
                        'accesstoken': (
                            'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3M' +
                            'DBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
                        ) 
                    } ,
                    },
                }
              ),
                ]),
                    ],className='twelve columns'),
           
            ])])])
    

#Generating the appropriate data for a user when you hover over the graph
def appendData(user):
    text=['Age','BMI']
    #Check Fruit Consumption
    if(users[3][user] == '0'):
        text.append('None')
    elif(users[3][user] == '10'):
        text.append(' 1 Portion per day')
    elif(users[3][user] == '15'):
        text.append(' 2 Portions per day')
    elif(users[3][user] == '25'):
        text.append('3 Portions per day')
    elif(users[3][user] == '30'):
        text.append('4 Portions per day')
    elif(users[3][user] == '60'):
        text.append('5+ Portions per day')
        
    #Check Vitamin Consumption
    if(users[4][user] == '15'):
        text.append('Taking any Supplements')
    elif(users[4][user] == '45'):
        text.append('No Supplements taken')
    else:
        text.append('Taking VitaminD')
    #Check Self Assessment
    if(users[5][user] == '40'):
        text.append('Very Good')
    elif(users[5][user]== '35'):
        text.append('Good')
    elif(users[5][user]== '25'):
         text.append('Fair')
    elif(users[5][user]== '15'):
         text.append('Bad')
    else:
         text.append('Very Bad')
    #Check MVPA
    if(users[6][user] == '60'):
        text.append('Meets MVPA Guidelines')
    if(users[6][user] == '45'):
        text.append('Some Activity')
    if(users[6][user] == '20'):
        text.append('Low Activity')
    if(users[6][user] == '15'):
        text.append('Very Low Activity')
    #Check Alcohol
    if(users[7][user]== '30'):
        text.append('Non-drinker')
    if(users[7][user]== '15'):
        text.append('Moderate')
    if(users[7][user]== '0'):
        text.append('Hazardous/Harmful')
    #Check Cigratte
    if(users[8][user]== '5'):
        text.append('Current Smoker')
    if(users[8][user]== '20'):
        text.append('Ex-Smoker')
    if(users[8][user]== '30'):
        text.append('Never Smoked Before')
    #Check E-Cigrattes
    if(users[9][user]== '10'):
        text.append('Current using')
    if(users[9][user]== '15'):
        text.append('Ever previously smoked')
    if(users[9][user]== '20'):
        text.append('Never Smoked Before')
    #Check Water-Fluid Consumption
    if(users[10][user] == '0'):
        text.append('None')
    elif(users[10][user]=='25'):
        text.append('1-5 Glasses per day')
    elif(users[10][user]=='35'):
        text.append('6-8 Glasses per day')
    elif(users[10][user]=='50'):
        text.append('8+ Glasses per day')
    return text


#Checking if the current data of user is same as the target one, in order to display a separate line graph for target.
def isCurrent_Target_Same(current,target):
    for x in current:
        for y in target:
            if(x != y):
                return False
    return True

@app.callback(
dash.dependencies.Output('rectab', component_property='style'),
             [dash.dependencies.Input('tabs', 'value')])
def render_content(tab):
    if tab =='SH':
        return {'display': 'none'}


@app.callback(
dash.dependencies.Output('SHtab', component_property='style'),
             [dash.dependencies.Input('tabs', 'value')])
def render_content(tab):
    if tab =='R':
        return {'display': 'none'}



#Callback function that calls 'update_image_src' whenever the slider values are changed, or the radio buttons are selected

@app.callback(
        dash.dependencies.Output('graph1', 'figure'),
        [dash.dependencies.Input('activitySlider', 'value'),
         dash.dependencies.Input('options','value'),
         dash.dependencies.Input('usersList','value'),
        dash.dependencies.Input('bmiSlider','value')])

def update_image_src(ac_value,selection,userdropdown,bmi_value):
    data = []
    title = ""
    Xlable= "Categories"
    Ylable = "Frequency"
    
    #Change BMI
    #Dummy Values
    if(bmi_value == 1):
        testCase_User['targetData'][1] = 14
    elif(bmi_value == 2):
        testCase_User['targetData'][1] = 22
    elif(bmi_value == 3):
        testCase_User['targetData'][1] = 24.4
    elif(bmi_value == 4 ):
        testCase_User['targetData'][1] = 35
    elif(bmi_value == 5):
        testCase_User['targetData'][1] = 50
    
    #Change Activity
    if(ac_value == 1):
        testCase_User['targetData'][5] = 60
    elif(ac_value == 2):
        testCase_User['targetData'][5] = 45
    elif(ac_value == 3):
        testCase_User['targetData'][5] = 20
    elif(ac_value == 4):
        testCase_User['targetData'][5] = 15
    #Check for Selection
        #1. MyData
    if(selection == "mD"):
        data.append({'x':testCase_User['x'],'y': testCase_User['currentData'],'type':'scatter','text':appendData(1),'name':'You'})
        if(bmi_value != 3 or ac_value != 1):
            data.append({'x':testCase_User['x'],'y': testCase_User['targetData'],'type':'scatter','text':appendData(1),'name':'You(Target)'})
        title=testCase_User['name'] + '\'s Data'
        #2. vs Competitors
    if(selection == "vC"):
        data.append({'x':testCase_User['x'],'y': testCase_User['currentData'],'type':'scatter','text':appendData(1),'name':'You'})
        if(bmi_value != 3 or ac_value != 1):
            data.append({'x':testCase_User['x'],'y': testCase_User['targetData'],'type':'scatter','text':appendData(1),'name':'You(Target)'})
        title=testCase_User['name'] + ' vs Competitors/Supporters'
            #2.a Check for userDropdown List
                #Compare with all competitors
        if(len(userdropdown) < 1):
            count = 2
            for x in users[0]:
                if(x == 'ind' or  x == 'Zain'):
                    continue
                txt=[]
                txt=appendData(count)
                data.append({'x':testCase_User['x'],'y': returnUserArray(count),'type':'scatter','text':txt,'name':x})
                count = count + 1
        else:
            for y in userdropdown:
                count = 0
                for z in users[0]:
                    if(z == y):
                        break
                    count = count + 1
                txt=[]
                txt=appendData(count)
                data.append({'x':testCase_User['x'],'y': returnUserArray(count),'type':'scatter','text':txt,'name':y})
        #3. vs All
    if(selection == "vA"):
        title=testCase_User['name'] + ' vs Scotland (Age-Range and Avg)'
        data.append({'x': vsZain.ind, 'y': vsZain.age, 'type': 'bar','name': u'Age-Range(16-24)'})
        data.append({'x': vsZain.ind, 'y': vsZain.avg, 'type': 'bar','name': u'Average'})
    
    
    figure = {
        'data': data,
        'layout': {
            'title': title,
            'xaxis' : dict(
                title=Xlable,
                titlefont=dict(
                family='Oldtown',
                size=20,
                color='#742e26'
            )),
            'yaxis' : dict(
                title=Ylable,
                titlefont=dict(
                family='Oldtown',
                size=20,
                color='#742e26'
            ))
        }
    }
    return figure
    

#graph3 is for the first tab that displays data sets from NHS
@app.callback(
        dash.dependencies.Output('graph3', 'figure'),
        [dash.dependencies.Input('ind', 'value'),
        dash.dependencies.Input('ageSlider','value')])

def update_image_src2(selected_dropdown_value,slider_value):
    data = []
    if selected_dropdown_value=='ALL':
        if slider_value== 1:
            data.append({'x': BMIA.Bmi, 'y': BMIA.Age_16_24, 'type': 'bar','name': u'BMI Index(kg/m^2)'})
            data.append({'x': VEGA.Veg, 'y': VEGA.Age_16_24, 'type': 'bar','name': u'Vegetable Consumption'})
            data.append({'x': VITA.Vit, 'y': VITA.Age_16_24, 'type': 'bar','name': u'Vitamins Consumption'})
            data.append({'x': SAA.s_a, 'y': SAA.Age_16_24, 'type': 'bar','name': u'Self Assessment'})
            data.append({'x': ECA.e_c, 'y': ECA.Age_16_24, 'type': 'bar','name': u'E-Cigrattes Consumption'})
            data.append({'x': CA.c_a, 'y': CA.Age_16_24, 'type': 'bar','name': u'Cigrattes Consumption'})
            data.append({'x': ALA.a_l, 'y': ALA.Age_16_24, 'type': 'bar','name': u'Alcohol Consumption'})       
            data.append({'x': ASA.a_s, 'y': ASA.Age_16_24, 'type': 'bar','name': u'Activity Summary'})
        if slider_value== 2:
            data.append({'x': BMIA.Bmi, 'y': BMIA.Age_25_34, 'type': 'bar','name': u'BMI Index(kg/m^2)'})
            data.append({'x': VEGA.Veg, 'y': VEGA.Age_25_34, 'type': 'bar','name': u'Vegetable Consumption'})
            data.append({'x': VITA.Vit, 'y': VITA.Age_25_34, 'type': 'bar','name': u'Vitamins Consumption'})
            data.append({'x': SAA.s_a, 'y': SAA.Age_25_34, 'type': 'bar','name': u'Self Assessment'})
            data.append({'x': ECA.e_c, 'y': ECA.Age_25_34, 'type': 'bar','name': u'E-Cigrattes Consumption'})
            data.append({'x': CA.c_a, 'y': CA.Age_25_34, 'type': 'bar','name': u'Cigrattes Consumption'})
            data.append({'x': ALA.a_l, 'y': ALA.Age_25_34, 'type': 'bar','name': u'Alcohol Consumption'})       
            data.append({'x': ASA.a_s, 'y': ASA.Age_25_34, 'type': 'bar','name': u'Activity Summary'})
        if slider_value== 3:
            data.append({'x': BMIA.Bmi, 'y': BMIA.Age_35_44, 'type': 'bar','name': u'BMI Index(kg/m^2)'})
            data.append({'x': VEGA.Veg, 'y': VEGA.Age_35_44, 'type': 'bar','name': u'Vegetable Consumption'})
            data.append({'x': VITA.Vit, 'y': VITA.Age_35_44, 'type': 'bar','name': u'Vitamins Consumption'})
            data.append({'x': SAA.s_a, 'y': SAA.Age_35_44, 'type': 'bar','name': u'Self Assessment'})
            data.append({'x': ECA.e_c, 'y': ECA.Age_35_44, 'type': 'bar','name': u'E-Cigrattes Consumption'})
            data.append({'x': CA.c_a, 'y': CA.Age_35_44, 'type': 'bar','name': u'Cigrattes Consumption'})
            data.append({'x': ALA.a_l, 'y': ALA.Age_35_44, 'type': 'bar','name': u'Alcohol Consumption'})       
            data.append({'x': ASA.a_s, 'y': ASA.Age_35_44, 'type': 'bar','name': u'Activity Summary'})
        if slider_value== 4:
            data.append({'x': BMIA.Bmi, 'y': BMIA.Age_45_54, 'type': 'bar','name': u'BMI Index(kg/m^2)'})
            data.append({'x': VEGA.Veg, 'y': VEGA.Age_45_54, 'type': 'bar','name': u'Vegetable Consumption'})
            data.append({'x': VITA.Vit, 'y': VITA.Age_45_54, 'type': 'bar','name': u'Vitamins Consumption'})
            data.append({'x': SAA.s_a, 'y': SAA.Age_45_54, 'type': 'bar','name': u'Self Assessment'})
            data.append({'x': ECA.e_c, 'y': ECA.Age_45_54, 'type': 'bar','name': u'E-Cigrattes Consumption'})
            data.append({'x': CA.c_a, 'y': CA.Age_45_54, 'type': 'bar','name': u'Cigrattes Consumption'})
            data.append({'x': ALA.a_l, 'y': ALA.Age_45_54, 'type': 'bar','name': u'Alcohol Consumption'})       
            data.append({'x': ASA.a_s, 'y': ASA.Age_45_54, 'type': 'bar','name': u'Activity Summary'})
        if slider_value== 5:
            data.append({'x': BMIA.Bmi, 'y': BMIA.Age_55_64, 'type': 'bar','name': u'BMI Index(kg/m^2)'})
            data.append({'x': VEGA.Veg, 'y': VEGA.Age_55_64, 'type': 'bar','name': u'Vegetable Consumption'})
            data.append({'x': VITA.Vit, 'y': VITA.Age_55_64, 'type': 'bar','name': u'Vitamins Consumption'})
            data.append({'x': SAA.s_a, 'y': SAA.Age_55_64, 'type': 'bar','name': u'Self Assessment'})
            data.append({'x': ECA.e_c, 'y': ECA.Age_55_64, 'type': 'bar','name': u'E-Cigrattes Consumption'})
            data.append({'x': CA.c_a, 'y': CA.Age_55_64, 'type': 'bar','name': u'Cigrattes Consumption'})
            data.append({'x': ALA.a_l, 'y': ALA.Age_55_64, 'type': 'bar','name': u'Alcohol Consumption'})       
            data.append({'x': ASA.a_s, 'y': ASA.Age_55_64, 'type': 'bar','name': u'Activity Summary'})
        if slider_value== 6:
            data.append({'x': BMIA.Bmi, 'y': BMIA.Age_65_74, 'type': 'bar','name': u'BMI Index(kg/m^2)'})
            data.append({'x': VEGA.Veg, 'y': VEGA.Age_65_74, 'type': 'bar','name': u'Vegetable Consumption'})
            data.append({'x': VITA.Vit, 'y': VITA.Age_65_74, 'type': 'bar','name': u'Vitamins Consumption'})
            data.append({'x': SAA.s_a, 'y': SAA.Age_65_74, 'type': 'bar','name': u'Self Assessment'})
            data.append({'x': ECA.e_c, 'y': ECA.Age_65_74, 'type': 'bar','name': u'E-Cigrattes Consumption'})
            data.append({'x': CA.c_a, 'y': CA.Age_65_74, 'type': 'bar','name': u'Cigrattes Consumption'})
            data.append({'x': ALA.a_l, 'y': ALA.Age_65_74, 'type': 'bar','name': u'Alcohol Consumption'})       
            data.append({'x': ASA.a_s, 'y': ASA.Age_65_74, 'type': 'bar','name': u'Activity Summary'})
        if slider_value== 7:
            data.append({'x': BMIA.Bmi, 'y': BMIA.Age_75, 'type': 'bar','name': u'BMI Index(kg/m^2)'})
            data.append({'x': VEGA.Veg, 'y': VEGA.Age_75, 'type': 'bar','name': u'Vegetable Consumption'})
            data.append({'x': VITA.Vit, 'y': VITA.Age_75, 'type': 'bar','name': u'Vitamins Consumption'})
            data.append({'x': SAA.s_a, 'y': SAA.Age_75, 'type': 'bar','name': u'Self Assessment'})
            data.append({'x': ECA.e_c, 'y': ECA.Age_75, 'type': 'bar','name': u'E-Cigrattes Consumption'})
            data.append({'x': CA.c_a, 'y': CA.Age_75, 'type': 'bar','name': u'Cigrattes Consumption'})
            data.append({'x': ALA.a_l, 'y': ALA.Age_75, 'type': 'bar','name': u'Alcohol Consumption'})       
            data.append({'x': ASA.a_s, 'y': ASA.Age_75, 'type': 'bar','name': u'Activity Summary'})
        if slider_value== 8:
            data.append({'x': BMIA.Bmi, 'y': BMIA.Avg, 'type': 'bar','name': u'BMI Index(kg/m^2)'})
            data.append({'x': VEGA.Veg, 'y': VEGA.Avg, 'type': 'bar','name': u'Vegetable Consumption'})
            data.append({'x': VITA.Vit, 'y': VITA.Avg, 'type': 'bar','name': u'Vitamins Consumption'})
            data.append({'x': SAA.s_a, 'y': SAA.Avg, 'type': 'bar','name': u'Self Assessment'})
            data.append({'x': ECA.e_c, 'y': ECA.Avg, 'type': 'bar','name': u'E-Cigrattes Consumption'})
            data.append({'x': CA.c_a, 'y': CA.Avg, 'type': 'bar','name': u'Cigrattes Consumption'})
            data.append({'x': ALA.a_l, 'y': ALA.Avg, 'type': 'bar','name': u'Alcohol Consumption'})       
            data.append({'x': ASA.a_s, 'y': ASA.Avg, 'type': 'bar','name': u'Activity Summary'})         
        title='All Categories'
        Xlable='Categories'
        Ylable='Frequency'
    if selected_dropdown_value=='B':
        if slider_value== 1:
            data.append({'x': BMI.Bmi, 'y': BMI.Age_16_24, 'type': 'bar','name': u'Male'})
            data.append({'x': BMI.Bmi,'y': BMIF.Age_16_24, 'type': 'bar','name': u'Female'})
        elif slider_value== 2:
            data.append({'x': BMI.Bmi, 'y': BMI.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': BMI.Bmi,'y': BMIF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': BMI.Bmi, 'y': BMI.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': BMI.Bmi,'y': BMIF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': BMI.Bmi, 'y': BMI.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': BMI.Bmi,'y': BMIF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': BMI.Bmi, 'y': BMI.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': BMI.Bmi,'y': BMIF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': BMI.Bmi, 'y': BMI.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': BMI.Bmi,'y': BMIF.Age_65_74, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': BMI.Bmi, 'y': BMI.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': BMI.Bmi,'y': BMIF.Age_75, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': BMI.Bmi,'y':  BMI.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': BMIF.Bmi,'y':  BMIF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='BMI'
        Xlable='BMI(kg/m2)'
        Ylable='Frequency'
    if selected_dropdown_value== 'F':
        if slider_value== 1:
            data.append({'x': VEG.Veg, 'y': VEG.Age_16_24, 'type': 'scatter', 'name': u'Male'})
            data.append({'x': VEG.Veg,'y': VEGF.Age_16_24, 'type': 'scatter', 'name': u'Female'})
        elif slider_value== 2:
            data.append({'x': VEG.Veg, 'y': VEG.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VEG.Veg,'y': VEGF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': VEG.Veg, 'y': VEG.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VEG.Veg,'y': VEGF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': VEG.Veg, 'y': VEG.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VEG.Veg,'y': VEGF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': VEG.Veg, 'y': VEG.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VEG.Veg,'y': VEGF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': VEG.Veg, 'y': VEG.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VEG.Veg,'y': VEGF.Age_65_74, 'type': 'scatter', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': VEG.Veg, 'y': VEG.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VEG.Veg,'y': VEGF.Age_75, 'type': 'scatter', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': VEG.Veg,'y':  VEG.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': VEG.Veg,'y':  VEGF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='Fruit & Veg Consumption'
        Xlable='Portions per day'
        Ylable='Frequency'       
    if selected_dropdown_value== 'V':
        if slider_value== 1:
            data.append({'x': VIT.Vit, 'y': VIT.Age_16_24, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VIT.Vit,'y':  VITF.Age_16_24, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 2:
            data.append({'x': VIT.Vit, 'y': VIT.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VIT.Vit,'y': VITF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': VIT.Vit, 'y': VIT.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VIT.Vit,'y': VITF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': VIT.Vit, 'y': VIT.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VIT.Vit,'y': VITF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': VIT.Vit, 'y': VIT.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VIT.Vit,'y': VITF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': VIT.Vit, 'y': VIT.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VIT.Vit,'y': VITF.Age_65_74, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': VIT.Vit, 'y': VIT.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': VIT.Vit,'y': VITF.Age_75, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': VIT.Vit,'y':  VIT.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': VIT.Vit,'y':  VITF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='Vitamins & Mineral Consumption'
        Xlable='Suplements intake'
        Ylable='Frequency'
        
    if selected_dropdown_value== 'S':
        if slider_value== 1:
            data.append({'x': SA.s_a, 'y':  SA.Age_16_24, 'type': 'bar', 'name': u'Male'})
            data.append({'x': SA.s_a,'y':  SAF.Age_16_24, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 2:
            data.append({'x': SA.s_a, 'y': SA.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': SA.s_a,'y': SAF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': SA.s_a, 'y': SA.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': SA.s_a,'y': SAF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': SA.s_a, 'y': SA.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': SA.s_a,'y': SAF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': SA.s_a, 'y': SA.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': SA.s_a,'y': SAF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': SA.s_a, 'y': SA.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': SA.s_a,'y': SAF.Age_65_74, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': SA.s_a, 'y': SA.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': SA.s_a,'y': SAF.Age_75, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': SA.s_a,'y':  SA.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': SA.s_a,'y':  SAF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='Self Assessed General Health'
        Xlable='Self-Assessment'
        Ylable='Frequency'

    if selected_dropdown_value== 'AL':
        if slider_value== 1:
            data.append({'x': AL.a_l, 'y':  AL.Age_16_24, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AL.a_l,'y':  ALF.Age_16_24, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 2:
            data.append({'x': AL.a_l, 'y': AL.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AL.a_l,'y': ALF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': AL.a_l, 'y': AL.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AL.a_l,'y': ALF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': AL.a_l, 'y': AL.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AL.a_l,'y': ALF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': AL.a_l, 'y': AL.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AL.a_l,'y': ALF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': AL.a_l, 'y': AL.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AL.a_l,'y': ALF.Age_65_74, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': AL.a_l, 'y': AL.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AL.a_l,'y': ALF.Age_75, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': AL.a_l,'y':  AL.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': AL.a_l,'y':  ALF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='Alcohol Consumption'
        Xlable='Alcohol units per week'
        Ylable='Frequency'
    if selected_dropdown_value== 'C':
        if slider_value== 1:
            data.append({'x': C.c_a, 'y':  C.Age_16_24, 'type': 'bar', 'name': u'Male'})
            data.append({'x': C.c_a,'y':  CF.Age_16_24, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 2:
            data.append({'x': C.c_a, 'y': C.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': C.c_a,'y': CF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': C.c_a, 'y': C.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': C.c_a,'y': CF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': C.c_a, 'y': C.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': C.c_a,'y': CF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': C.c_a, 'y': C.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': C.c_a,'y': CF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': C.c_a, 'y': C.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': C.c_a,'y': CF.Age_65_74, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': C.c_a, 'y': C.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': C.c_a,'y': CF.Age_75, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': C.c_a,'y':  C.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': C.c_a,'y':  CF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='Cigrattes'
        Xlable='Levels'
        Ylable='Frequency'
        
    if selected_dropdown_value== 'EC':
        if slider_value== 1:
            data.append({'x': EC.e_c, 'y':  EC.Age_16_24, 'type': 'bar', 'name': u'Male'})
            data.append({'x': EC.e_c,'y':  ECF.Age_16_24, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 2:
            data.append({'x': EC.e_c, 'y': EC.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': EC.e_c,'y': ECF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': EC.e_c, 'y': EC.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': EC.e_c,'y': ECF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': EC.e_c, 'y': EC.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': EC.e_c,'y': ECF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': EC.e_c, 'y': EC.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': EC.e_c,'y': ECF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': EC.e_c, 'y': EC.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': EC.e_c,'y': ECF.Age_65_74, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': EC.e_c, 'y': EC.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': EC.e_c,'y': ECF.Age_75, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': EC.e_c,'y':  EC.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': EC.e_c,'y':  ECF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='E-Cigrattes'
        Xlable='Levels'
        Ylable='Frequency'  

    if selected_dropdown_value== 'D':
        if slider_value== 1:
            data.append({'x': DA.d_a, 'y':  DA.Age_16_24, 'type': 'bar', 'name': u'Male'})
            data.append({'x': DA.d_a,'y':  DAF.Age_16_24, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 2:
            data.append({'x': DA.d_a, 'y': DA.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': DA.d_a,'y': DAF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': DA.d_a, 'y': DA.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': DA.d_a,'y': DAF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': DA.d_a, 'y': DA.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': DA.d_a,'y': DAF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': DA.d_a, 'y': DA.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': DA.d_a,'y': DAF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': DA.d_a, 'y': DA.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': DA.d_a,'y': DAF.Age_65_74, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': DA.d_a, 'y': DA.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': DA.d_a,'y': DAF.Age_75, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': DA.d_a,'y':  DA.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': DA.d_a,'y':  DAF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='Detailed Activity'
        Xlable='Activity Type'
        Ylable='Frequency'

    if selected_dropdown_value== 'A':
        if slider_value== 1:
            data.append({'x': AS.a_s, 'y':  AS.Age_16_24, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AS.a_s,'y':  ASF.Age_16_24, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 2:
            data.append({'x': AS.a_s, 'y': AS.Age_25_34, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AS.a_s,'y': ASF.Age_25_34, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 3:
            data.append({'x': AS.a_s, 'y': AS.Age_35_44, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AS.a_s,'y': ASF.Age_35_44, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 4:
            data.append({'x': AS.a_s, 'y': AS.Age_45_54, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AS.a_s,'y': ASF.Age_45_54, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 5:
            data.append({'x': AS.a_s, 'y': AS.Age_55_64, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AS.a_s,'y': ASF.Age_55_64, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 6:
            data.append({'x': AS.a_s, 'y': AS.Age_65_74, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AS.a_s,'y': ASF.Age_65_74, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 7:
            data.append({'x': AS.a_s, 'y': AS.Age_75, 'type': 'bar', 'name': u'Male'})
            data.append({'x': AS.a_s,'y': ASF.Age_75, 'type': 'bar', 'name': u'Female'})
        elif slider_value== 8:
            data.append({'x': AS.a_s,'y':  AS.Avg, 'type': 'scatter', 'name': u'Male(Average)'})
            data.append({'x': AS.a_s,'y':  ASF.Avg, 'type': 'scatter', 'name': u'Female(Average)'})
        title='Activity Summary (MVPA)'
        Xlable='Levels'
        Ylable='Frequency'
        
    figure = {
        'data': data,
        'layout': {
            'title': title,
            'xaxis' : dict(
                title=Xlable,
                titlefont=dict(
                family='oldtown',
                size=20,
                color='#742e26'
            )),
            'yaxis' : dict(
                title=Ylable,
                titlefont=dict(
                family='oldtown',
                size=20,
                color='#742e26'
            ))
        }
    }
    return figure
if __name__ == '__main__':
    app.run_server(debug=True)