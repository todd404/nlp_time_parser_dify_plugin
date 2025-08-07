from collections.abc import Generator
import json
import time
from typing import Any, cast
import jionlp as jio

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class TimeParserTool(Tool):
    """
    A tool to parse time expressions from Chinese text using jioNLP.
    """
    def _parse_time(self, text: str, base_time_text: str | None) -> list[dict[str, Any]]:
        """
        Parses time expressions from the given text.

        :param text: The text to parse.
        :param base_time_text: The base time for relative time parsing, in 'YYYY-MM-DD HH:MM:SS' format.
                               If None or invalid, the current system time is used.
        :return: A list of dictionaries, each representing a parsed time entity.
        """
        # Determine the base time for parsing.
        # Default to the current system time as a timestamp.
        time_base = time.time()

        # If the user provides base_time_text (format %Y-%m-%d %H:%M:%S),
        # try to parse it into a timestamp.
        if base_time_text:
            try:
                # Convert it to a time tuple, then to a timestamp.
                time_struct = time.strptime(base_time_text, '%Y-%m-%d %H:%M:%S')
                time_base = time.mktime(time_struct)
            except (ValueError, TypeError):
                # If the format is incorrect or the type is wrong,
                # ignore it and use the default current system time.
                # In a real-world scenario, you might want to log this event
                # or return an error/warning to the user.
                pass

        # 提取时间
        time_entities = jio.ner.extract_time(text)

        # 解析时间
        parsed_times = []
        for entity in time_entities:
            # 使用确定的 time_base 来解析文本中的时间
            parsed_time = cast(dict[str, Any], jio.parse_time(entity['text'], time_base=time_base))
            # 确保解析结果有效
            if parsed_time and parsed_time.get('time'):
                parsed_time_info = {
                    'start_time': parsed_time['time'][0],
                    'end_time': parsed_time['time'][1],
                    'time_type': parsed_time['type'],
                    'time_text': entity['text'],
                    'definition': parsed_time['definition'],
                }
                parsed_times.append(parsed_time_info)

        # 输出解析结果
        return parsed_times

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        The entry point for the tool invocation.
        """
        time_text = tool_parameters['time_text']
        # base_time_text is an optional parameter, safely get it using .get().
        base_time_text = tool_parameters.get('base_time_text')
        parsed_time = self._parse_time(time_text, base_time_text)

        # Yield a structured JSON message for machine consumption.
        yield self.create_json_message({
            "result": parsed_time
        })

        # Yield a human-readable text message.
        # This is a pretty-printed JSON string of the result.
        parsed_time_json = json.dumps(parsed_time, ensure_ascii=False, indent=2)
        yield self.create_text_message(parsed_time_json)
