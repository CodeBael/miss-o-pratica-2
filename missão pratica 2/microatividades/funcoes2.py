def login_Usuario(perfil):
    if (perfil.lower() == "admin"):
        print("Bem vindo, administrador!")
    else: 
        print("Bem vindo, usuário!")

login_Usuario("Admin")
login_Usuario("admin")
login_Usuario("User")
login_Usuario("usuário")
login_Usuario("etc.")
