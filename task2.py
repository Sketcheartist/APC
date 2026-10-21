
from flask import Flask, request, render_template_string
import fitz  # PyMuPDF
import io

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB limit

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>PDF Reader</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            margin: 0;
            padding: 30px 15px;
        }
        .container {
            max-width: 850px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 15px #ccd2da;
        }
        h1 {
            text-align: center;
            color: #174a7e;
        }
        .upload-box {
            background: #f4f8fc;
            border: 2px dashed #528ac0;
            padding: 25px;
            text-align: center;
            border-radius: 10px;
        }
        input[type=file] {
            display: block;
            margin: 20px auto;
            max-width: 100%;
        }
        button {
            background: #1769aa;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #104e82;
        }
        .result {
            margin-top: 25px;
        }
        .pdf-text {
            background: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 6px;
            padding: 18px;
            white-space: pre-wrap;
            overflow-wrap: anywhere;
            line-height: 1.6;
            max-height: 500px;
            overflow-y: auto;
        }
        .error {
            color: #b42318;
            background: #fff0ef;
            padding: 12px;
            border-radius: 5px;
        }
        .success {
            color: #167443;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>PDF Upload & Reader</h1>
    <p style="text-align:center">
        Upload a PDF document and extract its text instantly.
    </p>

    <form method="POST" enctype="multipart/form-data">
        <div class="upload-box">
            <h3>Select your PDF file</h3>
            <input type="file" name="pdf_file"
                   accept=".pdf,application/pdf" required>
            <button type="submit">Upload & Read PDF</button>
        </div>
    </form>

    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

    {% if pdf_text is not none %}
        <div class="result">
            <h2 class="success">PDF Read Successfully!</h2>
            <p><b>File:</b> {{ filename }}</p>
            <p><b>Total pages:</b> {{ page_count }}</p>
            <p><b>Extracted characters:</b> {{ pdf_text|length }}</p>

            <h3>Extracted PDF Data</h3>
            <div class="pdf-text">{{ pdf_text }}</div>

            {% if pdf_text.strip() %}
            <button type="button" onclick="downloadText()">
                Download Extracted Text
            </button>
            {% else %}
            <p>This PDF contains no extractable text.
               It may be a scanned document requiring OCR.</p>
            {% endif %}
        </div>

        <script>
            function downloadText() {
                const text = {{ pdf_text|tojson }};
                const blob = new Blob([text], {
                    type: "text/plain;charset=utf-8"
                });
                const url = URL.createObjectURL(blob);
                const link = document.createElement("a");
                link.href = url;
                link.download = "extracted_text.txt";
                link.click();
                URL.revokeObjectURL(url);
            }
        </script>
    {% endif %}
</div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("pdf_file")

        if not file or not file.filename:
            return render_template_string(
                HTML, error="Please select a PDF file.",
                pdf_text=None
            )

        if not file.filename.lower().endswith(".pdf"):
            return render_template_string(
                HTML, error="Please upload a PDF file.",
                pdf_text=None
            )

        try:
            file_bytes = file.read()

            if not file_bytes.startswith(b"%PDF-"):
                raise ValueError("The uploaded file is not a valid PDF.")

            # Read the PDF directly from memory
            with fitz.open(
                stream=io.BytesIO(file_bytes), filetype="pdf"
            ) as pdf:
                page_count = len(pdf)

                if page_count == 0:
                    raise ValueError("The PDF has no pages.")

                if page_count > 500:
                    raise ValueError("PDF must have 500 pages or fewer.")

                extracted_text = "\n\n".join(
                    f"--- Page {i + 1} ---\n{page.get_text()}"
                    for i, page in enumerate(pdf)
                )

            return render_template_string(
                HTML,
                pdf_text=extracted_text,
                filename=file.filename,
                page_count=page_count,
                error=None
            )

        except Exception:
            return render_template_string(
                HTML,
                error=(
                    "Unable to read this PDF. Please check that "
                    "it is valid, not password-protected, and "
                    "within the supported size and page limits."
                ),
                pdf_text=None
            )

    return render_template_string(
        HTML, pdf_text=None, error=None
    )


@app.errorhandler(413)
def file_too_large(error):
    return render_template_string(
        HTML,
        error="File too large. Maximum upload size is 16 MB.",
        pdf_text=None
    ), 413


if __name__ == "__main__":
    app.run(debug=True)
