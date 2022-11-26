def encrypt(text, shift, encrypt=True):

  
  # alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  alphabet = 'dUoKXRvma4wQjENuJnFLc7CBkV01H6ezqZtpbIOsgYW3r8l2DGA5T9xiPMfhSy'
  new_text = ''
  for c in text:
      index = alphabet.find(c)
      if index == -1:
          new_text += c
      else:
          new_index = index + shift if encrypt == True else index - shift
          new_index %= len(alphabet)
          new_text += alphabet[new_index:new_index+1]
  return new_text



def decrypt(text, shift, encrypt=True):
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  

  new_text = ''
  for c in text:
      index = alphabet.find(c)
      if index == -1:
          new_text += c
      else:
          new_index = index + - + shift if encrypt == True else index - shift
          new_index %= len(alphabet)
          new_text += alphabet[new_index:new_index+1]
  
  return new_text

# print(encrypt(text='Walnut', shift=69, encrypt=True))

# print('\nDecrypting...\n')

# list = []
# for i in range(62):
  
#   decryption = encrypt(text='Gu9kCY', shift=i, encrypt=True)
#   print(decryption)
#   list.append(decryption)

#   find = 'Walnut'
#   print(list.count(find))



