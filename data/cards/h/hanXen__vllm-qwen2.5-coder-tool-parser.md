# hanXen/vllm-qwen2.5-coder-tool-parser

⭐ 18 · Python · 推送 2026-04-29 · [GitHub](https://github.com/hanXen/vllm-qwen2.5-coder-tool-parser) · 个人维护

**让 Qwen2.5-Coder 在 vLLM 上正确实现工具调用的解析器插件**

面向 vLLM 的工具调用解析器插件加聊天模板组合：解决 Qwen2.5-Coder 模型在 vLLM 中使用 --tool-call-parser hermes 时静默失败的问题。机制是通过聊天模板在系统提示注入 <tools> 标签少样本示例，引导模型输出 <tools>...</tools> 格式，解析器再用正则提取 JSON 转为 OpenAI 兼容的 tool_calls 对象，支持流式与非流式。README 给出 vLLM v0.7.x–v0.19.x 兼容矩阵、80 个单元测试与 50 个集成测试，并列出 7B/14B/32B 三个已测试模型。该插件正贡献上游 vLLM（Issue #32926 / PR #32931）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 <tools> 标签实现 100% 格式合规（对比 hermes 提示被模型忽略）
- 支持单次调用、并行调用（重复标签/JSON 数组/JSONL）、未闭合标签等格式
- 覆盖 vLLM v0.7.x–v0.19.x 兼容矩阵并含内部 API 变更回退处理
- 80 个单元测试 + 50 个端到端集成测试，结果文件存于 results/

## 适用场景

- 在 vLLM 上部署 Qwen2.5-Coder 并获得结构化 tool_calls 输出
- 修复 tool_calls 数组为空或工具调用被当作纯文本返回的问题
- 需要流式输出下解析并行工具调用的 agent 应用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: A vLLM tool parser for Qwen2.5-Coder models that use `<tools>` tag format for tool calling.
> L35:     --tool-parser-plugin qwen2_5_coder_tool_parser.py \

## 星数曲线

```mermaid
xychart-beta
    title "hanXen/vllm-qwen2.5-coder-tool-parser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a2457d649421` · [字段定义](../../DATASET.md)*
