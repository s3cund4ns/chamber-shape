vertex_shader_src = '''
#version 460 core

layout (location = 0) in vec3 vertex_pos;
layout (location = 1) in vec3 vertex_color;

out vec3 fragment_color;

void main()
{
    gl_Position = vec4(vertex_pos, 1.0);
    fragment_color = vertex_color;
}
'''

fragment_shader_src = '''
#version 460 core

in vec3 fragment_color;

out vec4 color;

void main()
{
    color = vec4(fragment_color, 1.0);
}
'''