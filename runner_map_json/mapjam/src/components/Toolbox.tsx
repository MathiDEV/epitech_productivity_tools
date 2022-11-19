import { Box, Image } from "@chakra-ui/react";
import sprites from '../data/sprites.json';
import { Setter, State } from "../dto/setter";
import { Tool } from "../dto/tools";

const tools: { type: Tool, icon: string }[] = [
    {
        type: "brush" as Tool,
        icon: "https://cdn-icons-png.flaticon.com/128/483/483917.png",
    },
    {
        type: "pot" as Tool,
        icon: "https://cdn-icons-png.flaticon.com/128/483/483918.png",
    },
    {
        type: "picker" as Tool,
        icon: "https://cdn-icons-png.flaticon.com/128/483/483909.png",
    },
]

export default function Toolbox({ brushState, toolState }: { brushState: State<string | null>, toolState: State<Tool> }) {
    const [brush, setBrush] = brushState;
    const [tool, setTool] = toolState;
    return (
        <Box>
            <Box display="flex" flexWrap="nowrap" gap="0.5em" px="1em" pt="1em">
                {tools.map((t) => (<Box opacity={tool === t.type ? 1 : 0.3} onClick={() => setTool(t.type)} cursor="pointer">
                    <Image
                        height="2em"
                        src={t.icon} />
                </Box>))}
            </Box>
            <Box overflowX="scroll" display="flex" flexWrap="wrap" p="1em">
                <Box display="flex" flexWrap="nowrap" gap="0.5em">
                    {Object.keys(sprites).map((i) => (
                        SpritePreview(setBrush, brush, i)
                    ))}
                </Box>
            </Box>
        </Box>
    )
}

function SpritePreview(setBrush: Setter<string | null>, brush: string | null, i: string): JSX.Element {
    const data = sprites[i as keyof typeof sprites];
    return <Box
        onClick={() => setBrush(brush === i ? null : i)}
        key={i}
        w="2.5em"
        h="2.5em"
        bg={`url(${data.path})`}
        bgSize="100% 100%"
        border={brush === i ? "2px solid red" : "none"}
        transform={brush === i ? "scale(1.2)" : "scale(1)"}
        _hover={{ transform: brush === i ? "scale(1.2)" : "scale(1.1)", opacity: brush === i ? "1" : "0.5" }}
        transition="transform 0.2s, opacity 0.2s"
        cursor="pointer">
        {data.agressive && <Box bgColor="rgba(255, 255, 255, 0.5)" backdropFilter="blur(5px)" display="inline-block" borderBottomRightRadius="5px" p="1px">
            💀
        </Box>}
        {!data.agressive && !data.collision && <Box bgColor="rgba(255, 255, 255, 0.5)" backdropFilter="blur(5px)" display="inline-block" borderBottomRightRadius="5px" p="1px">
            🍃
        </Box>}
    </Box>;
}
