# matonhp5108/Opencodex

⭐ 53 · TypeScript · MIT · 推送 2026-08-29 · [GitHub](https://github.com/matonhp5108/Opencodex) · [官网](https://marketplace.visualstudio.com/items?itemName=EvaanChowdhry.opencodex-agent) · 个人维护

**VS Code 内的开源免费编码 agent 扩展**

VS Code 扩展，在编辑器内提供编码 agent 循环：读取工作区、制定计划、编辑文件、运行命令，支持子代理、MCP 工具、并行 Git worktree、Chromium 浏览器测试与影子检查点。默认 OpenCode 提供商无需账号或 API key，可切换 OpenRouter、Groq、Gemini、Mistral，或用 Ollama 本地运行模型；API key 存于 VS Code SecretStorage。可从 SKILL.md 包（SkillsMP 或 GitHub）扩展技能。要求 VS Code 1.106.0+，从 Marketplace 安装。

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

- 默认 OpenCode 提供商免账号免 API key 启动，另支持 OpenRouter/Groq/Gemini/Mistral/Ollama
- Ask/Auto edits/Open access 三档审批模式，API key 存于加密 SecretStorage
- 并行 Git worktree、影子检查点、浏览器测试与子代理委托
- MCP 服务器工具与 SKILL.md 技能包（SkillsMP/GitHub）扩展

## 适用场景

- 在 VS Code 里让 agent 按计划实施多步骤代码修改并逐步确认
- 无需 API key 即可开始使用免费模型编码
- 本地 Ollama 模型完成编码任务，提示词不发送云端

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L4:  A free, open-source coding agent inside VS Code.
> L18: Opencodex brings a Codex-style agent loop to the editor you already use. Open a folder, choose a free model, and de
> L38: 4. Complete the one-time setup. The default OpenCode provider needs no account or API key.

## 星数曲线

```mermaid
xychart-beta
    title "matonhp5108/Opencodex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-31 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `74757dcac903` · [字段定义](../../DATASET.md)*
