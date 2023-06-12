from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Créer une session Chrome avec des options
chrome_options = Options()
chrome_options.add_argument("--start-fullscreen")
driver = webdriver.Chrome(options=chrome_options)

# Appeler l’application web pranx
driver.get("https://pranx.com/fake-dos/")

# Renvoie le titre de la page et son lien
print('Le titre de la page est {0}, et le lien est {1}'.format(driver.title, driver.current_url))

# Attendre une action de l'utilisateur avant de fermer la fenêtre
input("Appuyez sur une touche pour fermer la fenêtre du navigateur...")

# Fermer la fenêtre du navigateur
driver.quit()
