class Solution:
    def GCD(self, n1, n2):
        def find(n1,n2):
            if n1 == n2:
                return n1
            return find(abs(n1-n2), min(n1,n2))
        return find(n1,n2)
        
    def GCD_2(self, n1, n2):
        while n2:
            n1, n2 = n2, n1%n2
        return abs(n1)


    def LCM(self, n1, n2):
        a, b = n1, n2
        while b:
            a, b = b, a%b
        return (n1*n2)//abs(a)