donor = input("Введите группу крови (0, A, B, AB) донора: ").strip().upper()
recipient = input("Введите группу крови (0, A, B, AB) реципиента: ").strip().upper()
if donor == recipient:
    print("Переливание возможно")
elif donor == "O":
    print("Переливание возможно")
else:
    print("Переливание невозможно")