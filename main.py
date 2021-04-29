import feedparser, datetime

velog_blog_rss_uri="https://v2.velog.io/rss/@whdud132"
feed = feedparser.parse(velog_blog_rss_uri)

markdown_text = """
![header](https://capsule-render.vercel.app/api?&type=wave&color=gradient&text=new%20Jay();&height=300)

<h3 align="center"> 👋 Hi there 👋 </h3>
<p align="center">
I'm Jay, I'm junior developer. 🌱 <br>
Please watch me grow up. 👨‍💻
</p>
<h3 align="center">📚 Technology Stack 📚</h3>

<p align="center">
  <img src="https://img.shields.io/badge/-Java-008396?logo=Java&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/-Javascript-F7DF1E?&logo=Javascript&logoColor=black"/></a>&nbsp
  <img src="https://img.shields.io/badge/-Typescript-3178C6?&logo=Typescript&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/-Spring-6DB33F?&logo=Spring&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/-NestJS-E0234E?&logo=NestJS&logoColor=white"/></a><br>
  <img src="https://img.shields.io/badge/-Docker-2496ED?&logo=Docker&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/-React-61DAFB?&logo=React&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/-GraphQL-E10098?&logo=GraphQL&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/-Nextjs-000000?&logo=Next.js&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/-Apollo-311C87?&logo=Apollo%20GraphQL&logoColor=white"/></a>&nbsp
</p>

<h3 align="center">📞 Connect 📞</h3>

<p align="center">
  <a href="https://velog.io/@whdud132"><img src="https://img.shields.io/badge/Tech%20Blog-11B48A?style=flat-square&logo=Vimeo&logoColor=white&link=https://velog.io/@whdud132"/></a>&nbsp
  <a href="mailto:gameclow2@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:gameclow2@gmail.com"/></a>
</p>

  ![EungyuCho's github stats](https://github-readme-stats.vercel.app/api?username=EungyuCho&show_icons=true)
  ![solved.ac tier](http://mazassumnida.wtf/api/generate_badge?boj=cho2304)

### ✍ Recent blog posts 
""" # list of blog posts will be appended here

lst = []

j=0
for i in feed['entries']:
    j+= 1
    if j >5:
        break
    else:
        # dt = datetime.datetime.strptime(i['published'], "%a, %d %B %Y %H:%M:%S %z").strftime("%B %d, %Y")
        dt = i['published']
        # markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
        markdown_text += f"[{i['title']}]({i['link']}) <br>\n"
        print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()