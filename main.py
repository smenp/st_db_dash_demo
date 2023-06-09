import streamlit as st
import repo

view_tab, add_tab = st.tabs(["View Probes", "Add Probe"])

with add_tab:
    st.write("Enter probe name")
    probe_name = st.text_input("Probe name")
    probe_num = st.number_input("Probe number", 1, step=1)
    submitted = st.button("Submit")

    if submitted:
        repo.add(probe_name, probe_num)

with view_tab:
    probes_df = repo.get_all_probes()
    st.dataframe(probes_df)