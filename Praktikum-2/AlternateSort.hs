-- Nama : Ahmad Nadil
-- NIM : 16521516
-- Judul : Alternate Sort

module AlternateSort where 

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

-- Fungsi untuk mencari nilai minimum dalam sebuah list
elementTerkecil :: [Int] -> Int
elementTerkecil li
    | null li = 0
    | length li == 1 = head li
    | length li == 2 = if head li > last li then last li else head li
    | otherwise = 
        if head li < head(tail li) then elementTerkecil ([head li] ++ (tail(tail li))) 
        else elementTerkecil (tail li)

-- Fungsi untuk mencari nilai maximum dalam sebuah list
elementTerbesar :: [Int] -> Int
elementTerbesar li
    | null li = 0
    | length li == 1 = head li
    | length li == 2 = if head li < last li then last li else head li
    | otherwise = 
        if head li > head(tail li) then elementTerbesar ([head li] ++ (tail(tail li))) 
        else elementTerbesar (tail li)

-- Fungsi Utama
alternateSort :: [Int] -> [Int]
alternateSort li 
    | null li = []
    | length li == 1 = li
    | otherwise = [elementTerkecil li,elementTerbesar li] ++ alternateSort(let l1 = remove (element (elementTerkecil li) li) li in remove (element (elementTerbesar l1)l1) l1)
