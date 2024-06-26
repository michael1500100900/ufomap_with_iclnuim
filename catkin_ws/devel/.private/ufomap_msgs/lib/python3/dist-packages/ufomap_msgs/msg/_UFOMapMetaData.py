# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ufomap_msgs/UFOMapMetaData.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ufomap_msgs.msg

class UFOMapMetaData(genpy.Message):
  _md5sum = "3469fb65109a0fe2f8055afe98d145fa"
  _type = "ufomap_msgs/UFOMapMetaData"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# File version used
string version

# Class id of the contained Octree
string id

# Resolution (in m) of the octree leaf nodes
float64 resolution

# Number of depth levels
uint8 depth_levels

# If data is compressed
bool compressed

# Size of data uncompressed
int32 uncompressed_data_size

# Bounding volume
ufomap_msgs/BoundingVolume bounding_volume
================================================================================
MSG: ufomap_msgs/BoundingVolume
ufomap_msgs/AABB[] aabbs

# ufomap_msgs/Capsule[] capsules

# ufomap_msgs/Cone[] cones

# ufomap_msgs/Cylinder[] cylinders

# ufomap_msgs/Ellipsoid[] ellipsoids

ufomap_msgs/Frustum[] frustums

ufomap_msgs/LineSegment[] line_segments

ufomap_msgs/OBB[] obbs

ufomap_msgs/Plane[] planes

ufomap_msgs/Point[] points

ufomap_msgs/Ray[] rays

ufomap_msgs/Sphere[] spheres

# ufomap_msgs/Triangle[] triangles
================================================================================
MSG: ufomap_msgs/AABB
ufomap_msgs/Point center

ufomap_msgs/Point half_size
================================================================================
MSG: ufomap_msgs/Point
float64 x
float64 y
float64 z
================================================================================
MSG: ufomap_msgs/Frustum
ufomap_msgs/Plane[6] planes
================================================================================
MSG: ufomap_msgs/Plane
ufomap_msgs/Point normal

float64 distance
================================================================================
MSG: ufomap_msgs/LineSegment
ufomap_msgs/Point start

ufomap_msgs/Point end
================================================================================
MSG: ufomap_msgs/OBB
ufomap_msgs/Point center

ufomap_msgs/Point half_size

ufomap_msgs/Point rotation
================================================================================
MSG: ufomap_msgs/Ray
ufomap_msgs/Point origin

ufomap_msgs/Point direction
================================================================================
MSG: ufomap_msgs/Sphere
ufomap_msgs/Point center

