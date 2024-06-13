from lib import *
import pandas as pd
st.title("Forecasting Sales")


left_column, center ,right_column = st.columns(3)
with left_column:
    st.subheader("Critical Values 1%:")
    st.subheader(f"-3.4519023023726696")

with center:
    st.subheader("Critical Values 5%:")
    st.subheader(f"-2.8710320399170537")

with right_column:
    st.subheader("Critical Values 10%::")
    st.subheader(f"-2.57182745012602")

left_column, center ,right_column = st.columns(3)
with left_column:
    st.subheader("ADF Statistic:")
    st.subheader(f"-15.946856446772234")

with center:
    pass  

with right_column:
    st.subheader("p-value:")
    st.subheader(f"7.432666346087219e-29")



st.markdown("<h2 style='text-align: center; color: green;'>Data Stasioner</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
        .main h1 {
        text-align: center;
    }
     .stDataFrame {
        width: 50%;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("""---""")
st.subheader("Distribusi Data tiap Kuartil")


left_column,right_column = st.columns(2)
with left_column:
    st.markdown("Data Q1-2023")
    image_path = './src/kuartil1.png'
    st.markdown(
        f"""
        <style>
        .center {{
            display: flex;
            justify-content: center;
        }}
        .center img {{
            width: 100%;
            height: auto;
        }}
        <div class="center">
            <img src="data:image/jpeg;base64,{st.image(image_path)}"/>
        </div>
        """,
        unsafe_allow_html=True
    )


with right_column:
    st.markdown("Data Q2-2023")
    image_path = './src/kuartil2.png'
    st.markdown(
        f"""
        <style>
        .center {{
            display: flex;
            justify-content: center;
        }}
        .center img {{
            width: 100%;
            height: auto;
        }}
        <div class="center">
            <img src="data:image/jpeg;base64,{st.image(image_path)}"/>
        </div>
        """,
        unsafe_allow_html=True
    )


left_column,right_column = st.columns(2)
with left_column:
    st.markdown("Data Q3-2023")
    image_path = './src/kuartil3.png'
    st.markdown(
        f"""
        <style>
        .center {{
            display: flex;
            justify-content: center;
        }}
        .center img {{
            width: 100%;
            height: auto;
        }}
        <div class="center">
            <img src="data:image/jpeg;base64,{st.image(image_path)}"/>
        </div>
        """,
        unsafe_allow_html=True
    )


with right_column:
    st.markdown("Data Q4-2023")
    image_path = './src/kuartil4.png'
    st.markdown(
        f"""
        <style>
        .center {{
            display: flex;
            justify-content: center;
        }}
        .center img {{
            width: 100%;
            height: auto;
        }}
        <div class="center">
            <img src="data:image/jpeg;base64,{st.image(image_path)}"/>
        </div>
        """,
        unsafe_allow_html=True
    )



st.subheader("Distribusi Data 2023")
left_column,center, right_column = st.columns([1,2,1])
with left_column:
    pass
with center:
    image_path = './src/persebarantahun.png'

    st.markdown(
        f"""
        <style>
        .center {{
            display: flex;
            justify-content: center;
        }}
        .center img {{
            width: 100%;
            height: auto;
        }}
        <div class="center">
            <img src="data:image/jpeg;base64,{st.image(image_path)}"/>
        </div>
        """,
        unsafe_allow_html=True
    )
with right_column:
    pass

st.markdown("""---""")
st.subheader("ACF dan PACF")
image_path = './src/acfpacf.png'

st.markdown(
    f"""
    <style>
    .center {{
        display: flex;
        justify-content: center;
    }}
    .center img {{
        width: 100%;
        height: auto;
    }}
    <div class="center">
        <img src="data:image/jpeg;base64,{st.image(image_path)}"/>
    </div>
    """,
    unsafe_allow_html=True
)
cutoff_acf = pd.read_csv('./src/ACF.csv')
cutoff_pacf =pd.read_csv('./src/PACF.csv')
left_column,right_column = st.columns(2)
with left_column:
    st.write('Lags yang melampaui batas cut-off pada ACF:', cutoff_acf)

with right_column:
    st.write('Lags yang melampaui batas cut-off pada PACF:', cutoff_pacf)

st.markdown("""---""")
st.subheader("Model ARIMA")
dfAIC = pd.read_csv("./src/nilaiAIC.csv")
NamaModel = [
        'AR(4)I(0)MA(4)', 'AR(4)I(0)MA(6)', 'AR(4)I(0)MA(8)', 'AR(4)I(0)MA(10)', 'AR(4)I(0)MA(20)', 'AR(4)I(0)MA(36)', 'AR(4)I(0)MA(40)',
        'AR(6)I(0)MA(4)', 'AR(6)I(0)MA(6)', 'AR(6)I(0)MA(8)', 'AR(6)I(0)MA(10)', 'AR(6)I(0)MA(20)', 'AR(6)I(0)MA(36)', 'AR(6)I(0)MA(40)',
        'AR(8)I(0)MA(4)', 'AR(8)I(0)MA(6)', 'AR(8)I(0)MA(8)', 'AR(8)I(0)MA(10)', 'AR(8)I(0)MA(20)', 'AR(8)I(0)MA(36)', 'AR(8)I(0)MA(40)',
        'AR(9)I(0)MA(4)', 'AR(9)I(0)MA(6)', 'AR(9)I(0)MA(8)', 'AR(9)I(0)MA(10)', 'AR(9)I(0)MA(20)', 'AR(9)I(0)MA(36)', 'AR(9)I(0)MA(40)',
        'AR(10)I(0)MA(4)', 'AR(10)I(0)MA(6)', 'AR(10)I(0)MA(8)', 'AR(10)I(0)MA(10)', 'AR(10)I(0)MA(20)', 'AR(10)I(0)MA(36)', 'AR(10)I(0)MA(40)', 
        'AR(13)I(0)MA(4)', 'AR(13)I(0)MA(6)', 'AR(13)I(0)MA(8)', 'AR(13)I(0)MA(10)', 'AR(13)I(0)MA(20)', 'AR(13)I(0)MA(36)', 'AR(13)I(0)MA(40)', 
        'AR(16)I(0)MA(4)', 'AR(16)I(0)MA(6)', 'AR(16)I(0)MA(8)', 'AR(16)I(0)MA(10)', 'AR(16)I(0)MA(20)', 'AR(16)I(0)MA(36)', 'AR(16)I(0)MA(40)', 
        'AR(20)I(0)MA(4)', 'AR(20)I(0)MA(6)', 'AR(20)I(0)MA(8)', 'AR(20)I(0)MA(10)', 'AR(20)I(0)MA(20)', 'AR(20)I(0)MA(36)', 'AR(20)I(0)MA(40)',
        'AR(26)I(0)MA(4)', 'AR(26)I(0)MA(6)', 'AR(26)I(0)MA(8)', 'AR(26)I(0)MA(10)', 'AR(26)I(0)MA(20)', 'AR(26)I(0)MA(36)', 'AR(26)I(0)MA(40)',
        'AR(28)I(0)MA(4)', 'AR(28)I(0)MA(6)', 'AR(28)I(0)MA(8)', 'AR(28)I(0)MA(10)', 'AR(28)I(0)MA(20)', 'AR(28)I(0)MA(36)', 'AR(28)I(0)MA(40)',
        'AR(36)I(0)MA(4)', 'AR(36)I(0)MA(6)', 'AR(36)I(0)MA(8)', 'AR(36)I(0)MA(10)', 'AR(36)I(0)MA(20)', 'AR(36)I(0)MA(36)', 'AR(36)I(0)MA(40)'
    ]
dfMODEL = pd.DataFrame(NamaModel)
dfMODEL["Nilai AIC"] = dfAIC
st.write(dfMODEL)

st.markdown(
    """
    <style>
        .main h1 {
        text-align: center;
    }
     .stDataFrame {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
image_path = './src/modelarima.png'
st.markdown(
    f"""
    <style>
    .center {{
        display: flex;
        justify-content: center;
    }}
    .center img {{
        width: 100%;
        height: auto;
    }}
    <div class="center">
        <img src="data:image/jpeg;base64,{st.image(image_path)}"/>
    </div>
    """,
    unsafe_allow_html=True
)

left_column, center ,right_column = st.columns(3)
with left_column:
    st.subheader("RMSE:")
    st.subheader(f"14.152")

with center:
    st.subheader("AIC:")
    st.subheader(f"2351.98")

with right_column:
    st.subheader("MAE:")
    st.subheader(f"12.84%")

