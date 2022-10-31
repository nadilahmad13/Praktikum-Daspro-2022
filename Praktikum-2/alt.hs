-- Nama   : Ahmad Nadil
-- NIM    : 16521516
-- Judul  : Alternate Sort

module AlternateSort where 
-- Fungsi Untuk Mengurutkan Nilai Dari Terkecil ke Terbesar
sorting :: [Int] -> [Int]
sorting li 
    | null li = []
    | otherwise = [minimum li] ++ sorting (remove (element (minimum li) li) li)


-- Fungsi Mencari Elemen Ke Berapa bilangan 'n' dalam sebuah list
element :: Int -> [Int] -> Int
element n li
    | null li = 0
    | otherwise = if head li == n then 1 else 1 + element n (tail li)

-- Fungsi untuk menghapus elemen ke n dalam sebuah list
remove :: Int -> [Int] -> [Int]
remove x li
    | null li = []
    | x == 1 = tail li
    | otherwise = [head li] ++ remove (x-1) (tail li)

-- Fungsi Utama
alternateSort :: [Int] -> [Int]
alternateSort li
    | null li = []
    | otherwise =  
        let list = sorting li
        in head list : last list : alternateSort (remove 1 (init list))
