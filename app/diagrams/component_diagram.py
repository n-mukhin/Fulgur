from graphviz import Digraph

def generate_component_diagram():
    dot = Digraph(name='Component Diagram', format='svg')
    dot.attr(rankdir='LR', fontsize='10')

 
    dot.attr('node', shape='rectangle', style='filled', color='lightblue')

    dot.node('UI', 'User Interface')
    dot.node('Auth', 'Authentication Service')
    dot.node('Battery', 'Battery Management Module')
    dot.node('Navigation', 'Navigation Module')
    dot.node('Charging', 'Charging Controller')
    dot.node('Telemetry', 'Telemetry Service')
    dot.node('Database', 'Database')
    dot.node('API', 'REST API')
    dot.node('Notification', 'Notification Service')

    dot.node('GPS_Service', 'External GPS Service', shape='ellipse', style='filled', color='lightgrey')
    dot.node('Charging_Stations', 'Charging Stations', shape='ellipse', style='filled', color='lightgrey')
    dot.node('Weather_API', 'Weather API', shape='ellipse', style='filled', color='lightgrey')

    dot.edge('UI', 'Auth', label='Authenticate')
    dot.edge('UI', 'API', label='API Requests')
    dot.edge('API', 'Battery', label='Manage Battery')
    dot.edge('API', 'Navigation', label='Manage Navigation')
    dot.edge('API', 'Charging', label='Manage Charging')
    dot.edge('API', 'Telemetry', label='Send Telemetry')
    dot.edge('API', 'Notification', label='Send Notifications')
    dot.edge('Battery', 'Database', label='Read/Write Data')
    dot.edge('Navigation', 'GPS_Service', label='Fetch Location')
    dot.edge('Navigation', 'Weather_API', label='Fetch Weather')
    dot.edge('Charging', 'Charging_Stations', label='Connect/Disconnect')
    dot.edge('Telemetry', 'Database', label='Store Data')
    dot.edge('Notification', 'UI', label='Display Notifications')

    return dot.pipe().decode('utf-8')
