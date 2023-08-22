from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from .forms import *

# Create your views here.


def homePage(request):
    children = Child.objects.all()
    context = {"children": children}
    return render(request, "fosterApp/admin-index.html", context)


# add system adminstrator
def addAdmin(request):
    if request.method == "POST":
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]

        myuser = User.objects.create_superuser(
            username=email, email=email, password=pass1
        )
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        return redirect("home")
    return render(request, "fosterApp/register.html")


# Register new child
def addChild(request):
    form = ChildForm()
    sponsors = Sponsor.objects.all()
    houses = House.objects.all()

    if request.method == "POST":
        fullName = request.POST["fname"]
        dateOfBirth = request.POST["dob"]
        gender = request.POST["gender"]
        dateOfAdm = request.POST["doa"]

        #parent details
        parentName = request.POST["parent"]
        parentId = request.POST["nationalID"]
        parentEmail = request.POST["email"]
        parentContact=request.POST["contact"]

        #sponsor-instance
        sponsor_name = request.POST["sponsor"]        
        sponsor, created = Sponsor.objects.get_or_create(fullName=sponsor_name)

        
        houseName = request.POST["house"]
        house, created = House.objects.get_or_create(name=houseName)
        address = request.POST["address"]

        #save parent details in parent/guardian table
        parent_instance=Guardian.objects.create(
            fullName=parentName,
            guardianId=parentId,
            guardianEmail=parentEmail,
            contact=parentContact

        )

        Child.objects.create(
            fullName=fullName,
            dateOfBirth=dateOfBirth,
            gender=gender,
            dateOfAdmn=dateOfAdm,
            sponsor=sponsor,
            houseName=house,
            guardianId=parent_instance,
            address=address,
        )
        return redirect("child-list")
    context = {"form": form, "houses": houses, "sponsors": sponsors}
    return render(request, "fosterApp/addchild.html", context)


# fetch registered children
def fetchChildren(request):
    children = Child.objects.all()
    context = {"children": children}
    return render(request, "fosterApp/children.html", context)


# update child


def updateChild(request, pk):
    child = Child.objects.get(id=pk)
    form = ChildForm(instance=child)

    sponsors = Sponsor.objects.all()
    houses = House.objects.all()

    if request.method == "POST":
        sponsor_name = request.POST["sponsor"]
        sponsor, created = Sponsor.objects.get_or_create(fullName=sponsor_name)

        houseName = request.POST["house"]
        house, created = House.objects.get_or_create(name=houseName)

        child.fullName = request.POST.get("fullName")
        child.guardian = request.POST.get("guardian")
        child.address = request.POST.get("address")
        child.houseName = house
        child.sponsor = sponsor
        child.save()
        return redirect("home")

    context = {"form": form, "houses": houses, "child": child, "sponsors": sponsors}
    return render(request, "fosterApp/update-child.html", context)


# deleteChild
def deleteChild(request, pk):
    child = Child.objects.get(id=pk)
    if request.method == "POST":
        child.delete()
        return redirect("child-list")
    return render(request, "fosterApp/delete.html", {"obj": child})


# add sponsor


def addSponsor(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        sponsorId = request.POST["idNo"]
        email = request.POST["email"]
        contact = request.POST["telNo"]
        occupation = request.POST["occupation"]

        Sponsor.objects.create(
            fullName=fname,
            sponsorId=sponsorId,
            sponsorEmail=email,
            contact=contact,
            occupation=occupation,
        )
        return redirect("home")
    return render(request, "fosterApp/add-sponsor.html")


# fetching sponsors
def getSponsors(request):
    sponsors = Sponsor.objects.all()
    context = {"sponsors": sponsors}
    return render(request, "fosterApp/sponsor-list.html", context)


def updateSponsor(request, pk):
    sponsor = Sponsor.objects.get(id=pk)
    
    if request.method == "POST":
        sponsor.fullName = request.POST['fname']
        sponsor.sponsorId = request.POST['idNo']
        sponsor.sponsorEmail = request.POST['email']
        sponsor.contact = request.POST['telNo']
        sponsor.occupation = request.POST['occupation']
        sponsor.save()

        
        return redirect('sponsor-list')
    context={'sponsor':sponsor}
    return render(request, "fosterApp/update-sponsor.html",context)

# deleteSponsor
def deleteSponsor(request, pk):
    sponsor = Sponsor.objects.get(id=pk)

    if request.method == "POST":
        sponsor.delete()
        return redirect("sponsor-list")
    return render(request, "fosterApp/delete.html", {"obj": sponsor})


def addEmployee(request):
    departments = Department.objects.all()
    if request.method == "POST":
        fname = request.POST["fname"]
        employeeId = request.POST["idNo"]
        email = request.POST["email"]
        contact = request.POST["telNo"]
        department = request.POST["department"]
        department = Department.objects.get(department=department)

        Employee.objects.create(
            fullName=fname,
            employeeId=employeeId,
            emplEmail=email,
            telNo=contact,
            department=department,
        )
        return redirect("home")
    context = {"departments": departments}
    return render(request, "fosterApp/add-employee.html", context)


# fetching employees
def getEmployees(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, "fosterApp/employee-list.html", context)
