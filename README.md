# 🏥 MedFlow

## The Counterfactual Hospital Operations Engine

> **Don't just predict what happens next. Test what happens if you choose differently.**

MedFlow is an interactive hospital operations simulator that creates **counterfactual futures** for the same hospital situation.

Instead of asking only:

> **“Who should we prioritize right now?”**

MedFlow asks:

> **“What happens to the hospital if we prioritize patients this way instead of another way?”**

The system simulates patient demand, waiting queues, resource availability, allocation decisions, and operational pressure under different strategies and stress scenarios.

---

## 🧠 The Core Idea: Counterfactual Operations

Imagine the same hospital at the same moment:

* same patients
* same beds
* same ICU capacity
* same doctors and nurses
* same operating rooms

Now change only the **decision policy**.

MedFlow simulates multiple possible operational futures and compares their consequences.

```text
Same hospital state
       ↓
Choose a strategy
       ↓
Simulate the next hours
       ↓
Observe queue + resources + allocation
       ↓
Change the strategy
       ↓
Simulate again
       ↓
Compare the alternate futures
```

This turns hospital management from a **static dashboard problem** into a **what-if decision problem**.

---

## 🚑 What MedFlow Simulates

MedFlow models:

* Patient arrivals
* Patient urgency
* Waiting time
* Department demand
* Beds
* ICU capacity
* Operating rooms
* Doctors
* Nurses
* Ambulances
* Patient-to-resource allocation
* Queue pressure
* Resource conflicts

---

## 🔀 Three Operational Futures

### 1. Urgency Only

Prioritize patients primarily according to urgency.

### 2. Urgency + Waiting

Include waiting time so patients who have waited longer gain priority.

### 3. Urgency + Waiting + Resource Fit

Also account for whether the resources required by a patient can realistically be allocated.

The strategies are evaluated under the same simulated hospital conditions so their operational behavior can be compared.

---

## 🌪️ Then We Break the Hospital

MedFlow can introduce controlled operational shocks:

### 🚑 Emergency Surge

A sudden increase in high-acuity demand.

### 👩‍⚕️ Staff Shortage

Reduced doctor and nurse availability.

### ⚠️ OR Failure

Operating-room capacity becomes unavailable.

The goal is not simply to produce a score.

The goal is to observe:

> **How does the hospital react?**

---

## 🎯 What MedFlow Answers

MedFlow helps explore questions such as:

* What happens if waiting time matters more?
* What happens if ICU capacity becomes constrained?
* What happens during an emergency surge?
* Which resources become bottlenecks?
* How does the queue evolve over the next few hours?
* Why was a particular patient given priority?
* What changes when the scheduling strategy changes?

---

## 🧠 Explainable by Design

MedFlow does not hide prioritization behind an unexplained black box.

For a selected patient, the system can expose factors such as:

* Urgency
* Waiting time
* Department
* Resource requirements
* Resource constraints
* Priority score
* Reason for prioritization

This makes the simulated decision traceable.

---

## 🔬 From Dashboard to Decision Laboratory

MedFlow is designed less like a conventional hospital dashboard and more like a **decision laboratory**.

A user can:

**Observe → Change a policy → Simulate → Stress-test → Compare → Understand**

The objective is to explore the operational consequences of decisions **before testing those decisions in the real world**.

---

## 🏗️ System Flow

```text
Patient arrivals
       ↓
Priority calculation
       ↓
Waiting queue
       ↓
Resource feasibility
       ↓
Patient allocation
       ↓
Simulation clock
       ↓
Operational metrics
       ↓
Counterfactual comparison
```

---

## 🚀 Built in 24 Hours

MedFlow was built as a **24-hour hackathon prototype by a first-semester student team**, approximately two weeks after starting college.

The current prototype uses synthetic data and focuses on demonstrating the operational simulation and decision-comparison architecture.

---

## 🌍 Future Direction

A production-scale system could extend the same architecture with:

* Real-time hospital data
* Predictive arrival forecasting
* Length-of-stay prediction
* Specialty-aware staff matching
* Live resource feeds
* Historical learning from hospital operations
* Hospital information-system integration
* Real-time alerts and monitoring

The long-term vision is a platform where hospitals can **test operational decisions in simulated futures before deploying them in reality**.

---

## 🛠️ Technology

**Python • Pandas • Streamlit • GitHub • Streamlit Community Cloud**

---

## 🌐 Live Demo

https://medflow-hospital.streamlit.app/

## 💻 Repository

https://github.com/gallachakrika/MedFlow
