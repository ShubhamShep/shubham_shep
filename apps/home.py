import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("INDICES GEOSPATIAL")

    st.markdown(
        """
     THESE IS CREATED BY SHUBHAM SHEP THE FOUNDER OF INDICES GEOSPTAIL PVT LTD 

    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
