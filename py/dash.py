import streamlit as st
import pandas as pd
import plotly.express as px
import os

pwd = '..'

try:
    df = pd.read_csv(f'../src/csv/supermarket_sales.csv', sep=';', decimal=',')
except:
    df = pd.read_csv(f'/app/src/csv/supermarket_sales.csv', sep=';', decimal=',')

    pwd = '/app'

st.set_page_config(page_title='SuperSales Insights', page_icon=f'{pwd}/src/img/cart.png', layout='wide')

st.title('Visão Mensal das Vendas de um Supermercado')
st.divider()

st.sidebar.title('Filtros')
st.sidebar.divider()




df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by=['Date'])

df['Month'] = df['Date'].apply(lambda x: str(x.month) + '/' + str(x.year))
month = st.sidebar.selectbox('Mês', sorted(df['Month'].unique()))

df_filtered = df[df['Month'] == month]

st.header('Análise Geral')

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Faturamento Diário:

fig_date = px.bar(df_filtered, x='Date', y='Total',
                  color='City', title='Faturamento Diário')
col1.plotly_chart(fig_date, use_container_width=True)

# Faturamento por Tipo de Produto

fig_prod = px.bar(df_filtered, x='Total', y='Product line',
                  color='City', title='Faturamento por Tipo de Produto',
                  orientation='h')
col2.plotly_chart(fig_prod, use_container_width=True)

# Faturamento por Dia

city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total, x='City', y='Total',
                  color='City',
                  title='Faturamento por Dia')
col3.plotly_chart(fig_city, use_container_width=True)

# Faturamento por Tipo de Pagamento

fig_kind_pay = px.pie(df_filtered, values='Total', names='Payment',
                      title='Faturamento por Tipo de Pagamento')
col4.plotly_chart(fig_kind_pay, use_container_width=True)

# Avaliação

city_rating = df_filtered.groupby('City')[['Rating']].mean().reset_index()
fig_rating = px.pie(city_rating, values='Rating', names='City',
                    title='Avaliação')
col5.plotly_chart(fig_rating, use_container_width=True)

# Avaliação Média por dia | Cidade

city_rating_mean = df_filtered.groupby(['Date', 'City'])[['Rating']].mean().reset_index()
city_rating_mean['Rating'] = city_rating_mean.groupby('City')['Rating'].rolling(window=1).mean().reset_index()['Rating']

# Plot the graph with the moving average
fig_city_rating = px.line(city_rating_mean, x='Date', y='Rating', color='City',
                          title='Média Móvel da Avaliação para as Cidades | (janela deslizante de tamanho 1)')
st.plotly_chart(fig_city_rating, use_container_width=True)

st.divider()
st.header('Análise por Sexo')

col6, col7 = st.columns(2)

# Faturamento por Tipo de Produto | Sexo

fig_prod_gender = px.bar(df_filtered, x='Total', y='Product line',
                         color='Gender', title='Faturamento por Tipo de Produto',
                         orientation='h')
col6.plotly_chart(fig_prod_gender, use_container_width=True)

# Cidade | Sexo

city_total = df_filtered.groupby(['City', 'Gender'])[['Total']].sum().reset_index()
fig_city_gender = px.bar(city_total, x='City', y='Total',
                         color='Gender',
                         title='Faturamento por Dia')
col7.plotly_chart(fig_city_gender, use_container_width=True)
