import json

print('''
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗         ██╗███████╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║         ██║██╔════╝██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║         ██║███████╗██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██   ██║╚════██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ╚█████╔╝███████║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                        
''')



mahasiswa = []
setiyawan = {"nama": "setiyawan", "alamat": "tegal"}
yayang = {"nama": "yayang", "alamat": "Tegal"}
duar = {"nama": "slamokom", "alamat": "mamang"}

mahasiswa.append(setiyawan)
mahasiswa.append(yayang)
mahasiswa.append(duar)

json_str = json.dumps(mahasiswa)
print(json_str)