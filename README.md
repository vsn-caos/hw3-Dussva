# ДЗ 3 — POSIX: mmap, fork, exec, pipe, sockets

## Задания

| Директория | Задача | Описание |
|---|---|---|
| `problem0-mmap-find-substrings` | posix/mmap/find-substrings-in-file | Найти все вхождения строки в файле через `mmap` |
| `problem1-fork-proc-print-numbers` | posix/fork/proc-print-numbers | Вывести числа 1..N через цепочку из N процессов |
| `problem2-exec-exec-python` | posix/exec/exec-python | Вычислить Python-выражение из stdin через `exec` |
| `problem3-pipe-connect-2-processes` | posix/pipe/connect-2-processes | Реализовать `CMD1 \| CMD2` |
| `problem4-sockets-tcp-client` | posix/sockets/tcp-client | TCP-клиент с бинарным int32 LE протоколом |

---

## Формат решения

В каждой директории находится файл **`solution.c`** — именно в нём нужно писать решение.

---

## Сборка и запуск локально

Требования: `gcc`, `make`, `python3` (для тестов задачи 4).

```bash
# Сборка и тестирование одной задачи
cd problem0-mmap-find-substrings
make          # собрать
make test     # прогнать тест-кейсы
make clean    # удалить бинарник
```

Запустить все задачи сразу:

```bash
for d in problem*/; do make -C "$d" test; done
```

---

## Подсказки

| Задача | Системные вызовы / функции |
|---|---|
| 0 | `open`, `fstat`, `mmap`, `munmap`, `close` |
| 1 | `fork`, `wait`/`waitpid`, `getpid` |
| 2 | `read`/`fgets`, `execvp` (или `execlp`) |
| 3 | `pipe`, `fork`, `dup2`, `execvp`, `waitpid` |
| 4 | `socket`, `connect`, `send`, `recv`, `inet_aton`/`inet_pton` |

