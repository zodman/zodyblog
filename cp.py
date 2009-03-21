
COMPRESS_CSS = {
    'group_one': {
        'source_filenames': (   
            'static/code.css', 
            'static/default.css', 
            'static/zody.css'
            ),
        'output_filename': 'static/all.css',
    },
    
}
COMPRESS_JS = {
    'all': {
        'source_filenames': (
            'static/zodyscripts.js'
        ),
        'output_filename': 'static/all.js'
    }
}
