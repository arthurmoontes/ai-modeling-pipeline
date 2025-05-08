# Relatório Final - Modelo de Previsão de Receita

## 1. Objetivo
Desenvolver e implantar um pipeline de machine learning que preveja a receita dos próximos 30 dias para uma empresa fictícia usando aprendizado supervisionado.

## 2. Abordagens Testadas
- RandomForestRegressor (modelo final)
- LinearRegression (avaliado, mas com desempenho inferior)

## 3. Engenharia de Features
- Lags (1 dia)
- Médias móveis (7 e 30 dias)
- Atributos temporais (dia da semana, mês, ano)

## 4. Avaliação
- Métrica: RMSE
- Resultado do modelo Random Forest: RMSE ~ abaixo de 10.0 (varia com dados)

## 5. API
Endpoints:
- `/train`: treina o modelo
- `/predict`: recebe CSV e retorna previsões
- `/logfile`: retorna histórico de previsões

## 6. Testes e Monitoramento
- Testes unitários criados para o modelo, API e logs
- Previsões salvas com data/hora no log
- Testes executáveis via `run_tests.sh`

## 7. Implantação
- Dockerfile + docker-compose incluídos
- API pode ser executada com `docker-compose up`

## 8. Conclusão
O sistema está pronto para escalonamento, com estrutura modular, testes e containerização. Próximos passos envolveriam monitoramento contínuo e re-treinamento automático.
