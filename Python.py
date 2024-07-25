import sqlite3

def search():
    conn = sqlite3.connect('assignment.db')
    c = conn.cursor()
    
    while True:
        search_string = input("Enter a string ")
        if search_string.strip() == "":
            print("Please enter a search string.")
        else:
            break
    
    c.execute("SELECT * FROM student_results WHERE name LIKE ?", ('%' + search_string + '%',))
    rows = c.fetchall()
    
    if len(rows) == 0:
        print("No matching names found.")
    else:
        total_marks = 0
        num_rows = len(rows)
        
        for row in rows:
            name, marks = row
            print(f"Name: {name}, Marks: {marks}")
            total_marks += marks
        
        if num_rows > 0:
            average_marks = total_marks / num_rows
        else:
            average_marks = 0
        
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks}")
    
    conn.close()

if __name__ == "__main__":
    search()
