# Conversion script for tiny-yolo-voc to Core ML.
# Needs Python 2.7 and Keras 1.2.2

import coremltools

print("Model About to be converted")
coreml_model = coremltools.converters.keras.convert(
    './model_data/tiny-yolo.h5')
print("Model Converted")

coreml_model.author = 'James and Frederik'
coreml_model.license = 'Top Secret EDEKA Project Licence'
coreml_model.short_description = "The Tiny YOLO network from the paper 'YOLO9000: Better, Faster, Stronger' (2016), arXiv:1612.08242"

coreml_model.input_description['image'] = 'Input image'
coreml_model.output_description['grid'] = 'The 13x13 grid with the bounding box data'

print("Model About to be saved")
print(coreml_model)

coreml_model.save('edeka.mlmodel')
