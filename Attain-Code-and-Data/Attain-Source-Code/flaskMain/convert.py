import subprocess
import argparse

def convert_to_image(in_file, out_file):

    cmd = "convert -density 300 {} {}.jpg".format(in_file, out_file)
    return subprocess.call(cmd, shell=True)

def run_cpp(executable_path, file_path):
    proc = subprocess.Popen(['./' + executable_path, file_path])
    proc.wait()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PDF to Image')
    parser.add_argument('pdf_file', help='PDF filepath')
    args = parser.parse_args()
    convert_to_image(args.pdf_file, args.pdf_file)
    run_cpp('basic_ocr', args.pdf_file + '.tiff')
