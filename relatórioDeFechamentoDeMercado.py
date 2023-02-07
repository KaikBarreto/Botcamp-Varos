import pandas as pd
import datetime 
import yfinance as yf
from matplotlib import pyplot as plt
# import mplcyberpunk
import win32com.client as win32
from time import sleep

codigos_de_negociacao = ["^BVSP", "BRL=X"]

hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days = 365)

dados_mercado = yf.download(codigos_de_negociacao, um_ano_atras, hoje)

dados_fechamento = dados_mercado['Adj Close']
dados_fechamento.columns = ["Dólar", "Ibovespa"]

dados_fechamento = dados_fechamento.dropna()

dados_anuais = dados_fechamento.resample("Y").last()
dados_mensais = dados_fechamento.resample("M").last()

retorno_anual = dados_anuais.pct_change().dropna()
retorno_mensal = dados_mensais.pct_change().dropna()
retorno_diario = dados_fechamento.pct_change().dropna()


retorno_diario_dolar = round(retorno_diario.iloc[-1, 0] * 100, 2)
retorno_diario_ibov = round(retorno_diario.iloc[-1, 1] * 100, 2)

retorno_mensal_dolar = round(retorno_mensal.iloc[-1, 0] * 100, 2)
retorno_mensal_ibov = round(retorno_mensal.iloc[-1, 1] * 100, 2)

retorno_anual_dolar = round(retorno_anual.iloc[-1, 0] * 100, 2)
retorno_anual_ibov = round(retorno_anual.iloc[-1, 1] * 100, 2)

plt.style.use("cyberpunk")
dados_fechamento.plot(y="Ibovespa", use_index = True, legend = False)
plt.show()
sleep(100)