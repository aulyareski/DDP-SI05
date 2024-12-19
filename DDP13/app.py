import streamlit as st

dashboard = st.Page("dasboard.py",title="dasboard")
nabung = st.Page("nabung.py",title="menabung")

pg = st.navigation(
    {
     "menu utama" : [dashboard],
     "transaksi" : [nabung],

    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []
    
pg.run()