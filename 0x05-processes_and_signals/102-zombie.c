#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


/**
 * whileinf - infinite while
 * Return: 0
 */
int whileinf(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - C program that creates 5 zombie processes.
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	char count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	whileinf();
	return (EXIT_SUCCESS);
}
