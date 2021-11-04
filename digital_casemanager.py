'''
Run Befehl ist:
streamlit run "C:/Users/Paul Wunderlich/PycharmProjects/Digitaler_Casemanager/digital_casemanager.py"

##################################
# Markdown Template:
st.markdown("* **Modul:**  Text")
##################################
# Alternative page_names
page_names = ["Einleitung",
              "Mobilität",
              "Kognitive und kommunikative Fähigkeiten",
              "Verhaltensweisen und psychische Problemlagen",
              "Selbstversorgung",
              "Umgang mit krankheits- oder therapiebedingten Anforderungen",
              "Gestaltung des Alltagslebens und sozialer Kontakte",
              "Gestaltung der Betreuung",
              "Analyse und Weitere Schritte"]

'''
# Libaries
import streamlit as st
import pandas as pd
import pickle

####################################################################################################
# Predefine variables
page_names = ["Einleitung",
              "Modul 1",
              "Modul 2",
              "Modul 3",
              "Modul 4",
              "Modul 5",
              "Modul 6",
              "Modul 7",
              "Analyse und Weitere Schritte"]

questions = ["Positionswechsel im Bett (bspw. Drehen und Wenden im Bett)",
              "Halten in der Sitzposition",
              "Aufstehen aus dem Sitz",
              "Umsetzen vom Bett bspw. in den Rollstuhl",
              "Sich innerhalb der Wohnung bewegen",
              "Sich außerhalb der Wohnung bewegen",
              "Treppensteigen",
              "Erkennen von vertrauten Personen",
              "Wissen von Uhrzeit und Datum",
              "Erinnerung an vergangene  Ereignisse (bspw. Familienfeiern, Reisen)",
              "Können Gefahren eingeschätzt werden (Herd ausgeschaltet?)",
              "Mitteilung von Bedürfnissen (bspw. Hunger oder Durst)",
              "Beteiligung an Gesprächen",
              "Verstehen von Aufforderungen",
              "Aggressives oder abwehrendes Verhalten",
              "Antriebslosigkeit",
              "Ängste",
              "traurige Stimmungslage",
              "Kämmen, Rasieren, Zähneputzen",
              "Waschen, Baden, Duschen",
              "An- und Auskleiden",
              "Toilettengang",
              "Essen zerkleinern, Flaschen öffnen",
              "Essen, Trinken",
              "Zubereitung von Mahlzeiten",
              "Einkaufen",
              "Reinigung von Wohnung od. Haus",
              "Instandhaltung von Wohnung od. Haus",
              "Gartenpflege",
              "Bereitstellung und/ oder Gabe von Medikamenten",
              "Anziehen von Kompressionsstrümpfen",
              "Gabe von Spritzen",
              "Verbandwechsel/ Wundversorgung",
              "Physiotherapeutische Übungen",
              "Arztbesuche oder Besuch anderer medizinischer Einrichtungen",
              "Einhaltung einer Diät",
              "Messung von Blutdruck-oder Blutzuckerwerten ect.",
              "Eigene Beschäftigung (bspw. Lesen, Musik hören)",
              "Gestaltung des Tagesrhythmus (z.B. Frühstück, Mittag- und Abendessen)",
              "Organisation von Aktivitäten (Spaziergang/-fahrt mit Bekannten/ Verwandten)",
              "Eigene Interaktion mit anderen Personen (z.B. persönliches Gespräch, Telefonat, WhatsApp, E-Mail)",
              "Ehe- od. Lebenspartner",
              "Eltern od. Kinder",
              "Nahe Angehörige wie bspw. Geschwister od. Nichte/Neffe",
              "Bekannte od. Freunde",
              "Nachbarn od. ehrenamtliche Personen",
              "Professionelle Dienstleister wie bspw. ambulanter Pflegedienst od. stationäre Pflegeeinrichtung"]

answers_a = ["Ohne fremde Hilfe möglich",
             "Etwas fremde Hilfe nötig",
             "Überwiegend fremde Hilfe nötig",
             "Komplett fremde Hilfe nötig",
             "Nicht erforderlich"]

answers_b = ["Immer",
             "Häufig",
             "Selten",
             "Nie"]

answers_c = ["Keine Auffälligkeiten",
             "Leichte Auffälligkeiten",
             "Mäßige Auffälligkeiten",
             "Schwere Auffälligkeiten"]

answers_d = ["Ja",
             "Nein"]

