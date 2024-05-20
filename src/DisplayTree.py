import shutil    # For getting the terminal width
class TreeVisualizer:
    
    @staticmethod
    def display(nodo):
        lines, *_ = TreeVisualizer.displayAux(nodo)
        width = shutil.get_terminal_size().columns  # Get the terminal width
        for line in lines:
            print(line.center(width))  # Center each line

    @staticmethod
    def displayAux(nodo):
        """
        Retorna una lista de strings, el ancho, la altura y la coordenada horizontal de la raíz.
        """
        if nodo.derecha is None and nodo.izquierda is None:
            line = f'{nodo.dato.apellido}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if nodo.derecha is None:
            leftLines, leftWidth, leftHeight, leftMiddle = TreeVisualizer.displayAux(nodo.izquierda)
            valorStr = f'{nodo.dato.apellido}'
            valorWidth = len(valorStr)
            firstLine = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + valorStr
            secondLine = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + valorWidth) * ' '
            shiftedLines = [line + valorWidth * ' ' for line in leftLines]
            return [firstLine, secondLine] + shiftedLines, leftWidth + valorWidth, leftHeight + 2, leftWidth + valorWidth // 2

        if nodo.izquierda is None:
            rightLines, rightWidth, rightHeight, rightMiddle = TreeVisualizer.displayAux(nodo.derecha)
            valorStr = f'{nodo.dato.apellido}'
            valorWidth = len(valorStr)
            firstLine = valorStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondLine = (valorWidth + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            shiftedLines = [valorWidth * ' ' + line for line in rightLines]
            return [firstLine, secondLine] + shiftedLines, rightWidth + valorWidth, rightHeight + 2, valorWidth // 2

        leftLines, leftWidth, leftHeight, leftMiddle = TreeVisualizer.displayAux(nodo.izquierda)
        rightLines, rightWidth, rightHeight, rightMiddle = TreeVisualizer.displayAux(nodo.derecha)
        valorStr = f'{nodo.dato.apellido}'
        valorWidth = len(valorStr)
        firstLine = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + valorStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
        secondLine = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + valorWidth + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
        if leftHeight < rightHeight:
            leftLines += [leftWidth * ' '] * (rightHeight - leftHeight)
        elif rightHeight < leftHeight:
            rightLines += [rightWidth * ' '] * (leftHeight - rightHeight)
        zipped_lines = zip(leftLines, rightLines)
        lines = [firstLine, secondLine] + [a + valorWidth * ' ' + b for a, b in zipped_lines]
        return lines, leftWidth + rightWidth + valorWidth, max(leftHeight, rightHeight) + 2, leftWidth + valorWidth // 2
    