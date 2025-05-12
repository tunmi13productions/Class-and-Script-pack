import password_functs as p
pwlength = 16
print("First password, alphanumeric: "+str(p.generate_alphanumeric_password(pwlength)))
print("Second password, alphanumeric plus: "+str(p.generate_alphanumeric_password_plus(pwlength)))
print("Third password, numeric: "+str(p.generate_numeric_password(pwlength)))
print("Fourth password, alphabetic: "+str(p.generate_alphabetic_password(pwlength)))
