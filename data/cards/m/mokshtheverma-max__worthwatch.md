# mokshtheverma-max/worthwatch

⭐ 3 · Python · Apache-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/mokshtheverma-max/worthwatch) · 个人维护

**为订阅 YouTube 频道者筛选新视频并按自身项目生成个性化评价**

worthwatch 是一个 CLI 工具，读取用户所关注 YouTube 频道的新视频（优先字幕，可选音频转录），依据用户编写的 context.md 项目描述与 rules.toml 代码规则，由 LLM 判定视频是否值得观看并生成摘要，输出每日 digest。评价中的引用须逐字匹配转录文本，否则删除。提供 MCP 服务器与插件，供 Claude Code、Codex、Cursor 等 agent 调用八类工具。支持 agent/ollama/Gemini/Claude/Codex/API 多种模型后端，无需 GPU，数据存本地。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按用户 context.md 与 rules.toml 规则生成个性化视频判定与 digest
- 引用须匹配转录原文的校验机制，模型输出后由代码规则复核
- 内置 MCP 服务器（八类工具）与 Claude Code 插件安装方式
- 多模型后端：agent 模式、ollama 本地模型、Gemini 免费档、OpenAI/Groq/OpenRouter API

## 适用场景

- 跟踪多个 YouTube 频道而不逐条观看，筛出与自己项目相关的视频
- 把订阅内容判定接入 Claude Code 等 agent 的工作流
- 用本地 Ollama 模型在离线状态下运行视频评价

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: worthwatch checks the YouTube channels you follow and tells you which new videos are worth your time.
> L42: - **Made for AI agents.** An MCP server and a skill, so Claude Code, Codex, Cursor and others can
> L127: `worthwatch mcp` is an MCP server with eight tools: check your channels for new videos, read a

## 星数曲线

```mermaid
xychart-beta
    title "mokshtheverma-max/worthwatch 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `76b148bcc090` · [字段定义](../../DATASET.md)*
