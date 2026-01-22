from virtual_clipboard import virtual_clipboard

vclip = virtual_clipboard()
print("Start copying.")
vclip.text = "hi there."
print(vclip.text)
vclip.text = "I am a clipboard."
print(vclip.text)
vclip.text = "Read me!"
print(vclip.text)
print(vclip.copied_items)
