package util;

import java.util.Scanner;

public class HelloWorld {
	public void helloWorld() {
		System.out.println("Do you want to see an exception? Please answer y/n");
		try {
			Scanner sc = new Scanner(System.in);
			String option = sc.nextLine();
			sc.close();
		
			if(option.equals("Y") || option.equals("y")) {
				throw new RuntimeException();
			} else if (option.equals("N") || option.equals("n")) {
				System.out.println("Hello World!");
			} else {
				System.out.println("Invalid input!");
			}
		} catch (RuntimeException re) {
			re.printStackTrace();
		}
	}
}
