from plotUtils import plotArray

def bubbleSortVisualization(arr, arr_chart):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            steps = []
            steps.append({
                'array': arr.copy(),
                'highlight': [i, i + 1],
            })

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

                steps.append({
                    'array': arr.copy(),
                    'highlight': [i, i + 1],
                })

            for step in steps:
                plotArray(arr_chart, step)

        n -= 1

    # Clear Chart From Any Additional Colors When The Algorithm Is Done
    steps = []
    steps.append({
        'array': arr.copy(),
    })
    for step in steps:
        plotArray(arr_chart, step)
