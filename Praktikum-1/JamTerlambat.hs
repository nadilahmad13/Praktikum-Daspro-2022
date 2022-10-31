module JamTerlambat where
detik :: Int -> Int -> Int -> Int 
jamTerlambat :: Int -> Int -> Int -> (Int,Int,Int,Bool,Int)

detik j m d = (j*3600) + (m*60) + d
jamTerlambat j m d =
    let start = (detik 8 30 0)
        entrance = (detik j m d)
        diff = 
            if start < entrance then entrance - start 
            else start - entrance
    in (diff `div` 3600, (diff`mod`3600) `div` 60, (diff `mod` 3600)`mod`60, start < entrance, if start < entrance then diff*10 else 0)