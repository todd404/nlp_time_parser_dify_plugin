## Chinese Time Parser

**Author:** todd_wu
**Version:** 0.0.1
**Type:** tool

### Overview

This plugin provides a powerful and fast tool for extracting and parsing time-related expressions from Chinese text. It is built on the excellent [jioNLP](https://github.com/dongrixinyu/JioNLP) library and does not rely on any large language models, ensuring high performance.

It can understand various natural language expressions for time, such as "明天上午8点", "下周三", "3天后", or "2024年春节".

### Features

- **High-Speed Parsing**: Processes text quickly by using rule-based methods instead of models.
- **Comprehensive Recognition**: Recognizes time points, time spans, and recurring time expressions.
- **Flexible Time Base**: Allows specifying a custom base time for parsing relative expressions (e.g., "tomorrow"). If not provided, it defaults to the current system time.

### How to Use

The tool has two parameters:

1.  **`time_text` (required)**: The Chinese text containing time expressions that you want to parse.
    -   *Example*: `"我想预约后天下午3点到5点的会议"`

2.  **`base_time_text` (optional)**: A specific time to be used as a reference for relative time expressions. The format should be `YYYY-MM-DD HH:MM:SS`.
    -   *Example*: `"2024-08-15 10:00:00"`

#### Example Output

Given the input text `"我明天要去看电影"`, the tool will output the parsed time information, including the start and end timestamps, the type of time expression, and the original text snippet.

---

## 中文说明

### 概述

本插件提供了一个强大且快速的工具，用于从中文文本中提取和解析与时间相关的表述。它基于优秀的 jioNLP 库构建，不依赖任何大型语言模型，从而确保了极高的性能。

它能理解各种自然语言时间表述，例如“明天上午8点”、“下周三”、“3天后”或“2024年春节”。

### 功能特性

- **高速解析**: 基于规则而非模型，能够快速处理文本。
- **全面识别**: 可识别时间点、时间段和周期性时间。
- **灵活的时间基准**: 允许为相对时间（如“明天”）指定一个自定义的基准时间。如果未提供，则默认为当前系统时间。

### 如何使用

该工具有两个参数：

1.  **`time_text` (必需)**: 包含待解析时间表述的中文文本。
    -   *示例*: `"我想预约后天下午3点到5点的会议"`

2.  **`base_time_text` (可选)**: 用于解析相对时间表达式的参考时间。格式应为 `YYYY-MM-DD HH:MM:SS`。
    -   *示例*: `"2024-08-15 10:00:00"`

#### 输出示例

对于输入文本 `"我明天要去看电影"`，工具将输出解析后的时间信息，包括开始和结束时间戳、时间表达式的类型以及原始文本片段。