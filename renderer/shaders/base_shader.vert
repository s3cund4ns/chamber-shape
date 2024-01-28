#version 460 core

layout (location = 0) in vec3 vertex_pos;
//layout (location = 1) in vec3 vertex_color;

uniform mvp_matrix;

out vec3 fragment_color;

void main()
{
    gl_Position = vec4(mvp_matrix * vertex_pos, 1.0);
    fragment_color = vec3(0.0, 0.0, 1.0);
    //fragment_color = vertex_color;
}