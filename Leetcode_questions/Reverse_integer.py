#reverse integer
x=int(input())
y=str(abs(x))
y=y.strip()
out=y[::-1]
output=int(out)

if output<=-2**31 or output>=2**31-1:
    print(0)

elif x<0:
    output=output*-1
    print(output)

else:
    print(output)