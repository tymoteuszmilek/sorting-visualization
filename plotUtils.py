import matplotlib.pyplot as plt

def initPlotArray(arr_chart, arr):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color='#0000FF')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Array Visualization')
    arr_chart.pyplot(plt)
    plt.close()

def plotArray(arr_chart, step):
    arr = step['array']

    barColors = ['#0000FF' for _ in range(len(arr))]  # Default color: Blue

    if step.get('insert'):
        for index in step['insert']:
            barColors[index] = '#00FF00'  # Green for insert

    if step.get('highlight'):
        for index in step['highlight']:
            barColors[index] = '#FF0000'  # Red for highlight

    if step.get('boundaries'):
        for index in step['boundaries']:
            barColors[index] = '#FFFF00'  # Yellow for boundaries


    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color=barColors)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Array Visualization')
    arr_chart.pyplot(plt)
    plt.close()
