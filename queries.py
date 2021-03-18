get_users = """
	SELECT id, name FROM USERS
"""

get_user_by_id = """
	SELECT id, name, encoded_array FROM USERS WHERE id = %(id)s
"""

get_user_by_name = """
	SELECT id, name, encoded_array FROM USERS WHERE name = %(name)s
"""

get_user_passwords = """
	SELECT description, password FROM PASSWORDS WHERE user_id = %(user_id)s 
"""

add_password = """
	INSERT INTO PASSWORDS(user_id, password, description) VALUES(%(user_id)s, %(password)s, %(description)s)
"""


add_user = """
	INSERT INTO USERS(name, encoded_array) VALUES(%(name)s, %(encoded_array)s)
"""