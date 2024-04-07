import streamlit as st
import pickle


pickle_in=open("iris.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_output(SepalLength,SepalWidth,PetalLength,PetalWidth):
    res=classifier.predict([[SepalLength,SepalWidth,PetalLength,PetalWidth]])
    return res

def main():
    st.title("IRIS")
    html="""
    <div style="background-color:blue">
    </div>"""
    st.markdown(html,unsafe_allow_html=True)
    SepalLength=st.text_input("SepalLength","Type Here")
    SepalWidth=st.text_input("SepalWidth","Type Here")
    PetalLength=st.text_input("PetalLength","Type Here")
    PetalWidth=st.text_input("PetalWidth","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_output(SepalLength,SepalWidth,PetalLength,PetalWidth)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()