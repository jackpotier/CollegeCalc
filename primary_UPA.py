# number of universities
uniCount = 25

# define the ranking lists of universities (all lists are excluding schools that I don't want to attend))
econRank = [
  "harvard", "stanford", "princeton", "cal", "chicago", "yale", "northwestern",
  "columbia", "penn", "michigan", "cornell", "wisconsin", "duke", "minnesota",
  "brown", "boston university", "maryland", "texas", "boston college",
  "penn state", "unc", "virginia", "vanderbilt", "michigan state",
  "ohio state", "illinois", "asu", "georgetown", "indiana", "rice",
  "texas a&m", "arizona", "pitt", "usc", "notre dame", "purdue"
]  # economics undergraduate rankings based on https://www.usnews.com/best-graduate-schools/top-humanities-schools/economics-rankings?_sort=rank-asc
csRank = [
  "cal", "stanford", "georgia tech", "harvard", "cornell", "princeton",
  "texas", "michigan", "columbia", "illinois", "penn", "wisconsin",
  "usc", "purdue", "duke", "unc", "virginia tech", "umass", "asu", "minnesota",
  "penn state", "chicago", "utah", "pitt", "texas a&m", "virginia", "brown",
  "nc state", "tennessee", "arizona", "indiana", "rice"
]  # computer Science undergraduate rankings based on https://www.computersciencedegreehub.com/best/bachelors-computer-science/
ibRecruitRank = [
  "penn", "michigan", "harvard", "cornell", "princeton", "boston college",
  "columbia", "texas", "villanova", "virginia", "indiana",
  "notre dame", "georgetown", "northwestern", "florida", "cal", "georgia tech",
  "vanderbilt", "yale", "duke", "stanford", "usc", "chicago", "ohio",
  "wisconsin", "pitt", "cal", "georgia", "dartmouth", "unc"
]  # investment bank recruiting statistics from https://www.wallstreetoasis.com/forum/investment-banking/wso-rankings-for-investment-banks-university-power-rankings-part-10-of-10
overall = [
  "princeton", "harvard", "stanford", "yale", "chicago", "penn", "duke",
  "northwestern", "dartmouth", "brown", "vanderbilt", "rice", "cornell",
  "columbia", "notre dame", "cal", "georgetown", "michigan", "usc", "virginia",
  "florida", "unc", "boston college", "texas", "wisconsin",
  "boston university", "illinois", "georgia tech", "ohio state", "georgia",
  "purdue", "villanova"
]  # top national universities based on rankings from https://www.usnews.com/best-colleges/rankings/national-universities
swimTop12 = [
  "cal", "asu", "texas", "indiana", "nc state", "florida", "tennessee",
  "stanford", "virginia tech", "auburn", "ohio state", "georgia"
]  # the top 12 at the Mens NCAA Swimming Champs 2023, that at excluded from th final rankings
ncaaFromLast = [
  "northwestern", "brown", "yale", "harvard", "purdue", "georgia tech",
  "penn state", "pitt", "arizona", "columbia", "kentucky", "princeton", "utah",
  "unc", "wisconsin", "southern carolina", "minnesota", "michigan", "alabama",
  "notre dame", "virginia", "texas a&m"
]  # based off of schools ranked last to 13th at the Mens NCAA Swimming Champs 2023, for any other university not in this list ncaaFromLast_dis = 0


# define the weighting for each list (adding up to 1.00)
econ_weight = 0.18  # probable undergrad major
ibRecruit_weight = 0.30  # probable career path
overall_weight = 0.12  # how prestigious the school is
cs_weight = 0.05  # probable undergrad minor
ncaaFromLast_weight = 0.35  # how weak the swim team was at NCAA (weaker = more priority)

# calculate lengths of each ranking list
econ_len = len(econRank)
cs_len = len(csRank)
ibRecruit_len = len(ibRecruitRank)
overall_len = len(overall)
ncaaFromLast_len = len(ncaaFromLast)

#calculate the theoretical max score a university could recieve
max_score = (econ_weight * (1 - 1/econ_len)) + \
            (ibRecruit_weight * (1 - 1/ibRecruit_len)) + \
            (overall_weight * (1 - 1/overall_len)) + \
            (cs_weight * (1 - 1/cs_len)) + \
            (ncaaFromLast_weight * (1 - 0/ncaaFromLast_len))


# define a function to calculate the rank percentage score for a university
def calc_rank_percentage(u):
  # calculate the distance from the start of each list
  econ_dist = econRank.index(u) if u in econRank else econ_len
  ibRecruit_dist = ibRecruitRank.index(
    u) if u in ibRecruitRank else ibRecruit_len
  overall_dist = overall.index(u) if u in overall else overall_len
  cs_dist = csRank.index(u) if u in csRank else cs_len
  ncaaFromLast_dist = ncaaFromLast.index(
    u) if u in ncaaFromLast else 1

  # calculate the weighted rank score and therefore percentage for the university
  rank_score = (econ_weight * (1 - econ_dist/econ_len)) + \
               (ibRecruit_weight * (1 - ibRecruit_dist/ibRecruit_len)) + \
               (overall_weight * (1 - overall_dist/overall_len)) + \
               (cs_weight * (1 - cs_dist/cs_len)) + \
               (ncaaFromLast_weight * (1 - ncaaFromLast_dist/ncaaFromLast_len))
  rank_percentage = (rank_score / max_score)*100

  # return the rank score
  return rank_percentage

# sort the universities by their rank score
universities = econRank + ibRecruitRank + overall + csRank + ncaaFromLast
universities = list(set(universities))
ranked_universities = sorted(universities,
                             key=lambda u:
                             (-calc_rank_percentage(u), universities.index(u)))


# create a new list that contains only the top 20 universities that are not in swimTop12
top_universities = []
for u in ranked_universities:
    if len(top_universities) >= uniCount:
        break
    if u not in swimTop12:
        top_universities.append(u)

# print the list of my top universities
for i, u in enumerate(top_universities):
    print(f"{i+1}. {u}", "{}%".format(round(calc_rank_percentage(u),1)))