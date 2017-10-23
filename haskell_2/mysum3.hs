mysum :: Int -> [Int] -> Int
mysum acc []     = acc
mysum acc (x:xs) = n `seq` mysum n xs where n = acc + x

main = print $ mysum 0 $ take 1000000 [1..]
