import pandas as pd
import numpy as np
import os
from keras.models import load_model
import matplotlib.pyplot as plt

os.chdir(r'....') # Select path
variable = "grf_x" # Select variable name: grf_x, grf_y, grf_z, hip_flex_moment, hip_abd_moment, hip_rot_moment, knee_flex_moment, ankle_flex_moment
model = load_model("RNN_cycling_" + variable + ".h5")
file = pd.read_csv('data.csv')

x_data=[]
for i in range(0, len(file['hip_flex'])-5):
    x_data_=[]
    for j in range(i, i+5):
        x_data_.append([file['hip_flex'][j], file['knee_flex'][j], file['ankle_flex'][j], 
                               file['watts'][j], file['rpm'][j], file['hip_rot'][j], file['mass'][j]])
    x_data.append(x_data_)

x_test = np.array(x_data)
predictions = model.predict(x_test, verbose=0).flatten()
predictions = predictions
y_test = file[variable][5:]

plt.plot(predictions, color="red")
plt.plot(list(y_test), color="blue")
plt.show()
