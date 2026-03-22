import re, os
DATA = os.path.join(os.path.dirname(__file__), 'data.js')

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

IDEAS = [
mk("HCV01","The Church Density Map: Houses of Worship Per Capita by County","Churches, mosques, synagogues, and temples per 10,000 residents by county — the Bible Belt is real","MAP","US","County choropleth","religion","ARDA: Religious Congregations and Membership Study (thearda.com/rcms2020)",68,72,78,72,62,82,68,85),
mk("HCV02","Americas Religious Switching: Who Leaves Which Faith and Where They Go","Sankey diagram of religious affiliation changes — Catholic to None, Evangelical to Mainline, etc.","CHART","US","Special map","religion","Pew: Religious Landscape Study Switching (pewresearch.org/religion)",72,72,72,78,68,78,75,80),
mk("HCV03","The Megachurch Map: Every Church With 2000+ Weekly Attendance","Geographic distribution of Americas 1,700+ megachurches, concentrated in the Sun Belt and suburbs","MAP","US","Dot map","religion","Hartford Institute: Megachurch Database (hartfordinstitute.org/megachurch)",65,68,75,72,60,82,68,80),
mk("HCV04","God and GDP: National Religiosity vs. National Wealth","Percentage of population that says religion is very important plotted against GDP per capita — the US is the outlier","XREF","World","Scatter plot","religion","Pew: Global Religiosity Survey (pewresearch.org/religion/global-religious-landscape)",70,68,78,82,65,70,78,82),
mk("HCV05","The Missionary Map: Where American Missionaries Go","Destination countries for American missionaries by denomination, showing the geography of religious export","MAP","World","World choropleth","religion","Gordon-Conwell: Status of Global Christianity (gordonconwell.edu/center-for-global-christianity)",65,58,72,75,60,80,72,68),
mk("HCV06","Sharia Law Spectrum: How Islamic Law Is Applied Differently Across Muslim Countries","Degree of sharia implementation by country — from full criminal code to family law only to secular","MAP","World","World choropleth","religion","Pew: The Worlds Muslims (pewresearch.org/religion/the-worlds-muslims)",68,58,72,78,72,80,72,75),
mk("HCV07","The Tithe Belt: Charitable Giving as Percentage of Income by County","Religious charitable giving per capita by county, showing how faith drives Americas donation geography","MAP","US","County choropleth","religion","IRS: Statistics of Income Charitable Contributions (irs.gov/statistics/soi-tax-stats)",68,72,78,75,62,82,68,82),
mk("HCV08","The Sunday Morning Divide: Church Attendance Rate by State Over Time","Weekly church attendance rates by state, 2000 vs. 2025, showing the secularization acceleration","MAP","US","Bivariate choropleth","religion","Gallup: Church Attendance (news.gallup.com/poll/341963/church-membership-falls-below-majority)",72,72,78,72,70,78,68,78),
mk("HCV09","Where the Worlds Religions Meet: The Most Religiously Diverse Countries","Religious diversity index by country — Singapore, Suriname, and several African nations top the list","MAP","World","World choropleth","religion","Pew: Religious Diversity Index (pewresearch.org/religion/religious-diversity-index)",62,58,75,78,58,82,72,82),
mk("HCV10","The Creationism Map: States Where Evolution Acceptance Is Below 50%","Percentage of adults who accept evolution by state, showing deep geographic variation in scientific consensus","MAP","US","State choropleth","religion","Pew: Evolution Views by State (pewresearch.org/science)",72,68,78,78,72,78,72,78),
mk("HCV11","How Old Is Your Church: Age of Religious Congregations by Denomination","Average age of congregations by denomination — many mainline Protestant churches were founded 100+ years ago, evangelical churches much newer","CHART","US","Bar chart","religion","ARDA: National Congregations Study (thearda.com/ncs)",60,62,72,78,55,68,72,72),
mk("HCV12","The Holy Land Layered: Every Sacred Site in Jerusalem by Religion","Map of every Jewish, Christian, Muslim, and other sacred site within the Old City of Jerusalem","MAP","Middle East","City map","religion","UNESCO: Old City of Jerusalem World Heritage (whc.unesco.org/en/list/148)",68,58,68,72,68,90,78,72),
mk("HCV13","Religious Exemption Laws: Where Faith Overrides Health, Education, and Labor Rules","States with religious exemptions from vaccination, child medical care, employment discrimination, and education requirements","MAP","US","State choropleth","religion","National Conference of State Legislatures: Religious Exemptions (ncsl.org)",72,68,75,78,75,78,72,78),
mk("HCV14","The Seminary Pipeline: Where Americas Clergy Is Trained","Every accredited seminary and divinity school mapped by denomination and enrollment trends","MAP","US","Dot map","religion","ATS: Enrollment Data (ats.edu/resources/institutional-data)",58,55,72,68,55,80,68,75),
mk("HCV15","The Hajj Logistics Machine: How 2 Million People Converge on One City","Infrastructure, logistics, and crowd management of the annual Hajj pilgrimage to Mecca","MAP","Middle East","Special map","religion","Saudi Ministry of Hajj: Statistics (haj.gov.sa)",65,55,72,78,65,85,78,72),
mk("HCV16","Interfaith Marriage Rates: How Often People Marry Outside Their Religion","Percentage of marriages between different religions by faith and by decade — rising steadily","CHART","US","Line chart","religion","Pew: Interfaith Marriage (pewresearch.org/religion/intermarriage)",68,72,72,72,65,68,68,78),
mk("HCV17","The Religion of Congress: Faith Composition vs. The Nation They Represent","Religious affiliation of Congress members compared to the general population — massive overrepresentation of some faiths","CHART","US","Bar chart","religion","Pew: Faith on the Hill (pewresearch.org/religion/faith-on-the-hill)",68,68,78,78,68,70,72,85),
mk("HCV18","Buddhist America: Where Buddhism Has Taken Root in the US","Buddhist temples and meditation centers mapped by county, showing the geography of American Buddhism","MAP","US","Dot map","religion","Pluralism Project: Buddhism Directory (pluralism.org/religions/buddhism)",60,58,70,72,55,82,72,72),
mk("HCV19","The Amish Expansion: Americas Fastest-Growing Religious Community","Amish settlement growth from 1900 to present — doubling every 20 years, expanding into new states","MAP","US","Animated choropleth","religion","Young Center: Amish Population Profile (amishstudies.org)",62,62,72,82,58,80,78,78),
mk("HCV20","Witch Trials to Wicca: The Geography of American Paganism and New Age Spirituality","Where Wiccan, pagan, and new age spiritual communities concentrate in the US","MAP","US","Dot map","religion","ARDA: Alternative Spirituality Data (thearda.com)",58,58,65,78,55,78,78,62),
mk("HCV21","The Exorcism Revival: Countries Where Exorcism Practice Is Growing","Nations reporting increased demand for exorcism services — Philippines, Italy, Poland, parts of Africa and Latin America","MAP","World","World choropleth","religion","Vatican: International Association of Exorcists (aieprete.it)",62,55,62,85,65,75,82,55),
mk("HCV22","Americas Mosque Map: Growth of Islamic Centers Since 2000","Muslim mosques and Islamic centers in the US, showing 75% growth since 2000","MAP","US","Dot map","religion","ISNA: US Mosque Survey (isna.net)",65,60,72,72,62,82,68,75),
mk("HCV23","The Prosperity Gospel Geography: Where Wealth-and-Health Theology Thrives","Megachurches preaching prosperity theology mapped against median income of surrounding ZIP codes","XREF","US","Scatter plot","religion","Hartford Institute: Megachurch Survey (hartfordinstitute.org)",68,68,68,80,68,72,78,65),
mk("HCV24","Religious Freedom Violations: Countries Where Practicing Faith Gets You Arrested","Countries with highest rates of government restriction on religious practice, by faith targeted","MAP","World","World choropleth","religion","Pew: Government Restrictions on Religion (pewresearch.org/religion/government-restrictions)",78,62,75,72,80,80,68,82),
mk("HCV25","The Christmas Industrial Complex: Holiday Spending by Country","Christmas-related consumer spending per capita by country, showing commercialization beyond Christian populations","RANK","World","Bar chart","religion","Deloitte: Holiday Retail Survey (deloitte.com/us/en/pages/consumer-business)",62,78,75,72,55,70,68,78),
mk("HCV26","Where Churches Are Closing vs. Where They Are Opening","Net church openings and closings by county — the geography of American congregational decline and renewal","MAP","US","Bivariate choropleth","religion","Lifeway Research: Church Planting and Closing (lifewayresearch.com)",72,68,72,75,70,82,70,72),
mk("HCV27","The Sunday School Collapse: Youth Religious Education Enrollment Over Time","Decline in Sunday school and religious education enrollment across denominations, 1960-2025","CHART","US","Line chart","religion","ARDA: Religious Education Data (thearda.com)",72,68,72,72,70,68,68,72),
mk("HCV28","Kosher and Halal: The Religious Food Economy Map","Distribution of kosher and halal food production, certification, and retail in the US","MAP","US","Dot map","religion","OU Kosher: Certified Products (oukosher.org)",60,62,72,72,55,80,70,68),
mk("HCV29","The Catholic Priest Shortage: Parishes Per Active Priest Over Time","Ratio of Catholic parishes to active diocesan priests, 1965 vs. now — from 1:1 to 3:1 in many dioceses","CHART","US","Line chart","religion","CARA: Catholic Church Statistics (cara.georgetown.edu)",68,62,75,78,68,68,70,78),
mk("HCV30","Hindu Temple Boom: Indian-American Religious Architecture in the Suburbs","Growth of Hindu temples in US suburbs, concentrated in New Jersey, Texas, California, and Georgia","MAP","US","Dot map","religion","Hindu Temple Directory (hindutempleusa.com)",60,58,70,72,55,82,72,72),
mk("HCV31","The Bible Belt Is Moving: Most Religious Regions Then and Now","Shift in Americas most and least religious regions from 1970 to 2025","MAP","US","Bivariate choropleth","religion","Gallup: Most and Least Religious States (news.gallup.com/poll/religiousness)",68,68,75,75,68,82,70,78),
mk("HCV32","End Times Belief by Country: Who Thinks the World Is Ending Soon","Percentage of population that believes they are living in the end times, by country — remarkably high numbers","MAP","World","World choropleth","religion","Pew: Global Religious Futures (pewresearch.org/religion/religious-landscape-study)",65,62,68,85,68,78,78,72),
mk("HCV33","The Scientology Footprint: Every Church and Celebrity Centre Location","Map of every Church of Scientology worldwide, including real estate holdings and estimated membership","MAP","World","Dot map","religion","Tampa Bay Times: Scientology Database (tampabay.com/topics/specials/scientology.page)",62,58,68,78,62,80,75,68),
mk("HCV34","Americas Jewish Geography: Population Shifts from Northeast to Sun Belt","Jewish population by metro area over time, showing migration from New York and the Northeast to Florida, California, and Texas","MAP","US","Dot map","religion","Brandeis: American Jewish Population Project (brandeis.edu/ssri/programs/ajpp)",65,62,72,72,60,80,68,78),
mk("HCV35","The Prayer Gap: How Often People in Different Countries Pray Daily","Percentage of population that prays daily by country — from 75% in some African nations to 6% in some European ones","MAP","World","World choropleth","religion","Pew: Global Religion Daily Prayer (pewresearch.org/religion)",62,62,75,72,58,80,68,82),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All 35 ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HCV batch)")
