# kamrul1157024/terminal-ai

⭐ 16 · TypeScript · MIT · 推送 2026-02-11 · [GitHub](https://github.com/kamrul1157024/terminal-ai) · [官网](https://www.npmjs.com/package/terminal-ai-tool) · 个人维护

**把自然语言转为终端命令并执行的 CLI 应用**

Node.js/npm 分发的命令行工具：将用户的自然语言请求转换为终端命令并执行，提供非交互单命令模式与交互式 agent 模式（建议命令、说明理由、危险命令前确认、输出回传分析、多步上下文）。另支持管道输入处理、线程管理（跨会话保留对话上下文）与多 provider 配置档案切换，附费用追踪（README 自述不完全准确）。模型接入支持 OpenAI gpt-4o/gpt-4o-mini 与经 Ollama 的 llama3.2，Claude/Gemini 为规划支持。

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

- 自然语言转单条终端命令并执行，危险命令需确认
- 交互式 agent 模式：命令建议、理由说明、输出回传分析、多步上下文
- 线程机制跨会话保留对话上下文，可列表/附加/重命名/删除
- 多 provider 配置档案切换与命令费用追踪

## 适用场景

- 用自然语言完成文件查找、项目搭建等终端任务
- 跨多次会话持续跟进一个多步骤任务
- 在 OpenAI 与本地 Ollama 模型间切换使用

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: A CLI application that uses AI to process natural language commands and execute them in the terminal.
> L5: It supports openAI gpt-4o, gpt-4o-mini and llama3.2 through ollama. It will support claude and gemini soon.

## 星数曲线

```mermaid
xychart-beta
    title "kamrul1157024/terminal-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d7fbb61bf97a` · [字段定义](../../DATASET.md)*
