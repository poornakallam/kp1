 node {
    def mavenHome = tool name: "maven3.8.3"

 stage ('checkout')
 {
git 'https://github.com/poornakallam/maven-web-application.git'
  }
stage ('build')
 {
  sh "${mavenHome}/bin/mvn clean package"
  }
stage ('sonar')
  {
  sh "${mavenHome}/bin/mvn clean sonar:sonar package"
   }
stage ('uploadArtifact')
   {
   sh "${mavenHome}/bin/mvn deploy"
   }
stage ('EmailNotify')
  {
 emailext body: '''Build Saved...

Thanks,
Poorna Kallam''', subject: 'Build saved...', to: 'poorna.kallam@gmail.com'
}
   
}
