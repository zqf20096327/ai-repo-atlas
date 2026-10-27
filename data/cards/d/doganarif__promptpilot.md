# doganarif/promptpilot

⭐ 78 · Python · MIT · 推送 2026-06-23 · [GitHub](https://github.com/doganarif/promptpilot) · 个人维护

**给开发者的提示词版本管理与 A/B 测试 CLI 工具**

Python 库与 CLI 工具，面向使用 LLM API 的开发者：以 YAML 文件存储提示词并按版本记录演化（不依赖 Git），支持跨 OpenAI、Claude、Llama、HuggingFace 多供应商运行 A/B 测试，按 token 用量与回答质量比较提示词效果。提供 Python API（单版本对比、多变体、批量测试的 Runner 类），架构支持自定义 provider 与格式化器。要求 Python 3.11+ 与各服务的 API key，通过 pip 从 PyPI 安装，.env 文件配置密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提示词 YAML 文件存储与版本记录，无需 Git 依赖
- 跨 OpenAI/Claude/Llama/HuggingFace 的 A/B 测试，比较 token 用量与输出质量
- Python API 提供 MultiPromptTestRunner 与 BatchTestRunner
- 惰性加载依赖以缩短启动时间，支持自定义 provider 扩展

## 适用场景

- 我需要跟踪提示词的修改历史并随时回滚
- 我想比较两个提示词版本在 token 消耗和输出质量上的差异
- 我想在自己的 Python 工作流中集成提示词批量测试

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L21: - **A/B testing** to compare prompts based on token usage and response quality
> L22: - **Multi-provider support** for OpenAI, Claude, Llama, and HuggingFace

## 星数曲线

```mermaid
xychart-beta
    title "doganarif/promptpilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-27 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e548c463e212` · [字段定义](../../DATASET.md)*
