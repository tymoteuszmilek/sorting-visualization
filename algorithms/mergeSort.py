from plotUtils import plotArray
def mergeSortVisualization(arr, arr_chart):
    steps = []

    def _mergeSort(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            _mergeSort(arr, left, mid)
            _mergeSort(arr, mid + 1, right)

            steps = [{
                'array': arr.copy(),
                'insert': [left, right],
            }]
            for step in steps:
                plotArray(arr_chart, step)

            merge(arr, left, mid, right)

            # Clear Chart From Any Additional Colors When The Algorithm Is Done
            steps = [{
                'array': arr.copy(),
            }]
            for step in steps:
                plotArray(arr_chart, step)

    def merge(arr, left, mid, right):
        temp = []
        i = left
        j = mid + 1

        # Merge Two Halves Into temp array In Sorted Order
        while i <= mid and j <= right:

            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1

                steps = [{
                    'array': arr.copy(),
                    'highlight': [i - 1],
                    'insert': [left, right],
                }]
                for step in steps:
                    plotArray(arr_chart, step)

            else:
                temp.append(arr[j])
                j += 1

                steps = [{
                    'array': arr.copy(),
                    'highlight': [j - 1],
                    'insert': [left, right],
                }]
                for step in steps:
                    plotArray(arr_chart, step)

        # Append Remaining Elements From Left Half
        while i <= mid:
            temp.append(arr[i])
            i += 1

            steps = [{
                'array': arr.copy(),
                'highlight': [i - 1],
                'insert': [left, right],
            }]
            for step in steps:
                plotArray(arr_chart, step)

        # Append Remaining Elements From Right Half
        while j <= right:
            temp.append(arr[j])
            j += 1

            steps = [{
                'array': arr.copy(),
                'highlight': [j - 1],
                'insert': [left, right],
            }]
            for step in steps:
                plotArray(arr_chart, step)

        # Copy Sorted Elements From Temp Back To Original Array
        for k in range(len(temp)):
            arr[left + k] = temp[k]

            steps = [{
                'array': arr.copy(),
                'highlight': [left + k],
                'insert': [left, right],
            }]
            for step in steps:
                plotArray(arr_chart, step)

    _mergeSort(arr, 0, len(arr) - 1)