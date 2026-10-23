# prapaa-ai/agav

⭐ 170 · TypeScript · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/prapaa-ai/agav) · [官网](https://agav.dev) · 组织维护

**终端 AI 编程代理：在 CLI 中读写代码、跑测试、验证修改**

Apache 2.0 的终端自治编程代理，以自包含二进制安装（curl/PowerShell/cmd 脚本），无需 Node.js。可在仓库内检索代码、编辑文件、运行测试并验证修改；支持 7 个模型提供方（Anthropic、OpenAI、OpenRouter、NVIDIA NIM、Gemini、Vertex AI、Ollama），可用 /model 会话中切换模型。提供非交互 agav run 模式（JSON Schema 输出）用于 CI、跨会话记忆、技能与子代理、LSP 仓库感知编辑与沙箱化命令。README 标注为实验性 Beta，预期存在破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 7 个提供方，会话中 /model 切换，支持 Ollama 本地运行
- 非交互 agav run 模式含每工具权限与 JSON Schema 输出，可入 CI
- 会话可恢复/分支/搜索/导出，跨会话项目级记忆
- LSP 查询、测试运行、/undo 与计划 UI 的仓库感知编辑

## 适用场景

- 在终端里让代理审阅、编辑并验证仓库代码
- CI 脚本中非交互执行代码任务
- 用本地 Ollama 模型跑编程代理

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **Terminal-native autonomous agent for real repositories and projects**
> L76: **You choose the brain.** 7 providers — Anthropic, OpenAI, OpenRouter, NVIDIA NIM, Gemini, Vertex AI, Ollama. Switc
> L57: agav run "review the code in src/"

## 星数曲线

```mermaid
xychart-beta
    title "prapaa-ai/agav 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 168 --> 171
    line [169, 170, 170]
```

2026-10-18 169 → 2026-10-23 170（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `98838fd33b52` · [字段定义](../../DATASET.md)*
