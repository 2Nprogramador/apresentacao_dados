import streamlit as st


# Configuração da página
st.set_page_config(page_title="Proposta - Dados", layout="wide")

# Carregar o modelo LLAMA via Ollama

# Dividindo a tela em duas colunas
col1, col2 = st.columns([1, 1])

# Coluna 1: Títulos com caixas expansíveis
with col1:
    st.title("Gostaria de lhes apresentar o valor dos seus DADOS.")

    st.markdown("### **Como nós enxergamos os Dados?**")
    st.write(
        "No contexto da análise de dados para pequenos negócios, é essencial compreender como os elementos da cadeia de dados, metadados, informação, conhecimento e sabedoria interagem e se complementam. Essa cadeia forma a base para decisões mais estratégicas e eficazes."
    )
    with st.expander("Clique aqui para mais informações sobre 'Como nós enxergamos os Dados?'"):
        st.image("1(2).png")  # Preencha manualmente.

    st.markdown("### **Onde atuamos?**")
    st.write(
        "Nossa atuação está focada em ajudar pequenos negócios a extrair o máximo valor de seus dados, utilizando Python como uma poderosa ferramenta para análises e automações. Destacamos que atuamos na Coleta de Dados, Manipulação e Organização dos Dados, Análise de Dados e Automação de Processos."
    )
    with st.expander("Clique aqui para mais informações sobre 'Onde atuamos?'"):
        st.image("2(3).png")  # Preencha manualmente.

    st.markdown("### **Como atuamos?**")
    st.write(
        "Ao atuar em quase toda a cadeia de dados, oferecemos uma solução integrada que simplifica a complexidade do processo e garante resultados mensuráveis. Além disso, a flexibilidade e o poder do Python nos permitem adaptar nossas soluções às necessidades específicas de cada negócio, independente do setor ou do tamanho da operação."
    )
    with st.expander("Clique aqui para mais informações sobre 'Como atuamos?'"):
        st.image("3(3).png")  # Preencha manualmente.

    st.markdown("### **Benefícios Diretos**")
    st.write(
        "- Raio-X Completo do Negócio.\n"
        "- Fiscalização/Controle de Processos.\n"
        "- Decisão Baseada em Evidências."
    )
    with st.expander("Clique aqui para mais informações sobre 'Benefícios Diretos'"):
        st.image("atividade_5.png")  # Preencha manualmente.

    st.markdown("### **Benefícios Indiretos**")
    st.write(
        "- Automatização de Tarefas\n"
        "- Realização de Análise Preditiva.\n"
        "- Identificação/Redução de Ineficiências."
    )
    with st.expander("Clique aqui para mais informações sobre 'Benefícios Indiretos'"):
        st.image("atividade_6.png")  # Preencha manualmente.

    st.markdown("### **Primeiros Passos do Projeto**")
    st.write(
        "Nosso processo começa com o entendimento detalhado do funcionamento do seu negócio, mapeando operações, desafios e oportunidades. Identificamos quais dados são essenciais para o negócio e os que ainda precisam ser coletados.\n\n"
        "Em seguida, projetamos soluções personalizadas para coleta e armazenamento, garantindo que as informações sejam organizadas, acessíveis e intuitivas. Por meio das automações, eliminamos tarefas manuais repetitivas, como geração de relatórios operacionais, financeiros, contratuais e etc. Dessa forma, otimizando o tempo da sua equipe para atividades mais estratégicas e tornando os dados ativos valiosos."
    )
    with st.expander("Clique aqui para mais informações sobre 'Primeiros Passos do Projeto'"):
        st.image("atividade_8.png")  # Preencha manualmente.

