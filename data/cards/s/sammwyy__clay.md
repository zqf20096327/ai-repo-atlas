# sammwyy/clay

⭐ 24 · C · 推送 2026-08-25 · [GitHub](https://github.com/sammwyy/clay) · 个人维护

**终端里的紧凑 AI 编码代理外壳，自带多模型接入**

Clay 是一个面向偏好终端工作流的编码代理 harness：以单个自包含二进制分发（除 libcurl 外无第三方依赖），可连接 OpenAI、OpenAI Codex、Grok、OpenRouter、Groq、DeepSeek、Mistral、Together AI 及任意 OpenAI 兼容端点。提供 read/write/edit 等文件工具、Linux 下默认沙箱化的 shell 执行、基于 git 的检查点与 /undo、跨会话长期记忆、自动上下文折叠 /compact、并行 subagent 委派、MCP stdio 工具接入与 SKILL.md 技能按需加载。当前版本 v0.0.4；Windows 仅支持 Unleashed 模式（无沙箱）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个自包含二进制，除 libcurl 外无第三方依赖
- Linux 默认沙箱：独立文件系统/网络/资源限制，四模式切换
- 每次写/编/执行前自动快照到 git 仓库，/checkpoints 可恢复任意点
- 最多四个 subagent 并行执行 todowrite 计划的独立分支

## 适用场景

- 在终端中让 AI 直接读写工作区文件完成编码任务
- 以非交互 -p 模式接入 CI 跑测试并汇总失败
- 通过 MCP 与 SKILL.md 技能扩展代理能力

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: Clay is a compact coding-agent harness built for people who prefer to stay in the terminal. It connects to the mode
> L27: |**Your models, your choice**|Connect OpenAI, OpenAI Codex (ChatGPT Plus/Pro), Grok, OpenRouter, Groq, DeepSeek, Mi
> L21: No giant framework to learn. No crowded dashboard. A single self-contained binary, no third-party dependency beside

## 星数曲线

```mermaid
xychart-beta
    title "sammwyy/clay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `70db848a8cc0` · [字段定义](../../DATASET.md)*
