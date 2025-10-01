
# CFD-NN Pressure Drop Prediction

A pipeline for automating OpenFOAM simulations with PyFoam and training a neural network to predict pressure drop across various geometries and Reynolds numbers.

## Overview

This project:
- Runs automated OpenFOAM sweeps for multiple geometries at different Reynolds numbers
- Extracts pressure drop data from simulation results
- Trains a neural network that uses **geometry embeddings** to generalize predictions to unseen geometries

## Project Structure

```
├── geometries/          # Geometry files (STL, blockMeshDict)
├── scripts/
│   ├── run_sweep.py    # Main script to launch CFD cases
│   ├── extract_data.py # Parse OpenFOAM results
│   └── train_model.py  # Neural network training
├── data/               # Simulation results and trained models
└── requirements.txt    # Python dependencies
```

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run CFD sweep:**
   ```bash
   python scripts/run_sweep.py
   ```

3. **Extract data and train model:**
   ```bash
   python scripts/extract_data.py
   python scripts/train_model.py
   ```

## Key Feature

The model uses **geometry embeddings** to learn continuous representations of different geometries, enabling better generalization compared to traditional approaches.

*Note: This project is under active development. Structure and scripts may change.*