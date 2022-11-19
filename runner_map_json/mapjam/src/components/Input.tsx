import { Box, Button, Input } from "@chakra-ui/react";
import { ChangeEvent } from "react";
import { Map, MapTile } from "../dto/map";
import { Setter } from "../dto/setter";

export default function FileInput({ setter }: { setter: Setter<Map[] | null> }) {
    const handleImport = (event: ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.item(0);
        if (file) {
            const reader = new FileReader();
            reader.onload = (event) => {
                const res: Map[] = JSON.parse(event.target?.result as string ?? "[]");
                setter(res);
            };
            reader.readAsText(file);
        }
    }

    return (
        <Box>
            <Input
                type="file"
                accept="application/json"
                onChange={handleImport}
                id="file"
                display="none"
            />
            <Button
                as="label"
                htmlFor="file"
                variant="outline"
            >Import Map</Button>
        </Box>
    )
}