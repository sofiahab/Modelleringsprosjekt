#!/usr/bin/env python
# coding: utf-8

# # Modelleringsprosjekt
# 
# ###### Sofia Håbrekke, 2E
# 

# # 1. Hensikt
# Hensikten med oppgaven er å utforske forskjellige modeller for tempratur og varmeinnstråling. 

# # Teori 
# 
# ##  1
# 
# ### Gjennomsnittlig varmestråling vertikalt på jorda
# I oppgave 1 skal vi finne gjennomsnittlig vertikal stråling på jorda. Dette kan vi gjøre ved bruk av Stefan boltzmanns lov. Denne loven gjør det mulig å regne ut hvor mye varmestråling et objekt sender ut, ved å bruke tempraturen. 
# 
# $ $
# $ \textrm{Stefan - Boltzmanns lov} $
# 
# Loven sier at alle gjenstander som har en tempratur over absolutt nullpunkt (-273.15 C/ 0 K) sender ut varmestråling, en EM-stråling som fører varme.  Det er mulig å regne ut varmestrålingen ved bruk av formelen
# 
# $$S = \sigma T^4 $$
# 
# der $\sigma$ er Stefan - Boltzmanns konstant og tilsvarer $5.6703 \cdot 10^{-8} W / ( m^2 K^4 )$ og tempraturen "T" er målt i Kelvin. Strålingen S" er strålingen fra et legme målt i $W/m^2$ og man må tenke på arealet til legmet for å få den fullstendige strålingen
# 
# $$ $$
# $ \textrm{Kalkulering av gjennomsnittlig EM-stråling som treffer vertikalt på jorda} $
# 
# Når vi skal kalkulere gjennomsnittlig vertikal stråling på jorda kan vi bruke en formel som bruker solens varmestråling og distansen mellom sola og planeten i solsystemet. Formelen ser slik ut:
# 
# $$ S = \frac{radius_{sol}^2}{distanse_{\textrm{sol og planet}}^2} \cdot \textrm{varmestråling sol} $$
# 
# her ser vi S som gjennomsnittlig stråling som treffer planeten i $W/m^2$
# 
# Vi kan bruke Stefan - Boltzmanns lov til å regne ut hvor mye varmestråling sola gir av seg, og formelen for vertikal stråling til å regne ut hvor mye som gjennomsnittlig varmestråling som treffer vertikalt på jordens atmosfære

# ##  2
# ### Gjennomsnittlig tempratur, med albedo
# 
# For å lage et utrykk for gjennomsnittlig tempratur for jorda kan vi bruke både energiprinsippet og Stefan- Boltzmanns lov. 
# 
# $$ $$
# $ \textrm{Energiprinsippet} $
# 
# energiprinsippet siier at energi er konstant, det kan ikke forsvinne eller skapes, det sier også at
# 
# $$ Energi_{inn} = Energi_{ut} $$
# 
# Vi kaller innstrålingen $K_s$
# 
# 
# $K_s = \sigma T^4 $
# 
# Siden vi skal regne med refleksjonen/ albdoen og at $energi_{inn} = energi_{ut}$ må vi gange strålingnen med $(1-albedo)$
# 
# $K_s \cdot (1-albedo) = \sigma T^4 $
# 
# Vi deler også innstrålingen på 4 for å ta i betrakning at sola ikke skinner vertikale stråler inn på jorda hele dagen, og at den ikke skinner likt på alle steder på jorda, for å få en mer realistisk modell
# 
# $\frac{K_s \cdot (1-albedo)}{4} = \sigma T^4 $
# 
# 
# $ \textrm{Om vi snur på likningen får vi :} $
# 
# $$ T = \sqrt[4]{\frac{K_s \cdot (1-abedo)}{4\sigma}} $$

