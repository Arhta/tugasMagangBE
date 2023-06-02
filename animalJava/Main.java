package tugasMagangBE.animalJava;
/*
1. Lengkapi lah source code di atas
2. Buatlah kelas turunan `Animal` dengan nama`Chicken` yang memiliki 
atribut `name`, `legs`, dan `age` serta buatlah function dengan nama `walk` 
dan `eat` yang memiliki fungsi untuk mengirimkan sebuah string ke console. */

class Animal {
    private String name;
    private int legs;
    private int age;

    // Construct
    public Animal(String name, int legs, int age) {
        this.name = name;
        this.legs = legs;
        this.age = age;
        
    }
    // Setters
    public void setName(String name){
        this.name = name;
    }
    public void setLegs(int legs){
        this.legs = legs;
    }
    public void setAge(int age){
        this.age = age;
    }

    // Getters
    public String getName(){
        return this.name;
    }
    public int getLegs(){
        return this.legs;
    }
    public int getAge(){
        return this.age;
    }

}

class Chicken extends Animal{
    public Chicken(String name, int leg, int age){
        super(name, leg, age);
    }

    public void walk() {
        System.out.println("walking");
    }

    public void eat() {
        System.out.println("eating");
    }

} 

public class Main {
    public static void main(String[] args) {
        Chicken chicken = new Chicken("Chicken", 4, 10);
        
        System.out.println(chicken.getName());  // Output: "Chicken"
        System.out.println(chicken.getLegs());  // Output: 4
        System.out.println(chicken.getAge());  // Output: 10

        // Set animal's second attribute from 4 to 2
        chicken.setLegs(2);
        System.out.println("Animal: " + chicken.getName() + " Have " + chicken.getLegs() + " Legs");  // Output: "Animal: Chicken Have 2 Legs"

        chicken.walk();
        chicken.eat();
    }
}
