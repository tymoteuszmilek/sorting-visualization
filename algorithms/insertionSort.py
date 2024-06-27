from plotUtils import plotArray
def insertionSortVisualization(arr, arr_chart):
    n = len(arr)

    for i in range(1, n):
        currentValue = arr[i]
        j = i - 1

        # Initial Visualization Before Sorting Step
        steps = [{
            'array': arr.copy(),
            'highlight': [i, j],
        }]
        for step in steps:
            plotArray(arr_chart, step)

        # Search The Correct Index To Insert currentValue
        while j >= 0 and currentValue < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

            # Only Visualization Purposes
            if j >= 0:
                temp = arr[j + 1]
                arr[j + 1] = currentValue
                steps = [{
                    'array': arr.copy(),
                    'highlight': [j + 1, j],
                    'insert': [i],
                }]
                for step in steps:
                    plotArray(arr_chart, step)
                arr[j + 1] = temp

        arr[j + 1] = currentValue

        steps = [{
            'array': arr.copy(),
            'highlight': [j + 1, j + 2],
            'insert': [i],
        }]
        for step in steps:
            plotArray(arr_chart, step)

    # Clear Chart From Any Additional Colors When The Algorithm Is Done
    steps = [{
        'array': arr.copy(),
    }]
    for step in steps:
        plotArray(arr_chart, step)

    return steps


