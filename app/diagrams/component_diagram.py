from graphviz import Digraph

def generate_component_diagram():
    dot = Digraph(comment='Electric Car Management System - Component Diagram', format='svg')
    dot.attr('node', shape='rectangle', style='filled', color='lightgrey')

    dot.node('UI', 'User Interface')
    dot.node('Battery', 'Battery Management Module')
    dot.node('Navigation', 'Navigation Module')
    dot.node('Communication', 'Communication Module')
    dot.node('Sensors', 'Vehicle Sensors')
    dot.node('GPS_Service', 'External GPS Service')
    dot.node('Charging_Service', 'Charging Station API')
    dot.node('Database', 'Database')

    dot.edges(['UIBattery', 'UINavigation', 'UICommunication'])
    dot.edge('Battery', 'Sensors', label='Data from')
    dot.edge('Navigation', 'GPS_Service', label='Uses')
    dot.edge('Communication', 'GPS_Service', label='Fetches Data')
    dot.edge('Communication', 'Charging_Service', label='Interfaces with')
    dot.edge('UI', 'Database', label='Reads/Writes')
    dot.edge('Battery', 'Database', label='Logs Data')
    dot.edge('Navigation', 'Database', label='Stores Preferences')

    return dot.pipe().decode('utf-8')
