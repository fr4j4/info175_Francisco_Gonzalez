# -*- coding: utf-8 -*-
def fibbo(n):
	#calcula el n-ésimo elemento de la serie fibbonacci
	if n==0:
		return 0
	elif n==1:
		return 1
	elif n>1:
		return fibbo(n-1)+fibbo(n-2)

print fibbo(1)
print fibbo(2)
print fibbo(3)
print fibbo(4)
print fibbo(5)
print fibbo(6)
print fibbo(7)