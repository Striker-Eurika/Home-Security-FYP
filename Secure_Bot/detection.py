from ultralytics import YOLO
from django import template


register = template.Library()
model = YOLO('yolov8n.pt')


def detect_from_image(img_name):
    results = model.predict("media/images/" + img_name, save=True, project="media/images", name="predict",
                            exist_ok=True)


@register.filter
def get_detections(img_name):
    return img_name.replace("/images", "/images/predict")