# version 330

in vec2 v_texture;

uniform sampler2D tex;

out vec4 out_color;

void main()
{
    out_color = texture(tex, v_texture);
}