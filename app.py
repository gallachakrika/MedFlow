import streamlit as st
import pandas as pd
import numpy as np
import random
from collections import defaultdict

st.set_page_config(page_title="MedFlow Pro", page_icon="🏥", layout="wide", initial_sidebar_state="expanded")

# ---------- MEDFLOW COMMAND CENTER CSS ----------
st.markdown("""
<style>

/* Main application */
[data-testid="stAppViewContainer"] {
    background: #070b12;
    color: #f5f7fa;
}

[data-testid="stHeader"] {
    background: #070b12;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0b111c;
    border-right: 1px solid #1d2939;
}

[data-testid="stSidebar"] * {
    color: #f5f7fa !important;
}

/* Main text */
h1, h2, h3, h4, p, label {
    color: #f5f7fa !important;
}

/* Hero */
.hero {
    padding: 24px 28px;
    border-radius: 18px;
    background: linear-gradient(135deg, #0b1728, #102a43);
    border: 1px solid #20344d;
    color: white;
    margin-bottom: 20px;
}

.hero h1 {
    margin: 0;
    font-size: 2.3rem;
    letter-spacing: 1px;
}

.hero p {
    margin: 6px 0 0;
    color: #9fb3c8 !important;
}

/* General cards */
.card {
    background: #0d1522;
    border: 1px solid #1e2b3d;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,.20);
}

/* Command center cards */
.command-card {
    background: #0d1522;
    border: 1px solid #1e2b3d;
    border-radius: 16px;
    padding: 18px;
    min-height: 110px;
}

.command-title {
    color: #8fa6bd !important;
    font-size: .78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.command-value {
    color: #f5f7fa !important;
    font-size: 2rem;
    font-weight: 800;
    margin-top: 5px;
}

/* Pressure meter */
.pressure {
    background: #0d1522;
    border: 1px solid #26364a;
    border-radius: 20px;
    padding: 24px;
    text-align: center;
}

.pressure-value {
    font-size: 3.2rem;
    font-weight: 900;
    color: #f5f7fa !important;
}

.pressure-label {
    color: #9fb3c8 !important;
    font-size: .8rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

/* Section headings */
.section-title {
    color: #f5f7fa !important;
    font-size: 1.15rem;
    font-weight: 800;
    margin: 18px 0 10px;
}

/* Patient severity */

.patient-critical {
    border-left: 6px solid #ff4d4f;
    background: rgba(255, 77, 79, 0.12);
}

.patient-high {
    border-left: 6px solid #ff9f43;
    background: rgba(255, 159, 67, 0.10);
}

.patient-medium {
    border-left: 6px solid #feca57;
    background: rgba(254, 202, 87, 0.09);
}

.patient-low {
    border-left: 6px solid #2ed573;
    background: rgba(46, 213, 115, 0.08);
}
/* Severity badges */
.badge {
    padding: 5px 9px;
    border-radius: 99px;
    font-weight: 700;
    font-size: .8rem;
}

.badge-critical {
    background: rgba(255,77,79,.15);
    color: #ff6b6b !important;
}

.badge-high {
    background: rgba(255,159,67,.15);
    color: #ffb366 !important;
}

.badge-medium {
    background: rgba(254,202,87,.15);
    color: #ffd86b !important;
}

.badge-low {
    background: rgba(46,213,115,.15);
    color: #5ee69a !important;
}

/* Explanation panel */
.explain {
    background: #101b2b;
    border: 1px solid #29415e;
    border-radius: 16px;
    padding: 20px;
}

.explain-title {
    color: #7dd3fc !important;
    font-weight: 800;
    font-size: 1rem;
}

.explain-text {
    color: #c7d4e3 !important;
    line-height: 1.7;
}

/* Crisis alert */
.crisis {
    background: rgba(255,77,79,.10);
    border: 1px solid rgba(255,77,79,.45);
    border-radius: 14px;
    padding: 14px 18px;
    color: #ff8585 !important;
    font-weight: 700;
}

/* Forecast */
.forecast {
    background: #0d1522;
    border: 1px solid #1e2b3d;
    border-radius: 16px;
    padding: 18px;
}

.forecast-time {
    color: #7dd3fc !important;
    font-weight: 800;
}

.forecast-text {
    color: #c7d4e3 !important;
}

/* Small text */
.small {
    color: #8fa6bd !important;
    font-size: .86rem;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    border: 1px solid #29415e;
    background: #102033;
    color: #f5f7fa;
    font-weight: 700;
}

.stButton > button:hover {
    border-color: #4b8bb8;
}

/* Metrics */
[data-testid="stMetric"] {
    background: #0d1522;
    border: 1px solid #1e2b3d;
    padding: 14px;
    border-radius: 14px;
}

/* Tables */
[data-testid="stDataFrame"] {
    border: 1px solid #1e2b3d;
    border-radius: 12px;
}

/* Dividers */
hr {
    border-color: #1e2b3d !important;
}

/* Dark sidebar number inputs */

[data-testid="stSidebar"] [data-testid="stNumberInput"] input {
    background-color: #0d1522 !important;
    color: #f5f7fa !important;
    border: none !important;
}

[data-testid="stSidebar"] [data-testid="stNumberInput"] > div {
    background-color: #0d1522 !important;
    border: 1px solid #1e2b3d !important;
    border-radius: 10px !important;
}

[data-testid="stSidebar"] [data-testid="stNumberInput"] button {
    background-color: #0d1522 !important;
    color: #8fa6bd !important;
    border: none !important;
}

[data-testid="stSidebar"] [data-testid="stNumberInput"] button:hover {
    background-color: #1e2b3d !important;
    color: #f5f7fa !important;
}

/* Scheduling Strategy dropdown */

[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] > div {
    background-color: #0d1522 !important;
    border: 1px solid #1e2b3d !important;
}

[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] span {
    color: #f5f7fa !important;
}

</style>
""", unsafe_allow_html=True)

