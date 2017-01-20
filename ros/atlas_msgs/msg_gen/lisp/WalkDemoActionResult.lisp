; Auto-generated. Do not edit!


(cl:in-package atlas_msgs-msg)


;//! \htmlinclude WalkDemoActionResult.msg.html

(cl:defclass <WalkDemoActionResult> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (status
    :reader status
    :initarg :status
    :type actionlib_msgs-msg:GoalStatus
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalStatus))
   (result
    :reader result
    :initarg :result
    :type atlas_msgs-msg:WalkDemoResult
    :initform (cl:make-instance 'atlas_msgs-msg:WalkDemoResult)))
)

(cl:defclass WalkDemoActionResult (<WalkDemoActionResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WalkDemoActionResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WalkDemoActionResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name atlas_msgs-msg:<WalkDemoActionResult> is deprecated: use atlas_msgs-msg:WalkDemoActionResult instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <WalkDemoActionResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader atlas_msgs-msg:header-val is deprecated.  Use atlas_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <WalkDemoActionResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader atlas_msgs-msg:status-val is deprecated.  Use atlas_msgs-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <WalkDemoActionResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader atlas_msgs-msg:result-val is deprecated.  Use atlas_msgs-msg:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WalkDemoActionResult>) ostream)
  "Serializes a message object of type '<WalkDemoActionResult>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'status) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'result) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WalkDemoActionResult>) istream)
  "Deserializes a message object of type '<WalkDemoActionResult>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'status) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'result) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WalkDemoActionResult>)))
  "Returns string type for a message object of type '<WalkDemoActionResult>"
  "atlas_msgs/WalkDemoActionResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WalkDemoActionResult)))
  "Returns string type for a message object of type 'WalkDemoActionResult"
  "atlas_msgs/WalkDemoActionResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WalkDemoActionResult>)))
  "Returns md5sum for a message object of type '<WalkDemoActionResult>"
  "e62dca2bf26ccbf63139e15689379528")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WalkDemoActionResult)))
  "Returns md5sum for a message object of type 'WalkDemoActionResult"
  "e62dca2bf26ccbf63139e15689379528")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WalkDemoActionResult>)))
  "Returns full string definition for message of type '<WalkDemoActionResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%WalkDemoResult result~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: atlas_msgs/WalkDemoResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result~%atlas_msgs/AtlasSimInterfaceState end_state~%bool success~%~%================================================================================~%MSG: atlas_msgs/AtlasSimInterfaceState~%# For interfacing Boston Dynamics' AtlasSimInterface Dynamics Behavior Library~%# Feedback from AtlasSimInterface Controller after calling process_control_input~%# This ROS message should track AtlasControlOutput struct in~%# AtlasSimInterfaceTypes.h.~%# With the exception of addition of k_effort to provide user a way to switch~%# to/from PID servo control in AtlasPlugin.cpp on a per joint basis.~%~%int32 NO_ERRORS                        =  0    # no error detected~%int32 ERROR_UNSPECIFIED                = -1    # unspecified error~%int32 ERROR_VALUE_OUT_OF_RANGE         = -2    # passed value is out of range~%int32 ERROR_INVALID_INDEX              = -3    # passed index is invalid (too low or too high)~%int32 ERROR_FAILED_TO_START_BEHAVIOR   = -4    # robot failed to start desired behavior~%int32 ERROR_NO_ACTIVE_BEHAVIOR         = -5    # robot has no active behavior~%int32 ERROR_NO_SUCH_BEHAVIOR           = -6    # behavior doesn't exist~%int32 ERROR_BEHAVIOR_NOT_IMPLEMENTED   = -7    # behavior exists but not implemented~%int32 ERROR_TIME_RAN_BACKWARD          = -8    # a time earlier than previous times was given~%~%Header header~%~%int32 error_code                         # error code returned by~%                                         # process_control_input.~%                                         # See AtlasSimInterfaceTypes.h~%                                         # AtlasErrorCode for list of enums.~%                                         # The list is mimic'd here above.~%~%int32 current_behavior                   # current active behavior.~%int32 desired_behavior                   # desired behavior specified by usesr~%                                         # input. This may lag from~%                                         # current_behavior by a few simulation~%                                         # steps.~%~%# below are information from AtlasControlOutput in AtlasSimInterfaceTypes.h~%~%float64[28] f_out                        # torque command from BDI controller.~%~%atlas_msgs/AtlasPositionData pos_est     # Position and velocity estimate of robot pelvis~%~%geometry_msgs/Pose[2] foot_pos_est      # World position estimate for feet~%                                         # 0 - left, 1 - right~%~%atlas_msgs/AtlasBehaviorFeedback behavior_feedback~%atlas_msgs/AtlasBehaviorStepFeedback step_feedback~%atlas_msgs/AtlasBehaviorStandFeedback stand_feedback~%atlas_msgs/AtlasBehaviorWalkFeedback walk_feedback~%atlas_msgs/AtlasBehaviorManipulateFeedback manipulate_feedback~%~%# additional vector for transitioning from servo model in AtlasPlugin~%# to BDI servo.~%~%uint8[] k_effort       # k_effort can be an unsigned int 8value from 0 to 255, ~%                       # at run time, a double between 0 and 1 is obtained~%                       # by dividing by 255.0d.~%~%~%================================================================================~%MSG: atlas_msgs/AtlasPositionData~%# mirrors AtlasPositionData in AtlasControlTypes.h~%geometry_msgs/Vector3 position~%geometry_msgs/Vector3 velocity~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorFeedback~%# mirrors AtlasBehaviorFeedback~%#~%# Transition flags:~%#    - STATUS_TRANSITION_IN_PROGRESS~%#~%#        A transition is in progress.~%#~%#    - STATUS_TRANSITION_SUCCESS~%#~%#        Successful transition.~%#~%#    - STATUS_FAILED_TRANS_UNKNOWN_BEHAVIOR~%#~%#        Failed to transition; unknown behavior.~%#~%#    - STATUS_FAILED_TRANS_ILLEGAL_BEHAVIOR~%#~%#        Denied request for an illegal behavior transition.  This may~%#        happen if a transition to a new behavior is requested without~%#        going through a required intermediate behavior. (e.g., can't~%#        go from Walk straight to Manipulate.)~%#~%#    - STATUS_FAILED_TRANS_COM_POS~%#~%#        Failed to transition; the position of the COM is too far from~%#        the center of support.~%#~%#    - STATUS_FAILED_TRANS_COM_VEL~%#~%#        Failed to transition; the COM velocity too high.~%#~%#    - STATUS_FAILED_TRANS_VEL~%#~%#        Failed to transition; some joint velocities too high.~%#~%#  \\em Warnings:~%#~%#    - STATUS_WARNING_AUTO_TRANS~%#~%#        An automatic transition occurred; see behavior specific~%#        feedback for reason.~%#~%#  \\em Errors:~%#~%#    - STATUS_ERROR_FALLING~%#~%#        COM below acceptable threshold, cannot recover.~%~%# copied from AtlasBehaviorFlags~%uint32 STATUS_OK                            = 0~%uint32 STATUS_TRANSITION_IN_PROGRESS        = 1~%uint32 STATUS_TRANSITION_SUCCESS            = 2~%uint32 STATUS_FAILED_TRANS_UNKNOWN_BEHAVIOR = 4~%uint32 STATUS_FAILED_TRANS_ILLEGAL_BEHAVIOR = 8~%uint32 STATUS_FAILED_TRANS_COM_POS          = 16~%uint32 STATUS_FAILED_TRANS_COM_VEL          = 32~%uint32 STATUS_FAILED_TRANS_VEL              = 64~%uint32 STATUS_WARNING_AUTO_TRANS            = 128~%uint32 STATUS_ERROR_FALLING                 = 256~%~%uint32 status_flags  # can be one of above~%~%int32 trans_from_behavior_index  # use this as a parm to get_behavior_at_index() to get behavior string~%int32 trans_to_behavior_index  # use this as a parm to get_behavior_at_index() to get behavior string~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorStepFeedback~%# mirrored from AtlasControlTypes.h~%uint32 STEP_SUBSTATE_SWAYING = 0  # Feet are in double support. This flag does not latch. Only one of STEP_SUBSTATE_SWAYING or STEP_SUBSTATE_STEPPING will be set at any given time.~%uint32 STEP_SUBSTATE_STEPPING = 1 # Actively stepping; one foot is in the air. This flag does not latch.~%~%uint32 status_flags    # use AtlasBeahviorFeedback/status_flags~%float64 t_step_rem~%uint32 current_step_index~%uint32 next_step_index_needed~%atlas_msgs/AtlasBehaviorStepData desired_step_saturated~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorStepData~%# multi_step walking trajectory parameters~%uint32 step_index              # Step index, matlab style, starting from 1,~%                               # monotonically increasing during walking~%                               #  resets to 1 if robot leaves walk behaviors~%uint32 foot_index              # Foot_index can be LEFT_FOOT or RIGHT_FOOT~%float64 duration               # Step duration, when in doubt, 0.63s is a~%                               # good guess.~%geometry_msgs/Pose pose        # Foot pose in Atlas world frame~%float64 swing_height           # Step apex swing height measured form the~%                               # midpoint between the feet.~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorStandFeedback~%# mirrored from AtlasControlTypes.h~%uint32 status_flags    # use AtlasBeahviorStandFlags~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorWalkFeedback~%# mirrored from AtlasControlTypes.h~%float64 t_step_rem~%uint32 current_step_index~%uint32 next_step_index_needed~%uint32 status_flags    # use AtlasBeahviorFeedback/status_flags~%atlas_msgs/AtlasBehaviorStepData[4] step_queue_saturated # 4 is hardcoded in AtlasSimInterface library.~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorManipulateFeedback~%# mirrored from AtlasControlTypes.h~%uint32 status_flags    # use AtlasBeahviorManipulateFlags~%atlas_msgs/AtlasBehaviorPelvisServoParams clamped~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorPelvisServoParams~%# mirrored from AtlasControlTypes.h~%~%float64 pelvis_height~%float64 pelvis_yaw~%float64 pelvis_lat~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WalkDemoActionResult)))
  "Returns full string definition for message of type 'WalkDemoActionResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%WalkDemoResult result~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: atlas_msgs/WalkDemoResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result~%atlas_msgs/AtlasSimInterfaceState end_state~%bool success~%~%================================================================================~%MSG: atlas_msgs/AtlasSimInterfaceState~%# For interfacing Boston Dynamics' AtlasSimInterface Dynamics Behavior Library~%# Feedback from AtlasSimInterface Controller after calling process_control_input~%# This ROS message should track AtlasControlOutput struct in~%# AtlasSimInterfaceTypes.h.~%# With the exception of addition of k_effort to provide user a way to switch~%# to/from PID servo control in AtlasPlugin.cpp on a per joint basis.~%~%int32 NO_ERRORS                        =  0    # no error detected~%int32 ERROR_UNSPECIFIED                = -1    # unspecified error~%int32 ERROR_VALUE_OUT_OF_RANGE         = -2    # passed value is out of range~%int32 ERROR_INVALID_INDEX              = -3    # passed index is invalid (too low or too high)~%int32 ERROR_FAILED_TO_START_BEHAVIOR   = -4    # robot failed to start desired behavior~%int32 ERROR_NO_ACTIVE_BEHAVIOR         = -5    # robot has no active behavior~%int32 ERROR_NO_SUCH_BEHAVIOR           = -6    # behavior doesn't exist~%int32 ERROR_BEHAVIOR_NOT_IMPLEMENTED   = -7    # behavior exists but not implemented~%int32 ERROR_TIME_RAN_BACKWARD          = -8    # a time earlier than previous times was given~%~%Header header~%~%int32 error_code                         # error code returned by~%                                         # process_control_input.~%                                         # See AtlasSimInterfaceTypes.h~%                                         # AtlasErrorCode for list of enums.~%                                         # The list is mimic'd here above.~%~%int32 current_behavior                   # current active behavior.~%int32 desired_behavior                   # desired behavior specified by usesr~%                                         # input. This may lag from~%                                         # current_behavior by a few simulation~%                                         # steps.~%~%# below are information from AtlasControlOutput in AtlasSimInterfaceTypes.h~%~%float64[28] f_out                        # torque command from BDI controller.~%~%atlas_msgs/AtlasPositionData pos_est     # Position and velocity estimate of robot pelvis~%~%geometry_msgs/Pose[2] foot_pos_est      # World position estimate for feet~%                                         # 0 - left, 1 - right~%~%atlas_msgs/AtlasBehaviorFeedback behavior_feedback~%atlas_msgs/AtlasBehaviorStepFeedback step_feedback~%atlas_msgs/AtlasBehaviorStandFeedback stand_feedback~%atlas_msgs/AtlasBehaviorWalkFeedback walk_feedback~%atlas_msgs/AtlasBehaviorManipulateFeedback manipulate_feedback~%~%# additional vector for transitioning from servo model in AtlasPlugin~%# to BDI servo.~%~%uint8[] k_effort       # k_effort can be an unsigned int 8value from 0 to 255, ~%                       # at run time, a double between 0 and 1 is obtained~%                       # by dividing by 255.0d.~%~%~%================================================================================~%MSG: atlas_msgs/AtlasPositionData~%# mirrors AtlasPositionData in AtlasControlTypes.h~%geometry_msgs/Vector3 position~%geometry_msgs/Vector3 velocity~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorFeedback~%# mirrors AtlasBehaviorFeedback~%#~%# Transition flags:~%#    - STATUS_TRANSITION_IN_PROGRESS~%#~%#        A transition is in progress.~%#~%#    - STATUS_TRANSITION_SUCCESS~%#~%#        Successful transition.~%#~%#    - STATUS_FAILED_TRANS_UNKNOWN_BEHAVIOR~%#~%#        Failed to transition; unknown behavior.~%#~%#    - STATUS_FAILED_TRANS_ILLEGAL_BEHAVIOR~%#~%#        Denied request for an illegal behavior transition.  This may~%#        happen if a transition to a new behavior is requested without~%#        going through a required intermediate behavior. (e.g., can't~%#        go from Walk straight to Manipulate.)~%#~%#    - STATUS_FAILED_TRANS_COM_POS~%#~%#        Failed to transition; the position of the COM is too far from~%#        the center of support.~%#~%#    - STATUS_FAILED_TRANS_COM_VEL~%#~%#        Failed to transition; the COM velocity too high.~%#~%#    - STATUS_FAILED_TRANS_VEL~%#~%#        Failed to transition; some joint velocities too high.~%#~%#  \\em Warnings:~%#~%#    - STATUS_WARNING_AUTO_TRANS~%#~%#        An automatic transition occurred; see behavior specific~%#        feedback for reason.~%#~%#  \\em Errors:~%#~%#    - STATUS_ERROR_FALLING~%#~%#        COM below acceptable threshold, cannot recover.~%~%# copied from AtlasBehaviorFlags~%uint32 STATUS_OK                            = 0~%uint32 STATUS_TRANSITION_IN_PROGRESS        = 1~%uint32 STATUS_TRANSITION_SUCCESS            = 2~%uint32 STATUS_FAILED_TRANS_UNKNOWN_BEHAVIOR = 4~%uint32 STATUS_FAILED_TRANS_ILLEGAL_BEHAVIOR = 8~%uint32 STATUS_FAILED_TRANS_COM_POS          = 16~%uint32 STATUS_FAILED_TRANS_COM_VEL          = 32~%uint32 STATUS_FAILED_TRANS_VEL              = 64~%uint32 STATUS_WARNING_AUTO_TRANS            = 128~%uint32 STATUS_ERROR_FALLING                 = 256~%~%uint32 status_flags  # can be one of above~%~%int32 trans_from_behavior_index  # use this as a parm to get_behavior_at_index() to get behavior string~%int32 trans_to_behavior_index  # use this as a parm to get_behavior_at_index() to get behavior string~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorStepFeedback~%# mirrored from AtlasControlTypes.h~%uint32 STEP_SUBSTATE_SWAYING = 0  # Feet are in double support. This flag does not latch. Only one of STEP_SUBSTATE_SWAYING or STEP_SUBSTATE_STEPPING will be set at any given time.~%uint32 STEP_SUBSTATE_STEPPING = 1 # Actively stepping; one foot is in the air. This flag does not latch.~%~%uint32 status_flags    # use AtlasBeahviorFeedback/status_flags~%float64 t_step_rem~%uint32 current_step_index~%uint32 next_step_index_needed~%atlas_msgs/AtlasBehaviorStepData desired_step_saturated~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorStepData~%# multi_step walking trajectory parameters~%uint32 step_index              # Step index, matlab style, starting from 1,~%                               # monotonically increasing during walking~%                               #  resets to 1 if robot leaves walk behaviors~%uint32 foot_index              # Foot_index can be LEFT_FOOT or RIGHT_FOOT~%float64 duration               # Step duration, when in doubt, 0.63s is a~%                               # good guess.~%geometry_msgs/Pose pose        # Foot pose in Atlas world frame~%float64 swing_height           # Step apex swing height measured form the~%                               # midpoint between the feet.~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorStandFeedback~%# mirrored from AtlasControlTypes.h~%uint32 status_flags    # use AtlasBeahviorStandFlags~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorWalkFeedback~%# mirrored from AtlasControlTypes.h~%float64 t_step_rem~%uint32 current_step_index~%uint32 next_step_index_needed~%uint32 status_flags    # use AtlasBeahviorFeedback/status_flags~%atlas_msgs/AtlasBehaviorStepData[4] step_queue_saturated # 4 is hardcoded in AtlasSimInterface library.~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorManipulateFeedback~%# mirrored from AtlasControlTypes.h~%uint32 status_flags    # use AtlasBeahviorManipulateFlags~%atlas_msgs/AtlasBehaviorPelvisServoParams clamped~%~%================================================================================~%MSG: atlas_msgs/AtlasBehaviorPelvisServoParams~%# mirrored from AtlasControlTypes.h~%~%float64 pelvis_height~%float64 pelvis_yaw~%float64 pelvis_lat~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WalkDemoActionResult>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'status))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WalkDemoActionResult>))
  "Converts a ROS message object to a list"
  (cl:list 'WalkDemoActionResult
    (cl:cons ':header (header msg))
    (cl:cons ':status (status msg))
    (cl:cons ':result (result msg))
))
