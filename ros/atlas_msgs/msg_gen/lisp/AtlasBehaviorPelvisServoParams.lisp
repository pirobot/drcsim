; Auto-generated. Do not edit!


(cl:in-package atlas_msgs-msg)


;//! \htmlinclude AtlasBehaviorPelvisServoParams.msg.html

(cl:defclass <AtlasBehaviorPelvisServoParams> (roslisp-msg-protocol:ros-message)
  ((pelvis_height
    :reader pelvis_height
    :initarg :pelvis_height
    :type cl:float
    :initform 0.0)
   (pelvis_yaw
    :reader pelvis_yaw
    :initarg :pelvis_yaw
    :type cl:float
    :initform 0.0)
   (pelvis_lat
    :reader pelvis_lat
    :initarg :pelvis_lat
    :type cl:float
    :initform 0.0))
)

(cl:defclass AtlasBehaviorPelvisServoParams (<AtlasBehaviorPelvisServoParams>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AtlasBehaviorPelvisServoParams>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AtlasBehaviorPelvisServoParams)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name atlas_msgs-msg:<AtlasBehaviorPelvisServoParams> is deprecated: use atlas_msgs-msg:AtlasBehaviorPelvisServoParams instead.")))

(cl:ensure-generic-function 'pelvis_height-val :lambda-list '(m))
(cl:defmethod pelvis_height-val ((m <AtlasBehaviorPelvisServoParams>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader atlas_msgs-msg:pelvis_height-val is deprecated.  Use atlas_msgs-msg:pelvis_height instead.")
  (pelvis_height m))

(cl:ensure-generic-function 'pelvis_yaw-val :lambda-list '(m))
(cl:defmethod pelvis_yaw-val ((m <AtlasBehaviorPelvisServoParams>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader atlas_msgs-msg:pelvis_yaw-val is deprecated.  Use atlas_msgs-msg:pelvis_yaw instead.")
  (pelvis_yaw m))

(cl:ensure-generic-function 'pelvis_lat-val :lambda-list '(m))
(cl:defmethod pelvis_lat-val ((m <AtlasBehaviorPelvisServoParams>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader atlas_msgs-msg:pelvis_lat-val is deprecated.  Use atlas_msgs-msg:pelvis_lat instead.")
  (pelvis_lat m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AtlasBehaviorPelvisServoParams>) ostream)
  "Serializes a message object of type '<AtlasBehaviorPelvisServoParams>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'pelvis_height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'pelvis_yaw))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'pelvis_lat))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AtlasBehaviorPelvisServoParams>) istream)
  "Deserializes a message object of type '<AtlasBehaviorPelvisServoParams>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pelvis_height) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pelvis_yaw) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pelvis_lat) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AtlasBehaviorPelvisServoParams>)))
  "Returns string type for a message object of type '<AtlasBehaviorPelvisServoParams>"
  "atlas_msgs/AtlasBehaviorPelvisServoParams")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AtlasBehaviorPelvisServoParams)))
  "Returns string type for a message object of type 'AtlasBehaviorPelvisServoParams"
  "atlas_msgs/AtlasBehaviorPelvisServoParams")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AtlasBehaviorPelvisServoParams>)))
  "Returns md5sum for a message object of type '<AtlasBehaviorPelvisServoParams>"
  "82f59d8aa26e61afaf2c8dbb7b4e7856")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AtlasBehaviorPelvisServoParams)))
  "Returns md5sum for a message object of type 'AtlasBehaviorPelvisServoParams"
  "82f59d8aa26e61afaf2c8dbb7b4e7856")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AtlasBehaviorPelvisServoParams>)))
  "Returns full string definition for message of type '<AtlasBehaviorPelvisServoParams>"
  (cl:format cl:nil "# mirrored from AtlasControlTypes.h~%~%float64 pelvis_height~%float64 pelvis_yaw~%float64 pelvis_lat~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AtlasBehaviorPelvisServoParams)))
  "Returns full string definition for message of type 'AtlasBehaviorPelvisServoParams"
  (cl:format cl:nil "# mirrored from AtlasControlTypes.h~%~%float64 pelvis_height~%float64 pelvis_yaw~%float64 pelvis_lat~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AtlasBehaviorPelvisServoParams>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AtlasBehaviorPelvisServoParams>))
  "Converts a ROS message object to a list"
  (cl:list 'AtlasBehaviorPelvisServoParams
    (cl:cons ':pelvis_height (pelvis_height msg))
    (cl:cons ':pelvis_yaw (pelvis_yaw msg))
    (cl:cons ':pelvis_lat (pelvis_lat msg))
))
