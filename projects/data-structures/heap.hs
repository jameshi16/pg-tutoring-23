-- Heap.hs - i regret my life choices. This is a min heap, and probably the
-- slowest possible heap because of !!. A better way to implement this would
-- be to run list comprehension and doing some really smart magic.

-- Too bad :clueless:

module Heap where

-- In theory, heaps are supposed to start at 1. I'm lazy so we do
-- some calculations

parentInd :: Int -> Int
parentInd x = max 0 (div (x + 1) 2) - 1

leftChildInd :: Int -> Int
leftChildInd x = (x + 1) * 2 - 1

rightChildInd :: Int -> Int
rightChildInd x = (x + 1) * 2

-- There is a faster way to swap, I know.
swap :: [a] -> Int -> Int -> [a]
swap [] _ _ = error "bruh"
swap xs a b = [element ind x | (ind, x) <- zip [0..] xs]
              where element ind val
                      | ind == a = xs !! b
                      | ind == b = xs !! a
                      | otherwise = val

sink :: (Ord a) => [a] -> Int -> [a]
sink xs ind
  | ind >= div (length xs) 2 = xs
  | xs !! ind > xs !! smallerChild =
    (flip sink) smallerChild $ swap xs smallerChild ind
  | otherwise = xs
  where leftChild = leftChildInd ind
        rightChild = rightChildInd ind
        smallerChild
          | rightChild >= length xs = leftChild
          | xs !! leftChild > xs !! rightChild = rightChild
          | otherwise = leftChild

swim :: (Ord a) => [a] -> Int -> [a]
swim xs ind
  | ind <= 0 = xs
  | ele < parentEle = swap xs parentIdx ind
  | otherwise = xs
  where parentIdx = parentInd ind
        parentEle = xs !! parentIdx
        ele = xs !! ind

pop :: (Ord a) => [a] -> ([a], a)
pop xs = (sink (init $ swap xs 0 $ length xs - 1) 0, head xs)

heapify :: (Ord a) => [a] -> [a]
heapify xs = helper (parentInd $ length xs - 1) xs
  where helper i ys
          | i < 0 = error (show i)
          | i <= 0 = sink ys 0
          | otherwise = helper (i - 1) $ sink ys i
