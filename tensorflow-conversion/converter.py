import tfcoreml as tf_converter
tf_converter.convert(tf_model_path = 'retrained_graph.pb',
                     mlmodel_path = 'edeka.mlmodel',
                     output_feature_names = ['final_result:0'])	