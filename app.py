from flask import Flask, render_template, request, send_file, send_from_directory
import tempfile
import os
from huffman import HuffmanCoding  # Assuming you have the HuffmanCoding class to handle compression

app = Flask(__name__)

# Set the folder where files will be uploaded
UPLOAD_FOLDER = r"C:\Users\User\Desktop\3rd Year\DSA\Text-File-Compressor-In-Python-main\Text-File-Compressor-In-Python-main\uploads"

# Initialize the HuffmanCoding object
huffman_coding = HuffmanCoding()

# Fixed path to the test file (for testing)
TEST_FILE_PATH = r"C:\Users\User\Desktop\3rd Year\DSA\Text-File-Compressor-In-Python-main\Text-File-Compressor-In-Python-main\Test.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save uploaded file temporarily
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            file.save(temp_file.name)

            # Compress the uploaded file
            compressed_file_path = huffman_coding.compress(temp_file.name)  # Compress the file

            # Extract the directory and file name from the compressed file path
            compressed_file_dir = os.path.dirname(compressed_file_path)
            compressed_file_name = os.path.basename(compressed_file_path)

            # Return the compressed file for download
            return send_from_directory(
                directory=compressed_file_dir,  # Directory where the compressed file is located
                path=compressed_file_name,      # Actual file name (this is where 'path' goes)
                as_attachment=True             # Force download as an attachment
            )

    return '''
    <form method="post" enctype="multipart/form-data">
        Upload a file: <input type="file" name="file">
        <input type="submit">
    </form>
    '''

@app.route('/decompress', methods=['POST'])
def decompress_file_route():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        # Save the uploaded file to the 'uploads' folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Decompress the file using Huffman Coding and get the decompressed file path
        decompressed_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'decompressed_' + file.filename)
        decompressed_text = huffman_coding.decompress(file_path)  # Decompress directly
        
        # Save the decompressed text as a file for downloading
        with open(decompressed_file_path, 'w') as f:
            f.write(decompressed_text)

        # Return the decompressed text and a download link
        return render_template('decompress.html', decompressed_text=decompressed_text, decompressed_file=decompressed_file_path)
    
@app.route('/download_decompressed/<filename>')
def download_decompressed(filename):
    decompressed_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    return send_file(decompressed_file_path, as_attachment=True)

@app.route('/test_compress', methods=['POST'])
def test_compress():
    # Compress the fixed test file
    compressed_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compressed_test_file.bin')
    huffman_coding.compress(TEST_FILE_PATH, compressed_file_path)

    # Return the compressed file
    return send_file(compressed_file_path, as_attachment=True)

@app.route('/test_decompress', methods=['POST'])
def test_decompress():
    # Decompress the fixed test file
    compressed_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compressed_test_file.bin')
    decompressed_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'decompressed_test_file.txt')

    huffman_coding.decompress(compressed_file_path, decompressed_file_path)

    # Return the decompressed file
    return send_file(decompressed_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
