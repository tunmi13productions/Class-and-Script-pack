from menu import menu, pygame, speak
import time

def main():
	win = pygame.display.set_mode((600, 400))
	pygame.display.set_caption("Menu Test")
	m = menu(wrap = True)
	m.add_item("option 1", "o1")
	m.add_item("option2", "o2")
	m.add_item("option3", "o3")
	result = m.run("Choose an option.")
	speak(f"You selected: {m.get_focused_item()}.")
	time.sleep(2)
	pygame.quit()

main()