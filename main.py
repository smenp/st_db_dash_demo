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
    probes_df['to_delete'] = False
    probes_df_new = st.data_editor(probes_df)
    delete_action = st.button("Delete selected probes")
    if delete_action:
        probes_todelete = probes_df[probes_df_new['to_delete'] == True].id
        repo.delete(probes_todelete.values)
        st.experimental_rerun()
