#!/bin/bash

# Roda os testes automatizados
echo "Executando testes..."
python -m unittest discover -s tests -p "test_*.py"
