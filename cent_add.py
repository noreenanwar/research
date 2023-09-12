import json

# Load the COCO formatted data
with open('C:\\Users\\Admin\\work\\PhD\\code\\mmdetection-main\\data\\coco\\annotations\\instances_val2017.json', 'r') as f:
    data = json.load(f)

# Add center points to annotations
for annotation in data['annotations']:
    x, y, w, h = annotation['bbox']
    center_x = format(x + w / 2, '.4f')
    center_y = format(y + h / 2, '.4f')
    annotation['center'] = [float(center_x), float(center_y)]

# Save the updated data back to a JSON file
with open('C:\\Users\\Admin\\work\\PhD\\code\\mmdetection-main\\data\\coco\\annotations\\instances_val2017_updated_coco.json', 'w') as f:
    json.dump(data, f, indent=4)
