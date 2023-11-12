-- Binary Tree (search for demonstration purposes)
module BinaryTree where

data Tree a = Node (Tree a) a (Tree a) | Leaf deriving (Show)

empty :: Tree a
empty = Leaf

addNode :: (Ord a) => a -> (Tree a) -> (Tree a)
addNode a (Leaf) = (Node Leaf a Leaf)
addNode a (Node lhs b rhs)
  | a <= b = Node (addNode a lhs) b rhs
  | a > b = Node lhs b (addNode a rhs)
addNode _ _ = error "Impossible case"

inorder :: (Tree a) -> [a]
inorder (Leaf) = []
inorder (Node lhs b rhs) = inorder lhs ++ b : inorder rhs

exists :: (Ord a) => (Tree a) -> a -> Bool
exists (Leaf) _ = False
exists (Node lhs b rhs) a
  | a == b = True
  | a < b = exists lhs a
  | a >= b = exists rhs a
exists _ _ = error "Impossible case"

{--
  Try:
  addNode 9 $ empty
  (flip exists) 1 $ addNode 4 $ addNode 10 $ addNode 3 $ addNode 1 $ addNode 9 $ empty
  inorder $ addNode 4 $ addNode 10 $ addNode 3 $ addNode 1 $ addNode 9 $ empty
-}
