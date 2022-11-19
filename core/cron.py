def cron_teste():

    pessoas = (
        {'nome': 'Hercules', 'idade': 25},
        {'nome': 'Graciele', 'idade': 32},
        {'nome': 'Amanda', 'idade': 50},
        {'nome': 'Teresa', 'idade': 23},
        {'nome': 'Pablo', 'idade': 34},
    )

    for i in pessoas:
        print('PRINT >>> Pessoa: {}, Idade: {}'.format(
            i['nome'], i['idade']
        ))


cron_teste()
