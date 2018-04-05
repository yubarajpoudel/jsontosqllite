
"""
Developed by: Yubaraj Poudel
yubarajpoudel708@gmail.com
convert the json file to sqllite file
provide the json file
prvide the name of the output file
"""
import sys
import sqlite3

def __convert(*args):
	try:
		conn = sqlite3.connect(args[2])
		c = conn.cursor()
		print(sqlite3.version)	
		print("....................................\n")
		print("Choose the option\n")
		print("1. Create new table\n")
		print("2. Insert data into table\n")
		print("3. delete table\n")

		print(".............................")

		choice = int(input("Enter your choice"))
		if choice == 1:
			tableName = input("Enter the table name :\t")
			schemas= input("Enter the schema separated by space ( for eg name,phone):\t")
			print("tableName = {}, schemas = {}".format(tableName, schemas))
			# Create table
			sql = "CREATE TABLE {}(".format(tableName)
			first = True
			for schema in schemas.split(","):
				if not first:
					sql = sql + ","

				sql = sql + "{} text".format(schema)
				first = False

			sql = sql+")"
			print(sql)
			c.execute(sql)
			conn.commit()
			conn.close()
			print("{} created successfully ".format(tableName))			
			pass
		elif choice == 2:
			pass
		elif choice == 3:
			pass
	except:
	 	print("File exception")

def main():
	print("arguments lenght = %s"%(str(len(sys.argv))))
	try:
		if len(sys.argv) == 3:
			print("valid")
			print(sys.argv[1])
			if(sys.argv[1].lower().endswith('.json')):
				with open(sys.argv[1], "r") as inputJSON:
					data = inputJSON.read()
					
				dbName = input("Enter Preferred DatabaseName \n")
				print("Database Name = {}".format(dbName))
				destination = sys.argv[2]
				# with open(destination, "w") as outputFile:
				__convert(data, dbName, destination)
				# print(data)
			else:
				print("invalid input jsonfile")
		else:
			print("invalid")
	except:
		print("Error in providing the arguments")

if __name__ == '__main__':
  main()

