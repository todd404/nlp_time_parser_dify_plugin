from collections.abc import Generator
from typing import Any
import jionlp as jio

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class TimeParserTool(Tool):
    def _parse_time(self, text: str) -> list[dict[str, Any]]:
        # 提取时间
        time_entities = jio.ner.extract_time(text)

        # 解析时间
        parsed_times = []
        for entity in time_entities:
            parsed_time = jio.parse_time(entity['text'])
            parsed_time = {
                'start_time': parsed_time['time'][0],
                'end_time': parsed_time['time'][1],
                'time_type': parsed_time['type'],
                'time_text': entity['text']
            }
            parsed_times.append(parsed_time)

        # 输出解析结果
        return parsed_times

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        time_text = tool_parameters['time_text']
        parsed_time = self._parse_time(time_text)

        yield self.create_json_message({
            "result": parsed_time
        })
