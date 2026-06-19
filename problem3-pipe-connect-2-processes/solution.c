#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

// Программе передаётся два аргумента: CMD1 и CMD2.
// Необходимо запустить два процесса, выполняющих эти команды,
// и перенаправить стандартный поток вывода CMD1 на стандартный поток ввода CMD2.
// Эквивалентно: CMD1 | CMD2
// Родительский процесс должен завершаться самым последним.

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <CMD1> <CMD2>\n", argv[0]);
        return 1;
    }

    // TODO: создайте канал (pipe),
    //       запустите CMD1 (argv[1]) так, чтобы его stdout → write-конец канала,
    //       запустите CMD2 (argv[2]) так, чтобы его stdin  ← read-конец канала,
    //       дождитесь завершения обоих дочерних процессов.

    return 0;
}
