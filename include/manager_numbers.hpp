#pragma once
#include <fstream>
#include <iostream>
#include<random>
#include <string>
#include <vector>

// Cabecalho do gen_data
void gen_data(int n, std::string &save_dir);

// ler os dados gerados
void read_data(std::vector<int> &numbers, std::string &save_dir, int size, int interval);

void write_results(std::vector<int> &numbers, std::string &save_path);