# ##  3
# ### Forenklet atmosfære
# $$ \textrm{Energiprinsippet} $$
# - Energi kan ikke skapes eller forsvinne. 
# - Planeter er et lukket system som får tilført energi fra verdensrommet, bla sola
# - Planetene sender også ut stråling, og dette kan gi tre muligheter ;
# 
# 
# 1. $ Energi_{inn} = Energi_{ut} $, planetens tempratur er konstant
# 2. $ Energi_{inn} < Energi_{ut} $, planetens tempratur minker med tid
# 3. $ Energi_{inn} > Energi_{ut} $, planetens tempratur øker med tid
# 
# Vi må også minne oss selv på at ingen av disse er faktisk sanne, men kun en forenkling. 
# 
# $ $
# $$ \textrm{Forenklet atmosfære} $$
# - Pga atmosfæren har vi positiv tempratur på jorda
# - For å tegne en forenklet atmosfære kan vi tenke på 3 antagelser 
# 
# 
# 1. Atmosfæren har konstant tempratur, dvs at hele atmosfæren er en stor blokk med samme tempratur
# 2. Atmosfæren er fullstendig gjennomsiktig for stråling fra jorden, dvs at all stråling fra solen treffer jordoverflaten
# 3. atmosfæren tar inn all stråling fra jorden
# 
# selvfælgelig vet vi at alle disse ikke er sanne i virkeligheten, men de er nyttige når vi skal lage en modell for en atmosfære 
# 
# Vi antar at strålingen går rett gjennom atmosfæren og treffer jordoverflaten, jorden reflekterer all varmestråling, og atmosfæren vil sende ut litt stråling til verdensrommet, og litt reflekteres tilbake til jorda. 
# 
# 
# $$ $$
# $ \textrm{Stefan- Boltzmanns lov} $
# 
# $S = \sigma T^4 $
# 
# Når vi skla bruke Stefan - Boltzmanns lov i denne modellen skal den gjelde for både jordkloden og atmosfæren
# 
# #### Modellen
# 
# vi har to modeller der vi antar at $energi_{inn} = energi_{ut}$
# 
# - det ene systemet er varmestråling fra solen inn i systemet, og varmestråling ut av systemet fra atmosfæren til verdensrommet
# - det andre systemet vil være varmestråling som treffer jordoverflaten og varmestråling ut fra jordoverflaten
# 
# - bruk Stefan - Boltzmanns lov varmestråling fra jorden og atmosfæren 
# - lag et likningsystem med to ukjente og løs for tempraturen ved jordoverflaten

# ### Likningsystem 
# 
# for å regne ut tempraturen må vi sette opp et likningsystem med 2 ukjente, og finne $T_s$
# 
# #### System 1 :
# 
# I system 1 tar vi for oss energibevaringsloven, og pilene 1 og 2, ut. 
# Pil 1 er det eneste som går inn i likningsystemet, og pil 2(ut) er den eneste som går ut, derfor må de være like store. 
# 
# $ $
# siden $energi_{inn} = energi_{ut}$ er $Pil_1 = Pil_2 (ut)$
# 
# $ S_{a} = \sigma T_{a}^4 $
#  
# $ S_{a} = s0 \cdot (1-albedo) $
# 
# da ender vi opp med : 
# 
# $ s0 \cdot (1-albedo) = \sigma T_{a}^4  $
# 
# 
# $$ $$
# #### System 2 :
# 
# $ S_{inn + reflektert} = T_{sum}^4 $
# 
# $ S_{\textrm{inn + reflektert}} = S_{inn} + S_{reflektert} $
# 
# $$ $$
# som sett i forrige likning, pga energibevaringsloven må $ energi_{inn} = energi_{ut} $, og derfor må også energien inn i systemet være lik energien til pil 2, eller: 
# 
# $$ $$
# $ S_{inn} = s0 \cdot (1-albedo) $
# 
# siden  $ energi_{inn} = energi_{ut} $ må både pil 2 (inn) og pil 2 (ut) være like store : 
# 
# $ S_{reflektert} = \sigma T_{a}^4 $
# 
# derfor må : 
# 
# $ s0 \cdot (1-albedo) + \sigma T_{a}^4 =  \sigma T_{sum}^4 $
# 
# 
# ### Ferdig likningsystem 
# 
# $\textrm{I:   } s0 \cdot (1-albedo) = \sigma T_{a}^4  $
# 
# $\textrm{II:  } s0 \cdot (1-albedo) + \sigma T_{a}^4 =  \sigma T_{sum}^4 $
# 
# $$ $$
# $$ \textrm{ deretter setter jeg system I inn i system II} $$
# 
# $$ $$
# $\textrm{II : }$ 
# 
# $ s0 \cdot (1-albedo) + \sigma T_{a}^4 =  \sigma T_{s}^4 $
#     
# $ 2 \cdot (s0 \cdot (1-albedo)) = \sigma T_s^4 $
# 
# $$ $$
# $\textrm{vi snur likningen og ender opp med : }$
# 
# $ T_s = \sqrt[4]{\frac{2 \cdot s0 \cdot (1-albedo)}{\sigma}} $

