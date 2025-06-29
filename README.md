### Online handwriting Generation: Data Augmentation using Geometric, Frequency, and Beta Modeling approaches for Improving Multi-lingual Online Handwriting Recognition
#### Overview

We introduce new data augmentation methods that generate more shape and dynamic variations to improve the performance of recognition systems using small datasets. Four data augmentation
strategies are employed in this study. The first strategy employs geometric methods that include: italicity angle, change of magnitude ratio, and baseline inclination angle.
The second strategy applies a frequency treatment that attenuates or amplifies the trajectory high harmonics to generate handwriting modified styles. The third strategy employs the beta-elliptic model to
extract a combined static and dynamic representation of the handwritten trajectory which undergoes limited random change around its parameters in order to generate more modified samples. The hybrid strategy consists of combining these strategies to maximize variations of the online handwriting trajectory (OHT).
##### Using beta-elliptic model:
![image](https://github.com/user-attachments/assets/347dfde9-a003-4511-ac93-19b199592ebe)
##### Using frequency method
![image](https://github.com/user-attachments/assets/3f412f5c-50f4-4d53-a692-52d630453f28)

#### Requirements
- Python 3.6+
- TensorFlow 2.x
- NumPy
- Matplotlib (for visualization)

#### Citation

Hamdi, Y., Boubaker, H. & Alimi, A.M. Data Augmentation using Geometric, Frequency, and Beta Modeling approaches for Improving Multi-lingual Online Handwriting Recognition. IJDAR 24, 283–298 (2021). https://doi.org/10.1007/s10032-021-00376-2
