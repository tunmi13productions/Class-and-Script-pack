import simple_menu
import lucia
import sys
if not lucia.running: lucia.initialize()
def main():
	lucia.show_window("menu")
	s = simple_menu.simple_menu(clicksound = "menuclick.ogg", edgesound = "menuedge.ogg", entersound = "menuenter.ogg", wrapsound="menuwrap.ogg", leftright = True, updown = True, wrapping = True, homeend = True)
	s.add_music("mm1.ogg")
	for i in range(50):
		s.add_item("Item "+str((i+1)),str(i))
	pos = s.run("Select an option.",True)
	s.fade_music(20)
	sys.exit()
if __name__ == "__main__": main()