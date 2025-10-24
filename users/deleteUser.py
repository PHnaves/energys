
# Função para deletar um usuário
from Connection.connection import connect_database

def deletar_usuario(id_usuario):
    connection = connect_database()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        connection.commit()
        print("Usuário deletado com sucesso!")
        connection.close()