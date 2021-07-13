import sqlite3

conn = sqlite3.connect("food_blog.db")

cursor_name = conn.cursor()

cursor_name.execute("""CREATE TABLE meals (
meal_id INTEGER PRIMARY KEY, 
meal_name VARCHAR unique NOT NULL
)""")
cursor_name.execute(""" CREATE TABLE ingredients (
ingredient_id INTEGER PRIMARY KEY,
ingredient_name VARCHAR UNIQUE NOT NULL
)""")

cursor_name.execute("""CREATE TABLE measures (
measure_id INTEGER PRIMARY KEY,
measure_name VARCHAR UNIQUE

)""")


cursor_name.execute("""INSERT INTO meals (meal_name)
 VALUES
  ('breakfast'),
   ('brunch'),
    ('lunch'),
     ('supper')""")
cursor_name.execute("""INSERT INTO ingredients (ingredient_name)
VALUES
('milk'),
 ('cacao'),
  ('strawberry'),
   ('blueberry'),
    ('blackberry'),
     ('sugar')""")

cursor_name.execute("""INSERT INTO measures (measure_name)
VALUES 
('ml'),
 ("g"),
  ('l'),
   ('cup'),
    ('tbsp'),
     ('tsp'),
      ('dsp'),
       ('')""")

conn.commit()
conn.close()
