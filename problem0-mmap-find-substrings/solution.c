#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>

// Программе передаются два аргумента: имя файла и строка для поиска.
// Необходимо найти все вхождения строки в текстовом файле,
// используя отображение на память с помощью системного вызова mmap.
// На стандартный поток вывода вывести список всех позиций (с нуля),
// где встречается искомая строка, по одной на строку.

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <filename> <search_string>\n", argv[0]);
        return 1;
    }

    const char *filename = argv[1];
    const char *pattern  = argv[2];
    size_t pat_len = strlen(pattern);

    int fd = open(filename, O_RDONLY);
    if (fd < 0) {
        perror("open");
        return 1;
    }

    struct stat st;
    if (fstat(fd, &st) < 0) {
        perror("fstat");
        close(fd);
        return 1;
    }
    size_t file_size = (size_t)st.st_size;

    if (file_size == 0 || pat_len > file_size) {
        close(fd);
        return 0;
    }

    char *data = mmap(NULL, file_size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (data == MAP_FAILED) {
        perror("mmap");
        close(fd);
        return 1;
    }

    char *ptr = data;
    while (ptr <= data + file_size - pat_len) {
        char *found = memmem(ptr, (size_t)(data + file_size - ptr), pattern, pat_len);
        if (found == NULL) break;
        printf("%ld\n", (long)(found - data));
        ptr = found + 1;
    }

    munmap(data, file_size);
    close(fd);

    return 0;
}
