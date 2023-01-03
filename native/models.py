from  django.db import models
class students(models.Model):
      name=models.CharField(max_length=100)
      grade=models.CharField(max_length=2)
    
      def __str__(self):
           
              return  self.name
class teachers(models.Model):
        name=models.CharField(max_length=100)
        salary=models.CharField(max_length=100)
        def __str__(self):
             return  self.name
    
class empploys(models.Model):
        name=models.CharField(max_length=100)
        salary=models.CharField(max_length=100)
            
        def __str__(self):
              return  self.name


