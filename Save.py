from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'Save',
    'version': '0.1.1-Dev',
    'name': 'Save The Server',
    'author': [
        'A_Words',
        'SongXin233'
    ],
    'link': 'https://github.com/A-Words/Save',
}

# 插件加载、重载、卸载事件
def on_load(server, prev_module):
    if prev_module is None:
        server.logger.info('正在加载插件')
    else:
        server.logger.info('正在重载插件')

    # 插件注册指令树
    server.register_help_message('!!save', 'Save the worlds or plugins')
    server.register_command(
        Literal('!!save'). \
        then(
            Literal('all').runs(save_all)
        ). \
        then(
            Literal('world'). \
            then(Text('name'))
        ). \
        then(
            Literal('plugin'). \
            then(Text('name'))
        )
    )

#插件移除
def on_remove(server):
    server.logger.info('插件停止使用')

#发送信息
def print_message(source: CommandSource, msg, tell = True, prefix = '[Save]'):
    msg = prefix + msg
    if source.is_player and not tell:
        source.get_server().say(msg)
    else:
        source.reply(msg)

# 保存函数
def save_all(source: CommandSource):
    source.get_server().execute('save-all')
    print_message(source, '执行了保存服务器数据操作，正在保存数据！')
