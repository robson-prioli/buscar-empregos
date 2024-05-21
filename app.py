import json
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote


def processar_dados(job):
    with st.spinner('Carregando...'):
        job_serialized = quote(job)

        driver = webdriver.Chrome()
        driver.get(f"https://www.trabalhabrasil.com.br/vagas-empregos/{job_serialized}")

        jobsName = driver.find_elements(By.XPATH, "//h2[@class='job__name']")
        jobsDetail = driver.find_elements(By.XPATH, "//h3[@class='job__detail']")
        jobsDescription = driver.find_elements(By.XPATH, "//p[@class='job__description']")

        for i in range(len(jobsName)):
            with st.container(border=True):
                st.subheader(jobsName[i].text)
                st.write(f"Detalhe: {jobsDetail[i].text}")
                st.write(f"Descrição: {jobsDescription[i].text}")

        st.success('Carregamento concluído!')


with st.container(border=True):
    st.title('iEmprego')
    job = st.text_input(label="", placeholder="Vaga desejada")
    
    if st.button("Buscar"):
        processar_dados(job)







