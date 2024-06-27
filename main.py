import streamlit as st
import numpy as np

from algorithms import bubbleSort, insertionSort, mergeSort, quickSort, selectionSort
from plotUtils import initPlotArray as initPlotArray

sortingAlgorithms = {
    "Bubble Sort": bubbleSort.bubbleSortVisualization,
    "Selection Sort": selectionSort.selectionSortVisualization,
    "Insertion Sort": insertionSort.insertionSortVisualization,
    "Merge Sort": mergeSort.mergeSortVisualization,
    "Quick Sort": quickSort.quickSortVisualization,
}
def main():
    minLen = 2
    maxLen = 50
    defaultLen = 30
    maxValue = 100

    st.title('Sorting Algorithm Visualization')
    algorithm = st.selectbox('Choose Sorting Algorithm', list(sortingAlgorithms.keys()))
    arraySize = st.slider('Array Size', min_value=minLen, max_value=maxLen, value=defaultLen, step=1)
    array = np.random.randint(1, maxValue + 1, arraySize)
    arr_chart = st.empty()

    initPlotArray(arr_chart, array)

    if st.button('Sort'):
        sorted_array = array.copy()
        sortingAlgorithms[algorithm](sorted_array, arr_chart)

if __name__ == '__main__':
    main()
