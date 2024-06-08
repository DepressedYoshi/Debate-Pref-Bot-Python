# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

class DebateTeam:
    def __init__(self, school="", team="", side="", year=23):
        self.school = self.wikiSchoolName(school) if school else ""
        self.team = team
        self.teamCode = self.wikiTeamCode(team) if team else ""
        self.side = side
        self.year = year

    def wikiSchoolName(self, school):
        tag = school.lower()
        keyword_to_school = {
        "woodward": "WoodwardAcademy",
        "liberalartsand": "LiberalArtsAndScienceAcademy",
        "lasa": "LiberalArtsAndScienceAcademy",
        "damien": "DamienHSStLucyPriory",
        "dhs": "DamienHSStLucyPriory",
        "clatchy": "CKMcClatchy",
        "baltimore city": "BaltimoreCityCollege",
        "brophy": "BrophyCollegePrep",
        "carrollton": "CarrolltonSacredHeart",
        "greenhill": "GreenhillSchool",
        "royce": "Head-Royce",
        "isidore": "IsidoreNewmanSchool",
        "jesuit": "JesuitDallas",
        "little rock": "LittleRockCentral",
        "marist": "MaristSchool",
        "mba": "MontgomeryBellAcademy",
        "montgomery bell": "MontgomeryBellAcademy",
        "nsu": "NSUUniversitySchool",
        "northside": "NorthsideCollegePreparatory",
        "overland": "OverlandParkWest",
        "sidwell": "Sidwell",
        "lukes": "StLukesSchool",
        "lab": "UniversityOfChicagoLab",
        "pace": "PaceAcademy",
        }
        for keyword, wiki_name in keyword_to_school.items():
            if keyword in tag:
                return wiki_name
        return school.replace(" ", "").replace("'", "").replace("-", "")


    def wikiTeamCode(self, team):
        index = team.find("&")
        n2 = team[index+2:]
        return team[:2] + n2[:2]
    #!!!UNCOMMENT THE FOLLOWING IF POOL  SIZE IS SMALL 
    # def linkIsGood(self,driver, url):  
    #     try:
    #         # Open the URL
    #         driver.get(url)

    #         # Now check the HTML content
    #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_teamname_j0ylg_1")))  # Adjust time as needed
    #         page_source = driver.page_source
    #         soup = BeautifulSoup(page_source, 'html.parser')

    #         h1_tag = soup.find('h1', {'class': '_teamname_j0ylg_1'})
    #         if h1_tag:
    #             for sibling in h1_tag.next_siblings:
    #                 if sibling.name == 'button' and 'pure-button _claim_j0ylg_5' in sibling.get('class', []):
    #                     return False
    #                 if sibling.name is not None or sibling.strip():
    #                     return True
    #         return False
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         return False

# Perform login once
    def changeTeamCode(self):
        str = self.teamCode
        self.teamCode = str[2:] + str[:2]
        
    def __str__(self):
            url = f"https://opencaselist.com/hspolicy{self.year}/{self.school}/{self.teamCode}/{self.side}"
            return url


