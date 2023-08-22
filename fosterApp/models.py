from django.db import models

# Create your models here.
#sponsors table
class Sponsor(models.Model):
    fullName=models.CharField(max_length=100,blank=False, default=None)
    sponsorEmail=models.EmailField(max_length=50)
    sponsorId=models.CharField(max_length=10)
    contact=models.CharField(max_length=100)
    occupation=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName
    
class Guardian(models.Model):
    fullName=models.CharField(max_length=100)
    guardianEmail=models.EmailField(max_length=50)
    guardianId=models.CharField(max_length=10)
    contact=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName



#House Table
class House(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

#children table
class Child(models.Model):
    fullName=models.CharField(max_length=100)
    dateOfBirth=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    dateOfAdmn=models.CharField(max_length=50)
    guardianId=models.ForeignKey(Guardian,on_delete=models.CASCADE,related_name='rey')
    sponsor=models.ForeignKey(Sponsor, on_delete=models.SET_NULL,null=True)
    houseName=models.ForeignKey(House,on_delete=models.CASCADE)
    address=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created','-updated']

    def __str__(self):
        return self.fullName
    

#departments table
class Department(models.Model):
    department=models.CharField(max_length=50) 

    def __str__(self):
        return self.department


#employee table
class Employee(models.Model):
    fullName=models.CharField(max_length=100)    
    emplEmail=models.EmailField()
    telNo=models.CharField(max_length=20)
    employeeId=models.CharField(max_length=10,unique=True)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName
    



    
