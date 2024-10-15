#Lenguaje 1: Python

import numpy as np

# Selecciona el conjunto de datos
conjunto = [2, 3, 4, 5, 6]

# Calcular la mediana
media = np.median(conjunto)
ds = (np.median([x for x in conjunto if x > media]) - media) / 2

print(f"Media: {media}")
print(f"Ds: {ds}")

#Lenguaje 2: C++

#include <iostream>
#include <vector>

// Selecciona el conjunto de datos
std::vector<int> conjunto = {2, 3, 4, 5, 6};

int main() {
    // Calcular la mediana
    int media = std::accumulate(conjunto.begin(), conjunto.end(), 0) / conjunto.size();
    double ds = (std::accumulate(std::begin(conjunto), std::end(conjunto),
                                    std::numeric_limits<double>::max()) -
                media) / 2.0;

    // Imprime la mediana y la desviación estándar
    std::cout << "Media: " << media << std::endl;
    std::cout << "Ds: " << ds << std::endl;

    return 0;
}


#Lenguaje 3: Java

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Selecciona el conjunto de datos
        int[] conjunto = {2, 3, 4, 5, 6};

        // Calcular la mediana
        double media = Arrays.stream(conjunto).reduce(0.0, (a, b) -> a + b);

        // Desviación estándar calculada con d.s. simple
        double ds_simple = (conjunto[3] - media) / 2;

        // Imprime la mediana y la desviación estándar
        System.out.println("Media: " + media);
        System.out.println("Ds_simple: " + ds_simple);

        return;
    }
}

#Lenguaje 4: C#

using System;

class Program {
    static void Main() {
        // Selecciona el conjunto de datos
        int[] conjunto = {2, 3, 4, 5, 6};

        // Calcular la mediana
        double media = CalculateMedia(conjunto);

        // Desviación estándar calculada con d.s. simple
        double ds_simple = (conjunto[3] - media) / 2;

        Console.WriteLine("Media: " + media);
        Console.WriteLine("Ds_simple: " + ds_simple);

        return;
    }

    static double CalculateMedia(int[] conjunto) {
        int n = conjunto.Length;
        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += conjunto[i];
        }
        return sum / n;
    }
}

#Lenguaje 5: Ruby

# Selecciona el conjunto de datos
conjunto = [2, 3, 4, 5, 6]

# Calcular la mediana
media = conjunto.sort!.average

# Desviación estándar calculada con d.s. simple
ds_simple = (conjunto[3] - media).abs / 2

puts "Media: #{media}"
puts "Ds_simple: #{ds_simple}"

#Lenguaje 6: R
# Selecciona el conjunto de datos
conjunto <- c(2, 3, 4, 5, 6)

# Calcular la mediana
media <- median(conjunto)

# Desviación estándar calculada con d.s. simple
ds_simple <- (max(conjunto) - media) / 2

print(paste("Media: ", media))
print(paste("Ds_simple: ", ds_simple))


#Lenguaje 7: Swift
import Foundation

// Selecciona el conjunto de datos
let conjunto = [2, 3, 4, 5, 6]

// Calcular la mediana
let media: Double = conjunto.reduce(0, +) / conjunto.count

// Desviación estándar calculada con d.s. simple
let ds_simple = (conjunto[3] - media).abs / 2

print("Media: \(media)")
print("Ds_simple: \(ds_simple)")


#Lenguaje 8: JavaScript
// Selecciona el conjunto de datos
const conjunto = [2, 3, 4, 5, 6];

// Calcular la mediana
let media = (conjunto.reduce((acc, val) => acc + val, 0) / conjunto.length);

// Desviación estándar calculada con d.s. simple
let ds_simple = Math.abs(conjunto[3] - media) / 2;

console.log(`Media: ${media}`);
console.log(`Ds_simple: ${ds_simple}`);

return;



#Lenguaje 9: Go
package main

import (
	"fmt"
)

func main() {
	// Selecciona el conjunto de datos
	conjunto := []int{2, 3, 4, 5, 6}

	// Calcular la mediana
	media := CalculateMedian(conjunto)
	dsSimple := (MathMax(conjunto[3], media)) / 2

	fmt.Println("Media:", media)
	fmt.Println("Ds_simple:", dsSimple)

	return
}

func CalculateMedian(conjunto []int) float64 {
	n := len(conjunto)
	if n == 0 {
		return 0.0
	}
	sort.Ints(conjunto)
	mid := n / 2
	return float64(conjunto[mid])
}

func MathMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}


#Lenguaje 10: Kotlin

import java.util.*

// Selecciona el conjunto de datos
val conjunto = intArrayOf(2, 3, 4, 5, 6)

// Calcular la mediana
fun calculateMedian(conjunto: IntArray): Double {
    val n = conjunto.size
    if (n == 0) {
        return 0.0
    }
    val sortedConjunto = conjunto.sorted()
    val mid : Int = n / 2
    return sortedConjunto[mid]
}

// Desviación estándar calculada con d.s. simple
fun calculateDsSimple(conjunto: IntArray): Double {
    var dsSimple = 0.0
    for (i in conjunto.indices) {
        val value = conjunto[i]
        if (value > calculateMedian(conjunto)) {
            dsSimple += (value - calculateMedian(conjunto))
        }
    }
    return dsSimple / n
}

fun main() {
    println("Media: ${calculateMedian(conjunto)}")
    println("Ds_simple: $calculateDsSimple(conjunto)")
}
