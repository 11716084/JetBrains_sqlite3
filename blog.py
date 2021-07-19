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

cursor_name.execute("PRAGMA foreign_keys = ON;")
conn.commit()

insert_recipes = "INSERT INTO recipes (recipe_name, recipe_description) VALUES (?, ?);"

print("Pass the empty recipe name to exit.")


cursor_name.execute("""CREATE TABLE serve (
serve_id INTEGER PRIMARY KEY,
recipe_id INTEGER NOT NULL,
meal_id INTEGER NOT NULL,
FOREIGN KEY (recipe_id)
    REFERENCES  recipes (recipe_id)
FOREIGN  KEY (meal_id)
    REFERENCES  meals (meal_id)
)""")


def add_recipes(cursor_name, recipe_name, recipe_description):
    cursor_name.execute(insert_recipes, (recipe_name, recipe_description))


while True:
    recipe_name = input("Recipe name:")
    if recipe_name != "":
        recipe_description = input("Recipe description:")
        add_recipes(cursor_name, recipe_name, recipe_description)

        cursor_name.execute("""SELECT recipe_id
        FROM recipes
        WHERE recipe_name = ? AND recipe_description = ?;""", (recipe_name, recipe_description,))

        x = [str(numb[0]) for numb in cursor_name.fetchall()]
        recipe_id = int(x[0])
        when_served = input("""1) breakfast  2) brunch  3) lunch  4) supper
        When the dish can be served:""")
        meal = when_served.split()
        meal_id = 1
        for i in range(0, len(meal)):
            meal_id = int(meal[i])
            cursor_name.execute('INSERT INTO serve (recipe_id, meal_id) VALUES (?, ?);', (recipe_id, meal_id,))
            conn.commit()

    else:
        break
conn.commit()
conn.close()
