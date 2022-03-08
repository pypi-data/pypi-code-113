# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class StaticRigidbodyData(object):
    __slots__ = ['_tab']

    # StaticRigidbodyData
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # StaticRigidbodyData
    def Id(self): return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # StaticRigidbodyData
    def Mass(self): return self._tab.Get(tdw.flatbuffers.number_types.Float32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # StaticRigidbodyData
    def Kinematic(self): return self._tab.Get(tdw.flatbuffers.number_types.BoolFlags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # StaticRigidbodyData
    def DynamicFriction(self): return self._tab.Get(tdw.flatbuffers.number_types.Float32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(12))
    # StaticRigidbodyData
    def StaticFriction(self): return self._tab.Get(tdw.flatbuffers.number_types.Float32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # StaticRigidbodyData
    def Bounciness(self): return self._tab.Get(tdw.flatbuffers.number_types.Float32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(20))

def CreateStaticRigidbodyData(builder, id, mass, kinematic, dynamicFriction, staticFriction, bounciness):
    builder.Prep(4, 24)
    builder.PrependFloat32(bounciness)
    builder.PrependFloat32(staticFriction)
    builder.PrependFloat32(dynamicFriction)
    builder.Pad(3)
    builder.PrependBool(kinematic)
    builder.PrependFloat32(mass)
    builder.PrependInt32(id)
    return builder.Offset()
