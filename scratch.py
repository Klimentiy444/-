contacts=[['Анна','+79161234567'],['Алексей','+79264443322']]
komanda=(input())
count=0
if komanda == 'поиск':
    poisk = input("Найти:").strip()
    for name,phone in contacts:
        if poisk in name or poisk in phone:
            print(name,'-',f'{phone[:4]}***{phone[-2:]}')

if komanda == 'список':
    for name,phone in contacts:
        count+=1
        print(f'{count}.',name,'-',f'{phone[:4]}***{phone[-2:]}')















