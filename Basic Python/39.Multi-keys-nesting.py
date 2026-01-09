# Multi keys & nesting dictionary


mahasiswa_3 = {
    'nama': 'gama',
    'nim': '13S24026',
    'sks': 120,
    'umur': 17,
    'tahun lahir': 2007
}

mahasiswa_2 ={
    'nama': 'lambok',
    'nim': '13S24022',
    'sks': 120,
    'umur': 19,
    'tahun lahir': 2005
}

mahasiswa_1 = {
    'nama': 'michael',
    'nim': '13S24037',
    'sks': 120,
    'umur': 18,
    'tahun lahir': 2006
}

data_mahasiswa = {
    'mhs_1': mahasiswa_1,
    'mhs_2': mahasiswa_2,
    'mhs_3': mahasiswa_3
}

print(f"{'KEY':<6}  {'NAMA':<10}  {'NIM':<10}  {'SKS':<5}  {'UMUR':<5}  {'TAHUN LAHIR':<12}")
print("-"*60)

for mahasiswa in data_mahasiswa:
    KEY  = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM  = data_mahasiswa[KEY]['nim']
    SKS  = data_mahasiswa[KEY]['sks']
    UMUR = data_mahasiswa[KEY]['umur']
    TAHUN_LAHIR = data_mahasiswa[KEY]['tahun lahir']
    print(f"{KEY:<6}  {NAMA:<10}  {NIM:<10}  {SKS:<5}  {UMUR:<5}  {TAHUN_LAHIR:<12}")