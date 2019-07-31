def artifactory_name = "Artifactory Docker Registered"
def artifactory_repo = "conan-local-protected"
String docker_image = "conanio/gcc8"

node {
    docker.image(docker_image).inside('--net=docker_jenkins_artifactory') {
        def server = Artifactory.server artifactory_name
        //def client = Artifactory.newConanClient(userHome: "${env.WORKSPACE}/conan_home".toString())
        def client = Artifactory.newConanClient()
        client.run(command: "remote add --force --insert 0 conan-local-public http://artifactory:8081/artifactory/api/conan/conan-local")            
        def remoteName = client.remote.add server: server, repo: artifactory_repo

        stage("Get project") {
              checkout scm
        }

        stage("Get dependencies and create app") {
            String createCommand = "create . sword/sorcery"
            client.run(command: createCommand)
        }

        stage("Upload packages") {
            String uploadCommand = "upload core-communications* --all -r ${remoteName} --confirm"
            def buildInfo = client.run(command: uploadCommand)
            //b.env.collect()
            server.publishBuildInfo buildInfo
        }
    }
}
