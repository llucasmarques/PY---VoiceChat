/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package chat.networking;

import java.io.IOException;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Lucas Marques
 */
public class TransmissorMensagem extends Thread{
    
    String mensagem, hostname;
    int porta;
    
    //Construtores
    public TransmissorMensagem(){
    
    }
    public TransmissorMensagem(String mensagem, String hostname, int porta){
        this.porta = porta;
        this.hostname = hostname;
        this.mensagem = mensagem;
    }

    @Override
    public void run() { //Conecta e desconecta 
        try {
        Socket s = new Socket(hostname, porta);
        s.getOutputStream().write(mensagem.getBytes());
        s.close();
        } catch (IOException ex) {
            Logger.getLogger(TransmissorMensagem.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    
}
