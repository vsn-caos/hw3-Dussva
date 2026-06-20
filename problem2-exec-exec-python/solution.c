#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
// Программе на стандартный поток ввода задается арифметическое выражение
// в синтаксисе языка python3. Необходимо вычислить это выражение и вывести результат.
// Использовать дополнительные процессы запрещено — нужно использовать exec.
int main(void) {
    char expr[4096];
    if (fgets(expr, sizeof(expr), stdin) == NULL) {
        return 1;
    }

    size_t len = strlen(expr);
    if (len > 0 && expr[len - 1] == '\n') {
        expr[len - 1] = '\0';
    }

    char cmd[4096 + 32];
    snprintf(cmd, sizeof(cmd), "print(%s)", expr);

    char *args[] = { "python3", "-c", cmd, NULL };
    execvp("python3", args);

    perror("execvp");
    return 1;
}
