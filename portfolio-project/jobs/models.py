from django.db import models

# Steps to do add new model:

# 1. Create class with corresponding name inheriting from models.Model
# 2. Create variables inside class using models.<Field>
# 3. Add app to settings file ('<app_name>.apps.<AppnameConfig>'). You can see this in apps.py for your respective model
# 4. Create migration with python manage.py makemigrations
# 5. Migrate with python manange.py migrate
# 6. Add new model to admin inside admin.py file with admin.site.register(<ClassName>) if you want to have admin database functionality

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)