URGENCY = {"Critical":4,"High":3,"Medium":2,"Low":1}
DEPARTMENTS = ["Emergency","Cardiology","Neurology","Pediatrics","Orthopedics","General"]
DEPT_MULTIPLIER = {"Emergency":1.15,"Cardiology":1.0,"Neurology":1.0,"Pediatrics":0.95,"Orthopedics":0.9,"General":0.85}
RESOURCES = ["beds","icu","or","doctors","nurses","ambulances"]

def generate_patients(n, seed, surge=False):
    rng=random.Random(seed)
    names=["Aarav","Diya","Kabir","Ananya","Vihaan","Ishita","Arjun","Meera","Rohan","Aadhya",
           "Advik","Sara","Neil","Tara","Kian","Maya","Reyansh","Nisha","Ayaan","Ira"]
    rows=[]
    for i in range(n):
        if surge and i < max(1,n//5):
            urgency=rng.choices(["Critical","High","Medium"],[55,35,10])[0]
            arrival=rng.randint(0,8)
            dept="Emergency" if rng.random()<.65 else rng.choice(DEPARTMENTS)
        else:
            urgency=rng.choices(["Critical","High","Medium","Low"],[8,20,42,30])[0]
            arrival=rng.randint(0,24)
            dept=rng.choice(DEPARTMENTS)
        if urgency=="Critical":
            icu=1 if rng.random()<.75 else 0
            or_req=1 if rng.random()<.4 else 0
            req={"beds":1,"icu":icu,"or":or_req,"doctors":1,"nurses":2,"ambulances":1 if dept=="Emergency" else 0}
            service=rng.randint(3,7)
        elif urgency=="High":
            req={"beds":1,"icu":1 if rng.random()<.25 else 0,"or":1 if rng.random()<.2 else 0,
                     "doctors":1,"nurses":1,"ambulances":1 if dept=="Emergency" and rng.random()<.4 else 0}
            service=rng.randint(2,5)
        elif urgency=="Medium":
            req={"beds":1,"icu":0,"or":1 if rng.random()<.1 else 0,"doctors":1,"nurses":1,"ambulances":0}
            service=rng.randint(2,4)
        else:
            req={"beds":1,"icu":0,"or":0,"doctors":1,"nurses":1,"ambulances":0}
            service=rng.randint(1,3)
        rows.append({"Patient":f"P-{i+1:03d}","Name":rng.choice(names),"Arrival":arrival,
                     "Urgency":urgency,"Department":dept,"Service":service,**req})
    return pd.DataFrame(rows).sort_values("Arrival").reset_index(drop=True)

def priority_score(p, now, strategy, available=None):
    wait = max(0, now - int(p["Arrival"]))
    u = URGENCY[p["Urgency"]]
    dept = DEPT_MULTIPLIER[p["Department"]]

    # Strategy 1: urgency is the dominant factor
    if strategy == "Urgency only":
        return u * 1000 - p["Arrival"]

    # Strategy 2: urgency + waiting time
    if strategy == "Urgency + waiting":
        waiting_bonus = min(wait, 24) * 15 * dept
        return u * 1000 + waiting_bonus - p["Arrival"]

    # Strategy 3: urgency + waiting + resource fit
    waiting_bonus = min(wait, 24) * 15 * dept

    fit = 0
    if available:
        for r in RESOURCES:
            need = int(p[r])
            free = available.get(r, 0)

            if need == 0:
                continue

            if free >= need:
                fit += 5
            else:
                fit -= 10

    return u * 1000 + waiting_bonus + fit - p["Arrival"]

def simulate(df, caps, strategy, horizon, surge=False, shortage=False, failure=False):
    avail=caps.copy()
    arrivals=defaultdict(list)
    for _,p in df.iterrows(): arrivals[int(p.Arrival)].append(p.to_dict())
    waiting=[]
    active=[]
    finished=[]
    timeline=[]
    events=[]
    utilization={r:0 for r in RESOURCES}
    max_queue=0

    for t in range(horizon):
        # Release patients.
        keep=[]
        for x in active:
            if x["end"]<=t:
                for r,v in x["req"].items(): avail[r]+=v
                finished.append(x)
                events.append((t,"DISCHARGE",x["patient"],x["name"]))
            else: keep.append(x)
        active=keep

        # Apply external conditions.
        temp_caps=caps.copy()
        if shortage and 18<=t<=30:
            temp_caps["doctors"]=max(1,caps["doctors"]//2)
            temp_caps["nurses"]=max(1,caps["nurses"]//2)
        if failure and 12<=t<=14:
            temp_caps["or"]=0

        # Rebuild availability from capacity and active usage, ensuring no conflicts.
        for r in RESOURCES:
            used=sum(x["req"][r] for x in active)
            avail[r]=max(0,temp_caps[r]-used)

        for p in arrivals[t]:
            waiting.append(p)
            events.append((t,"ARRIVAL",p["Patient"],p["Name"]))

        max_queue=max(max_queue,len(waiting))
        waiting.sort(key=lambda p:priority_score(p,t,strategy,avail),reverse=True)

        assigned=[]
        for p in waiting:
            req={r:int(p[r]) for r in RESOURCES}
            if all(avail[r]>=req[r] for r in RESOURCES):
                for r,v in req.items(): avail[r]-=v
                item={"patient":p["Patient"],"name":p["Name"],"arrival":p["Arrival"],
                      "start":t,"end":t+int(p["Service"]),"wait":t-p["Arrival"],
                      "urgency":p["Urgency"],"department":p["Department"],"service":p["Service"],
                      "req":req}
                active.append(item); assigned.append(p)
                events.append((t,"ASSIGN",p["Patient"],p["Name"]))
        waiting=[p for p in waiting if p not in assigned]

        # Utilization uses capacity * time denominator.
        for r in RESOURCES:
            utilization[r]+=sum(x["req"][r] for x in active)

        timeline.append({"Hour":t,"Waiting":len(waiting),"In treatment":len(active),
                         "Available beds":avail["beds"],"Available ICU":avail["icu"],
                         "Available OR":avail["or"],"Available doctors":avail["doctors"],
                         "Available nurses":avail["nurses"],"Available ambulances":avail["ambulances"]})

    all_handled=finished+active
    total=len(df)
    avg_wait=np.mean([x["wait"] for x in all_handled]) if all_handled else 0
    max_wait=max([x["wait"] for x in all_handled],default=0)
    util={r: utilization[r]/(max(1,caps[r])*horizon) if caps[r]>0 else 0 for r in RESOURCES}
    completion=len(finished)/total if total else 0

    schedule=pd.DataFrame(all_handled)
    if not schedule.empty:
        for r in RESOURCES: schedule[r.title()]=schedule["req"].apply(lambda x:x[r])
        schedule["Status"]=np.where(schedule["end"]<=horizon,"Completed","In treatment")
        schedule=schedule[["patient","name","department","urgency","arrival","start","end","wait","service",
                           "Beds","Icu","Or","Doctors","Nurses","Ambulances","Status"]]
        schedule.columns=["Patient","Name","Department","Urgency","Arrival","Start","End","Wait (h)","Service (h)",
                          "Beds","ICU","OR","Doctors","Nurses","Ambulances","Status"]
    else:
        schedule=pd.DataFrame(columns=["Patient","Name","Department","Urgency","Arrival","Start","End","Wait (h)",
                                       "Service (h)","Beds","ICU","OR","Doctors","Nurses","Ambulances","Status"])
    metrics={"Patients":total,"Completed":len(finished),"Completion rate":completion,
             "Average wait":float(avg_wait),"Maximum wait":float(max_wait),"Max queue":max_queue,**util}
    return pd.DataFrame(timeline),schedule,metrics,events

# ---------- Session state ----------
if "seed" not in st.session_state: st.session_state.seed=42
if "patients" not in st.session_state: st.session_state.patients=generate_patients(60,42,False)


# ---------- Adaptive Response Engine ----------
def adaptive_pressure(timeline, df, caps, horizon):
    """Explainable operational pressure index for the simulated hospital."""
    latest = timeline.iloc[-1]
    util = []
    for r, col in [("beds","Available beds"),("icu","Available ICU"),("or","Available OR"),
                   ("doctors","Available doctors"),("nurses","Available nurses")]:
        cap = max(1, caps[r])
        used = max(0, cap - float(latest[col]))
        util.append(used / cap)
    resource_pressure = float(np.mean(util))
    queue_pressure = min(1.0, float(latest["Waiting"]) / max(1, caps["beds"]))
    recent = df[df["Arrival"] >= max(0, horizon - 6)]
    demand_pressure = min(1.0, len(recent) / max(1, caps["beds"]))
    score = round(100 * (0.45*resource_pressure + 0.35*queue_pressure + 0.20*demand_pressure))
    if score >= 75:
        state = "CRISIS"
    elif score >= 50:
        state = "HIGH PRESSURE"
    elif score >= 30:
        state = "WATCH"
    else:
        state = "STABLE"
    return score, state, resource_pressure, queue_pressure, demand_pressure

def decision_explanation(patient, now, caps):
    req = {r:int(patient[r]) for r in RESOURCES if r in patient.index}
    available = {r:int(caps.get(r,0)) for r in RESOURCES}
    blockers = [r for r in RESOURCES if req[r] > available[r]]
    wait = max(0, now - int(patient["Arrival"]))
    urgency_points = URGENCY[str(patient["Urgency"])] * 25
    wait_points = min(wait, 12) * 2
    fit = 20 if not blockers else 0
    score = urgency_points + wait_points + fit
    if blockers:
        reason = "Held because " + ", ".join(blockers) + " capacity is currently insufficient."
    else:
        reason = "Feasible now: all required resources are available."
    return score, wait, reason, blockers

# ---------- Sidebar ----------
st.sidebar.markdown("## 🏥 MedFlow")
st.sidebar.caption("Hospital Operations Simulator")
st.sidebar.markdown("---")
num=st.sidebar.slider("Number of patients",10,200,60)
horizon=st.sidebar.slider("Simulation horizon",12,96,48)
strategy=st.sidebar.selectbox("Scheduling strategy",["Urgency only","Urgency + waiting","Urgency + waiting + resource fit"])
st.sidebar.markdown("### Stress scenarios")
surge=st.sidebar.checkbox("🚑 Emergency surge")
shortage=st.sidebar.checkbox("👩‍⚕️ Staff shortage")
failure=st.sidebar.checkbox("⚠️ OR failure (12–14h)")
st.sidebar.markdown("### Hospital capacity")
beds=st.sidebar.number_input("Beds",1,300,35)
icu=st.sidebar.number_input("ICU beds",0,100,7)
ors=st.sidebar.number_input("Operating rooms",0,50,3)
doctors=st.sidebar.number_input("Doctors",1,150,12)
nurses=st.sidebar.number_input("Nurses",1,300,28)
ambulances=st.sidebar.number_input("Ambulances",0,100,6)
st.sidebar.markdown("---")
seed=st.sidebar.number_input("Random seed",0,999999,st.session_state.seed)
if st.sidebar.button("🎲 Generate / Reset Simulation",use_container_width=True):
    st.session_state.seed=int(seed)
    st.session_state.patients=generate_patients(num,int(seed),surge)
    st.rerun()

df=st.session_state.patients.copy()
# Keep patient count responsive if user changes slider without clicking.
if len(df)!=num or (surge and not st.session_state.get("last_surge",False)):
    df=generate_patients(num,int(seed),surge)
    st.session_state.patients=df
st.session_state.last_surge=surge

caps={"beds":int(beds),"icu":int(icu),"or":int(ors),"doctors":int(doctors),"nurses":int(nurses),"ambulances":int(ambulances)}
timeline,schedule,metrics,events=simulate(df,caps,strategy,horizon,surge,shortage,failure)

# ---------- Header ----------
st.markdown("""
<div class="hero">
<h1>🏥 MedFlow</h1>
<p>Prioritize Patients • Optimize Resources • Prevent Conflicts • Stress-Test Hospital Capacity</p>
</div>
""",unsafe_allow_html=True)

scenario=[]
if surge: scenario.append("Emergency surge")
if shortage: scenario.append("Staff shortage")
if failure: scenario.append("OR failure")
st.caption("Active scenario: "+(", ".join(scenario) if scenario else "Normal operations")+"  |  Strategy: "+strategy)

# ---------- KPIs ----------
cols=st.columns(6)
kpis=[("Patients",metrics["Patients"]),("Completed",metrics["Completed"]),("Completion",f'{metrics["Completion rate"]:.0%}'),
      ("Avg wait",f'{metrics["Average wait"]:.1f} h'),("Max wait",f'{metrics["Maximum wait"]:.1f} h'),("Peak queue",metrics["Max queue"])]
for c,(label,val) in zip(cols,kpis): c.metric(label,val)

# ---------- Navigation ----------
pages=["🏠 Command Center","🧠 Adaptive Response","👥 Patient Queue","🗓️ Allocation Board","📈 Analytics","🧪 Strategy Lab","🚨 Stress Test","ℹ️ How It Works"]
page=st.radio("Navigation",pages,horizontal=True,label_visibility="collapsed")

if page=="🏠 Command Center":
    st.markdown(
        "### Adaptive hospital operations — prioritize patients, balance resources, and respond to pressure in real time."
    )
    st.caption(
        "MedFlow combines urgency, waiting time, and resource availability to support explainable allocation decisions."
    )
    # ---------- COMMAND CENTER HEADER ----------
    pressure, state, rp, qp, dp = adaptive_pressure(
        timeline, df, caps, horizon
    )

    # Determine pressure label
    if pressure >= 75:
        pressure_label = "CRITICAL"
    elif pressure >= 50:
        pressure_label = "HIGH"
    elif pressure >= 30:
        pressure_label = "WATCH"
    else:
        pressure_label = "STABLE"

    st.markdown("""
    <div class="hero">
        <h1>🏥 MEDFLOW</h1>
        <p>ADAPTIVE HOSPITAL COMMAND CENTER</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------- CRISIS ALERT ----------
    if state == "CRISIS":
        st.markdown(
            '<div class="crisis">🚨 CRISIS MODE — Hospital capacity is under severe pressure.</div>',
            unsafe_allow_html=True
        )
    elif state == "HIGH PRESSURE":
        st.markdown(
            '<div class="crisis">⚠️ HIGH PRESSURE — Resource bottlenecks are emerging.</div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- PRESSURE + NEXT 6 HOURS ----------
    pressure_col, forecast_col = st.columns([1, 1.6])

    with pressure_col:
        st.markdown(f"""
        <div class="pressure">
            <div class="pressure-label">Hospital Pressure</div>
            <div class="pressure-value">{pressure:.0f}%</div>
            <div class="pressure-label">{pressure_label}</div>
        </div>
        """, unsafe_allow_html=True)

    with forecast_col:
        recent = df[df["Arrival"] >= max(0, horizon-6)]
        expected = max(1, int(round(len(recent) / 6 * 6)))
        critical = int((recent["Urgency"] == "Critical").sum())

        st.markdown("""
        <div class="forecast">
            <div class="section-title">🔮 NEXT 6 HOURS</div>
        """, unsafe_allow_html=True)

        fc1, fc2, fc3 = st.columns(3)

        fc1.metric(
            "Expected arrivals",
            expected
        )

        fc2.metric(
            "Critical cases",
            critical
        )

        fc3.metric(
            "Resource pressure",
            f"{rp:.0%}"
        )

        if critical >= max(2, int(caps["icu"] * 0.5)) or rp >= .75:
            st.warning(
                "⚠️ Forecast signal: protect ICU and staff capacity."
            )
        else:
            st.success(
                "✓ Current simulated capacity can absorb the recent demand pattern."
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------- RESOURCE STATUS ----------
    st.markdown(
        '<div class="section-title">LIVE RESOURCE STATUS</div>',
        unsafe_allow_html=True
    )

    resources = [
        ("ICU", "icu"),
        ("BEDS", "beds"),
        ("DOCTORS", "doctors"),
        ("NURSES", "nurses"),
        ("OPERATING ROOMS", "or"),
    ]

    resource_cols = st.columns(5)

    for col, (label, key) in zip(resource_cols, resources):

        utilization = float(metrics[key])
        utilization = max(0, min(100, utilization))

        if utilization >= 85:
            status = "CRITICAL"
        elif utilization >= 65:
            status = "HIGH"
        elif utilization >= 40:
            status = "MODERATE"
        else:
            status = "LOW"

        with col:
            st.markdown(f"""
            <div class="command-card">
                <div class="command-title">{label}</div>
                <div class="command-value">{utilization:.0f}%</div>
                <div class="small">{status} UTILIZATION</div>
            </div>
            """, unsafe_allow_html=True)

    # ---------- NOW / NEXT / RISK ----------
    st.markdown(
        '<div class="section-title">NOW → NEXT → RISK</div>',
        unsafe_allow_html=True
    )

    now_col, next_col, risk_col = st.columns(3)

    with now_col:
        waiting_now = int(timeline.iloc[-1]["Waiting"])

        st.markdown(f"""
        <div class="command-card">
            <div class="command-title">NOW</div>
            <div class="command-value">{waiting_now}</div>
            <div class="small">PATIENTS WAITING</div>
        </div>
        """, unsafe_allow_html=True)

    with next_col:
        st.markdown(f"""
        <div class="command-card">
            <div class="command-title">NEXT</div>
            <div class="command-value">{expected}</div>
            <div class="small">EXPECTED ARRIVALS / 6H</div>
        </div>
        """, unsafe_allow_html=True)

    with risk_col:
        risk_text = "LOW"

        if pressure >= 75:
            risk_text = "CRITICAL"
        elif pressure >= 50:
            risk_text = "HIGH"
        elif pressure >= 30:
            risk_text = "WATCH"

        st.markdown(f"""
        <div class="command-card">
            <div class="command-title">RISK</div>
            <div class="command-value">{risk_text}</div>
            <div class="small">CURRENT OPERATING RISK</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------- LIVE PATIENT FLOW ----------
    st.markdown(
        '<div class="section-title">👥 LIVE PATIENT FLOW</div>',
        unsafe_allow_html=True
    )

    display_patients = (
    df.assign(UrgencyRank=df["Urgency"].map(URGENCY))
      .sort_values(
          ["UrgencyRank", "Arrival"],
          ascending=[False, True]
      )
      .head(6)
    )

    for _, patient in display_patients.iterrows():

        urgency = patient["Urgency"]

        if urgency == "Critical":
            icon = "🚨"
            css = "patient-critical"
        elif urgency == "High":
            icon = "🔴"
            css = "patient-high"
        elif urgency == "Medium":
            icon = "🟠"
            css = "patient-medium"
        else:
            icon = "🟢"
            css = "patient-low"

        st.markdown(f"""
        <div class="command-card {css}" style="margin-bottom:8px;">
            <b>{icon} {patient["Patient"]}</b>
            &nbsp;&nbsp; {patient["Name"]}
            &nbsp;&nbsp; | &nbsp;&nbsp;
            <b>{urgency}</b>
            &nbsp;&nbsp; | &nbsp;&nbsp;
            {patient["Department"]}
            &nbsp;&nbsp; | &nbsp;&nbsp;
            Required: {patient["Service"]}h
        </div>
        """, unsafe_allow_html=True)

    # ---------- WHY THIS PATIENT ----------
    # ---------- WHY THIS PATIENT ----------
st.markdown(
    '<div class="section-title">🧠 WHY THIS PATIENT?</div>',
    unsafe_allow_html=True
)

explain_col, patient_col = st.columns([1.5, 1])

with patient_col:
    selected = st.selectbox(
        "Select patient",
        df["Patient"].tolist()
    )

with explain_col:
    selected_patient = df[
        df["Patient"] == selected
    ].iloc[0]

    score, wait, reason, blockers = decision_explanation(
        selected_patient,
        horizon,
        caps
    )

    st.markdown("### 🧠 Decision Explanation")

    st.write(f"**Patient:** {selected}")
    st.write(f"**Priority score:** {score:.0f}")
    st.write(f"**Urgency:** {selected_patient['Urgency']}")
    st.write(f"**Waiting time:** {wait} hours")
    st.write(f"**Department:** {selected_patient['Department']}")
    st.write(f"**Reason:** {reason}")

    if blockers:
        st.warning(
            "Resource constraint: " + ", ".join(blockers)
        )
    else:
        st.success(
            "✓ Required resources currently fit the configured capacity."
        )

    # ---------- RESOURCE TREND ----------
    st.markdown(
        '<div class="section-title">📊 RESOURCE PRESSURE TREND</div>',
        unsafe_allow_html=True
    )

    st.line_chart(
        timeline.set_index("Hour")[
            ["Waiting", "In treatment"]
        ],
        height=260
    )

    st.caption(
        "MedFlow uses synthetic simulation data. "
        "This dashboard is a prototype for resource-management research "
        "and is not intended for real clinical decisions."
    )
    st.subheader("Adaptive Response Engine")
    st.caption("MedFlow continuously interprets queue pressure, resource load and recent demand to explain what the hospital should watch next.")

    pressure, state, rp, qp, dp = adaptive_pressure(timeline, df, caps, horizon)
    a,b,c,d = st.columns(4)
    a.metric("Hospital pressure", f"{pressure}/100")
    b.metric("Operational state", state)
    c.metric("Resource pressure", f"{rp:.0%}")
    d.metric("Queue pressure", f"{qp:.0%}")

    if state == "CRISIS":
        st.error("🚨 CRISIS MODE — prioritize capacity protection and rapid reassessment.")
    elif state == "HIGH PRESSURE":
        st.warning("⚠️ HIGH PRESSURE — bottlenecks are emerging.")
    elif state == "WATCH":
        st.info("👀 WATCH — capacity is tightening, but remains manageable.")
    else:
        st.success("✅ STABLE — no major simulated bottleneck detected.")

    st.markdown("### 🔮 Next 6-hour demand signal")
    recent = df[df["Arrival"] >= max(0, horizon-6)]
    expected = max(1, int(round(len(recent) / 6 * 6)))
    critical = int((recent["Urgency"]=="Critical").sum())
    ec1,ec2,ec3 = st.columns(3)
    ec1.metric("Recent arrivals / 6h", len(recent))
    ec2.metric("Critical arrivals", critical)
    ec3.metric("Projected next-6h load", expected)
    if critical >= max(2, int(caps["icu"]*0.5)) or rp >= .75:
        st.warning("Prediction signal: protect ICU/staff capacity for incoming high-acuity demand.")
    else:
        st.info("Prediction signal: current capacity can absorb the recent demand pattern under this simulation.")

    st.markdown("### 🧠 Explainable patient decisions")
    st.caption("Select a patient to see the factors MedFlow considers. This is a simulation explanation, not clinical advice.")
    choices=df["Patient"].tolist()
    selected=st.selectbox("Patient", choices)
    p=df[df["Patient"]==selected].iloc[0]
    score,wait,reason,blockers=decision_explanation(p,horizon,caps)
    x,y,z=st.columns(3)
    x.metric("Decision score", f"{score:.0f}")
    y.metric("Waiting time", f"{wait} h")
    z.metric("Urgency", str(p["Urgency"]))
    st.markdown(f"**Why:** {reason}")
    if blockers:
        st.markdown("**Resource bottleneck:** " + ", ".join(blockers))
    else:
        st.markdown("**Resource fit:** ✓ all requested resources fit the current configured capacity.")

    st.markdown("### 🎮 What-if controls")
    st.caption("Change the scenario to see how the simulator responds. Use the sidebar for the full simulation controls.")
    w1,w2,w3=st.columns(3)
    extra=w1.slider("Emergency arrivals to add",0,20,0)
    nurse_cut=w2.slider("Extra nurse reduction",0,50,0,5)
    icu_cut=w3.slider("ICU beds unavailable",0,max(1,int(icu)),0)
    whatif_caps=caps.copy()
    whatif_caps["nurses"]=max(0,caps["nurses"]-nurse_cut)
    whatif_caps["icu"]=max(0,caps["icu"]-icu_cut)
    whatif_pressure=min(100, pressure + extra*2 + nurse_cut*0.6 + icu_cut*3)

    st.metric(
        "What-if pressure",
        f"{whatif_pressure:.0f}/100",
        delta=f"{whatif_pressure-pressure:+.0f} vs current"
    )

    if whatif_pressure >= 75:
        st.error("What-if result: simulated hospital enters CRISIS territory.")

    elif whatif_pressure >= 50:
        st.warning("What-if result: simulated hospital enters HIGH PRESSURE territory.")

    else:
        st.success("What-if result: simulated hospital remains below high-pressure threshold.")

    st.subheader("Patient → resource allocation")
    if schedule.empty:
        st.warning("No patient could be allocated within this simulation.")
    else:
        st.dataframe(schedule,use_container_width=True,height=560,hide_index=True)
        st.download_button("⬇️ Download allocation CSV",schedule.to_csv(index=False).encode(),"medflow_allocation.csv","text/csv")
    st.markdown("### Resource conflict check")
    if schedule.empty:
        st.success("No allocations — therefore no allocation conflict.")
    else:
        conflicts=[]
        for t in range(horizon):
            active=schedule[(schedule["Start"]<=t)&(schedule["End"]>t)]
            for r,cap in caps.items():
                col={"beds":"Beds","icu":"ICU","or":"OR","doctors":"Doctors","nurses":"Nurses","ambulances":"Ambulances"}[r]
                if active[col].sum()>cap: conflicts.append((t,col,active[col].sum(),cap))
        if conflicts: st.error(f"{len(conflicts)} capacity violations detected.")
        else: st.success("✓ Zero resource capacity violations detected.")

if page=="📈 Analytics":
    st.subheader("Operations analytics")
    a,b=st.columns(2)
    with a:
        st.markdown("### Waiting vs treatment load")
        st.line_chart(timeline.set_index("Hour")[["Waiting","In treatment"]])
    with b:
        st.markdown("### Resource utilization")
        util=pd.DataFrame({"Utilization":[metrics[r] for r in RESOURCES]},
                          index=[r.title() for r in RESOURCES])
        st.bar_chart(util)
    st.markdown("### Department demand")
    dept=df.groupby(["Department","Urgency"]).size().unstack(fill_value=0)
    st.bar_chart(dept)
    st.markdown("### Key performance indicators")
    perf=pd.DataFrame({
        "Metric":["Completion rate","Average waiting time","Maximum waiting time","Peak queue","Beds utilization","ICU utilization","OR utilization"],
        "Value":[f'{metrics["Completion rate"]:.1%}',f'{metrics["Average wait"]:.2f} h',f'{metrics["Maximum wait"]:.2f} h',
                 metrics["Max queue"],f'{metrics["beds"]:.1%}',f'{metrics["icu"]:.1%}',f'{metrics["or"]:.1%}']
    })
    st.dataframe(perf,use_container_width=True,hide_index=True)

elif page=="🧪 Strategy Lab":

    st.subheader("Scheduling Strategy Comparison")

    strategies = [
        "Urgency only",
        "Urgency + waiting",
        "Urgency + waiting + resource fit"
    ]

    rows = []

    for s in strategies:

        _, _, m, _ = simulate(
            df,
            caps,
            s,
            horizon,
            surge,
            shortage,
            failure
        )

        rows.append({
            "Strategy": s,
            "Completed": m["Completed"],
            "Completion rate": m["Completion rate"],
            "Avg wait (h)": m["Average wait"],
            "Max wait (h)": m["Maximum wait"],
            "Beds utilization": m["beds"],
            "ICU utilization": m["icu"],
            "OR utilization": m["or"]
        })

    comp = pd.DataFrame(rows)

    # Strategy comparison table
    st.markdown("### 📊 Strategy Performance")

    st.dataframe(
        comp.style.format({
            "Completion rate": "{:.1%}",
            "Avg wait (h)": "{:.2f}",
            "Max wait (h)": "{:.2f}",
            "Beds utilization": "{:.1%}",
            "ICU utilization": "{:.1%}",
            "OR utilization": "{:.1%}"
        }),
        use_container_width=True,
        hide_index=True
    )

    # Completed patients graph
    st.markdown("### 🏥 Patients Completed by Strategy")

    completion_chart = comp.set_index("Strategy")[["Completed"]]

    st.bar_chart(
        completion_chart,
        use_container_width=True
    )

    # Waiting time graph
    st.markdown("### ⏱️ Waiting Time Comparison")

    wait_chart = comp.set_index("Strategy")[
        ["Avg wait (h)", "Max wait (h)"]
    ]

    if (
        comp["Avg wait (h)"].max() > 0
        or comp["Max wait (h)"].max() > 0
    ):

        st.bar_chart(
            wait_chart,
            use_container_width=True
        )

    else:

        st.info(
            "All patients were completed without waiting "
            "in this scenario."
        )

    # Resource utilisation graph
    st.markdown("### ⚙️ Resource Utilisation Comparison")

    resource_chart = comp.set_index("Strategy")[
        [
            "Beds utilization",
            "ICU utilization",
            "OR utilization"
        ]
    ]

    st.bar_chart(
        resource_chart,
        use_container_width=True
    )

    st.caption(
        "This comparison is descriptive: each strategy is evaluated "
        "under the same simulated hospital scenario."
    )

    
elif page=="🚨 Stress Test":
    st.subheader("Hospital stress-test simulator")
    st.markdown("Use the sidebar checkboxes to simulate operational shocks.")
    cards=[]
    if surge: cards.append(("🚑 Emergency surge","Large burst of critical/high-priority arrivals"))
    if shortage: cards.append(("👩‍⚕️ Staff shortage","Doctor/nurse capacity is reduced for hours 18–30"))
    if failure: cards.append(("⚠️ OR failure","Operating-room capacity is unavailable for hours 12–14"))
    if not cards: st.success("No stress scenario active. Turn one on from the sidebar.")
    for title,desc in cards: st.markdown(f"**{title}** — {desc}")
    st.markdown("### Queue response")
    st.line_chart(timeline.set_index("Hour")[["Waiting"]])
    st.markdown("### Remaining resources")
    st.line_chart(timeline.set_index("Hour")[["Available beds","Available ICU","Available OR","Available doctors","Available nurses"]])

elif page=="ℹ️ How It Works":
    st.subheader("How MedFlow works")
    st.markdown("""
### 1. Patient arrival
Every simulated patient has:
- arrival time
- urgency
- department
- service duration
- resource requirements

### 2. Priority engine
Three explainable strategies are available:
- **Urgency only** — baseline triage-style priority.
- **Urgency + waiting** — waiting time gradually raises priority to reduce starvation.
- **Urgency + waiting + resource fit** — resource availability is a secondary scheduling signal.

### 3. Resource checker
A patient is assigned only if **all** requested resources are available simultaneously.

### 4. Simulation clock
At every simulated hour:
1. completed patients release resources
2. new patients enter the queue
3. waiting patients are ranked
4. feasible patients are allocated
5. utilization and queue metrics are updated

### 5. Stress scenarios
The hospital can be stress-tested using:
- emergency surges
- staff shortages
- operating-room failures

### 6. Safety boundary
MedFlow is a **hackathon simulation prototype**, not a clinical decision-support system. It should not be used for real patient-care decisions.
""")
    st.code("""Patient arrivals
      ↓
Priority calculation
      ↓
Waiting queue
      ↓
Resource feasibility check
      ↓
Allocation
      ↓
Simulation clock
      ↓
Metrics + dashboard""","text")

st.divider()
st.caption("MedFlow Pro • Hackathon prototype • Synthetic data only • Not for real clinical decisions")
