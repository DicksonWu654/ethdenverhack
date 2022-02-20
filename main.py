from v2_backend.dataset_processor import generate_dataset
from v2_backend.model import Model

generate_dataset('dataset', 10)
m = Model(padding=256)
m.build_model()
print(m.model.summary())