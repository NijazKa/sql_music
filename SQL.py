import psycopg2

conn = psycopg2.connect(database='netology_db', user='postgres', password=7777777)


def create_db() -> None: # Создем базу данных (можно название прокинуть, если надо создавать разные базы)
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS user_name (
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(40) NOT null,
                        last_name VARCHAR(40) not null,
                        email VARCHAR(40) UNIQUE not null,
                        phone VARCHAR(60)
                        );
                    """)
    conn.commit()
    conn.close()

def get_user_id(email: str) -> int: # Служебная функция получения Id пользователя по уникальному email
    with conn.cursor() as cur:
        cur.execute(""" 
                    SELECT id FROM user_name
                    WHERE email = %s
                    """, (email,))
        result = cur.fetchone()
        
        if result is None:
            return f'Пользователя с e-mail: {email} не сущетсвует' 
        else:
            return result[0]
    conn.close() 

def user_add(first_name: str, last_name: str, email: str, phone=None): # Добавление пользователя
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO user_name(first_name, last_name, email, phone)
                    VALUES(%s, %s, %s, %s);        
                    """, (first_name, last_name, email, phone))
        conn.commit()
        cur.execute("""
        SELECT * FROM user_name;
        """)
        print(cur.fetchall())
    conn.close()

def phone_add(user_id: int, new_phone: str): # Добавление телефона для пользователя
    with conn.cursor() as cur:
        cur.execute("""
                    UPDATE user_name
                    SET phone = COALESCE(CONCAT(phone, ' '), '') || %s 
                    WHERE id = %s;
                    """, (new_phone, user_id))
        conn.commit()
        cur.execute("""
                    SELECT * FROM user_name
                    WHERE id = %s 
                    """, (user_id,))
        print(cur.fetchone())
    conn.close()

def user_update(user_id: int, first_name=None, last_name=None, email=None): # обновление данных пользователя
    with conn.cursor() as cur:
        if first_name:
            cur.execute("""
                        UPDATE user_name SET first_name=%s WHERE id=%s;
                        """, (first_name, user_id)
                        )
        if last_name:
            cur.execute("""
                        UPDATE user_name SET last_name=%s WHERE id=%s;
                        """, (last_name, user_id)
                        )
        if email:
            cur.execute("""
                        UPDATE user_name SET email=%s WHERE id=%s;
                        """, (email, user_id)
                        )   
        conn.commit()
    conn.close()
      
def phone_replace(user_id: int, old_phone: str, new_phone=None): # Объединил функции замены и удаления номера
    with conn.cursor() as cur:
        if new_phone:
            cur.execute("""
                        UPDATE user_name
                        SET phone = REPLACE(phone, %s, %s)
                        WHERE phone LIKE %s AND id = %s;
                        """, (old_phone, new_phone, '%' + old_phone + '%', user_id))
        else:
            cur.execute("""
                        UPDATE user_name
                        SET phone = REPLACE(phone, %s, '')
                        WHERE phone LIKE %s AND id = %s;
                        """, (old_phone, '%' + old_phone + '%', user_id))
        conn.commit()
    conn.close()

def user_delete(user_id: int): # Удаление пользователя
    with conn.cursor() as cur:
        cur.execute("""
                    DELETE FROM user_name
                    WHERE id = %s;
                    """, (user_id,))
        conn.commit()
    conn.close()

def user_search(first_name=None, last_name=None, email=None, phone=None): # поиск пользователя по определенным данным
    with conn.cursor() as cur:
        if first_name:
            cur.execute("""
                        SELECT * FROM user_name WHERE first_name=%s;
                        """, (first_name,))
            result = cur.fetchall()
            if result == []:
                print('Такой пользоватль не найден')
            else:
                print(result)
            return

        elif last_name:
            cur.execute("""
                        SELECT * FROM user_name WHERE last_name=%s;
                        """, (last_name,))
            result = cur.fetchall()
            if result == []:
                print('Такой пользоватль не найден')
            else:
                print(result)
            return
        
        elif email:
            cur.execute("""
                        SELECT * FROM user_name WHERE email=%s;
                        """, (email,))
            result = cur.fetchall()
            if result == []:
                print('Такой пользоватль не найден')
            else:
                print(result)
            return      
        
        elif phone:
            cur.execute("""
                        SELECT * FROM user_name WHERE phone LIKE %s;
                        """, ('%' + phone + '%',))
            result = cur.fetchall()
            if result == []:
                print('Такой пользоватль не найден')
            else:
                print(result)
            return       
        
        else:
            return 'Такой пользоватль не найден'
    conn.close()




# Функция, создающая структуру БД (таблицы).
create_db()

# # Функция, позволяющая добавить нового клиента.
user_add('Alexandr', 'Petrov', 'alex@mail.ru', '+7932232323')
user_add('Sergey', 'Ivanov', 'serg@mail.ru')
user_add('Ivan', 'Karpov', 'ivan@mail.ru', '+7932432323')

# # Функция, позволяющая добавить телефон для существующего клиента.
phone_add(2, '+79872345000')
phone_add(3, '+79872225540')

# # Функция, позволяющая изменить данные о клиенте.
user_update(1, last_name='Sidorov')

# Функция, позволяющая удалить телефон для существующего клиента.
phone_replace(3, '+7932432323')

# Функция, позволяющая удалить существующего клиента.
user_delete(1)

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону
user_search(email='ivan@mail.ru')
user_search(last_name='Ivanov')
