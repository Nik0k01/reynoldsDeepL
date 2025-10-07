# Predicting Pressure Drop in CFD Domains using ML

This project explores whether it’s possible to **predict the pressure drop in fluid flow** directly from **geometry type and Reynolds number**, using data generated from **OpenFOAM** simulations.

It’s a follow-up to my earlier experiment where I tried to make a neural network *“look at colorful CFD plots and guess the Reynolds number.”*
Spoiler: both humans and computers failed spectacularly.
This time, we go tabular and more grounded.

---

## 🧩 Project Overview

* **Goal:** Predict the **pressure drop** in different flow geometries using **Reynolds number** and **geometry embedding**.
* **Motivation:** Understand whether a model trained on certain geometries can generalize to *new, unseen* ones.
* **Tools:** `Salome`, `OpenFOAM`, `PyFoam`, `Python`, `scikit-learn`, `PyTorch / FastAI`.

---

## ⚙️ Workflow

1. **Geometry & Meshing**

   * 8 distinct geometries were modeled in *Salome* and meshed for OpenFOAM.
   * Each geometry was simulated across ~80 Reynolds numbers by varying viscosity.

2. **Simulation**

   * All cases were automated with `PyFoam`.
   * Pressure data exported to CSV using OpenFOAM function objects.

3. **Machine Learning**

   * Neural network with **geometry embeddings** trained to predict pressure drop.
   * Compared with a **Random Forest Regressor** for robustness and extrapolation.

4. **Evaluation**

   * Both models tested on **unseen geometries**.
   * Random Forest achieved lower MAE and handled unknown geometry classes more gracefully.

---

## 📊 Key Findings

* Random Forest achieved **MAE ≈ 0.23**, outperforming the neural network (**MAE ≈ 0.46**).
* Neural networks struggled to generalize to unseen geometries.
* Good meshing is more art than science.
* Fancy models don’t always beat a well-tuned classical one.

---

## 🗂️ Repository Structure

```
├── flowCases/
│   ├── backwardStepRe=1.00/
│   ├── backwardStepRe=26.30/
│   └── ...
├── data/
│   ├── master_results.csv
│   └── test_set.csv
├── scripts/
│   ├── caseRunner.py
│   ├── postProcessor.py
│   └── ...
├── notebooks/
│   ├── models/
│   ├── extract_pressure_drop.py
│   ├── architectureTweaking.ipynb
│   └── ...
├── templates/
│   ├── backwardStepTemplate/
│   ├── bendTemplate/
│   └── ...
└── README.md
```

---

## 🧾 References

* **OpenFOAM** – Open-source CFD solver
* **Salome** – Geometry and mesh generation platform
* **FastAI** – Deep learning library built on PyTorch
* **scikit-learn** – Classical ML toolkit
