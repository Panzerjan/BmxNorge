from bmx.comi import CommissionerManager

manager = CommissionerManager('./files/comi.json')

list = manager.list_commissioner()

print(list)