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

- Prepare the input data. Input data are compose for the hip, knee and ankle flexion and hip rotation joint angles along with watts, rpm and subject´s mass. Input data should be scaled about the maximum corresponding value.
- An example of input data is storaged in the .csv file. 
- Load the appropiate RNN to predict the desired kinetic variable.

<br>

See the example code to perform predictions.
