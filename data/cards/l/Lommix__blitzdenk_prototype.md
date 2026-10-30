# Lommix/blitzdenk_prototype

⭐ 16 · Rust · MIT · 推送 2026-06-14 · [GitHub](https://github.com/Lommix/blitzdenk_prototype) · 个人维护

**Rust 终端多模型 AI 编码代理（原型，已冻结开发）**

用 Rust 编写的终端交互式 AI TUI 工具，目标是替代网页搜索、辅助 bug 分析并执行编码任务；非完全自主 agent，保留较多用户控制。通过环境变量读取多家 API key（OpenAI/Anthropic/Gemini/Groq/xAI/DeepSeek），基于 rust-genai 支持所有常见可处理 tool calls 的 AI API，模型列表可自行扩展（含 Ollama）。提供会话保存与恢复、自定义快捷 prompt、Neovim 分屏接入。README 明确标注为旧原型且开发已冻结。安装需 cargo 编译，依赖系统上的 ripgrep。MCP 尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 支持多家 AI-API，只要能处理 tool calls 即可接入
- 会话以 JSON 保存并可在重开时恢复
- 配置文件自定义可用模型列表与颜色（Ollama 亦可加入）
- 支持以斜杠前缀调用自定义快捷 prompt

## 适用场景

- 在终端里用对话完成编码任务与 bug 分析
- 在不同模型供应商之间切换使用同一工具
- 配合 Neovim 以分屏方式快速调用

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L3: Interactive multi purpose personal AI Tui, similar to tools like opencode or claudecode.
> L13: Supports all common AI-APIs that can handle tool calls.

## 星数曲线

```mermaid
xychart-beta
    title "Lommix/blitzdenk_prototype 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b1a840144fbf` · [字段定义](../../DATASET.md)*
