from rolepermissions.roles import AbstractUserRole


class Organizador(AbstractUserRole):
    ...


class Cliente(AbstractUserRole):
    available_permissions = {
        'change_cliente':True,
        'add_bilhete': True,
        'view_bilhete': True
    }