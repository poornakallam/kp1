//@Library('latest')_

//maven config 
mavenPipelinePlugin{

//build configuration
cleanWorkspace = true
pipeLineBuildToolName = "apache-maven-3.0.5"
pipelineJdkToolName = "JDK17"
buildDefinitionFile = "pom.xml"

baselineVersion = 1.0

//package and publish artifactory
artifactoryRepo = "maven"
puslidhMasterToRelease = false
executeCreateArtifact = true
execurePublishArtifact  = true
enableAutoVersioning = (branchname == "develop" || branch == "feature")SSS

//custom goals & parameters
builtParameters = "-U clean install"
publishParameters = "clean install"

//code scan
executeCodeScan = true
scanFailFast = false
sonarPropertyFile = "sonar-project.properties"

//binariesPath = "complete"
pipelineScanServerToolName = "enterprise-sonar-2"
pipelineScanClientToolName = "sonar"

}
