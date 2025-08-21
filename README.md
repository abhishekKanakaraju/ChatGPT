# ChatGPT

## Slide Reconstruction Script

`slide_reconstructor.py` converts a static image of a PowerPoint slide into an
editable `.pptx` file. It uses Tesseract OCR to extract text and OpenCV to
detect basic shapes.

### Usage

```bash
python slide_reconstructor.py path/to/slide.png output.pptx
```

Ensure that Tesseract, OpenCV, and python-pptx are installed in your
environment. The script is a starting point and may require manual adjustments
for complex slides.
