import csv
import sys
from  debate_team import DebateTeam  # Import the DebateTeam class, adjust the import as per your file organization
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# driver.get('https://opencaselist.com/login')
# username_elem = driver.find_element(By.ID, 'username')
# password_elem = driver.find_element(By.ID, 'password')
# username_elem.send_keys('YLi25@damien-hs.edu')
# password_elem.send_keys('C?Qdu8pRYxRs*gv')
# password_elem.send_keys(Keys.RETURN)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_home_13sim_1")))  # Adjust as per the page after login

# Example use of DebateTeam
debate_team = DebateTeam("School", "Team", "Side", 23)



# Function to read CSV and create DebateTeam objects
def genWikiLink(file_path, sides=None):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header row if there is one
        for row in reader:
            if len(row) >= 2:  # Check if the row has at least two columns
                school = row[0]
                team = row[2]
                side = sides if sides else ""
                debate_team = DebateTeam(school, team, side)
                # url = f"https://opencaselist.com/hspolicy{debate_team.year}/{debate_team.school}/{debate_team.teamCode}/{debate_team.side}"
                # if debate_team.linkIsGood(driver, url):
                print(debate_team)
                # else:
                #     debate_team.changeTeamCode
                #     print(debate_team)
    # driver.quit()


genWikiLink(r'C:\Users\joshu\Desktop\Project\Python\Template Scout Schhet.csv')


#command line access
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: wikigen.py <file_path> [sides]")
    else:
        file_path = sys.argv[1]
        sides = sys.argv[2] if len(sys.argv) > 2 else None
        genWikiLink(file_path, sides)
