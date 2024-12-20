import qrcode
import cv2
import os
from fpdf import FPDF

# Function to generate a QR Code and save as PNG and PDF
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Save the QR Code as a PNG file
    png_path = f"/input/{filename}.png"
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(png_path)

    # Convert PNG to PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.image(png_path, x=50, y=50, w=100)  # Centered on A4
    pdf_path = f"/output/{filename}.pdf"
    pdf.output(pdf_path)


    print(f"QR Code saved as PNG (/input/{filename}.png) and PDF (/output/{filename}.pdf)")

# Function to decode a QR Code from an image
def decode_qr_code(image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return None
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()

    data, _, _ = detector.detectAndDecode(img)
    if data:
        print(f"Decoded Data: {data}")
        return data
    else:
        print("No QR Code found or unable to decode.")
        return None

# Main menu
def main():
    while True:
        print("\nQR Code Encoder/Decoder")
        print("1. Generate QR Code")
        print("2. Decode QR Code")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            data = input("Enter the data for the QR Code: ")
            filename = input("Enter the filename (without extension): ")
            generate_qr_code(data, filename)
        elif choice == "2":
            files = os.listdir("/input")
            if not files:
                print("No files found in the 'input/' directory.")
                continue
            print("Available files in 'input/':")
            for i, file in enumerate(files):
                print(f"{i + 1}. {file}")
            file_index = int(input("Select a file by number: ")) - 1
            image_path = f"/input/{files[file_index]}"
            decode_qr_code(image_path)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
