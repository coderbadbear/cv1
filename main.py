import streamlit as st
from PIL import Image

st.set_page_config(page_title="Ahmet Sabri Aru", page_icon="🚀", layout="wide")

#assets yükleme
a_photo = Image.open("fotolar/b.png")

#başlık zımbırtısı
with st.container():
    st.subheader("Prof. Dr. Ahmet Sabri ARU")
    st.write("ahmet-sabri-aru@caltech.edu")
    st.write("[Research Web Site ](https://cosmology.caltech.edu)")
    text_column, image_column = st.columns((10, 1))
    with image_column:
        st.image(a_photo)
    st.subheader("Refrences")
    st.write("""Richard Feynman : +1 (555) 555-1234\n
Paul Dirac : +44 11 1234 5678\n
Max Tegmark : +1 (555) 555-4321\n
             """)



with st.container():
    st.subheader("""Institution Information\n
Faculty / Institute / Unit: Faculty of Science\n
Department: Department of Astronomy and Space Sciences\n
Department of science: Department of Astrophysics""")


    with text_column:
        st.subheader("International researcher IDs")
        st.write("""ORCID : 0000-0000-0000-0000\n
Publons / Web Of Science ResearcherID : AAA-1111-2023""")

    with text_column:
        st.subheader("Research Field")
        st.write(""" Theoretical Astrophysics\n
Cosmology\n
Einstein's Theory of Gravitation\n
Dark Energy and Dark Matter\n
Quasars & Other Active Black Holes """)

    with text_column:
        st.subheader("Metrics ")
        st.write("""Number of Publications : Unisis : 43\n
Number of Citations : Unisis : 809\n
Number of Average Citations : Unisis : 18,81\n
H-Index : Unisis : 16
""")

    with text_column:
        st.subheader("Education Information")
        st.write("""1. Post Doktora, 2032 - 2033, Massachusetts Institute Of Technology, Kavli Institute For Astrophysics And Space Research, Physic, United States Of
America,\n
2. Doktora, 2028 - 2032, Cambridge University, Graduate School of Natural and Applied Science, Department of Astronomy and Space Sciences (Dr), UK""")

    with text_column:
        st.subheader("Academic and Administrative Experience")
        st.write("""1. Other Academic Duty, 2033 - 2034, Observatoire De Paris, Physic, Paris Diderot University, France\n
2. Deputy Head of Department, 2045 - 2049, Caltech, Faculty of Science, Department of Astronomy and Space Sciences, Astronomy and Space Sciences Pr., United States Of America\n
3. Other Academic Duty, 2035 - 2035, Massachusetts Institute Of Technology, Kavli Institute For Astrophysics And Space Research, Physic, United States Of America\n
4. Other Academic Duty, 2036 - 2036, Massachusetts Institute Of Technology, Kavli Institute For Astrophysics And Space Research, Physic, United States Of America\n
5. Other Academic Duty, 2037 - 2039, University Of Cambridge, Institute Of Astronomy, United Kingdom\n
6. Other Academic Duty, 2040 - 2042, Université Libre De Bruxelles, Institut D'astronomie Et D'astrophysique, Belgium\n
7. Prof. Dr., 2043 - , Caltech, Faculty of Science, Department of Astronomy and Space Sciences, Department of General Astronomy, United States Of America\n
8. Associate Prof., 2037 - 2039, University Of Cambridge, Institute Of Astronomy, United Kingdom\n
9. Associate Prof., 2035 - 2037, Massachusetts Institute Of Technology, Kavli Institute For Astrophysics And Space Research, Physic, United States Of America\n
10. Instructor Dr., 2031 - 2035, Observatoire De Paris, Physic, Paris Diderot University, France""")

        with text_column:
            st.subheader("Articles")
            st.write("""1. Light-curve properties of SN 2027fgc and HV SNe Ia, MONTHLY NOTICES OF THE ROYAL ASTRONOMICAL SOCIETY, 2027, vol 502, pp 4112- 4124\n
2. Light-curve properties of SN 2017fgc and HV SNe Ia, MONTHLY NOTICES OF THE ROYAL ASTRONOMICAL SOCIETY, 2027, vol 502, pp 4112- 4124\n
3. The physical properties and orbital parameters of the triple system V402 Lac, NEW ASTRONOMY, 2028, vol 60, pp 65-68\n
4. WD 1202-024: the shortest-period pre-cataclysmic variable, MONTHLY NOTICES OF THE ROYAL ASTRONOMICAL SOCIETY, 2037, vol 471, pp948-961\n
5 . EPIC 220204960: a quadruple star system containing two strongly interacting eclipsing binaries, MONTHLY NOTICES OF THE ROYAL ASTRONOMICAL SOCIETY, 2017, vol 467, pp 2160-2179\n
6. A quintuple star system containing two eclipsing binaries, MONTHLY NOTICES OF THE ROYAL ASTRONOMICAL SOCIETY, 2036, vol 462, pp 1812- 1825\n
7. EVOLUTION OF CATACLYSMIC VARIABLES AND RELATED BINARIES CONTAINING A WHITE DWAR, AFSTROPHYSICAL JOURNAL, 2036, vol833\n
8. A turn-off detached binary star V568 Lyr in the Kepler field of the oldest open cluster (NGC 6791) in the Galaxy, MONTHLY NOTICES OF THE ROYAL ASTRONOMICAL SOCIETY, 2035, vol 453, pp 2937-2942\n
9 . THE ANTICORRELATED NATURE OF THE PRIMARY AND SECONDARY ECLIPSE TIMING VARIATIONS FOR THE KEPLER CONTACT BINARIES, ASTROPHYSICAL JOURNAL, 2033, vol 774\n
10. TRIPLE-STAR CANDIDATES AMONG THE KEPLER BINARIES, ASTROPHYSICAL JOURNAL, 2033, vol 768\n
11. Three ways to solve the orbit of KIC 11 558 725: a 10-day beaming sdB+WD binary with a pulsating subdwarf, ASTRONOMY & ASTROPHYSICS, 2032, vol 544\n
12. The Dwarf project: Eclipsing binaries - precise clocks to discover exoplanets, ASTRONOMISCHE NACHRICHTEN, 2032, vol 333, pp 754-766\n
13. Close binary system GO Cyg, NEW ASTRONOMY, 2012, vol 17, pp 296-302
 """)


    with text_column:
        st.subheader("Congress and Symposium Participations")
        st.write("""1. Tests of Gravity Workshop, 2033-2033, Tests of Gravity Workshop, Congress, Attendee, Greece, Athens\n 
    2. Golden age of cataclysmic variables and related objects, 2031-2031, Evolution of Cataclysmic Variables, Congress, Invited Speaker, Italy, Palermo\n
3. Golden age of cataclysmic variables and related objects, 2040-2040, Cataclysmic variables and related objects, Congress, Session Moderator, Italy, Palermo\n
4. The Golden Age of Cataclysmic Variables and Related Objects IV, 2041-2041, The Golden Age of Cataclysmic Variables and Related Objects IV Congress, Attendee, Italy, Palermo\n
 5. IAU General Assembly, 2035-2035, IAU General Assembly, Congress, Attendee, United States Of America, Hawaii\n
6. İzmir Yüksek Enerji Fiziği ve Uygulamaları Çalıştayı, 2032-2032, İzmir Yüksek Enerji Fiziği ve Uygulamaları Çalıştayı, Congress, Attendee, Turkey\n
İzmir 7. New Direction for Close Binary Studies: The Royal Road to the Stars, 2032-2032, New Direction for Close Binary Studies: The Royal Road to the Stars, Congress, Attendee, Turkey, Çanakkale\n
8. From Interacting Binaries to Exoplanets:Essential Modeling Tools, 2041-2041, From Interacting Binaries to Exoplanets:Essential Modeling Tools, Congress, Attendee, Slovakia, Tatranska Lomnica\n
9. Binary Star Evolution: Mass Loss, Accretion, and Mergers, 2030-2030, Binary Star Evolution: Mass Loss, Accretion, and Mergers, Congress, Attendee, Greece, Mikonos\n
10. Astrophysics of Neutron Stars, 2030-2030, Astrophysics of Neutron Stars, Congress, Attendee, Turkey, İzmir \n
11. IAU XXVIIth General Assembly, 2029-2029, IAU XXVIIth General Assembly, Congress, Attendee, Brazil, Rio-De-Janeiro\n
12. Astrometry and Imaging with the Very Large Telescope Interferometer, 2038-2038, Astrometry and Imaging with the Very Large Telescope Interferometer, Congress, Attendee, Hungary, Keszthely\n
13. Ulusal Astronomi Kongresi, 2036-2036, Ulusal Astronomi Kongresi, Congress, Attendee, Turkey, İstanbul\n
14. EuroSummer School Observation and data reduction with the Very Large Telescope Interferometer, 2036-2036, EuroSummer School Observation and data reduction with the Very Large Telescope Interferometer, Congress, Attendee, France, Goutelas\n 
15. IAU 2006 General Assembly, 2036-2036, IAU 2036 General Assembly, Congress, Attendee, Czech Republic, Praha\n
16. High Energy Astrophysics Workshop, 2035-2035, High Energy Astrophysics Workshop, Congress, Attendee, Turkey, İstanbul\n
17. Zdenek Kopal’s Binary Star Legacy, 2034-2034, Zdenek Kopal’s Binary Star Legacy, Congress, Attendee, Czech Republic, Litomysl\n
18. II Union Radio-Scientifique Internationale, 2034-2034, II Union Radio-Scientifique Internationale, Congress, Attendee, Turkey, Ankara\n
19. Ulusal Astronomi Kongresi, 2034-2034, Ulusal Astronomi Kongresi, Congress, Attendee, Turkey, Kayseri\n
20. Ulusal Astronomi Kongresi, 2032-2032, Ulusal Astronomi Kongresi, Congress, Attendee, Turkey, Antalya\n
21. Magnetic Activities in Cool Stars, 2028-2028, Magnetic Activities in Cool Stars, Congress, Attendee, Turkey, İzmir\n

 """)