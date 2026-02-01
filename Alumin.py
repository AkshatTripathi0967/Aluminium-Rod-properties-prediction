import pandas as pd 
import streamlit as st
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
st.title("Wire Rod Casting Parameter Predictor")
   
df = pd.read_excel("wire_rod_casting_parameters_100k_realistic.csv.xlsx")

X = df.drop(["UTS_MPa","Elongation","Conductivity_IACS"],axis = 1)
y = df[["UTS_MPa","Elongation","Conductivity_IACS"]]

 
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_poly)
  
model = linear_model.LinearRegression()
model.fit(X_train_scaled,y)


  
with st.form("Wire Rod Caasting Details"):
  Cu_Content = st.text_input("Cu_Content")
  O2_Content_ppm=st.text_input("O2_Content_ppm")
  P_Content_ppm= st.text_input("P_Content_ppm")
  S_Content_ppm= st.text_input("S_Content_ppm")
  Ag_Content_ppm= st.text_input("Ag_Content_ppm")
  Casting_Temp_C= st.text_input("Casting_Temp_C")
  Cooling_Water_Temp_C= st.text_input("Cooling_Water_Temp_")
  Casting_Speed_m_per_min = st.text_input("Casting_Speed_m_per_min")
  Cast_Bar_Entry_Temp_C= st.text_input("Cast_Bar_Entry_Temp_C")
  Emulsion_Temp_C= st.text_input("Emulsion_Temp_C")
  Emulsion_Pressure_bar= st.text_input("Emulsion_Pressure_bar")
  Emulsion_Concentration = st.text_input("Emulsion_Concentration")
  Rod_Quench_Water_Pressure_bar = st.text_input("Rod_Quench_Water_Pressure_bar")
  submit = st.form_submit_button("Predict")

def create_input_dataframe(a,b,c,d,e,f,g,h,i,j,k,l,m):
  new_data = pd.DataFrame(columns=X.columns)
  new_data.loc[0]=0.0
  new_data["Cu_Content"]=float(a)
  new_data["O2_Content_ppm"]=float(b)
  new_data["P_Content_ppm"]=float(c)
  new_data["S_Content_ppm"]=float(d)
  new_data["Ag_Content_ppm"]=float(e)
  new_data["Casting_Temp_C"]=float(f)
  new_data["Cooling_Water_Temp_C"]=float(g)
  new_data["Casting_Speed_m_per_min"]=float(h)
  new_data["Cast_Bar_Entry_Temp_C"]=float(i)
  new_data["Emulsion_Temp_C"]=float(j)
  new_data["Emulsion_Pressure_bar"]=float(k)
  new_data["Emulsion_Concentration"]=float(l)
  new_data["Rod_Quench_Water_Pressure_bar"]=float(m)


  new_data_scaled_1 = poly.transform(new_data)  
  new_data_poly = scaler.transform(new_data_scaled_1)  



  prediction = model.predict(new_data_poly)
  return prediction
    
  

if submit:
  
  
  create =create_input_dataframe(Cu_Content,O2_Content_ppm,P_Content_ppm,S_Content_ppm,Ag_Content_ppm,Casting_Temp_C,Cooling_Water_Temp_C,Casting_Speed_m_per_min,Cast_Bar_Entry_Temp_C,Emulsion_Temp_C,Emulsion_Pressure_bar,Emulsion_Concentration,Rod_Quench_Water_Pressure_bar)
  
  st.header("Predicted Values")
  st.text_area("UTS_MPa",value=create[0][0])
  st.text_area("Elongation",value=create[0][1])
  st.text_area("Conductivity_IACS",value=create[0][2])
else:
    st.write("Click on Predict to get the values")  
