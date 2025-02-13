import sys

def extract_logs(log_file, target_date, output_file):
    with open(log_file, 'r') as file, open(output_file, 'w') as output:
        for line in file:
            if line.startswith(target_date):
                output.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    target_date = sys.argv[1]
    log_file = "large_log.txt"  
    output_file = f"output/output_{target_date}.txt"

    extract_logs(log_file, target_date, output_file)
    print(f"Logs for {target_date} saved to {output_file}")


