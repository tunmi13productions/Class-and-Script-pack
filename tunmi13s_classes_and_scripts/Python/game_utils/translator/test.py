import translator
t = translator.translator("Spanish","languages/Spanish.txt")
print(f"{t.translate('This is a test!')} {t.translate('This took about')} 30 {t.translate('minutes')} {t.translate('to make!')}")