module DeretAritmatika where
deretAritmatika :: Int -> Int -> Int -> Float
deretAritmatika n a b = fromIntegral n*(2*fromIntegral a + (fromIntegral n-1)*fromIntegral b)/2