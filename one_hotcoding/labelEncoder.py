import numpy as np

original_array = np.array([
    (1, 'John', 23, 'F'),
    (2, 'Jane', 45, 'M'),
    (3, 'Jim', 12, 'M'),
    (4, 'Mark', 67, 'M'),
    (5, 'Mary', 13, 'F'),
    (6, 'Mike', 34, 'M')
])

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder

LabelEncoder_x = LabelEncoder()
original_array[:, 3] = LabelEncoder_x.fit_transform(original_array[:, 3]) 
print(original_array)