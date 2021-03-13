#FIRST VERSION , NOT FINAL VERSION , PLEASE USE CAREFULLY


PLUGIN_METADATA = {
    'id': 'save',
    'version': 'BETA-0.01',
    'name': 'Save',
    'author': 'A_Words',
    'link': 'https://github.com/A-Words/Save'
}


def save():
	server.execute('/save')


def on_load(server: ServerInterface, prev):
	server.register_help_message('!!save', '保存世界')
	server.register_command(Literal('!!save').runs(save))
