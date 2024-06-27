from plotUtils import plotArray
def quickSortVisualization(arr, arr_chart):

    def _quickSort(arr, left, right):
        if left < right:
            partitionPos = partition(arr, left, right)
            _quickSort(arr, left, partitionPos - 1)
            _quickSort(arr, partitionPos + 1, right)

            # Clear Chart From Any Additional Colors When The Algorithm Is Done
            steps = [{
                'array': arr.copy(),
            }]
            for step in steps:
                plotArray(arr_chart, step)

    def partition(arr, left, right):
        i = left
        j = right - 1
        pivot = arr[right] # Take Last Element Of Arr As 'Pivot'

        steps = [{
            'array': arr.copy(),
            'insert': [right],
        }]
        for step in steps:
            plotArray(arr_chart, step)


        # Swap Elements [i, j] if arr[i] > pivot and arr[j] < pivot and i < j
        while i <= j:
            while i <= j and arr[i] < pivot:
                i += 1

            while i <= j and arr[j] > pivot:
                j -= 1

            if i < j:

                arr[i], arr[j] = arr[j], arr[i]

                steps = [{
                    'array': arr.copy(),
                    'insert': [right],
                    'highlight': [i, j]
                }]
                for step in steps:
                    plotArray(arr_chart, step)

                i += 1
                j -= 1

        # Place the pivot element in its correct position
        if arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]

        return i

    _quickSort(arr, 0, len(arr) - 1)