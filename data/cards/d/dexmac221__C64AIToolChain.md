# dexmac221/C64AIToolChain

⭐ 29 · C · MIT · 推送 2026-09-05 · [GitHub](https://github.com/dexmac221/C64AIToolChain) · 个人维护

**用 AI agent 开发 Commodore 64 汇编游戏的工具链与基准**

面向 AI agent 的 C64 开发工具链：提供 cc65 交叉编译器、可经 socket 远程监控驱动的 VICE 模拟器（端口 6510）、Python 桥接脚本与开发规则文件，让 agent 设计、构建、试玩并交付 6502 汇编/C 游戏。已测试 Google Gemini 3、Claude Sonnet/Opus/Fable、OpenAI GPT-5.5/Codex 等模型，配合 Claude Code、GitHub Copilot、Cursor 等 harness，以及本地 Ollama VLM（gemma4:12b）做视觉核验。仓库附带十余个由各模型生成的完整游戏与预编译 .prg 文件，可直接在 VICE 中运行；安装需自备 cc65、VICE、Python 3 与 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cc65 交叉编译 + VICE 远程监控 socket + Python 桥接脚本的结构化反馈闭环
- System 1/System 2 双循环：快速 bot 驱动摇杆字节，LLM 仅在异常时介入
- 本地 Ollama VLM 做视觉核验，并与 screen RAM 交叉校验
- 附多个由不同模型生成的完整游戏及预编译 .prg 文件

## 适用场景

- 让 AI agent 在受限老硬件上开发、调试并试玩 6502 游戏
- 作为 agent 多领域自主解决问题的基准与对比案例
- 直接在 VICE 中运行各模型产出的 C64 游戏作品

## 场景标签

`编码 Agent` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L3: **C64AIToolChain** is a Commodore 64 development toolchain designed as a **creative benchmark for AI agents**. An ag
> L141: - **AI Models (tested)**:

## 星数曲线

```mermaid
xychart-beta
    title "dexmac221/C64AIToolChain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ac8ddf2333a5` · [字段定义](../../DATASET.md)*
