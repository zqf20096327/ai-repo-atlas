# joone/loz

⭐ 261 · TypeScript · 推送 2026-02-17 · [GitHub](https://github.com/joone/loz) · 个人维护

**让 LLM 执行系统命令并支持 Unix 管道的 CLI 工具**

基于 Node.js 的命令行工具：将自然语言指令转译为对应操作系统的 shell 命令（Linux/macOS/PowerShell/cmd），支持 Unix 管道处理其他工具的输出，可自动生成 Git commit message，并提供 ReAct 式 Agent 模式迭代完成编码任务。LLM 后端可在 OpenAI API、Ollama（本地）与 GitHub Copilot 之间切换。安全机制包括危险命令拦截、Safe Mode 逐条确认、沙箱目录限制与默认禁网。经 npm 全局安装或克隆源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转 shell 命令，跨 Linux/macOS/Windows
- Unix 管道模式处理其他命令行工具的输入输出
- Agent 模式以 ReAct 循环迭代执行编码任务（含沙箱/禁网/步数上限）
- loz commit 依据暂存 diff 自动生成 Git 提交信息

## 适用场景

- 用自然语言执行系统命令而无需记忆具体语法
- 把 LLM 嵌入 shell 管道处理命令输出（统计、转换、纠错）
- 让 Agent 自动修复失败测试或完成代码改动
- 自动生成符合规范的 Git commit message

## 场景标签

 · 领域:开发者工具/命令行自动化

## 证据(README 行号)

> L29: Loz is a command-line tool that enables your preferred LLM to execute system commands and utilize Unix pipes, integ
> L74: Loz supports OpenAI API, Ollama, and GitHub Copilot so you can switch between these LLM services easily, using the 

## 星数曲线

```mermaid
xychart-beta
    title "joone/loz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 260 --> 262
    line [261, 261]
```

2026-10-18 261 → 2026-10-22 261（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b2e615273f9f` · [字段定义](../../DATASET.md)*
