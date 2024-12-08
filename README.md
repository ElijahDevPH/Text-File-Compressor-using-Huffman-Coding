# File Compressor and Decompressor using Huffman Coding

This project implements a file compression and decompression system using the Huffman Coding algorithm. The goal is to reduce file sizes by encoding the data with a prefix-free binary code, and to restore the original content through decompression.

## Features

- **File Compression**: Upload a file to compress using the Huffman Coding algorithm and download the compressed file.
- **File Decompression**: Upload a compressed file to decompress and view the original content. Optionally, download the decompressed file.
- **Interactive Web Interface**: Provides an easy-to-use interface built with Flask and styled with CSS.
- **Background Animation**: Adds a dynamic animated background using the Vanta.js library.

## Technologies Used

- **Python**: Core logic for Huffman compression and decompression.
- **Flask**: Lightweight framework for the web interface.
- **HTML/CSS**: Frontend design and layout.
- **Vanta.js**: Interactive background effects.
- **JavaScript**: Enhances the UI/UX.

## How It Works

1. **Compression**:
    - Upload a text file.
    - The file is compressed using the Huffman Coding algorithm.
    - The compressed file is available for download.

2. **Decompression**:
    - Upload a compressed `.bin` file.
    - The system decompresses the file and shows the original content in the browser.
    - Optionally, download the decompressed file.

## File Structure

