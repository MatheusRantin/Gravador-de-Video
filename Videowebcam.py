import cv2




class Gravacao:

    def __init__ (self, nomeVideo, formatoVideo, formatoExtensao):
        self.nomeVideo = nomeVideo
        self.formatoVideo = formatoVideo
        self.formatoExtensao = formatoExtensao

    def chamarCamera(self):

        
    #Abrindo camera padrão
        cap = cv2.VideoCapture(0)

        #Definindo codec e criando o objeto video

        fourcc = cv2.VideoWriter_fourcc(*f'{self.formatoVideo}')
        out = cv2.VideoWriter(f'{self.nomeVideo}.{self.formatoExtensao}', fourcc, 20.0, (640, 480))

        while cap.isOpened():
        #Capturando quadro a quadro
            ret, frame = cap.read()

            if ret == True:
                frame = cv2.flip(frame, 0)

                out.write(frame)
                cv2.imshow('Camera de Gravacao', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                     break
            
                
            
        cap.release()
        out.release()
        cv2.destroyAllWindows()

       



if __name__ == "__main__":
    while True:
            print("SISTEMA DE CAMERA")
            selecao_de_opcao = int(input("1- Para ativar a camera;\n2-Para sair da camera\n"))
            
            #Escolhendo nome do arquivo 
            if selecao_de_opcao == 1:
                nomeVideo = input("Escreve um nome para o video que será salvo apos gravacao:\n")
                formatoVideo = int(input("Escolha o formato do video que deseja: \n1- avi \n2- mp4\n"))
            #Determinando formato do video 
                if formatoVideo == 1:
                        formatoVideo = 'XVID'
                        formatoExtensao = 'avi'
                        
                elif formatoVideo == 2:
                    formatoVideo = 'MP4V'
                    formatoExtensao = 'mp4'  
                    
                gravacao = Gravacao(nomeVideo, formatoVideo, formatoExtensao)
                print("Gravando ...")
                gravacao.chamarCamera()
                print("Fim da Gravacao")
                



            
            elif selecao_de_opcao ==2:
                print("Programa Finalizado")
            break
