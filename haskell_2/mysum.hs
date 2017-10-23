mysum :: [Int] -> Int
mysum []     = 0
mysum (x:xs) = x + mysum xs

main = print $ mysum $ take 1000000 [1..]