answers_modul_1 = [answers_a, answers_a, answers_a, answers_a, answers_a, answers_a, answers_a]
answers_modul_2 = [answers_b, answers_b, answers_b, answers_b, answers_b, answers_b, answers_b]
answers_modul_3 = [answers_c, answers_c, answers_c, answers_c]
answers_modul_4 = [answers_a, answers_a, answers_a, answers_a, answers_a, answers_a, answers_a, answers_a, answers_a, answers_a, answers_a]
answers_modul_5 = [answers_a, answers_a, answers_a, answers_a, answers_a, answers_a, answers_a, answers_a]
answers_modul_6 = [answers_b, answers_b, answers_b, answers_b]
answers_modul_7 = [answers_d, answers_d, answers_d, answers_d, answers_d, answers_d]

# Initialze further steps
further_steps = ["Altersgerechtes Wohnen zu Hause", "Ambulante Pflege", "Arzt", "Betreuung & Begleitung", "Einkauf",
                 "Ergotherapie", "Ernährung", "Haushaltshilfe", "Hilfsmittel", "Logopädie", "Medikamente",
                 "Mobilität & Bewegung", "Physiotherapie", "Psychotherapie", "Selbsthilfe & Unterstützungsangebote",
                 "Stationäre Pflege"]

####################################################################################################

# Logos
col1, col2 = st.columns(2)
col1.image("Digitaler_Casemanager/images/Logo init 2021.png", width=256)
col2.image("Digitaler_Casemanager/images/Logo work_care.png", width=256)

# Einleitung
st.title("Digitaler Casemanager")
st.markdown("### Einleitung")
st.markdown("Wir möchten mit dem digitalen Case Manager eine erste Anlaufstelle für Menschen mit Informationsbedarf "
            "im Bereich Pflege bieten und auch für diejenigen einen einfachen Zugang zu situationsbezogenen Informationen schaffen,"
            " die keinen Pflegestützpunkt oder eine sonstige Beratungsstelle in ihrer Nähe haben. Unser Anliegen ist es, pflegebedürftige "
            "Menschen und ihre Angehörigen schnell und bequem mit dem Wissen zu versorgen, was sie in ihrer Situation brauchen. "
            "Unser Datenintelligenz-gestützter digitale Case Manager ist kostenlos und rund um die Uhr nutzbar. "
            "So funktioniert unser digitaler Case Manager Unser digitaler Case Manager funktioniert schnell und unkompliziert: "
            "Sie beantworten Fragen zu Ihrem Gesundheitszustand und zu Ihrem Unterstützungsbedarf via Mausklick, um Ihre Pflegesituation zu erfassen. "
            )

explanation = st.expander("Erläuterung zu den Modulen")
with explanation:
    st.markdown("Die Fragestellungen sind in folgende sieben Module unterteilt: ")
    st.markdown("* **Modul 1 „Mobilität“:**  Hier finden Sie Fragen nach der Inanspruchnahme von fremder Hilfe wie "
                    "beispielsweise beim Aufstehen oder Treppensteigen.")
    st.markdown("* **Modul 2 „Kognitive und kommunikative Fähigkeiten“:**  In diesem Modul werden Fragen nach "
                    "geistigen Beeinträchtigungen gestellt wie etwa: Kann sich die zupflegende Person mitteilen?")
    st.markdown("* **Modul 3 „Verhaltensweisen und psychische Problemlagen“:** In diesem Modul werden Fragen bezüglich "
                    "aggressiven Verhaltens, zu Ängsten oder traurigen Stimmungslagen des Betroffenen gestellt.")
    st.markdown("* **Modul 4 „Selbstversorgung“:** Dieses Modul beinhaltet Fragestellungen hinsichtlich der "
                    "Körperpflege und der Haushaltsführung.")
    st.markdown("* **Modul 5 „Umgang mit krankheits- oder therapiebedingten Anforderungen“:** Hier finden Sie Fragen, "
                    "ob Ihr Angehöriger selbständig Medikamente einnehmen oder Blutzucker messen kann.")
    st.markdown("* **Modul 6 „Gestaltung des Alltagslebens und sozialer Kontakte“:** In diesem Modul liegt "
                "der Schwerpunkt auf der Frage, ob die zu pflegende Person ihren Alltag selbständig planen und mit "
                "anderen Menschen in Kontakt treten kann.")
    st.markdown("* **Modul 7 „Gestaltung der Betreuung“:** Im letzten Modul werden Sie danach gefragt, welche Personen"
                " die zu pflegende Person unterstützen oder betreuen.")

