from ner import Parser

p = Parser()

p.load_models("models/")

print(p.predict("Steve went to Paris"))

print(p.predict("Steve Went to Paris"))
##Output [('Steve', 'B-PER'), ('went', 'O'), ('to', 'O'), ('Paris', 'B-LOC')]

print(p.predict("Jay is from India"))
print(p.predict("Donald is the president of USA"))
print(p.predict("European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices"))
print(p.predict("Dr. Doull from the Royal College of Paediatrics in Wales backed the Fresh Start"))
print(p.predict("The ceremony at Auschwitz culminated a week of events around the world, including a commemoration in Jerusalem attended by dozens of world leaders, who urged collective vigilance against a resurgence of anti-Semitism worldwide"))
print(p.predict("Fifteen years ago, some 1,500 survivors attended the anniversary event."))
print(p.predict("As a result, Russia was not invited to the anniversary of the liberation of Auschwitz, even though the Soviet Army liberated the camp."))
print(p.predict("NAEYC asked two researchers about what their work tells us about toys, children, and play."))
print(p.predict("Many of the toys nominated by parents and teachers were used most often and in the most complex ways by boys."))