float64 radius"""
  __slots__ = ['version','id','resolution','depth_levels','compressed','uncompressed_data_size','bounding_volume']
  _slot_types = ['string','string','float64','uint8','bool','int32','ufomap_msgs/BoundingVolume']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       version,id,resolution,depth_levels,compressed,uncompressed_data_size,bounding_volume

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(UFOMapMetaData, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.version is None:
        self.version = ''
      if self.id is None:
        self.id = ''
      if self.resolution is None:
        self.resolution = 0.
      if self.depth_levels is None:
        self.depth_levels = 0
      if self.compressed is None:
        self.compressed = False
      if self.uncompressed_data_size is None:
        self.uncompressed_data_size = 0
      if self.bounding_volume is None:
        self.bounding_volume = ufomap_msgs.msg.BoundingVolume()
    else:
      self.version = ''
      self.id = ''
      self.resolution = 0.
      self.depth_levels = 0
      self.compressed = False
      self.uncompressed_data_size = 0
      self.bounding_volume = ufomap_msgs.msg.BoundingVolume()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.version
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_d2Bi().pack(_x.resolution, _x.depth_levels, _x.compressed, _x.uncompressed_data_size))
      length = len(self.bounding_volume.aabbs)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.aabbs:
        _v1 = val1.center
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v2 = val1.half_size
        _x = _v2
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.frustums)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.frustums:
        if len(val1.planes) != 6:
          self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (6, len(val1.planes), 'val1.planes')))
        for val2 in val1.planes:
          _v3 = val2.normal
          _x = _v3
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _x = val2.distance
          buff.write(_get_struct_d().pack(_x))
      length = len(self.bounding_volume.line_segments)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.line_segments:
        _v4 = val1.start
        _x = _v4
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v5 = val1.end
        _x = _v5
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.obbs)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.obbs:
        _v6 = val1.center
        _x = _v6
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v7 = val1.half_size
        _x = _v7
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v8 = val1.rotation
        _x = _v8
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.planes)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.planes:
        _v9 = val1.normal
        _x = _v9
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.distance
        buff.write(_get_struct_d().pack(_x))
      length = len(self.bounding_volume.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.rays)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.rays:
        _v10 = val1.origin
        _x = _v10
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v11 = val1.direction
        _x = _v11
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.spheres)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.spheres:
        _v12 = val1.center
        _x = _v12
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.radius
        buff.write(_get_struct_d().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bounding_volume is None:
        self.bounding_volume = ufomap_msgs.msg.BoundingVolume()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.version = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.version = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.id = str[start:end]
      _x = self
      start = end
      end += 14
      (_x.resolution, _x.depth_levels, _x.compressed, _x.uncompressed_data_size,) = _get_struct_d2Bi().unpack(str[start:end])
      self.compressed = bool(self.compressed)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.aabbs = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.AABB()
        _v13 = val1.center
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v14 = val1.half_size
        _x = _v14
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.aabbs.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.frustums = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Frustum()
        val1.planes = []
        for i in range(0, 6):
          val2 = ufomap_msgs.msg.Plane()
          _v15 = val2.normal
          _x = _v15
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          start = end
          end += 8
          (val2.distance,) = _get_struct_d().unpack(str[start:end])
          val1.planes.append(val2)
        self.bounding_volume.frustums.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.line_segments = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.LineSegment()
        _v16 = val1.start
        _x = _v16
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v17 = val1.end
        _x = _v17
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.line_segments.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.obbs = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.OBB()
        _v18 = val1.center
        _x = _v18
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v19 = val1.half_size
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v20 = val1.rotation
        _x = _v20
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.obbs.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.planes = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Plane()
        _v21 = val1.normal
        _x = _v21
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 8
        (val1.distance,) = _get_struct_d().unpack(str[start:end])
        self.bounding_volume.planes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.points = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.rays = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Ray()
        _v22 = val1.origin
        _x = _v22
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v23 = val1.direction
        _x = _v23
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.rays.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.spheres = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Sphere()
        _v24 = val1.center
        _x = _v24
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 8
        (val1.radius,) = _get_struct_d().unpack(str[start:end])
        self.bounding_volume.spheres.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.version
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_d2Bi().pack(_x.resolution, _x.depth_levels, _x.compressed, _x.uncompressed_data_size))
      length = len(self.bounding_volume.aabbs)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.aabbs:
        _v25 = val1.center
        _x = _v25
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v26 = val1.half_size
        _x = _v26
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.frustums)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.frustums:
        if len(val1.planes) != 6:
          self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (6, len(val1.planes), 'val1.planes')))
        for val2 in val1.planes:
          _v27 = val2.normal
          _x = _v27
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _x = val2.distance
          buff.write(_get_struct_d().pack(_x))
      length = len(self.bounding_volume.line_segments)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.line_segments:
        _v28 = val1.start
        _x = _v28
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v29 = val1.end
        _x = _v29
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.obbs)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.obbs:
        _v30 = val1.center
        _x = _v30
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v31 = val1.half_size
        _x = _v31
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v32 = val1.rotation
        _x = _v32
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.planes)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.planes:
        _v33 = val1.normal
        _x = _v33
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.distance
        buff.write(_get_struct_d().pack(_x))
      length = len(self.bounding_volume.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.rays)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.rays:
        _v34 = val1.origin
        _x = _v34
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v35 = val1.direction
        _x = _v35
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_volume.spheres)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_volume.spheres:
        _v36 = val1.center
        _x = _v36
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.radius
        buff.write(_get_struct_d().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bounding_volume is None:
        self.bounding_volume = ufomap_msgs.msg.BoundingVolume()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.version = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.version = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.id = str[start:end]
      _x = self
      start = end
      end += 14
      (_x.resolution, _x.depth_levels, _x.compressed, _x.uncompressed_data_size,) = _get_struct_d2Bi().unpack(str[start:end])
      self.compressed = bool(self.compressed)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.aabbs = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.AABB()
        _v37 = val1.center
        _x = _v37
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v38 = val1.half_size
        _x = _v38
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.aabbs.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.frustums = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Frustum()
        val1.planes = []
        for i in range(0, 6):
          val2 = ufomap_msgs.msg.Plane()
          _v39 = val2.normal
          _x = _v39
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          start = end
          end += 8
          (val2.distance,) = _get_struct_d().unpack(str[start:end])
          val1.planes.append(val2)
        self.bounding_volume.frustums.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.line_segments = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.LineSegment()
        _v40 = val1.start
        _x = _v40
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v41 = val1.end
        _x = _v41
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.line_segments.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.obbs = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.OBB()
        _v42 = val1.center
        _x = _v42
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v43 = val1.half_size
        _x = _v43
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v44 = val1.rotation
        _x = _v44
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.obbs.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.planes = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Plane()
        _v45 = val1.normal
        _x = _v45
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 8
        (val1.distance,) = _get_struct_d().unpack(str[start:end])
        self.bounding_volume.planes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.points = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.rays = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Ray()
        _v46 = val1.origin
        _x = _v46
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v47 = val1.direction
        _x = _v47
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_volume.rays.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_volume.spheres = []
      for i in range(0, length):
        val1 = ufomap_msgs.msg.Sphere()
        _v48 = val1.center
        _x = _v48
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 8
        (val1.radius,) = _get_struct_d().unpack(str[start:end])
        self.bounding_volume.spheres.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
_struct_d2Bi = None
def _get_struct_d2Bi():
    global _struct_d2Bi
    if _struct_d2Bi is None:
        _struct_d2Bi = struct.Struct("<d2Bi")
    return _struct_d2Bi
