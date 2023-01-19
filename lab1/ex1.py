import re

txt1 = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"

delete_numbers = re.sub("[0-9]+", "", txt1)
print(delete_numbers)

txt2 = "<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"

delete_html = re.sub(r"<.*?>", "", txt2)
print(delete_html)

txt3 = "Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. Mauris egestas erat " \
               "quam, ut faucibus eros congue et. In blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at " \
               "tristique augue risus eu risus."

delete_punctuation = re.sub("[.;,?!:]+", "", txt3)
print(delete_punctuation)
