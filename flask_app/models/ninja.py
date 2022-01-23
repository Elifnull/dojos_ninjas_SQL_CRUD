# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
            # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
            # Create an empty list to append our instances of users
        ninjas = []
            # Iterate over the db results and create instances of users with cls.
        for ninja in results:
            print (cls(ninja))
            print (ninja)
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age, dojo_id , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s, %(dojo_id)s , NOW() , NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def get_single(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(result)
        print((result[0]))
        return cls(result[0])

    @classmethod
    def update_user(cls, data):
        query ="UPDATE ninjas SET first_name=%(fname)s, last_name=%(lname)s, age=%(age)s, updated_at=NOW() WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data)
        return result
    
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data)
        print(result)
        return result