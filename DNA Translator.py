class DNATranslator:
# Deklarasi kelas Translator DNA
    def __init__(self, urutan_dna):
    # Konstruktor dari kelas dengan parameter urutan_dna
        self.urutan_dna = urutan_dna.upper()
        # Inisialisasi atribut urutan dna, memakai method upper() agar nilainya dikonversi ke huruf kapital
    def transkrip(self):
    # Deklarasi method untuk proses transkripsi dari DNA ke RNA
        urutan_rna = self.urutan_dna.replace('T', 'U')
        # Dilakukan penggantian karakter T ke U pada urutan DNA (cont. TGA menjadi UGA) menggunakan method replace()
        # Hasil penggantian disimpan di variabel urutan_rna
        return urutan_rna
        # mengembalikan nilai urutan rna yang telah dihasilkan

    def translasi(self):
    # Deklarasi method untuk proses translasi dari RNA menjadi asam amino
        tabel_kodon = {
            'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
            'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
            'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UAA': 'Stop', 'UAG': 'Stop',
            'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGA': 'Stop', 'UGG': 'Tryptophan',
            'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine',
            'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
            'CAU': 'Histidine', 'CAC': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine',
            'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine',
            'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine', 'AUG': 'Methionine',
            'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
            'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine',
            'AGU': 'Serine', 'AGC': 'Serine', 'AGA': 'Arginine', 'AGG': 'Arginine',
            'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
            'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine',
            'GAU': 'Aspartic Acid', 'GAC': 'Aspartic Acid', 'GAA': 'Glutamic Acid', 'GAG': 'Glutamic Acid',
            'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine'
        }
        # Merupakan pasanagan dari RNA ke asam amino sesuai dengan aturan dari tabel kodon

        urutan_rna = self.transkrip()
        # Memanggil method transkrip() untuk mendapatkan urutan RNA
        protein = ''
        # Sebuah String kosong untuk menampung urutan asam amino yang dihasilkan

        for i in range(0, len(urutan_rna), 3):
        # Perulangan for untuk melakukan iterasi urutan RNA dengan 3 lompatan
            kodon = urutan_rna[i:i+3]
            # Memotong urutan RNA menjadi 3 huruf sesuai dengan tabel kodon
            if kodon in tabel_kodon:
            # memeriksa apakah kodon ada di dalam tabel_kodon
                asam_amino = tabel_kodon[kodon]
                # mengambil nilai asam amino sesuai dengan kodon pada tabel_kodon, disimpan di variabel asam_amino
                if asam_amino == 'Stop':
                # pada kodon terdapat kodon stop, yaitu bila sampai ke kodon stop maka konversi berhenti
                    protein += " Stop"
                    # jika ditemukan kodon stop maka akan ditambahkan 'Stop' pada output asam amino
                    break
                    # menggunakan break untuk keluar dari perulangan for
                protein += asam_amino+ " "
                # menambahkan asam amino yang didapat ke dalam protein dan ditambahkan satu spasi dujung
            else:
            # jika kondisi if tidak dipenuhi maka else akan dijalankan
                protein += "Unknown"
                # jika kodon tidak ada dalam tabel kodon maka akan mengeluarkan "Unknown"

        return protein.strip()
        # Mengembalikan urutan asam amino yang dihasilkan

urutan_dna = input("Masukkan Urutan DNA: ")
# membuat input pengguna untuk memasukkan urutan DNA (Cont. ATGGTTACTCTAGTA)
translator = DNATranslator(urutan_dna)
# membuat objek translator dari kelas DNATranslator
urutan_rna = translator.transkrip()
# menggunakan objek translator untuk memanggil method transkrip() untuk proses transkripsi
# hasilnya disimpan di urutan_dna
protein = translator.translasi()
# menggunakan objek translator untuk memanggil method translasi() untuk proses translasi
# hasilnya disimpan di protein

print("Urutan RNA: " + urutan_rna)
# mencetak urutan rna 
print("Urutan Asam Amino: " + protein)
# mencetak urutann asam amino

print("==========Group 11==========")
print("======PBO INFORMATIKA B=====")
