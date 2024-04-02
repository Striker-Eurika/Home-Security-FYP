from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Alert
from django.views.decorators.csrf import csrf_exempt
from django.core.files.images import ImageFile
import io
from .detection import detect_from_image


def home(request):
    alerts = Alert.objects.all()
    detections = []
    for alert in alerts:
        detections.append(str(alert.photo.url).replace("/images", "/images/predict"))
    print(detections)
    return render(request, 'home.html', {'detections': detections, })


@csrf_exempt
def post_alert(request):
    if request.method == 'POST':
        img_name = 'alert_image' + str(len(Alert.objects.all())) + '.jpg'
        test_stuff = str(request.body)[:-45]
        print(bytes(test_stuff, 'utf-8'))
        Alert.objects.create(photo=ImageFile(io.BytesIO(request.body), name=img_name))
        detect_from_image(img_name)
        return HttpResponse('Image received OK!')
    else:
        return HttpResponse('Bad request!')