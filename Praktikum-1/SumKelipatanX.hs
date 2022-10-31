module SumKelipatanX where
sumKelipatanX :: Int -> Int -> Int -> Int

sumKelipatanX m n x
  | m == n = if mod n x == 0 then 1 else 0
  | mod n x == 0 = n + sumKelipatanX m (n-1) x
  | otherwise = sumKelipatanX m (n-1) x