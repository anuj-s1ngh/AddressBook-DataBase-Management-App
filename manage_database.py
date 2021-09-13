import sqlite3


def create_db_connection():
    # create/connect to sqlite3 db
    conn = sqlite3.connect(
        "address_book.db"
    )
    return conn


def create_db_cursor(conn):
    # create cursor
    c = conn.cursor()
    return c


def commit_db_changes(conn):
    # commit changes
    conn.commit()


def close_db_connection(conn):
    # close connection
    conn.close()


def create_db_table():
    # create table
    conn = create_db_connection()
    c = create_db_cursor(conn)

    c.execute(
        """
        CREATE TABLE addresses (
            first_name text,
            last_name text,
            street text,
            city text,
            state text,
            zipcode integer
        );
        """
    )

    commit_db_changes(conn)
    close_db_connection(conn)


def reset_table_index():
    conn = create_db_connection()
    c = create_db_cursor(conn)

    c.execute("UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'addresses';")

    commit_db_changes(conn)
    close_db_connection(conn)


def create_new_record(first_name, last_name, street, city, state, zipcode):
    # Insert into table
    conn = create_db_connection()
    c = create_db_cursor(conn)

    dict_to_insert = dict(
            first_name=first_name,
            last_name=last_name,
            street=street,
            city=city,
            state=state,
            zipcode=zipcode
        )
    # print(dict_to_insert)
    c.execute(
        """
        INSERT INTO addresses VALUES (:first_name, :last_name, :street, :city, :state, :zipcode);
        """,dict_to_insert
    )

    commit_db_changes(conn)
    close_db_connection(conn)


def update_record(dict_to_insert):
    # Insert into table
    conn = create_db_connection()
    c = create_db_cursor(conn)

    # print(dict_to_insert)
    c.execute(
        """
        UPDATE addresses SET first_name=:first_name, last_name=:last_name, street=:street, city=:city, state=:state, zipcode=:zipcode WHERE oid=:oid_num;
        """,dict_to_insert
    )

    commit_db_changes(conn)
    close_db_connection(conn)


def read_all_records():
    conn = create_db_connection()
    c = create_db_cursor(conn)

    c.execute("SELECT oid, * FROM addresses;")

    record_list = c.fetchall()

    commit_db_changes(conn)
    close_db_connection(conn)

    return record_list


def delete_record(oid_num):
    conn = create_db_connection()
    c = create_db_cursor(conn)

    c.execute("DELETE FROM addresses WHERE oid=:oid_num;",
        dict(oid_num=oid_num)
    )

    record_list = c.fetchall()

    commit_db_changes(conn)
    close_db_connection(conn)

    return record_list