# # Modeller
# 
# ## Modell 1

# In[63]:


from pylab import*


sigma = 5.67e-8                   # målt i w/m^2K^4

temp_sol = 5778                   # tempratur av sola, målt i Kelvin              
diameter_sol = 1391016e3          # diameter av sola, målt i m
radius_sol = (1391016e3)/2        # radius til sola, målt i m
distanse_sol_jord = 149600000e3   # distanse mellom sola og jorda, målt i m

radius_jord = 6371e3              # radius til jorda, måt i m 
albedo = 0.3                      # albedo/refelksjonstall


# Definerer funksjonen for varmestråling fra sola
def varmestråling(temp):
    return sigma*(temp**4)
    

# Funksjon for gjennomsnittlig varmestråling som treffer jorda
def vertikalstråling(r, d, v):
    return ((r**2)*v)/(d**2)

    
varmestråling_sol = varmestråling(temp_sol)
vertikal_stråling = vertikalstråling(radius_sol, distanse_sol_jord, varmestråling_sol)

print('gjennomnsittlig vertikal varmeinnstråling til jorda er', vertikal_stråling)


# ## Modell 2

# In[64]:


varmestråling = 1365.9483      # jordas vertikal innstråling, som gitt i forrige oppg
albedo = 0.3                   # albedo/refelksjonstall
sigma = 5.67e-8                # målt i w/m^2K^4



# funksjon for tempraturen (stefan- boltzmanns lov)
def Tempratur(s0):
    return ((s0*(1-albedo))/(4*sigma))**(1/4)


varmestråling_atmosfære = sum_stråling(varmestråling)
g_temp = Tempratur(varmestråling)


print('gjennomsnittstempraturen er', g_temp,'K',
     ', eller', g_temp-273.15, 'C')


# ## Modell 3

# In[65]:


varmestråling = 1365.9483      # jordas vertikal innstråling, som gitt i forrige oppg
albedo = 0.3                   # albedo/refelksjonstall
sigma = 5.67e-8                # målt i w/m^2K^4

def T_s(s0):
    return (2*(s0*(1-albedo))/sigma)**(1/4)

tempratur_jordoverflate = T_s(varmestråling)

print('jordoverflatetempraturen er', tempratur_jordoverflate,'K',
     ', eller', tempratur_jordoverflate-273.15, 'C')


# ## Modell 4/5?

# In[66]:


varmestråling = 1365.9483      # jordas vertikal innstråling, som gitt i forrige oppg
albedo = 0.3                   # albedo/refelksjonstall
sigma = 5.67e-8                # målt i w/m^2K^4

def T_s(s0):
    return (2*(s0*(1-albedo))/sigma)**(1/4)

tempratur_jordoverflate = T_s((varmestråling/4))

print('jordoverflatetempraturen er', tempratur_jordoverflate,'K',
     ', eller', tempratur_jordoverflate-273.15, 'C')


# ## Modell 5/6?

# In[67]:


tempratur = []
tid = []

for i in range (12):
    tid.append(i)
    tempratur.append(18)

    
plot( tid, tempratur, color ='red')

xlabel('månder')
ylabel('tempratur')

grid()
show()


# # Diskusjon

# ## Oppgave 1
# 
# $\textrm{Hvorfor fungerer denne modellen ? }$
# 
# Modellen fungerer fordi vi får et realistisk mål på solens utstråling samt hvor mye av de som faktisk treffer vertikalt på jordens atmosfære. Modellen tar i betrakning variabler som hvor stort objektet som gir ut varmestrålinger, sola, er, samt hvor stor distanse den er fra jorda. 
# 
# Ved å se på formelen alene ser vi at strålingen øker omvendt proposjonalt med distansen fra planeten. Dette er sant fodi jo lenger unna sola vi er, jo svakere er varmestrålingen, og 'strålene' er mer spredt ut enn når planeten er nermere. 
# 
# Strålingen øker også proposjonalt med størrelsen (radiusen) til sola. Jo større sola er, jo mer varme sender den ut, og derfor kan vi også se at dette aspektet ved modellen er riktig
# 

