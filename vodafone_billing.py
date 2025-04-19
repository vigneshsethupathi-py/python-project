import os

def process_billing(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()

    del data[0]  # Skip header

    isd_duration = std_duration = 0
    std_count = isd_count = free_count = 0
    cust_id = ''

    for line in data:
        line = line.strip()
        parts = line.split('#')
        duration = int(parts[3])
        cust_id = parts[0]
        call_type = parts[-1]

        if call_type == "std":
            std_count += 1
            std_duration += duration
        elif call_type == "isd":
            isd_count += 1
            isd_duration += duration
        elif call_type == "free":
            free_count += 1

    std_minutes = round(std_duration / 60, 2)
    isd_minutes = round(isd_duration / 60, 2)

    std_bill = round(std_minutes * 2 * 1.1, 2)
    isd_bill = round(isd_minutes * 7.5 * 1.1, 2)
    total_bill = round(std_bill + isd_bill, 2)

    print(f"STD Calls: {std_count}, Duration: {std_minutes} mins, Bill: ₹{std_bill}")
    print(f"ISD Calls: {isd_count}, Duration: {isd_minutes} mins, Bill: ₹{isd_bill}")
    print(f"Free Calls: {free_count}")
    print(f"Total Bill for {cust_id}: ₹{total_bill}")

if __name__ == "__main__":
    file_path = os.path.join("input", "9986019198.txt")
    process_billing(file_path)
