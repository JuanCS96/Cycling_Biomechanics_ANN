# Validity of recurrent neural networks to predict pedal forces and lower limb kinetics in cycling

<p align="center">

Recurrent Neural Networks to predict pedal forces and lower limb net joint moments from kinematic data in cycling.

## Requirements

- Python version 3.11.0.
- Tensorflow version 2.15.0 or higher.
- Numpy version 1.16.2 or higher.
- Pandas version 2.2.0 or higher.

---

## Instructions

- **Prepare the input data**. Input data contain the hip, knee and ankle flexion and hip rotation joint angles along with watts, rpm and subject's mass. Input data should be scaled about the maximum corresponding value. In order to use the provided neural networks, the names of the headers should appear as in the provided example:
![Example input data](https://github.com/JuanCS96/Cycling_Biomechanics_ANN/blob/main/img/image1.png?raw=true)
*Example of the input data. Check the appropriate headers.*
- **Load the appropiate RNN to predict the desired kinetic variable**, by assigning it in [this line](https://github.com/JuanCS96/Cycling_Biomechanics_ANN/blob/00809c9a00ef79d77af58babbec76bcae987d142/RNN_cycling_predictions.py#L8).

<br>

See the example [Python code](https://github.com/JuanCS96/Cycling_Biomechanics_ANN/blob/main/RNN_cycling_predictions.py) to perform predictions.

If you use this code, please cite the article associated with this study:

- Cordero-Sánchez, J., Bini, R., Serrancolí, G. Validity of recurrent neural networks to predict pedal forces and lower limb kinetics in cycling. *Journal of Biomechanics* 183. 2025. 112619. https://doi.org/10.1016/j.jbiomech.2025.112619.
