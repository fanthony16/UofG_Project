from django.shortcuts import render, redirect
from .forms import MakePrediction
from django.contrib import messages
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from .models import Predict
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def predict(request):
    if request.method== "POST":
        #form = UserCreationForm(request.POST)
        form = MakePrediction(request.POST)
        #form = form(initial={"stroke": True}) 
        #form = MakePrediction(request.POST)
        form_2 = MakePrediction(initial={"stroke": True})
        form_2.data.get("stroke")
        #form.fields("stroke").initial(True) 
        if form.is_valid():
            #form.save()
            stroke = form.cleaned_data.get('stroke') 
            gender = form.cleaned_data.get('gender')            
            age = int(form.cleaned_data.get('age'))
            hypertension = 1 if bool(form.cleaned_data.get('hypertension')) == True else 0
            heart_disease = 1 if bool(form.cleaned_data.get('heart_disease')) == True else 0
            ever_married = str(form.cleaned_data.get('ever_married'))
            work_type = form.cleaned_data.get('work_type')
            Residence_type = form.cleaned_data.get('Residence_type')
            avg_glucose_level = float(form.cleaned_data.get('avg_glucose_level'))
            bmi = float(form.cleaned_data.get('bmi'))
            smoking_status = form.cleaned_data.get('smoking_status')
            stroke = form_2.data.get("stroke")
            
            _data = CustomData(gender, age,hypertension,heart_disease, ever_married,work_type,
                    Residence_type,avg_glucose_level,bmi,smoking_status)
            _dataf = _data.get_data_as_data_frame()
            #print(_dataf) 
            
            _predict = PredictPipeline()
            new_predict = Predict(gender=gender,age=age,hypertension=hypertension,heart_disease=heart_disease,
                                   ever_married=ever_married,work_type=work_type,
                                   Residence_type=Residence_type,avg_glucose_level=avg_glucose_level,
                                   bmi=bmi,smoking_status= smoking_status,stroke = True)
            new_predict.save()
            #print(f'The Output Of the prediction is {_predict.predict(_dataf)}')
            _predicted_result = _predict.predict(_dataf)
            _bool = True if _predicted_result > 0 else False
            _predicted_result = (abs(_predicted_result) * 100)
            _formatedStr = "{:.2f}".format(_predicted_result[0])
            if _bool:
                messages.warning(request, f'The risk is high with probability of : {_formatedStr} %')
            else:
                messages.success(request, f'The risk is Low with probability of : {_formatedStr} %')
            
            context = {
                'form': form,
                'predicted_value': _predicted_result
                }
                
            return render(request,"predict/predict.html",context)    
            #return redirect('predict')

            #predicted_value        
    else:        
        
        form = MakePrediction()
        return render(request,"predict/predict.html",{'form': form})


class PredictionsListView(LoginRequiredMixin,ListView):
    model = Predict
    template_name = "predict/home.html"
    context_object_name = "predictions"
    ordering = ["id"]
    paginate_by = 5
    
    