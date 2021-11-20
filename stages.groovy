def call(String mavengoal) {
   if ("${mavengoal}" == "clean") {
   sh "mvn clean"
   }
   else if ("${mavengoal}" == "compile") {
   sh "mvn clean compile"
   }
   else if ("${mavengoal}" == "test") {
   sh "mvn clean test"
   }
   else if ("${mavengoal}" == "package") {
   sh "mvn clean package"
   }

 }
