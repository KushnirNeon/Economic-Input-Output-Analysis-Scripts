# Economic Input-Output Analysis

This repository contains two Python scripts for input-output economic modeling.

---

## 1. Full Production Output (`full_output.py`)

Calculates total production needed to satisfy forecasted demand in a two-sector economy.

**Features:**
- Computes the technological matrix \(A\)
- Calculates total production vector \(x\) using the Leontief model: \(x = (I - A)^{-1} \cdot c\)

# Frobenius Number & Price Vector Analysis

This Python script performs input-output economic analysis for a three-sector economy using an input-output matrix.

---

## Features

- Computes eigenvalues and eigenvectors of the input-output matrix \(A\)  
- Determines the Frobenius number (largest eigenvalue)  
- Finds right and left Frobenius vectors  
- Checks matrix productivity (stability of the economic system)  
- Computes the full cost matrix \(B = (I - A)^{-1}\)  
- Verifies convergence of the series \(E + A + A^2 + ... + A^N\)  
- Calculates the price vector \(P = B^T \cdot s\) and checks if all prices are positive
