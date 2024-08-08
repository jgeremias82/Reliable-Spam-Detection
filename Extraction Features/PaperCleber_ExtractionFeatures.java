import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

import com.sun.xml.internal.bind.v2.runtime.unmarshaller.XsiNilLoader.Array;


public class ArtigoCleber4 {
	
	public static void main(String[] args) {
		
		ArtigoCleber4 ac4 = new ArtigoCleber4();
		ArrayList<CleberFeatures> listFeatures = ac4.lerArquivoFeatures("./selectionFeaturesHam/features.csv");
		
		ArrayList<String> listString = ac4.lerArquivo("./selectionFeaturesHam/2019_tf_ham.treina");
		//ArrayList<String> listString = ac4.lerArquivo("./selectionFeaturesHam/2019_tf_ham.testa_sem_comentario");
		
		for(int i = 0; i < listString.size(); i++){
			
			String str = listString.get(i).toString();
			String[] strList = str.split(" ");
			ac4.removeFeatures(i, strList, listFeatures);
		
		}
	}
	public void removeFeatures(int idInstancia,String[] instacia, ArrayList<CleberFeatures> listFeatures){
		
		boolean gravar = false;
		//String strInstancia = idInstancia+" "+instacia[0];
		String strInstancia = instacia[0];
		for(int i = 1; i < instacia.length; i++){
		
			String str = instacia[i];
			int pos = str.indexOf(":");
			String aux = str.substring(0, pos);
			
			int feature = Integer.parseInt(aux);
			
			for(int j = 0; j < listFeatures.size(); j++){
				
				if(feature == listFeatures.get(j).getIdFeature()){
					gravar = true;
					strInstancia = strInstancia+" "+str; 
				}
			}
		}
		
		if(gravar){
			System.out.println(strInstancia);
			gravar("./selectionFeaturesHam/train_HAM_Poda8.libsvm", strInstancia);
			gravar = false;
		}
		
	}
	
	public void gravar(String path, String str){
		
		try {
			
			FileWriter arq = new FileWriter(path,true);
			PrintWriter gravarArq = new PrintWriter(arq);
			gravarArq.println(str);
			arq.close();
			
		} catch (Exception e) {
			// TODO: handle exception
		}
		
	}
	
	public ArrayList<CleberFeatures> lerArquivoFeatures(String file){
		
		try {
			
			File arquivo = new File (file);
			String linhas = new String();
            Scanner scan = new Scanner(arquivo);
            
            ArrayList<CleberFeatures> listFeatures = new ArrayList<CleberFeatures>();
            
            while(scan.hasNext()){ 
            	
            	CleberFeatures features = new CleberFeatures();
            	linhas = scan.nextLine();
            	String aux[] = linhas.split(";");
            	
            	features.setIdFeature(Integer.parseInt(aux[0]));
            	features.setFeature(aux[1]);
            	features.setOccurrences(Integer.parseInt(aux[2]));
            	    	
            	listFeatures.add(features);
            }
            scan.close();
            System.out.println("Arraylist features criado!!");
            return listFeatures;
            
		} catch (FileNotFoundException ex) {
			
			System.out.println(ex);
		}
		return null;
		
	}
	
	public ArrayList<String> lerArquivo(String file){
		
		try {
			
			File arquivo = new File (file);
			String linhas = new String();
            Scanner scan = new Scanner(arquivo);
            
            ArrayList<String> listIntancias = new ArrayList<String>();
            
            while(scan.hasNext()){ 
            		
            	linhas = scan.nextLine();
            	listIntancias.add(linhas);
            }
            
            scan.close();
            System.out.println("Arraylist instancias criado!!");
            return listIntancias;
            
		} catch (FileNotFoundException ex) {
			
			System.out.println(ex);
		}
		return null;
		
	}
}