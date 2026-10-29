# chocks/locode

⭐ 23 · TypeScript · MIT · 推送 2026-06-20 · [GitHub](https://github.com/chocks/locode) · [官网](https://locodecli.com) · 个人维护

**本地优先的 AI 编程 CLI：简单任务走 Ollama，复杂任务走 Claude**

面向开发者的命令行 AI 编程工具：交互式 REPL 与单次任务执行，通过 regex 路由规则与置信度阈值把简单任务交给本地 Ollama 模型、复杂任务升级到 Claude，以降低 token 消耗。提供本地模型评测（eval-local-models）、按平台/CPU/内存推荐模型、token 成本对比基准（benchmark）等命令。未设置 Anthropic API key 时自动降级为纯本地模式。README 声明为 Alpha 阶段软件，不建议生产使用。遥测默认关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地/云端双层路由：regex 规则 + 置信度升级阈值
- 本地模型工具调用可靠性评测与按机器配置（CPU/RAM）的模型推荐
- REPL 内 stats 命令展示 token 用量与节省估算
- 无 API key 时自动降级为 local-only 模式

## 适用场景

- 日常编码中用本地模型处理简单任务以节省 API token
- 评估本机最适合跑的 Ollama 编程模型
- 对比不同路由模式下的 token 成本

## 场景标签

`编码 Agent` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L8: Local-first AI coding CLI. Routes simple tasks to a local LLM (Ollama), complex tasks to Claude. Saves tokens.
> L35: |`locode`|Interactive REPL (default)|
> L157: - Simple prompts (e.g., `grep`) route to local LLM

## 星数曲线

```mermaid
xychart-beta
    title "chocks/locode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f315b930fa7f` · [字段定义](../../DATASET.md)*
