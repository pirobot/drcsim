
(cl:in-package :asdf)

(defsystem "atlas_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "VRCScore" :depends-on ("_package_VRCScore"))
    (:file "_package_VRCScore" :depends-on ("_package"))
    (:file "AtlasBehaviorManipulateFeedback" :depends-on ("_package_AtlasBehaviorManipulateFeedback"))
    (:file "_package_AtlasBehaviorManipulateFeedback" :depends-on ("_package"))
    (:file "AtlasBehaviorStepFeedback" :depends-on ("_package_AtlasBehaviorStepFeedback"))
    (:file "_package_AtlasBehaviorStepFeedback" :depends-on ("_package"))
    (:file "AtlasBehaviorWalkFeedback" :depends-on ("_package_AtlasBehaviorWalkFeedback"))
    (:file "_package_AtlasBehaviorWalkFeedback" :depends-on ("_package"))
    (:file "AtlasBehaviorWalkParams" :depends-on ("_package_AtlasBehaviorWalkParams"))
    (:file "_package_AtlasBehaviorWalkParams" :depends-on ("_package"))
    (:file "AtlasBehaviorPelvisServoParams" :depends-on ("_package_AtlasBehaviorPelvisServoParams"))
    (:file "_package_AtlasBehaviorPelvisServoParams" :depends-on ("_package"))
    (:file "AtlasBehaviorManipulateParams" :depends-on ("_package_AtlasBehaviorManipulateParams"))
    (:file "_package_AtlasBehaviorManipulateParams" :depends-on ("_package"))
    (:file "WalkDemoAction" :depends-on ("_package_WalkDemoAction"))
    (:file "_package_WalkDemoAction" :depends-on ("_package"))
    (:file "WalkDemoGoal" :depends-on ("_package_WalkDemoGoal"))
    (:file "_package_WalkDemoGoal" :depends-on ("_package"))
    (:file "ForceTorqueSensors" :depends-on ("_package_ForceTorqueSensors"))
    (:file "_package_ForceTorqueSensors" :depends-on ("_package"))
    (:file "WalkDemoFeedback" :depends-on ("_package_WalkDemoFeedback"))
    (:file "_package_WalkDemoFeedback" :depends-on ("_package"))
    (:file "AtlasBehaviorStepData" :depends-on ("_package_AtlasBehaviorStepData"))
    (:file "_package_AtlasBehaviorStepData" :depends-on ("_package"))
    (:file "WalkDemoActionGoal" :depends-on ("_package_WalkDemoActionGoal"))
    (:file "_package_WalkDemoActionGoal" :depends-on ("_package"))
    (:file "AtlasBehaviorStandFeedback" :depends-on ("_package_AtlasBehaviorStandFeedback"))
    (:file "_package_AtlasBehaviorStandFeedback" :depends-on ("_package"))
    (:file "WalkDemoActionFeedback" :depends-on ("_package_WalkDemoActionFeedback"))
    (:file "_package_WalkDemoActionFeedback" :depends-on ("_package"))
    (:file "WalkDemoResult" :depends-on ("_package_WalkDemoResult"))
    (:file "_package_WalkDemoResult" :depends-on ("_package"))
    (:file "SynchronizationStatistics" :depends-on ("_package_SynchronizationStatistics"))
    (:file "_package_SynchronizationStatistics" :depends-on ("_package"))
    (:file "AtlasBehaviorStandParams" :depends-on ("_package_AtlasBehaviorStandParams"))
    (:file "_package_AtlasBehaviorStandParams" :depends-on ("_package"))
    (:file "AtlasPositionData" :depends-on ("_package_AtlasPositionData"))
    (:file "_package_AtlasPositionData" :depends-on ("_package"))
    (:file "ControllerStatistics" :depends-on ("_package_ControllerStatistics"))
    (:file "_package_ControllerStatistics" :depends-on ("_package"))
    (:file "WalkDemoActionResult" :depends-on ("_package_WalkDemoActionResult"))
    (:file "_package_WalkDemoActionResult" :depends-on ("_package"))
    (:file "AtlasSimInterfaceCommand" :depends-on ("_package_AtlasSimInterfaceCommand"))
    (:file "_package_AtlasSimInterfaceCommand" :depends-on ("_package"))
    (:file "AtlasState" :depends-on ("_package_AtlasState"))
    (:file "_package_AtlasState" :depends-on ("_package"))
    (:file "AtlasBehaviorStepParams" :depends-on ("_package_AtlasBehaviorStepParams"))
    (:file "_package_AtlasBehaviorStepParams" :depends-on ("_package"))
    (:file "AtlasSimInterfaceState" :depends-on ("_package_AtlasSimInterfaceState"))
    (:file "_package_AtlasSimInterfaceState" :depends-on ("_package"))
    (:file "AtlasBehaviorFeedback" :depends-on ("_package_AtlasBehaviorFeedback"))
    (:file "_package_AtlasBehaviorFeedback" :depends-on ("_package"))
    (:file "Test" :depends-on ("_package_Test"))
    (:file "_package_Test" :depends-on ("_package"))
    (:file "AtlasCommand" :depends-on ("_package_AtlasCommand"))
    (:file "_package_AtlasCommand" :depends-on ("_package"))
  ))