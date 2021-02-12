test_set_1 = set()
 
test_set_1.add('python')
test_set_1.update({'-', 'izm', '.', 'com'})
 
print(test_set_1)

test_set_1 = {'python', '-', 'izm', '.', 'com'}
 
test_set_1.remove('-')
test_set_1.discard('.')
 
print(test_set_1)