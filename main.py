from jaraco import clipboard
from bs4 import BeautifulSoup
from tkinter import filedialog
import pickle
import difflib


def open_file():
    file = filedialog.askopenfile(initialdir = "/", title = "Select file").name
    return file

def recopilar():
    input_type = input("""
Elegir modo de recopilación de datos:
1. Copiar del portapapeles
2. Copiar html desde un archivo\n
""")



    if input_type == '1':
        html = clipboard.paste_html()
    elif input_type == '2':
        with open(open_file(), "r") as f:
            html = f.read()

    print(html)
    soup = BeautifulSoup(str(html),"html.parser")

    questions = soup.find_all('div', class_='Question')
    print(questions)
    with open("ans.pkl", "rb") as f:
        ans = pickle.load(f)

    for i in questions:
        print(len(ans))
        question = {}
        q = BeautifulSoup(str(i),"html.parser")
        name = q.find(class_='Question-item').getText()

        exists = False
        for x in ans:
            if x['name'] == name:
                exists = True

        if not exists:
            question['name'] = name
            if q.find(class_='Question-result--correct') is not None:
                text = q.find(class_='Question-result--correct').getText()
                text = text.replace('\n', '')
                question['correct'] = text
            else:
                question['correct'] = ''

            if q.find(class_='Question-result--incorrect') is not None:
                text = q.find(class_='Question-result--incorrect').getText()
                text = text.replace('\n', '')
                question['incorrect'] = [text.replace('REPASAR CLASE', '')]
            else:
                question['incorrect'] = []
            ans.append(question)
            print(f'Se ha añadido: \n{question}')
            print(f'\n La cosa queda asi:{ans}')
        else:
            for x in ans:
                if x['name'] == name:
                    if q.find(class_="Question-result--correct") is not None:
                        text = q.find(class_='Question-result--correct').getText()
                        text = text.replace('\n', '')
                        if x['correct'] != text:
                            x['correct'] = text

                    if q.find(class_='Question-result--incorrect') is not None:
                        text = q.find(class_='Question-result--incorrect').getText()
                        text = text.replace('\n', '')
                        if text not in x['incorrect']:
                            new = x['incorrect'].append(text.replace('REPASAR CLASE', ''))
                            x['incorrect'] = new
        #print(question)

        print(f'\n\n\n{ans}')

    with open("ans.pkl", "wb") as f:
        pickle.dump(ans, f)


def consultar():
    control = True
    while control:
        query = input("Pregunta: ")

        with open("ans.pkl", "rb") as f:
            ans = pickle.load(f)
        counter = 0
        for x in ans:
            counter = counter + 1
            matcher = difflib.SequenceMatcher(None, x['name'], query)
            if matcher.ratio() > 0.9:
                print("Se ha encontrado en la db:")
                print(f"\t {x['name']}")
                print(f"\t Correcto: {x['correct']}")
                print(f"\t Incorrecto: {x['incorrect']}")
        if counter > 0:
            print("No se ha encontrado nada similar en la db")





def consulta_masiva():
    with open("ans.pkl","rb") as f:
        ans = pickle.load(f)

    for i in ans:
        if len(i['incorrect']) > 0 and i['correct'] != '':
            print(i, end="\n\n")

    print(f'Se han encontrado {len(ans)}')

def main():
    input_type = input("""
Que quieres hacer:
1. Recopilar datos
2. Consultar datos
3. Consulta Masiva
4. (DEV) Vaciar db
""")


    if input_type == '1':
        recopilar()
    elif input_type == '2':
        consultar()
    elif input_type == '3':
        consulta_masiva()
    elif input_type == '4':
        with open("ans.pkl", "wb") as f:
            pickle.dump([], f)



if __name__ == "__main__":
    main()