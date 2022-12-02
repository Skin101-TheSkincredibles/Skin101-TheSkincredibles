import sqlite3
from productdisplay.models import Tags
#use this for the css later https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_column_cards

# def create_connection(db_file):
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except sqlite3.Error as e:
#         print(e)

#     return conn
# def load_initial_data(apps, schema_editor):
#     # get our model
#     # get_model(appname, modelname)
#     skincares = apps.get_model('productdisplay', 'SkinCareItem')
#     skincares.objects.create (
#         name = "Atomic Habits", author = "James Clear"
#         )
  
# def load_initial_data(apps, schema_editor):
#     skincare = apps.get_model('productdisplay', 'SkinCareItem')
#     tags = apps.get_model('productdisplay', 'Tags')
#     d = tags.objects.get(pk=4)
#     sc = skincare.objects.create(name='Derma365 Gentle Cleanser 100ml', type='cleanser', price='75500')
#     sc.tags.add(d)
# class Migration(migrations.Migration):

#     dependencies = [
#         ('productdisplay', '0003_delete_display'),
#     ]

#     operations = [
#         migrations.RunPython(load_initial_data)
#     ]


def main():
    # database = 'db.sqlite3'

    # create a database connection
    # print('hello')
    # p1 = Publication(title='The Python Journal')
    # conn = create_connection(database)
    # print(conn)
    # cur = conn.cursor()
    # res = cur.execute("SELECT * FROM productdisplay_tags")
    # onn = res.fetchall()
    # print(onn)

    t1 = Tags(name="Sensitive")
    t1.save()
    t2 = Tags(name="Oily")
    t2.save()
    t3 = Tags(name="Normal")
    t3.save()
    t4 = Tags(name="Acne-Prone")
    t4.save()
    t5 = Tags(name="Dry")
    t5.save()
    
if __name__ == '__main__':
    main()