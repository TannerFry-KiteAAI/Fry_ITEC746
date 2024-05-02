Much of the code for this API was pulled from the public repository of Frank P Moley III
https://github.com/fpmoles/itec-746

Requirements:
A Python Interpreter (I used Visual Studio Code)
Some method for running an API (I used Postman)
Database server (I used pgadmin 4)

Python requirements:
psycopg2-binary
pydantic
fastapi
fastapi-camelcase
uvicorn

1. In your database, import the schema included in this database. It includes the necessary tables and their indexes/constraints, as well as some available data for testing.
2. Install above python requirements in Python application
3. Open config file. Note environment attributes under __new__ function. Definitions:
DB_HOST: Address of host machine. Default is localhost
DB_USERNAME: Username of user for database server. Replace with your username
DB_PASSWORD: Password of user for database server. Replace with your password
DB_NAME = Name of database. Default is postgres
DB_PORT = Port number for database. Default is 5432
SCHEMA = Name of schema supplied with code.
Change Username, Password, and, if necessary, default files.

4. Open Main and Run (ctrl+shift+d in Visual Studio Code, or the triangle Play button the left pane)
5. In Postman, run GET, POST, PUT, and DELETE commands. GET, PUT, and DELETE will need the primary key of a tuple that already exists in the database. These keys will usually be uuids, with the exception of Type, which is an integer id. Run GET commands with no id to see all entities of that type that are in the database.

File paths (this is entered into Send box in Postman:
media
client
loan
hold
type

For example, to see all loans currently stored in database, enter:

localhost:8000/loan

To see details for a specific library item:

localhost:8000/media/ccb3a386-f36b-44d2-8940-74f7b6c52ad9

POST and PUT calls will require a JSON object representing the entity in the Request Body. In Postman, click on Body underneath the Send Request box, click Raw, set type to JSON, then provide the JSON object.
The object in the PUT request should match the object whose id is in the file path. The object in POST will use a generative variable for the id. The exception is Type, which will require a unique integer entered.

JSON formats:

Media:
    {
        "mid":"{{$guid}}",
        "title":"varchar",
        "dewey":"double precision",
        "location":"integer",
        "mediatype":"integer",
        "cancheck":"True/False"
    }
Client:
    {
        "cid": "{{$guid}}",
        "firstName": "varchar",
        "lastName": "varchar",
        "streetAddress": "varchar",
        "postal": "integer",
        "phone": "varchar",
        "email": "varchar",
        "pswd": "varchar"
    }
Loan:
    {
        "checkid":"{{$guid}}",
        "mediaid":"uuid",
        "clientid":"uuid"
	"dateout": "date (yyyy-mm-dd)"
	"datedue": "date (yyyy-mm-dd)"
    }
Hold:
    {
        "checkid":"{{$guid}}",
        "mediaid":"uuid",
        "clientid":"uuid"
	"holddate":"date (yyyy-mm-dd)"
	"holdqueue":"integer"
    }
Type:
    {
        "typeid": "integer",
        "mediaType": "varchar",
        "checkoutTime": "integer"
    }

{{$guid}} is a generative variable that will create a new, random uuid value. Use this variable when sending a POST request, replace with the known uuid when sending a PUT request.
Loan and Hold contain programatially defined attributes (dateout / datedue, and holddate / holdqueue, respectively). These are not necessary for a POST command and should be left out.
Also note, only media and type PUT commands will update the entire entity. Client update is applied on the client's password (setting to null), loan is applied to datedue, and hold is applied to holdqueue.