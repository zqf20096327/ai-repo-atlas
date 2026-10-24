# meer-ai/meer

⭐ 61 · TypeScript · MIT · 推送 2026-07-02 · [GitHub](https://github.com/meer-ai/meer) · [官网](https://meerai.dev) · 组织维护

**本地优先的开源终端 AI 编程助手，连接本地或远程模型**

面向开发者的 TypeScript 终端 AI CLI：连接本地 Ollama 模型或远程提供商（Meer Managed、OpenRouter、OpenAI、Anthropic、Gemini、DeepSeek、Z.AI），提供交互式 TUI 聊天、无头脚本模式（meer run/--print）、仓库问答（meer ask）、代码审查与提交信息生成。内置 60+ 结构化工具（文件读写、git、语义搜索、测试生成、安全扫描）、可恢复会话与长期记忆、Agent Skills（兼容 Claude Code/Codex 技能目录）与生命周期 Hooks。默认本地私有，配置存于 ~/.meer/。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地优先：默认连接本地 Ollama 模型，数据不出机器
- 60+ 结构化工具与 MCP 服务器自动加载
- 无头模式 meer run/--print 输出文本或 JSON 事件，可用于 CI 与脚本
- Agent Skills 兼容 Claude Code 与 Codex 的技能目录，Hooks 支持生命周期命令

## 适用场景

- 在终端里与代码库对话、生成提交信息与做代码审查
- 本地 Ollama 模型完成私有化编程辅助，不依赖云端
- CI/脚本中用无头模式自动执行编程任务
- 复用已有的 Claude Code/Codex 技能扩展 agent 能力

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L4: **MeerAI** (from the German word _"Meer"_ — *sea*) is an **open-source, local-first AI CLI** for developers.
> L17: - **Local-first or cloud-smart** — chat with local Ollama models, Meer Managed, or remote APIs (OpenAI, Anthropic, 
> L29: |**Chat (`meer`)**|Interactive TUI with streaming responses, plan tracking (restored on resume), tool timeline, dif

## 星数曲线

```mermaid
xychart-beta
    title "meer-ai/meer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-24 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ed4fd630f4fc` · [字段定义](../../DATASET.md)*
