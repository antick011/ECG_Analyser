from fpdf import FPDF

def generate_report(metrics, image_path, out_path="output/ecg_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="ECG Signal Report", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Average BPM: {metrics['avg_bpm']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Min R-R: {metrics['min_rr']:.2f}s", ln=True)
    pdf.cell(200, 10, txt=f"Max R-R: {metrics['max_rr']:.2f}s", ln=True)
    pdf.cell(200, 10, txt=f"RR Std Dev: {metrics['rr_std']:.2f}s", ln=True)

    pdf.ln(10)
    pdf.image(image_path, x=10, y=pdf.get_y(), w=180)
    pdf.output(out_path)
