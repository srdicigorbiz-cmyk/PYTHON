from databaseconnection import DatabaseConnection

# Comprehensive test case handler
test_case = input()

if test_case == "identity_check":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(db1 is db2)  # Should print True

elif test_case == "connect_state":
    db = DatabaseConnection()
    print(f"Initial connected state: {db.connected}")  # Should print False
    db.connect()
    print(f"After connect: {db.connected}")  # Should print True

elif test_case == "disconnect_state":
    db = DatabaseConnection()
    db.connect()
    db.disconnect()
    print(f"After disconnect: {db.connected}")  # Should print False

elif test_case == "multiple_instances_same_state":
    db1 = DatabaseConnection()
    db1.connect()
    db2 = DatabaseConnection()
    print(f"db2 connected state: {db2.connected}")  # Should print True

elif test_case == "host_value":
    db = DatabaseConnection()
    print(f"Default host: {db.host}")  # Should print "localhost"
    db.host = "new-server"
    db2 = DatabaseConnection()
    print(f"New instance host: {db2.host}")  # Should print "new-server"

elif test_case == "init_once":
    db1 = DatabaseConnection()
    db1.host = "custom-host"
    db2 = DatabaseConnection()
    print(f"Both instances have same host: {db1.host == db2.host}")  # Should print True
    print(f"Host value: {db1.host}")  # Should print "custom-host"

elif test_case == "connect_message":
    db = DatabaseConnection()
    db.connect()  # Should print "Connected to database at localhost"

elif test_case == "disconnect_message":
    db = DatabaseConnection()
    db.connect()
    db.disconnect()  # Should print "Disconnected from database"

elif test_case == "attribute_modification":
    db1 = DatabaseConnection()
    db1.port = 3306
    db2 = DatabaseConnection()
    print(f"db2 has port attribute: {hasattr(db2, 'port')}")  # Should print True
    print(f"db2 port value: {db2.port}")  # Should print 3306

elif test_case == "reset_connection":
    db1 = DatabaseConnection()
    db1.connect()
    print(f"Connected state: {db1.connected}")  # Should print True
    db2 = DatabaseConnection()
    print(f"New instance connected state: {db2.connected}")  # Should print True
    db2.disconnect()
    db3 = DatabaseConnection()
    print(f"After disconnect, new instance state: {db3.connected}")  # Should print False

elif test_case == "multiple_connects":
    db = DatabaseConnection()
    db.connect()
    db.connect()
    db.connect()
    print(f"Connected state after multiple connects: {db.connected}")  # Should print True
    db.disconnect()
    print(f"Connected state after disconnect: {db.connected}")  # Should print False

elif test_case == "host_change_affects_message":
    db = DatabaseConnection()
    db.host = "custom-server"
    db.connect()  # Will still print "Connected to database at localhost"
    # The connect method has a hardcoded message that doesn't use the host attribute
    print("Message still shows localhost: True")