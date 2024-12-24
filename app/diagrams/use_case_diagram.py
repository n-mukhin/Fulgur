from graphviz import Digraph

def generate_use_case_diagram():
    dot = Digraph(name='Use Case Diagram', format='svg')
    dot.attr(rankdir='LR', fontsize='5', dpi='72')
    dot.attr('graph', nodesep='0.1', ranksep='0.1')
    dot.node_attr.update(fontsize='5', width='0.3', height='0.3', penwidth='0.5')  
    dot.edge_attr.update(penwidth='0.5', arrowsize='0.5')  

    dot.node('Driver', 'Driver', shape='actor')
    dot.node('Service_Tech', 'Service Technician', shape='actor')
    dot.node('Administrator', 'Administrator', shape='actor')
    dot.node('External_API', 'External API', shape='actor')
    
    with dot.subgraph(name='cluster_Fulgur') as c:
        c.attr(style='dashed', color='blue', label='Fulgur System', fontsize='5')
        c.node_attr.update(shape='ellipse', style='filled', color='lightyellow')
        use_cases = [
            'Monitor_Battery', 'Navigate_Routes', 'Initiate_Charging', 'Receive_Alerts',
            'Update_Firmware', 'Manage_Users', 'Fetch_Weather', 'Access_Telemetry',
            'Schedule_Maintenance', 'View_Usage_Statistics'
        ]
        for uc in use_cases:
            c.node(uc, uc.replace('_', ' '))

    edges = {
        'Driver': ['Monitor_Battery', 'Navigate_Routes', 'Initiate_Charging', 'Receive_Alerts'],
        'Service_Tech': ['Update_Firmware', 'Access_Telemetry', 'Schedule_Maintenance'],
        'Administrator': ['Manage_Users', 'View_Usage_Statistics', 'Access_Telemetry'],
        'External_API': ['Fetch_Weather']
    }
    for actor, ucs in edges.items():
        for uc in ucs:
            dot.edge(actor, uc)

    with dot.subgraph() as s:
        s.attr(rank='same')
        s.edge('Driver', 'Service_Tech', style='invis')
        s.edge('Service_Tech', 'Administrator', style='invis')
        s.edge('Administrator', 'External_API', style='invis')

    return dot.pipe().decode('utf-8')

if __name__ == "__main__":
    diagram = generate_use_case_diagram()
    with open("use_case_diagram.svg", "w") as f:
        f.write(diagram)
