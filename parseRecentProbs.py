import json  # json 파일을 다루기 위한 모듈
import requests
from Database import Database
from datetime import datetime

def parseDate(s : str):
    return datetime.strptime(s, "%a %b %d %H:%M:%S %Y").strftime("%Y. %m. %d. ")

if __name__ == "__main__":
    recent = Database()
    recent.readDB("recent.json")

    with open("readme.md", "w", encoding="utf-8") as f:
        f.write("| 문제 번호 | 문제 이름 | 난이도 | 풀이 날짜 |\n")
        f.write("| --- | --- | --- | --- |\n")
        for problem in recent.DB["problems"]:
            id = problem["id"]
            title = problem["title"]
            level = problem["level"]
            date = parseDate(problem["update_date"])
            f.write(f"| {id} | [{title}](https://www.acmicpc.net/problem/{id}) | <img height=\"25px\" width=\"25px=\" src=\"https://static.solved.ac/tier_small/{level}.svg\"/> | {date} |\n")
        f.close()