# ## Oppgave 2
# 
# $ \textrm{ Hvorfor kan vi anta at planeten er en flat sirkel?}$
# 
# Vi kan anta at planeten er en flat sirkel fordi v bruker en forenklet modell, og i den bruker vi en utregning som forteller oss den vertikale innstrålingen på jorda. Vi tar også med a vi deler innstrålingen på 4 for å få en mer riktig beregning. 
# 
# $ $
# $ \textrm{Resultat }$ 
# 
# resultatet vi får, ca 254.81 K eller -18.34 C, er veldig annerledes fra det vi har observert, ca 15 C. Dette kan være fordi vi ikke tar for oss de mange variablene. I Oppgave 3 tar vi med en mer detaljert modell for atmosfæren der vi tar med innstrålingen, samt refelksjonen, og ikke refelksjonen/innstrålingen alene. 

# ## Oppgave 3
# 
# $ \textrm{ Hvordan påvirket den nye modellen resultatet?} $
# 
# I oppgave 3 lager vi et nytt likningsystem som gir en tempratur i overkant av 155 C. Tempraturen er allt for høy, dette kan være for en av mange mulige grunner. En av dem er at vi ikke tok for oss at ikke hele planeten får like sterk, vertikal stråling hele året rundt, slik som det er nærme ekvator. Noe annet vi ikke tok for oss er at vi ikke får varmestråling om kvelden når planeten er vendt mot sola. Vi har også regnet med at all varmeinnstråling går direkte gjennom atmosfæren, noe den ikke gjør. 

# ## Oppgave 4/5?
# I oppgave 3 ser vi at jordoverflatetempraturen er veldig høy, og dette kan være mange grunner til, bla;
# 
# - Vi har regnet med at alle solstrålene går direkte på jorda, slik de gjør ved ekvator, men for hele jorda.
# - Vi har regnet med at alle varmeinnstrålingne går direkte gjennom atmosfæren
# - Vi regner med at $energi_{inn} = energi_{ut}$
# - Vi regner med at all energi er reflektert av jordoverflaten
# 
# siden vi har dag og natt, og sola ikke hele tiden skinner vertikalt på jorda prøver vi å dele s0 på 4, slik at:
# 
# $2 \cdot (\frac{s0}{4} \cdot (1-albedo)) = \sigma T_s^4 $
# 
# $ T_s = \sqrt[4]{\frac{2 \cdot s0 \cdot (1-albedo)}{4\sigma}} $
# 

# 
# om vi prøver med det slik er tempraturen lik ca 30 C, dette ligner mer på det som har vært observert, mellom 10 og 25 C, men er ikke helt riktig heller. andre forslag til endringer jeg har er :
# 
# - regne med at varmestrålingen ikke treffer vertikalt alle steder, og er svakere nermere nord, dvs regne med at jorda er rund. 
# - regne med at en prosentdel av varmestrålingen ikke kommer inn i atmosfæren, men dette er være vanskelig å sette inn i koden fordi jeg ikke vet hvor stor den prosentandelen er. 
# 
# 

# ## Oppgave 5/6
# 
# I den siste oppgaven viste jeg ikke helt hvordan å gå fram, så jeg fant en by nær ekvator og så at gjennomsnittstempraturen hver månde gjennom hele året varierte nesten ingenting fra månde til månde. Tempraturen forandrer seg ikke mye fra sesong til sesong slik den gjør i norge, eller andre steder som ikke er nær ekvator. Dette er fordi energien de får inn er veldig konstant, varmestrålingen forandrer seg ikke fra sommer til vinter, slik den gjør her. Ekvator er der solstrålene kommer vertikalt inn på atmosfæren i samme styrke grad gjennom hele året, og har større forandringer mellom hver dag enn generelt mellom ukene og måndene.  
# 
# jeg tok utgangspunkt i byen Quito i Ecuador. 

# # Konklusjon
# 
# Vi har utforsket forskjellige modeller for å finne ut tempraturen til jorda, samt forstå matematikken, teorien og tankene bak modellene. Vi har utforsket og drøftet ulike modeller med mange ulike fordeler og ulemper, riktigheter og feilkilder, med varierende kompleksitet og nøyaktighet. Ingen av modellene er fullstendig riktige, men gir et godt bilde av det hele. 
# 
# Vi kan nok utvide modellene og finne enda mer nøyaktighet ved å legge til ulike variabler, slik som hvor mye av varmen som blir absorbert i bakken, og lagt til i hvor sor grad av varmestråler som faktisk kommer gjennom atmosfæren 

# In[ ]:




