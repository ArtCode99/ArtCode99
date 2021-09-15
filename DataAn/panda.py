import pandas as pd
import nampai as np
df=pd.read_csv('pokemon_data.csv')
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',15)

#print(df.head(4))

#Read Headers:
#print(df.columns)

#Read each/a specific column:
#print(df[['Name','HP']])      #putem sa afisam mai multe coloane, dar trebuie sa punem [[ ]]. ALternativ putem sa facem o lista cu coloanele si s-o dam ca parametru


#Read each row:
#print(df.iloc[1:4])             # folosim .iloc pentru a afisa randuri
#print (df.iloc[2,1])            # cu virgula intre ele putem specifica ce rand si ce coloane vrem

#Sa accesezi toate datele rand cu rand:
#for index, row in df.iterrows():
#    print(index,row)                 # asa trece prin toate inregistrarile. Putem dupa row-ul din print sa punem si ['Name'] sau ceva de genu si sa afiseze doar o col

# Ca sa accesezi anumite date in functie de text, nu de indecsi, foloseste .loc
#print(df.loc[df['Type 1'] == 'Fire'])             #e ca un fel de IF, ii zice sa printeze randurile acolo unde type 1 este egal cu fire


#Pt a afisa detalii despre date folosim describe: count, mean. std. min, max
#print(df.describe())

#Ca sa sortam
#df.sort_values('Name',ascending=True)
#df.sort_values(['Name','HP'],ascending=[1,0])     #ca sa sortezi dupa mai multe coloane


#Sa creezi o noua coloana :
#df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
#print(df)

# O modalitate mai usoara in loc sa aduni coloanele pe rand e cu iloc:
#df['Total']= df.iloc[ : , 4:10].sum(axis=1)              # afiseaza toate randurile, si coloanele doar 4-9, facand suma PE LINII


# Sa stergi o coloana tre sa asignezi din nou, si faci du drop:
#df = df.drop(columns=['HP'])


# Ca sa salvam un dataframe intr-un csv:
#df.to_csv("Modified_Poke.csv")            #AVEM FUNCTIA .to_cv("cale")


# FILTREEEE

#Daca vrei sa aplici mai multe filtre, ca sa folosesti  & sau | trebuie sa pui paranteze la fiecare (NU MERGE AND! ) :
#print(df.loc[(df["Type 1"]=='Grass') & (df['Type 2']=='Poison') | (df['HP']>50)])


#imp - dupa ce filtrezi, se modifica ampulea indexu, si te incurca daca mai vrei si alte procesari, asa ca trebuie RESETAT INDEXU:
#new_df=df.loc[(df["Type 1"]=='Grass') & (df['Type 2']=='Poison') | (df['HP']>50)]
#new_df.reset_index(drop=True,inplace=True)

#Ca sa filtrezi dupa o coloana care contine un anumit cuvant:
#df.loc[df['Name'].str.contains("Mega")]     #


#Conditional changes:
#df.loc[df['Type 1']=='Fire', 'Legendary']=True       # Daca punem virgula dupa conditie, putem sa punem o coloana si apoi egall cu ce sa primeasca
#print(df)


#GroupBy , bineinteles cu functii agregate
print(df.groupby(['Type 1']).mean().sort_values('Attack',ascending=False))




# CAND LUCREZI CU BIGDATA SIO AI UN fisier de vreo 20 de gb nu poti sa-l citesti pe tot o data, asa ca il citesti pe rand:
#for df in pd.read_csv("NUme.csv",chunksize=100)        #chunksize e numaru de randuri citite deodata
#    print(df)