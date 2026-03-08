import pandas as pd 
import streamlit as st
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
st.set_page_config(page_title="Wire Rod Casting Predictor", layout="wide")

st.title("⚙️ Wire Rod Casting Parameter Predictor")
   
df = pd.read_excel("wire_rod_casting_parameters_100k_realistic.csv.xlsx")

X = df.drop(["UTS_MPa","Elongation","Conductivity_IACS"],axis = 1)
y = df[["UTS_MPa","Elongation","Conductivity_IACS"]]

 
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_poly)

  
model = linear_model.LinearRegression()
model.fit(X_scaled,y)



  
st.markdown("Enter the process parameters below to predict casting performance.")

st.divider()

# -------- Chemical Composition --------
st.subheader("🧪 Chemical Composition")

col1, col2, col3 = st.columns(3)

with col1:
    Cu_Content = st.number_input("Cu_Content", value=99.99)
    O2_Content_ppm = st.number_input("O2_Content_ppm", value=336.9)

with col2:
    P_Content_ppm = st.number_input("P_Content_ppm", value=0.78)
    S_Content_ppm = st.number_input("S_Content_ppm", value=11.71)

with col3:
    Ag_Content_ppm = st.number_input("Ag_Content_ppm", value=26.87)

st.divider()

# -------- Casting Parameters --------
st.subheader("🔥 Casting Parameters")

col4, col5, col6 = st.columns(3)

with col4:
    Casting_Temp_C = st.number_input("Casting_Temp_C", value=1193.8)
    Cooling_Water_Temp_C = st.number_input("Cooling_Water_Temp_C", value=25.0)

with col5:
    Casting_Speed_m_per_min = st.number_input("Casting_Speed_m_per_min", value=20.0)
    Cast_Bar_Entry_Temp_C = st.number_input("Cast_Bar_Entry_Temp_C", value=800.0)

with col6:
    Emulsion_Temp_C = st.number_input("Emulsion_Temp_C", value=35.0)

st.divider()

# -------- Cooling System --------
st.subheader("💧 Cooling System Parameters")

col7, col8 = st.columns(2)

with col7:
    Emulsion_Pressure_bar = st.number_input("Emulsion_Pressure_bar", value=3.0)
    Emulsion_Concentration = st.number_input("Emulsion_Concentration", value=5.0)

with col8:
    Rod_Quench_Water_Pressure_bar = st.number_input(
        "Rod_Quench_Water_Pressure_bar", value=4.0
    )

st.divider()
def create_input_dataframe():
  new_data = pd.DataFrame(columns=X.columns)
  new_data.loc[0]=0.0
  new_data["Cu_Content"]=Cu_Content
  new_data["O2_Content_ppm"]=O2_Content_ppm
  new_data["P_Content_ppm"]=P_Content_ppm
  new_data["S_Content_ppm"]=S_Content_ppm
  new_data["Ag_Content_ppm"]=Ag_Content_ppm
  new_data["Casting_Temp_C"]=Casting_Temp_C
  new_data["Cooling_Water_Temp_C"]=Cooling_Water_Temp_C
  new_data["Casting_Speed_m_per_min"]=Casting_Speed_m_per_min
  new_data["Cast_Bar_Entry_Temp_C"]=Cast_Bar_Entry_Temp_C
  new_data["Emulsion_Temp_C"]=Emulsion_Temp_C
  new_data["Emulsion_Pressure_bar"]=Emulsion_Pressure_bar
  new_data["Emulsion_Concentration"]=Emulsion_Concentration
  new_data["Rod_Quench_Water_Pressure_bar"]=Rod_Quench_Water_Pressure_bar


  new_data_scaled_1 = poly.transform(new_data)  
  new_data_poly = scaler.transform(new_data_scaled_1) 

  return new_data_poly 
  

if st.button("🔍 Predict", use_container_width=True):
  new_data_poly = create_input_dataframe()
  prediction = model.predict(new_data_poly)
  
  
  
  st.header("📊 Predicted Values")

  col1, col2, col3 = st.columns(3)

  with col1:
    st.metric("UTS (MPa)", f"{prediction[0][0]:.2f}")

  with col2:
    st.metric("Elongation (%)", f"{prediction[0][1]:.2f}")

  with col3:
    st.metric("Conductivity (IACS)", f"{prediction[0][2]:.2f}")
else:
    st.write("Click on Predict to get the values")
