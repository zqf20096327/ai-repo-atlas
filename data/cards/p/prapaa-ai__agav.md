# prapaa-ai/agav

⭐ 204 · TypeScript · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/prapaa-ai/agav) · [官网](https://agav.dev) · 组织维护

**终端内运行的自主编码 agent：检查代码、改文件、跑测试**

以单一自包含二进制分发的终端原生编码 agent：读取仓库结构、编辑文件、运行测试并验证改动，支持交互模式与面向脚本/CI 的非交互模式（agav run，可选 JSON Schema 输出）。机制上围绕'每次模型调用'做成本控制：上下文缓存复用、中断无效修复循环、限制重试与预算、子 agent 隔离探索；提供会话恢复/分支、跨会话记忆、技能与子 agent 市场、/undo 与 LSP 查询。Apache 2.0，本地优先，工具按动作授权，macOS/Linux 可沙箱运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 单命令自包含安装，无需 Node.js
- 多 provider 接入：OpenAI/OpenRouter/NVIDIA NIM/Gemini/Vertex AI/Ollama，可中途切换模型
- 非交互 agav run 支持 CI 与 JSON Schema 输出、按工具权限控制
- 会话可恢复/分支/导出，跨项目记忆与子 agent 委派

## 适用场景

- 在终端里让 agent 完成跨文件改动并自动跑测试验证
- 在 CI 中以非交互模式执行受限的仓库任务
- 用 Ollama 本地模型运行编码 agent
- 通过后台任务保持长时命令与定时任务运行

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **Terminal-native autonomous agent for real repositories and projects**
> L96: * **Non-interactive mode** — `agav run` and `agav --print` with per-tool permissions and optional JSON Schema outpu

## 星数曲线

```mermaid
xychart-beta
    title "prapaa-ai/agav 星数(近 17 点)"
    x-axis ["2026-10-23", "2026-10-29", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 167 --> 207
    line [170, 171, 173, 170, 175, 177, 178, 181, 182, 183, 185, 188, 194, 198, 201, 203, 204]
```

2026-10-23 170 → 2026-11-25 204（+34）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `643cca8552a8` · [字段定义](../../DATASET.md)*
