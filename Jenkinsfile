
/*
    This is an example of a Jenkins pipeline trying to demonstrate the following use-case:
     * Set CONAN_USER_HOME to a fixed location.
        The problema is that the first job needs to actually add the remote while the
        following ones don't need to (call to 'client.remote.add' should not fail).

        Requires: https://github.com/jfrog/jenkins-artifactory-plugin/pull/179
*/

def artifactory_name = "Artifactory Docker"
def artifactory_repo = "conan-local"
String docker_image = "conanio/gcc8"

node {
    docker.image(docker_image).inside('--net=docker_jenkins_artifactory') {
        def server = Artifactory.server artifactory_name
        def client = Artifactory.newConanClient(userHome: "${env.WORKSPACE}/conan_home".toString())
        def remoteName = client.remote.add server: server, repo: artifactory_repo, force: true

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
            server.publishBuildInfo buildInfo
        }
    }
}
