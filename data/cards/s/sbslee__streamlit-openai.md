# sbslee/streamlit-openai

⭐ 20 · Python · MIT · 推送 2026-01-15 · [GitHub](https://github.com/sbslee/streamlit-openai) · 个人维护

**Streamlit 组件：为开发者快速搭建 OpenAI 驱动的聊天界面**

Python 包，提供 Streamlit 聊天组件封装 OpenAI Responses API：流式输出、函数调用、reasoning、远程 MCP、文件搜索、代码解释器、视觉、图像生成、网络搜索等工具集成，并支持文件上传、聊天历史保存/恢复（ZIP）、自动对话摘要与 token 用量统计。附 CLI 管理向量存储/文件/容器清理。开发者通过 pip 安装并设置 OPENAI_API_KEY 后用数行代码运行，可自定义模型、温度与指令；文件搜索同时最多两个向量存储，reasoning 模型不支持网络搜索。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 OpenAI Responses API 的流式聊天界面组件
- 集成函数调用、远程 MCP、文件搜索、代码解释器、视觉、图像生成、网络搜索
- 聊天历史 ZIP 保存/恢复与自动对话摘要
- CLI 删除向量存储、文件与容器，token 用量属性跟踪消耗

## 适用场景

- 在 Streamlit 应用中快速加入带工具调用的 AI 聊天界面
- 让助手读取上传的文档并检索回答（文件搜索/PDF 视觉）
- 在沙箱中运行 Python 代码分析文件并生成图表

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: This package provides a Streamlit component for building interactive chat
> L12: - Integration with OpenAI tools: reasoning, function calling, remote MCP, file search, code interpreter, vision, im

## 星数曲线

```mermaid
xychart-beta
    title "sbslee/streamlit-openai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3ebf47601cdf` · [字段定义](../../DATASET.md)*
