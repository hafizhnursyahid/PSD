from lib import *

st.set_page_config(
    layout="wide",   # Choose "wide" or "centered" layout
    initial_sidebar_state="expanded", # Control the initial state of the sidebar
    page_title="xyz Roastery Dashboard",
    page_icon=":coffee:"  # Optional: add a fun icon
)

st.title("xyz Roastery Dashboard")
## dummy data
df = pd.read_csv("./src/sampled_data.csv")

## query data
st.sidebar.header("Select Data:")
bulan = st.sidebar.multiselect(
    "Select the bulan Type:",
    options=df["bulan"].unique()
)

Coffeeshop = st.sidebar.multiselect(
    "Select the Client Type:",
    options=df["Coffeeshop"].unique()
)

Jenis = st.sidebar.multiselect(
    "Select the Jenis:",
    options=df["Jenis"].unique()
)
@st.cache_data

def filter_items(df, selected_coffeeshops, selected_bulan):
    filtered_df = df.copy()  
    if selected_coffeeshops:
        filtered_df = filtered_df[filtered_df["Coffeeshop"].isin(selected_coffeeshops)]
    if selected_bulan:
        filtered_df = filtered_df[filtered_df["bulan"].isin(selected_bulan)]
    return filtered_df["Item"].unique()

filtered_items = filter_items(df, tuple(Coffeeshop), tuple(bulan))

Item = st.sidebar.multiselect(
    "Select the Item:",
    options=filtered_items,
)

if not (bulan or Coffeeshop or Jenis or Item):
    df_selection = df
else:
    query_parts = []

    if bulan:
        if "All" in bulan:
            query_parts.append("True")
        else:
            query_parts.append("bulan in @bulan")

    if Coffeeshop:
        if "All" in Coffeeshop:
            query_parts.append("True")
        else:
            query_parts.append("Coffeeshop in @Coffeeshop")

    if Jenis:
        if "All" in Jenis:
            query_parts.append("True")
        else:
            query_parts.append("Jenis in @Jenis")
    
    if Item:
        if "All" in Item:
            query_parts.append("True")
        else:
            query_parts.append("Item in @Item")

    query = " and ".join(query_parts)
    df_selection = df.query(query)

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

st.write(df_selection)
st.markdown("""---""")

# KPI MATRIX
total_sales = df_selection['Total'].sum()
df_selection['Volume'] = [float(str(i).replace(",", "")) for i in df_selection['Volume']]
df_selection['Volume'].astype(float)
total_volume =((df_selection['Volume'] * df_selection['Qty'])/1000).sum()
customer_count = df_selection['Coffeeshop'].nunique() 
discounted_data = df_selection[df_selection['Diskon'] > 0]
operating_loss = ((discounted_data['Diskon'] / 100) * discounted_data['Total']).sum()

formatted_total_sales = f"Rp{total_sales:,.0f}"
formatted_total_volume = f"{total_volume:,.0f}"
formatted_operating_loss = f"Rp{operating_loss:,.0f}"

metric_css = """
<style>
.metric-container {
    display: flex;
    justify-content: space-around;
    margin: 20px 0;
}
.metric {
    flex: 1;
    margin: 0 10px;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 24px;
}
.metric.sales { background-color: #e0f7fa; }
.metric.customer { background-color: #fff9c4; }
.metric.orders { background-color: #bbdefb; }
.metric.loss { background-color: #ffcdd2; }
</style>
"""

st.markdown(metric_css, unsafe_allow_html=True)
st.markdown("""
<div class="metric-container">
    <div class="metric sales">
        <div>Total Sales</div>
        <div>Rp{total_sales:,.0f}</div>
    </div>
    <div class="metric customer">
        <div>Customer</div>
        <div>{customer_count}</div>
    </div>
    <div class="metric orders">
        <div>Total Volume</div>
        <div>{total_volume} Kg</div>
    </div>
    <div class="metric loss">
        <div>Operating Loss</div>
        <div>Rp{operating_loss:,.0f}</div>
    </div>
</div>
""".format(total_sales=total_sales, customer_count=customer_count, total_volume=total_volume, operating_loss=operating_loss), unsafe_allow_html=True)

