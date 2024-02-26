#include <unistd.h> /* for sleep */
#include <stdlib.h> /* for  exit */
#include <stdio.h> /* for printf */

/**
 * infinite_while - create infinite sleep loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: infinite_while zombies
 */
int main(void)
{
	pid_t zombie_pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", zombie_pid);
	}
	return (infinite_while());
}
