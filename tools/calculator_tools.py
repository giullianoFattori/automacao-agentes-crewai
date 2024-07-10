from langchain.tools import tool


class CalculatorTools:

    @tool("Make a calculation")
    def calculate(operation):
        """Útil para realizar qualquer cálculo matemático,
        como soma, subtração, multiplicação, divisão etc.
        A entrada para essa ferramenta deve ser uma expressão matemática,
        alguns exemplos são '200*7' ou '500/2*10'
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"