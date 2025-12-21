def greet(name):
    
    return f'Hello,{name}!Welcome to Data Science From Scratch'
def normalize_data(values):
    '''
    Experimental normalizatio(min-max scaling)
    Warning:Expereimental logic --- not 
    production-ready
    '''
    min_val=min(values)
    max_val=max(values)
    return [(v-min_val)/(max_val-min_val)for v in values]
    