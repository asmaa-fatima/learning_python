print("Welcome to Caesar Cipher!")

# def caesor(text, shift, direction):
#   end_text = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     if direction == 'encode':
#       new_position = (position + shift) % len(alphabet)
#     elif direction == 'decode':
#       new_position = (position - shift)
#     else:
#       print("Invalid direction")
#       return
#     new_letter = alphabet[new_position]
#     end_text += new_letter
#   print(f"Here is the {direction}d result: {end_text}")


def caesor(text, shift, direction):
  end_text = ""
  if direction == 'decode':
    shift *= -1

  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift) % len(alphabet)
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"Here is the {direction}d result: {end_text}")


# def encrpyt(text, shift):
#   cipher_text = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     new_position = (position + shift) % len(alphabet)
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter

#   print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#   original_text = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     new_position = (position - shift)
#     new_letter = alphabet[new_position]
#     original_text += new_letter

#   print(f"The decoded text is {original_text}")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
]
while True:
  direction = input(
      "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type you message: \n").lower()
  shift = int(input("Type the shift number: \n"))
  caesor(text, shift, direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    print("ENDED")
    break
# if direction == "encode":
#   encrpyt(text, shift)
# elif direction == "decode":
#   decrypt(text, shift)
# else:
#   print("Invalid input.")
