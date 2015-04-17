__author__ = 'Wolfram'
import pymysql


def ins(amount):
    ### first recreate DB per SQL file
    conn = pymysql.connect(host='10.0.0.17', port=3306, user='judith', passwd='judith', db='judith')
    cur = conn.cursor()
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla viverra ex consequat, aliquet ligula vitae, molestie metus. Curabitur ultrices interdum enim quis faucibus. Etiam porta nisi sem, sed volutpat lectus condimentum nec. Nunc rhoncus consequat fringilla. Nam sed ligula vel nisl hendrerit ullamcorper vel id mi. Donec at ex sem. Mauris fermentum aliquam nunc vestibulum sagittis. Ut cursus iaculis mi vel convallis. Nulla molestie convallis purus, convallis euismod quam ultrices vel. Vestibulum quis commodo nisl, sit amet volutpat metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."

    counter = 0
    current = 0
    insert = ""
    with open("newtitles2") as file:
        for line in file:
            if counter >= amount:
                break
            a = line.rstrip()
            a = ''.join(e for e in a if e.isalnum())
            insert += "('" + a + "', '" + lorem + "'),"
            counter += 1
            current += 1
            # print(insert[:-1])
            if (current >= 10000):
                #add ID
                cur.execute("INSERT INTO viki (name, text) VALUES " + insert[:-1] + ";")
                current = 0
                insert = ""
                conn.commit()
                print("added 10000")


    # a="1"
    cur.execute("INSERT INTO tak VALUES ('tak1', 10)")

    conn.commit()

    #print(cur.description)

    #print()

    #for row in cur:
    #    print(row)

    cur.close()
    conn.close()


def out():
    conn = pymysql.connect(host='10.0.106.8', port=3306, user='judith', passwd='judith', db='judith')
    cur = conn.cursor()

    cur.execute("SELECT * FROM viki")
    print(cur.description)

    print()

    for row in cur:
        print(row)

    cur.close()
    conn.close()


def clear():
    allowed = "abcdefghijklmnopqrstuvwxyz"
    with open("newtitles2", 'w') as new_file:
        with open("enwiki_titles") as old_file:
            for line in old_file:
                a = ''.join(e for e in line if e.lower() in allowed)
                if len(a) > 0:
                    new_file.write(a + "\n")


def doquery(query):
    conn = pymysql.connect(host='10.0.106.113', port=3306, user='judith', passwd='judith', db='judith')
    cur = conn.cursor()
    cur.execute(query)
    print(cur.description)
    print("--------")
    a = []
    for row in cur:
        print(row)
        a.append(row)

    cur.close()
    conn.close()
    return a

ins(10000)