# BARPLOT

sliderleft, sliderright = st.columns(2)
num_coffeeshops = sliderright.slider(
    "Number of Coffeeshops to Display", 1, len(df_selection["Coffeeshop"].unique()), 5
)
num_items = sliderleft.slider(
    "Number of Items to Display", 1, len(df_selection["Item"].unique()), 5
)

profit_by_PM = (
    df_selection.groupby(by=["Coffeeshop"])
    .sum()[["Total"]]
    .sort_values(by="Total", ascending=False)
    .head(num_coffeeshops)
)

profit_by_PB = (
    df_selection.groupby(by=["Item"])
    .sum()[["Total"]]
    .sort_values(by="Total", ascending=False)
    .head(num_items)
)

profit_by_PM2 = (
    df_selection.groupby(by=["Jenis"])
    .sum()[["Total"]]
    .sort_values(by="Total", ascending=False)
)

fig_product_sales = px.bar(
    profit_by_PM,
    x="Total",
    y=profit_by_PM.index,
    orientation="h",
    title="<b>Total Penjualan berdasarkan Client</b>",
    color_discrete_sequence=["#0083B8"] * len(profit_by_PM),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_PB_sales = px.bar(
    profit_by_PB,
    x=profit_by_PB.index,
    y="Total",
    orientation="v",
    title="<b>Total Penjualan berdasarkan Item</b>",
    color_discrete_sequence=["#0083B8"] * len(profit_by_PB),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column2, right_column2 = st.columns(2)
left_column2.plotly_chart(fig_PB_sales, use_container_width=True)
right_column2.plotly_chart(fig_product_sales, use_container_width=True)


# BAR PLOT BARIS DUA
profit_by_PM2 = (
    df_selection.groupby(by=["Jenis"]).sum()[["Total"]].sort_values(by="Total")
)
fig_product_sales2 = px.bar(
    profit_by_PM2,
    x="Total",
    y=profit_by_PM2.index,
    orientation="h",
    title="<b>Total Penjualan berdasarkan jenis</b>",
    color_discrete_sequence=["#0083B8"] * len(profit_by_PM2),
    template="plotly_white",
)
fig_product_sales2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

jenis_agg = df_selection.groupby('Jenis')['Total'].sum().reset_index()
jenis_agg = jenis_agg.sort_values(by='Total', ascending=False)
pie = px.pie(jenis_agg, values='Total', names='Jenis', title='Total Sales by Jenis', hole=0.6)
pie.update_traces(textposition='inside', textinfo='percent+label')


profit_by_PB2 = (
    df_selection.groupby(by=["Jenis"]).sum()[["Total"]].sort_values(by="Total")
)
fig_PB_sales2 = px.bar(
    profit_by_PB2,
    x=profit_by_PB2.index,
    y="Total",
    orientation="v",
    title="<b>Total Penjualan berdasarkan Jenis</b>",
    color_discrete_sequence=["#0083B8"] * len(profit_by_PB2),
    template="plotly_white",
)
fig_product_sales2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column21, right_column21 = st.columns(2)
left_column21.plotly_chart(pie, use_container_width=True)
right_column21.plotly_chart(fig_PB_sales2, use_container_width=True)

# LINE PLOT

dfline1 = df_selection.groupby('Tanggal')['Total'].sum().reset_index()
dfline1['Tanggal'] = pd.to_datetime(dfline1['Tanggal']) 

mypalette = Spectral11[0:3]
p = figure(
    title='Total Sales and Quantity Over Time', 
    x_axis_label='Date', 
    y_axis_label='Values', 
    x_axis_type='datetime'
)

mypalette = Spectral11[0:3]
p.line(x = dfline1['Tanggal'], y = dfline1['Total'], line_color=mypalette[1], line_width=2, legend_label='Total Sales')

p.legend.location = "top_left"
p.legend.click_policy="hide"


LINEcol1, LINEcol2 = st.columns([4, 1])

LINEcol1.bokeh_chart(p, use_container_width=True)
LINEcol2.write(dfline1)


