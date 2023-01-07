import random
import instruments as inst
import permission

channels = permission.channels
chann_req = False
roles = permission.roles
rol_req = False

def get_response(message: str, data, client) -> str:
    p_message = message.lower()
    global chann_req
    global rol_req

    if p_message == 'привет':
        return 'Привет!'
    
    if p_message == 'доступ':
        return f'Бот доступен для этих ролей `{roles}`'

    if p_message == 'изменит_доступ':
        rol_req = True
        return 'Сначала напишите слово `удалить` или `добавить` потом `название роли`'

    if p_message == 'помощь' or p_message == 'помошь':
        return '`Помогу чем смогу!.`'
    
    if p_message == 'привет, кто играть?':
        return f'Привет {data.author.mention}, возьми игровую роль вот тут <#1058155155608043602>'
    
    if p_message == 'канали' or p_message == 'каналы':
        return f'Доступные каналы `{channels}`'
    
    if p_message == 'изменить_каналы' or p_message == 'изменить_канали' or p_message == 'изменит_каналы' or p_message == 'изменит_канали':
        chann_req = True
        return 'Сначала напишите слово `удалить` или `добавить` потом `название канала`'

    if chann_req:
        flag = str(p_message.split(' ')[0])
        target_channel = str(p_message.split(' ')[1])

        if flag == 'удалить' and target_channel:
            if target_channel in channels and len(channels):
                print(f"channel {target_channel} has removed!")
                channels.remove(target_channel)
                inst.change_permission('channels', target_channel, flag)
                chann_req = False
                return f'Канал `{target_channel}` успешно удалено!.\nДоступные каналы `{channels}`'
            else:
                print("channel not found!")
                return 'Либо такого канала нет, либо в списке только этот остался'
       
        elif flag == 'добавить' and target_channel:
            if target_channel in channels:
                return f'{target_channel} есть в списке каналов!'
            else:
                channels.append(target_channel)
                inst.change_permission('channels', target_channel, flag)
                chann_req = False
                print(f"channel {target_channel} has added!")
                return f'Канал `{target_channel}` успешно добавлено!.\nДоступные каналы `{channels}`'
        chann_req = False
    
    if rol_req:
        flag = str(p_message.split(' ')[0])
        target_role = str(p_message.split(' ')[1])

        if flag == 'удалить' and target_role:
            if target_role in roles and len(roles) and target_role != 'admin':
                print(f"role {target_role} has removed!")
                roles.remove(target_role)
                inst.change_permission('roles', target_role, flag)
                rol_req = False
                return f'Роль `{target_role}` успешно удалено!.\nСуществующие роли `{roles}`'
            else:
                print("role not found!")
                return 'Либо в списке такогой роли нет либо его невозможно удалить!'
        elif flag == 'добавить' and target_role:
            if target_role in roles:
                return f'{target_role} есть в списке ролей!'
            else:
                roles.append(target_role)
                inst.change_permission('roles', target_role, flag)
                rol_req = False
                print(f"role {target_role} has added!")
                return f'Роль `{target_role}` успешно добавлено!.\nСуществующие роли `{roles}`'
        rol_req = False



    return 'Я не понял, что ты написал. Попробуйте ввести "!help".'