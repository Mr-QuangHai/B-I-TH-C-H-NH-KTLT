print("Nguyen Van An")
print("Msv:235752021610082")
def file_statistics(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        num_chars = len(content)
        num_words = len(content.split())
        num_lines = len(content.splitlines())
        
    print(f"Số ký tự: {num_chars}")
    print(f"Số từ: {num_words}")
    print(f"Số dòng: {num_lines}")

# Ví dụ sử dụng
file_statistics('file.txt')  # Thay 'file.txt' bằng tên file của bạn
