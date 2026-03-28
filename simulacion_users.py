from datetime import datetime, timedelta
import random


def simular_users(numero_users):

    users_list = ["admin","student"]
    role_list = [U1,U2]
    email_domains = ["example.com", "test.com", "sample.com"]
    password_list = ["password123", "admin2024", "user2024"]
    users = []

    for i in range(numero_users):
        fechaSimulada = fechaInicial + timedelta(days=random.randint(0, 360))
        user={
            "id": random.randint(1,1000),
            "role": random.choice(role_list),
            "name": random.choice(users_list),
            "email": random.choice(email_domains),
            "password": random.choice(password_list),
            "fechaCreacion": fechaSimulada.strftime("%Y-%m-%d")
        }
        users.append(user)
    return users

