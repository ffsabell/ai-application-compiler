import streamlit as st
import time

from compiler import compile_application
from validator import validate_schema
from repair_engine import repair_schema
from runtime import simulate_runtime

st.set_page_config(
    page_title="AI App Compiler",
    layout="wide"
)

st.title("🤖 AI Application Compiler")

st.markdown("""
### Natural Language → Application Specification

This system converts a user prompt into:

- Intent Analysis
- Architecture Design
- Database Schema
- API Schema
- UI Schema
- Authentication Rules
- Validation Report
- Runtime Simulation
""")

prompt = st.text_area(
    "Describe the application you want to build",
    height=200,
    placeholder="""
Example:

Build a CRM with login,
contacts,
dashboard,
role based access,
payments,
and admin analytics.
"""
)

if st.button("Generate Application"):

    if not prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    start_time = time.time()

    with st.spinner("Compiling Application..."):

        compiled = compile_application(prompt)

        errors = validate_schema(compiled)

        repaired_schema, repairs = repair_schema(
            compiled,
            errors
        )

        runtime = simulate_runtime(
            repaired_schema
        )

    latency = round(
        time.time() - start_time,
        2
    )

    st.success("Application Generated Successfully")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Compiled Output",
            "Validation",
            "Repairs",
            "Runtime"
        ]
    )

    with tab1:

        st.subheader(
            "Generated Application Specification"
        )

        st.json(
            repaired_schema
        )

    with tab2:

        st.subheader(
            "Validation Results"
        )

        if len(errors) == 0:

            st.success(
                "No validation errors detected."
            )

        else:

            st.error(
                "Validation issues found."
            )

            st.json(errors)

    with tab3:

        st.subheader(
            "Repair Results"
        )

        if len(repairs) == 0:

            st.success(
                "No repairs required."
            )

        else:

            st.json(repairs)

    with tab4:

        st.subheader(
            "Runtime Simulation"
        )

        if runtime["status"] == "SUCCESS":

            st.success(
                "Runtime simulation passed."
            )

        else:

            st.error(
                "Runtime simulation failed."
            )

        st.json(runtime)

    st.markdown("---")

    st.subheader("📊 Metrics Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Latency (seconds)",
            latency
        )

    with col2:

        st.metric(
            "Validation Errors",
            len(errors)
        )

    with col3:

        st.metric(
            "Repairs Applied",
            len(repairs)
        )

st.markdown("---")

st.markdown("""
## Pipeline

User Prompt

⬇

Compiler Engine

⬇

Validation Engine

⬇

Repair Engine

⬇

Runtime Simulator

⬇

Final Application Specification

---

### Features

✅ Intent Extraction

✅ Architecture Generation

✅ Database Schema Generation

✅ API Schema Generation

✅ UI Schema Generation

✅ Authentication Rules

✅ Validation Engine

✅ Repair Engine

✅ Runtime Simulation

✅ Metrics Dashboard
""")