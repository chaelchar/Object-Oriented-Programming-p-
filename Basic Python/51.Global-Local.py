## Global dan Local scope

# Global
nama = "kael"

def fungsi():
    print(f"fungsi menampilkan -> {nama}")

fungsi()
    
for i in range(0,2):
    print(f"loop ke-{i} -> ",nama)
