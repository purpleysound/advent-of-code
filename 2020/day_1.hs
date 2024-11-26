
twoSum :: Int -> [Int] -> Int
twoSum target numbers = product (filter complementInList numbers)
    where complementInList x = (target-x) `elem` numbers

part1 :: [Int] -> Int
part1 = twoSum 2020


threeSum :: Int -> [Int] -> Int
threeSum target numbers = product (filter complementsInList numbers)
    where complementsInList x = twoSum (target-x) numbers /= 1

part2 :: [Int] -> Int
part2 = threeSum 2020


main :: IO()
main = do
    input <- readFile "inputs/day_1.txt"
    let numbers = map read (lines input)
    print $ part1 numbers
    print $ part2 numbers
