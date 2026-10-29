# Shweta-Mishra-ai/github-autopilot

⭐ 24 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/Shweta-Mishra-ai/github-autopilot) · 个人维护

**自托管的 AI GitHub App：自动审查 PR、修 bug、扫描密钥**

可自托管的 GitHub App 与 MCP 服务，通过 LLM 提供 27 个斜杠命令（/fix、/improve、/security、/health 等）审查 PR、生成测试、扫描密钥与依赖、输出仓库健康评级；写操作限定维护者，不可逆操作要求确认。模型后端可选 Groq/Gemini/OpenRouter 云端，或 Ollama 完全本地（LLM_LOCAL_ONLY=1 时失败即报错、不回退云端，且有无外泄测试覆盖）。附带 Claude Code 插件、MCP 工具（9 个）、Redis 队列与运维看板；可经 Render 一键部署或 Docker Compose 本地运行（本地 8B 模型约需 6GB RAM）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 27 个 GitHub 评论斜杠命令（修复/审查/测试生成/密钥扫描/健康评级）
- Ollama 本地模式 LLM_LOCAL_ONLY=1 失败即关闭，不回退云端，并有无外泄测试
- 内置 MCP 服务器（9 个工具）与 Claude Code 插件，可从终端/编辑器调用
- 每条评论披露所用模型，夜评套件对照已知 bug 打分

## 适用场景

- 在我自己的基础设施上跑 AI 代码审查，代码不出本机
- 在 issue/PR 评论里用 /fix、/security 等命令让机器人处理任务
- 从终端或 MCP 编辑器（Claude Code/Cursor）审查指定 PR

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: Reviews pull requests, fixes bugs, scans for secrets — from a comment, your terminal, or your editor.
> L28: |🔒 **Your code can stay on your hardware**|Point it at a local Ollama and set `LLM_LOCAL_ONLY=1`. The router then *
> L267: **27 slash commands**, typed straight into a GitHub issue or pull request

## 星数曲线

```mermaid
xychart-beta
    title "Shweta-Mishra-ai/github-autopilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6121cf6d724b` · [字段定义](../../DATASET.md)*
