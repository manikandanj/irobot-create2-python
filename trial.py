import struct

vr = velocity + (rotation/2)
vl = velocity - (rotation/2)
cmd = struct.pack(">Bhh", 145, vr, vl)
print cmd