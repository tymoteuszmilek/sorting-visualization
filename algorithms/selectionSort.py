from plotUtils import plotArray
def selectionSortVisualization(arr, arr_chart):
    steps = []
    n = len(arr)

    for i in range(n-1):
        # Find Min Value In Range (i + 1, n) And Swap It With i Index Value
        minValueIndex = i
        for j in range(i+1, n):

            #Only Visuzalization Purposes
            if i == 0:
                steps = [{
                    'array': arr.copy(),
                    'highlight': [j, minValueIndex]
                }]
                for step in steps:
                    plotArray(arr_chart, step)
            else:
                steps = [{
                    'array': arr.copy(),
                    'insert': [i - 1],
                    'highlight': [j, minValueIndex],
                }]
                for step in steps:
                    plotArray(arr_chart, step)

            currValue = arr[j]
            if currValue < arr[minValueIndex]:
                minValueIndex = j

        # Swap Current Element With Min Element
        arr[i], arr[minValueIndex] = arr[minValueIndex], arr[i]

    # Clear Chart From Any Additional Colors When The Algorithm Is Done
    steps = [{
        'array': arr.copy(),
    }]
    for step in steps:
        plotArray(arr_chart, step)

    return steps