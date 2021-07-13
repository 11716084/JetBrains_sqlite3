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

cursor_name.execute("""CREATE TABLE recipes (
recipe_id INTEGER PRIMARY KEY,
recipe_name VARCHAR NOT NULL,
recipe_description VARCHAR
)""")

conn.commit()


insert_recipes = "INSERT INTO recipes (recipe_name, recipe_description) VALUES (?, ?);"

print("Pass the empty recipe name to exit.")


def add_recipes(cursor_name, recipe_name, recipe_description):
    cursor_name.execute(insert_recipes, (recipe_name, recipe_description))


while True:
    recipe_name = input("Recipe name:")
    if recipe_name != "":
        recipe_description = input("Recipe description:")
        add_recipes(cursor_name, recipe_name, recipe_description)
    else:
        break
conn.commit()
conn.close()
