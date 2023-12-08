import os

from visqol import visqol_lib_py
from visqol.pb2 import visqol_config_pb2
from visqol.pb2 import similarity_result_pb2

config = visqol_config_pb2.VisqolConfig()

mode = "audio"
if mode == "audio":
    config.audio.sample_rate = 48000
    config.options.use_speech_scoring = False
    svr_model_path = "libsvm_nu_svr_model.txt"
elif mode == "speech":
    config.audio.sample_rate = 16000
    config.options.use_speech_scoring = True
    svr_model_path = "lattice_tcditugenmeetpackhref_ls2_nl60_lr12_bs2048_learn.005_ep2400_train1_7_raw.tflite"
else:
    raise ValueError(f"Unrecognized mode: {mode}")

config.options.svr_model_path = os.path.join(
    os.path.dirname(visqol_lib_py.__file__), "model", svr_model_path)

api = visqol_lib_py.VisqolApi()

api.Create(config)

similarity_result = api.Measure(reference, degraded)

print(similarity_result.moslqo)
