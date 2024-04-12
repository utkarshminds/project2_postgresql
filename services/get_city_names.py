
def city_names(conn):
    '''
    Table name 'city'
    column name is 'name'
    
    Get all city names, population

    Sample queries

    cursor.execute("""
            SELECT name, rollno
            FROM students
            WHERE date = %s AND subject = %s
        """, (date, subject))
        rows = cursor.fetchall()


    '''

    try:
        conn.execute(
            """
            SELECT name FROM city
            """
        )
        rows = conn.fetchall()

        '''
        rows = [('kabul',), ('mumbai',), ... ]

        rows_data = ['kabul', 'mumbai', ...]
        '''

        rows_data = [city[0] for city in rows]

        return rows_data 

    except Exception as e:
        print(f'unable to execute query {e}')
        return None

