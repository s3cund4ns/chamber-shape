#version 150 core

in vec3 vertexPosition;
in vec3 vertexNormal;

uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;

void main() {
    gl_Position = projectionMatrix * modelViewMatrix * vec4(vertexPosition, 1.0);
    // Disable culling by always setting the front-facing flag to true
    gl_FrontFacing = true;
}