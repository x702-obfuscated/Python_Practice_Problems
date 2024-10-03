tests = [
    (["apple", "banana", "cherry"], ["apple", "banana", "cherry"]),  # 
    ( ["cat", "dog", "elephant"],["dog", "cat", "elephant"]),        
    ([], []),                                                         
    (["antelope", "lion", "zebra"],["zebra", "lion", "antelope"]), 
    (["apple", "banana", "kiwi", "pear"],["pear", "banana", "apple", "kiwi"]), 
    ( ["apple", "banana"],["apple", 42, "banana"]),                 
    (["hello", "world"],["hello", None, "world"]),                 
    (["123", "213", "321"],["123", "321", "213"]),                 
    (["B", "a", "c"],["a", "B", "c"]),                             
    (["APPLE", "apple", "banana"],["apple", "banana", "APPLE"]),   
    ( [],[1, 2, 3]),                                                
    (["", "apple", "banana"], ["", "apple", "banana"]),            
    (["  ", "spaces", "spaces "],["spaces ", "spaces", "  "]),    
    (["#hash", "apple", "banana"], ["#hash", "apple", "banana"]),  
    (["cat", "cat", "dog", "dog"],["dog", "dog", "cat", "cat"]),  
    (["A", "B", "a", "b"],["B", "b", "A", "a"]),                  
    (["Python", "WORLD", "hello"],["hello", "WORLD", "Python"]),  
    (["longword", "medium", "short"],["longword", "short", "medium"]), 
    (["-1", "0", "1"], ["-1", "0", "1"]),                           
    (["0", "1", "A", "a"],["a", "1", "A", "0"]),                  
    (["test"],[None, "test", 123.45]),                            
]