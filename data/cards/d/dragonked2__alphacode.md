# dragonked2/alphacode

⭐ 682 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/dragonked2/alphacode) · [官网](https://alphacli.github.io/) · 个人维护

**终端 AI 编码 agent：开发者免 API key 即可自动改码跑测试**

用 Rust 编写的终端内 AI 编码 agent，以原生二进制分发。工作循环为理解项目、规划、执行（编辑文件、运行命令与测试、搜索网页）、验证并报告变更。内置免费模型，无需 API key 即可启动，也可接入 Claude、GPT、Gemini、DeepSeek、Ollama 等 OpenAI 兼容端点。提供 40+ 工具、Firefox 浏览器与桌面应用自动化、Swarm 多 agent 并行模式、会话持久化与风险操作确认。Windows/macOS/Linux 提供一行安装脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置免费模型，无需 API key 与注册即可启动
- Rust 原生二进制，单会话约 28 MB 内存（自述基准）
- 40+ 内置工具：文件、shell、网页、Firefox 与桌面自动化
- Swarm 模式将大目标拆分给并行 agent；会话可恢复

## 适用场景

- 在终端里让 agent 定位并修复失败测试后重跑验证
- 不打开 IDE，用自然语言给项目加功能或重构
- 用 Firefox agent 自动化测试 Web 表单
- 用 Swarm 模式从架构、安全、测试多角度并行分析代码库

## 场景标签

`编码 Agent` `多智能体` `GUI 自动化` `浏览器自动化` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Built in Rust. Understands your codebase, edits files, runs commands and tests, drives a real Firefox session, con
> L115: It is an open-source alternative to terminal coding agents such as Claude Code, Codex CLI, Aider, and OpenCode, wi

## 星数曲线

```mermaid
xychart-beta
    title "dragonked2/alphacode 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 421 --> 705
    line [444, 459, 478, 479, 491, 504, 513, 521, 526, 444, 571, 582, 587, 600, 610, 618, 623, 626, 628, 629, 631, 635, 640, 658, 674, 678, 682]
```

2026-10-25 444 → 2026-11-27 682（+238）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `be1653e8e0cc` · [字段定义](../../DATASET.md)*
