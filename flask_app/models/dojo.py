# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

# model the class after the user table from our database
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas =[]
    # Now we use class methods to query our database
    @classmethod
    def get_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = (cls(results[0]))
        for n in dojo:
            dojo.ninjas.append(Ninja(n))
        return dojo

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
            # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
            # Create an empty list to append our instances of users
        dojos = []
            # Iterate over the db results and create instances of users with cls.
        for doj in results:
            print (cls(doj))
            print (doj)
            dojos.append( cls(doj) )
        return dojos

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES (%(name)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def get_single(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(result)
        print((result[0]))
        return cls(result[0])

    @classmethod
    def update_dojo(cls, data):
        query ="UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data)
        return result
    
    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data  )
        print(result)
        return result