/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package chat.networking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Lucas Marques
 */
public class Message extends Thread{
    
    ServerSocket server;
    int porta = 8989;
    GUIEscrevivel gui;
    
    //Construtor
    public Message(GUIEscrevivel gui, int porta){
        this.porta = porta;
        this.gui = gui;
        try {
            server = new ServerSocket(porta);

        } catch (IOException ex) {
            Logger.getLogger(Message.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public Message(){
        try {
            server = new ServerSocket(porta);
        } catch (IOException ex) {
            Logger.getLogger(Message.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }

    @Override
    public void run() {
        Socket clientSocket; //Inicializa uma varial chamada ClientSocket
        try {
            while((clientSocket = server.accept()) != null){ //Continua aceitando conexao com o servidor
                InputStream is = clientSocket.getInputStream();
                BufferedReader br = new BufferedReader(new InputStreamReader(is));
                String line = br.readLine();
                if(line != null){
                    gui.escrever(line);
                }
                
            }
        } catch (IOException ex) {
            Logger.getLogger(Message.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    
}
