# Steps

### Given 
- (A) 4 training datasets `train.csv` | X, Y1, Y2, Y3, Y4
- (B) one test dataset `test.csv` | X, Y
- (C) datasets for 50 ideal functions. All data `ideal.csv` | X, Y1, Y2, ... Y50

#### Step 1
Loading `train.csv`, `test.csv`, `ideal.csv`, data files to the sqlit DATABASE. It is Handled by the `DataLoader.py` file.

#### Step 2

# $$\sum_{T=4, I=N}^{T = 1, I = 1}(y_{T}^1+y_{I}^1)^2 + (y_{T}^1+y_{I}^2)^2 + (y_{T}^1+y_{I}^3)^2 + ... (y_{T}^1+y_{I}^N)^2 \over  N$$