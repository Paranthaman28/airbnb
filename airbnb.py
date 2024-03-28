import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image




df=pd.read_csv(r'C:\Users\Paranthaman\OneDrive\new_csv.csv')
st.set_page_config(page_title="AirBnb_Analysis by Paranthaman")
st.title(':bar_chart: AirBnb_Analysis')

SELECTED=option_menu(
    menu_title=None,
    options=['Home','Explore Data','Contact'],
    icons=['house','pencil-square','phone'],
    orientation='horizontal',
    styles={'container':{'padding':'10!important','width':'100'},"icon": {"color": "black", "font-size": "20px"}}
)
df__1=pd.read_csv(r'C:\\Users\\Paranthaman\\OneDrive\\new_csv.csv')

if SELECTED == "Home":

 st.header('Airbnb Analysis')
 st.subheader("Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.")
 st.subheader('Skills take away From This Project:')
 st.subheader('Python Scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDb, PowerBI or Tableau')
 st.subheader('Domain:')
 st.subheader('Travel Industry, Property management and Tourism')

if SELECTED == "Explore Data":
 tab1,tab2,tab3,tab4=st.tabs(['Price Analysis','Availability Analysis','LOCATION BASED Analysis','GEOSPATIAL VISUALIZATION'])
 with tab1:
  st.title('Price Analysis')
  col1,col2=st.columns(2)

  with col1:
   Room_type=st.selectbox("Select the Room Type",df__1['room_type'].unique())
   df1=df__1[df__1['room_type']==Room_type]

   df1.reset_index(drop= True, inplace= True)
   df_bar= pd.DataFrame(df1.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())

   df_bar.reset_index(inplace= True)

   fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
   st.plotly_chart(fig_bar)

  with col2:
    properties=st.selectbox("Select the property_type",df1['property_type'].unique())
    df2=df1[df1['property_type']==properties]
    df2.reset_index(drop= True, inplace= True)
    df_pie=pd.DataFrame(df2.groupby("host_response_time")[['price','bedrooms']].sum())
    df_pie.reset_index(inplace=True)
    fig_pi=px.pie(df_pie,values="price",names='host_response_time',
              hover_data=['bedrooms'])
    st.plotly_chart(fig_pi)

  col1,col2=st.columns(2)
  with col1:
    host_response_time=st.selectbox("Select the Host Response Time",df2['host_response_time'].unique())
    df3=df2[df2['host_response_time']==host_response_time]
    df_bar=pd.DataFrame(df3.groupby('bed_type')[['minimum_nights','maximum_nights','price']].sum())
    df_bar.reset_index(inplace=True)
    fif_bar=px.bar(df_bar,x='bed_type',y=['maximum_nights','minimum_nights'],
                  title='MINI and MAXI NIGHTS',hover_data='price',
                  barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r,width=600,height=500)
    
    st.plotly_chart(fif_bar)

  with col2:
   df_bar2=pd.DataFrame(df3.groupby('bed_type')[['accommodates','beds','bedrooms','price']].sum())
   df_bar2.reset_index(inplace=True)

   fig_bar_2=px.bar(df_bar2,x='bed_type',y=['bedrooms','beds','accommodates'],
                    title='Bedroom ,Beds,Accommondates',hover_data='price',
                    color_discrete_sequence=px.colors.sequential.Rainbow,width=500,height=600)
   
   st.plotly_chart(fig_bar_2)

 with tab2:
  st.title('Aavilabiity Analysis')
  col1,col2=st.columns(2)
  with col1:
    property_type_a=st.selectbox('Select the property type',df__1['property_type'].unique())
    df__1=df[df['property_type']==property_type_a]
    df__1.reset_index(drop=True,inplace=True)
    fig=px.sunburst(df__1, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=400,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Rainbow)
    st.plotly_chart(fig)
  with col2:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    fig_60=px.sunburst(df__1, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=400,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Rainbow_r)
    st.plotly_chart(fig_60)


  col1,col2=st.columns(2)
  with col1:
    fig_90=px.sunburst(df__1, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=400,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Rainbow)
    st.plotly_chart(fig_90)

  with col2:
    fig_360=px.sunburst(df__1, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=400,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Rainbow_r)
    st.plotly_chart(fig_360)

 with tab3:
  st.title('Location Analysis')
  df_2=pd.read_csv(r'C:\\Users\\Paranthaman\\OneDrive\\new_csv.csv')
  country=st.selectbox('Select the country',df_2['country'].unique())
  df_2_1=df_2[df_2['country']==country]
  df_2_1.reset_index(drop=True,inplace=True)
  properties_type=st.selectbox('Select the proprty types',df_2_1['property_type'].unique())
  df_2_2=df_2_1[df_2_1['property_type']==properties_type]
  df_2_2.reset_index(drop=True,inplace=True)
  st.dataframe(df_2_1)

  def select_the_file(values):
    if values == str(df_2_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df_2_2['price'].min())+' '+str("(30% of the Value)"):

        df_val_30= df_2_2[df_2_2["price"] <= differ_max_min*0.30 + df_2_2['price'].min()]
        df_val_30.reset_index(drop= True, inplace= True)
        return df_val_30
    elif values == str(differ_max_min*0.30 + df_2_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df_2_2['price'].min())+' '+str("(30% to 60% of the Value)"):
    
        df_val_60= df_2_2[df_2_2["price"] >= differ_max_min*0.30 + df_2_2['price'].min()]
        df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df_2_2['price'].min()]
        df_val_60_1.reset_index(drop= True, inplace= True)
        return df_val_60_1

    elif values == str(differ_max_min*0.60 + df_2_2['price'].min())+' '+str('to')+' '+str(df_2_2['price'].max())+' '+str("(60% to 100% of the Value)"):

        df_val_100= df_2_2[df_2_2["price"] >= differ_max_min*0.60 + df_2_2['price'].min()]
        df_val_100.reset_index(drop= True, inplace= True)
        return df_val_100


  differ_max_min= df_2_2['price'].max()-df_2_2['price'].min()
  val_sel= st.radio("Select the Price Range",[str(df_2_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df_2_2['price'].min())+' '+str("(30% of the Value)"),
                                                      
                                                      str(differ_max_min*0.30 + df_2_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df_2_2['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                      str(differ_max_min*0.60 + df_2_2['price'].min())+' '+str('to')+' '+str(df_2_2['price'].max())+' '+str("(60% to 100% of the Value)")])
                                            
  df_values= select_the_file(val_sel)

  st.dataframe(df_values)

  df_values_group=pd.DataFrame(df_values.groupby('accommodates')[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
  df_values_group.reset_index(inplace=True)

  fig_1= px.bar(df_values_group, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
  st.plotly_chart(fig_1)

  room_type=st.selectbox('select the Room type',df__1['room_type'].unique())

  df_values_1=df_values[df_values['room_type']==room_type]

  fig_2= px.bar(df_values_1, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
            hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
  st.plotly_chart(fig_2)

  fig_3= px.bar(df_values_1, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
              hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
  st.plotly_chart(fig_3)


 with tab4:

  st.title("GEOSPATIAL VISUALIZATION")
  st.write("")

  fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                  color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                  zoom=1)
  fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
  st.plotly_chart(fig_4) 



if SELECTED=='Contact':
  st.write('NAME     :  PARANTHAMAN P')
  st.write('E-MAIL   :  thaliavgahmu04@gamil.com')
  st.write('GITHUP,github:https://github.com/Paranthaman28/Paranthaman28')
  st.write('LINKED-IN:https://www.linkedin.com/in/paranthamam-p-b468101b0/')
  st.write('PHONE NUMBER:+91-6384234070')