from django.shortcuts import render

TOKEN = "1B1D61B5-1FC1-4A1D-A851-B4701F2EBC39"

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        
        api_req = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+str(zipcode)+"&distance=5&API_KEY="+str(TOKEN))
        
        try:
            api = json.loads(api_req.content)

            if api[0]['Category']['Name'] == "Good":
                category_description = "(0-50): A level that will not impact patients suffering from diseases related to air pollution."
                category_color = "good"
            elif  api[0]['Category']['Name'] == "Moderate":
                category_description = "(51-100): A level that may have a meager impact on patients in case of chronic exposure."
                category_color = "moderate"
            elif  api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                category_description = "(101-150): A level that may have harmful impacts on patients and members of sensitive groups."
                category_color = "usg"
            elif  api[0]['Category']['Name'] == "Unhealthy":
                category_description = "(151-200): A level that may have harmful impacts on patients and members of sensitive groups (children, aged or weak people), and also cause the general public unpleasant feelings."
                category_color = "unhealthy"
            elif  api[0]['Category']['Name'] == "Very Unhealthy":
                category_description = "(201-300): A level that may have a serious impact on patients and members of sensitive groups in case of acute exposure."
                category_color = "veryunhealthy"
            elif  api[0]['Category']['Name'] == "Hazardous":
                category_description = "(301-500): A level that may have a serious impact on patients and members of sensitive groups in case of acute exposure."
                category_color = "hazardous"

            
        except Exception:
            api = "Error"
            category_description = ""
            category_color = "error"


        return (render(request, 'home.html', {'api' : api , 'category_description' : category_description, 'category_color' : category_color},
        ))



    else:

        api_req = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=19946&distance=25&API_KEY="+str(TOKEN))
        
        try:
            api = json.loads(api_req.content)

            if api[0]['Category']['Name'] == "Good":
                category_description = "(0-50): A level that will not impact patients suffering from diseases related to air pollution."
                category_color = "good"
            elif  api[0]['Category']['Name'] == "Moderate":
                category_description = "(51-100): A level that may have a meager impact on patients in case of chronic exposure."
                category_color = "moderate"
            elif  api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                category_description = "(101-150): A level that may have harmful impacts on patients and members of sensitive groups."
                category_color = "usg"
            elif  api[0]['Category']['Name'] == "Unhealthy":
                category_description = "(151-200): A level that may have harmful impacts on patients and members of sensitive groups (children, aged or weak people), and also cause the general public unpleasant feelings."
                category_color = "unhealthy"
            elif  api[0]['Category']['Name'] == "Very Unhealthy":
                category_description = "(201-300): A level that may have a serious impact on patients and members of sensitive groups in case of acute exposure."
                category_color = "veryunhealthy"
            elif  api[0]['Category']['Name'] == "Hazardous":
                category_description = "(301-500): A level that may have a serious impact on patients and members of sensitive groups in case of acute exposure."
                category_color = "hazardous"

            
        except Exception:
            api = "Error"
            category_description = ""
            category_color = "error"


        return (render(request, 'home.html', {'api' : api , 'category_description' : category_description, 'category_color' : category_color},
        ))


def about(request):
    return (render(request, 'about.html', {}))