let matematika = 85;
let bahasaInggris = 90;
let ipa = 78;

let nilairatarata = (matematika+bahasaInggris+ipa)/3;

console.log (`nilai ratarata dari ketiga pelajaran Mahasiswa adalah: ${nilairatarata}`);
console.log (`Tipe data dari nilai rata rata nya adalah: ${typeof nilairatarata}`);

let statuskelulusan;
if (nilairatarata >= 80) {
    statuskelulusan = "Kamu Lulus Ya Sayang Cantik Dan Ganteng";
} else {
    statuskelulusan = "Yahhh Gak Lulus";
}

console.log (`Status Kelulusan Siswa: ${statuskelulusan}`);