st.markdown("Nach der Beantwortung aller Fragen erhalten Sie passende Empfehlungen für die weitere Versorgung "
            "und/ oder mögliche nächste Pflegeschritte mit Hinweisen auf "
            "Pflege- und Gesundheitseinrichtungen und –dienstleistern, Pflegehilfsmitteln "
            "und barrierefreien Wohnangeboten sowie jede Menge Informationen, die Ihre Situation betreffen.")

######################################
# Modul 1
modul_1 = st.expander("Modul 1: Mobilität", expanded=False)
with modul_1:
    # Questions for Modul 1
    m1 = []
    for i, question in enumerate(questions[0:7]):
        m1.append([st.radio(f"{i+1}. {question}:", answers_modul_1[i])])

######################################
# Modul 2
modul_2 = st.expander("Modul 2: Kognitive und kommunikative Fähigkeiten", expanded=False)
with modul_2:
    # Questions for Modul 2
    m2 = []
    for i, question in enumerate(questions[7:14]):
        m2.append([st.radio(f"{i+7+1}. {question}:", answers_modul_2[i])])

######################################
# Modul 3
modul_3 = st.expander("Modul 3: Verhaltensweisen und psychische Problemlagen", expanded=False)
with modul_3:
    # Questions for Modul 3
    m3 = []
    for i, question in enumerate(questions[14:18]):
        m3.append([st.radio(f"{i+14+1}. {question}:", answers_modul_3[i])])

######################################
# Modul 4
modul_4 = st.expander("Modul 4: Selbstversorgung", expanded=False)
with modul_4:
    # Questions for Modul 4
    m4 = []
    for i, question in enumerate(questions[18:29]):
        m4.append([st.radio(f"{i+18+1}. {question}:", answers_modul_4[i])])

######################################
# Modul 5
modul_5 = st.expander("Modul 5: Umgang mit krankheits- oder therapiebedingten Anforderungen", expanded=False)
with modul_5:
    # Questions for Modul 5
    m5 = []
    for i, question in enumerate(questions[29:37]):
        m5.append([st.radio(f"{i+29+1}. {question}:", answers_modul_5[i])])

######################################
# Modul 6
modul_6 = st.expander("Modul 6: Gestaltung des Alltagslebens und sozialer Kontakte", expanded=False)
with modul_6:
    # Questions for Modul 6
    m6 = []
    for i, question in enumerate(questions[37:41]):
        m6.append([st.radio(f"{i+37+1}. {question}:", answers_modul_6[i])])

######################################
# Modul 7
modul_7 = st.expander("Modul 7: Gestaltung der Betreuung", expanded=False)
with modul_7:
    # Questions for Modul 7
    m7 = []
    for i, question in enumerate(questions[41:47]):
        m7.append([st.radio(f"{i+41+1}. {question}:", answers_modul_7[i])])

######################################
# Weitere Schritte
st.title(page_names[8])
st.markdown('Durch das Klicken auf "Starte Analyse" beginnen starten Sie den Digitalen Case Manager.')
start_inference = st.button("Starte Analyse")

# Inferenz
if start_inference:
    antworten = m1 + m2 + m3 + m4 + m5 + m6 + m7

    # Erstellung eines dictionaries aus zwei Listen -> data=Liste von Listen
    dict_data = dict(zip(questions, antworten))

    answers = pd.DataFrame.from_dict(dict_data)

    # Antworten in Zahlen umwandeln
    vals_to_replace = {"Ohne fremde Hilfe möglich": 1, "Etwas fremde Hilfe nötig": 2,
                       "Überwiegend fremde Hilfe nötig": 3,
                       "Komplett fremde Hilfe nötig": 4, "Nicht erforderlich": 0,
                       "Immer": 1, "Häufig": 2, "Selten": 3, "Nie": 4,
                       "Keine Auffälligkeiten": 1, "Leichte Auffälligkeiten": 2, "Mäßige Auffälligkeiten": 3,
                       "Schwere Auffälligkeiten": 4,
                       "Ja": 1, "Nein": 2}
    for column in answers:
        answers[column] = answers[column].map(vals_to_replace)

    # Laden des gelernten Vorhersagemodells
    filename = './models/multi-label-classif_v2.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    # Inference
    prediction = loaded_model.predict(answers)

    # Umwandeln der Vorhersage in Text
    for column in range(len(prediction)):
        indices = [index for index, element in enumerate(prediction[column]) if element == 1]
        pred_steps = []
        for i in indices:
            pred_steps.append(further_steps[i])

        st.subheader("Weitere Pflegeschritte")
        for step in pred_steps:
            st.markdown(f"* {step}")
