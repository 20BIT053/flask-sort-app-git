from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sorting function (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Route to serve the webpage
@app.route('/')
def home():
    return render_template("index.html")  # Serves the HTML form

# API Route for sorting numbers
@app.route('/sort', methods=['POST'])
def sort_numbers():
    data = request.get_json()
    numbers = data.get("numbers", [])
    sorted_numbers = merge_sort(numbers)
    return jsonify({"sorted_numbers": sorted_numbers})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
