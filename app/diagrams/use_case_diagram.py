from graphviz import Digraph

def generate_use_case_diagram():
    dot = Digraph(comment='Electric Car Management System - Use Case Diagram', format='svg')
    dot.attr('node', shape='ellipse')

    dot.node('Driver', 'Driver')
    dot.node('MonitorBattery', 'Monitor Battery')
    dot.node('Navigate', 'Navigate')
    dot.node('ChargeVehicle', 'Charge Vehicle')
    dot.node('UpdatePreferences', 'Update Preferences')

    dot.edge('Driver', 'MonitorBattery')
    dot.edge('Driver', 'Navigate')
    dot.edge('Driver', 'ChargeVehicle')
    dot.edge('Driver', 'UpdatePreferences')

    with dot.subgraph(name='cluster_system') as c:
        c.attr(style='dashed')
        c.node_attr.update(style='filled', color='lightblue')
        c.node('System', 'Electric Car Management System')
        c.edge('System', 'MonitorBattery')
        c.edge('System', 'Navigate')
        c.edge('System', 'ChargeVehicle')
        c.edge('System', 'UpdatePreferences')
        c.attr(label='System')

    return dot.pipe().decode('utf-8')
