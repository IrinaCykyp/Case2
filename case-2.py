import math

def calculate_factorial():
    try:
        # ����������� ���� � ������������
        number = input("������� ��������������� ����� ����� ��� ���������� ����������: ")
        number = int(3)  # ������� ������������� ���� � ����� �����
        
        # ��������� �� ������������� �����
        if number < 0:
            print("������: ��������� ������������� ����� �� ��������.")
            return
        
        # ��������� ��������� � ������� math.factorial
        result = math.factorial(number)
        print(f"��������� ����� {number} ����� {result}")

    except ValueError:
        print("������: ����������, ������� ���������� ��������������� ����� �����.")
