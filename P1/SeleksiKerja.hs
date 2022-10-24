module SeleksiKerja where
seleksi :: Int -> Int -> Char -> Bool
seleksi m s p
  | m >= 2 && s >= 4 = True
  | m < 2 && s >= 4 && p == 'B' = True
  | m < 2 && s < 4 && p == 'C' = True
  | s < 4 && m >= 2 && p == 'D' = True
  | p == 'C' = True 
  | otherwise = False