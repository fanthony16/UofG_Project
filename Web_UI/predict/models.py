from django.db import models

# Create your models here.
class Predict(models.Model):
    
    male = "Male"
    female= "Female"
    _gender = [(male, "MALE"), (female, "FEMALE")]
    
    yes = "Yes"
    no = "No"
    ever_married = [(yes, "Yes"), (no, "No")]
    
    never_smoked = "never smoked"
    formerly_smoked = "formerly smoked"
    smokes = "smokes"
    unknown = "Unknown"
    smoking_statue = [(never_smoked, "Never Smoked"), (formerly_smoked, "Formerly Smoked"),
               (smokes, "Smokes"),(unknown, "Unknown")]
    
    rural = "Rural"
    urban= "Urban"
    residence_type = [(rural, "Rural"), (urban, "Urban")]
    children = "children"
    Govt_job = "Govt_job"
    Never_worked= "Never_worked"
    Private= "Private"
    Self_employed = "Self-employed"
    
    work_type = [(children, "Children"), (Govt_job, "Government Job"),
                 (Never_worked, "Never Worked"),(Private, "Private"),(Self_employed, "Self Employed")]
    
    gender = models.CharField(max_length=20, choices= _gender)
    age = models.IntegerField()
    hypertension = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    ever_married = models.CharField(max_length=3, choices = ever_married)
    work_type = models.CharField(max_length = 15, choices = work_type)
    Residence_type = models.CharField(max_length= 15, choices = residence_type)
    avg_glucose_level = models.DecimalField(max_digits=6, decimal_places=2)
    bmi = models.DecimalField(max_digits=6, decimal_places=2)
    smoking_status = models.CharField(max_length= 30, choices = smoking_statue)
    stroke = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.gender} - {self.age} - {self.stroke}'
    