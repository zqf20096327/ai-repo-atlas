# yigitkonur/cli-localize

⭐ 36 · Python · 推送 2026-02-21 · [GitHub](https://github.com/yigitkonur/cli-localize) · 个人维护

**面向 AI agent 的本地化文件翻译 CLI，支持 7 种格式**

面向 AI agent 设计的翻译命令行工具：将 SRT、JSON、PO、Android XML、iOS .strings、YAML、Flutter ARB 等 7 种本地化文件解析后，用 tiktoken (cl100k_base) 按目标 token 数切分为批次，以 IBF 紧凑格式交给 LLM 翻译，再经 5 层校验（结构、抽取、解码、内容、占位符）重组出译文文件。会话状态持久化到 .loc-*.json，支持崩溃后续跑与失败批次自动重试 3 次。提供分步命令与 oneshot 单轮工作流两种用法，运行时依赖仅 tiktoken 与 pyyaml，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种本地化格式自动识别（SRT/JSON/PO/Android XML/.strings/YAML/ARB）
- tiktoken cl100k_base 的 token 感知分批，输出按 1.2 倍膨胀估算
- IBF 线式紧凑传输格式与 5 层校验流水线
- 可恢复会话与失败批次自动重试（3 次）

## 适用场景

- 我在 agent 工作流中单轮调用 oneshot 翻译 i18n 文件
- 我需要翻译字幕文件且保持上下文连贯
- 大文件翻译中断后从断点继续

## 场景标签

 · 领域:本地化/翻译工具

## 证据(README 行号)

> L1: translation CLI built for AI agents. breaks localization files into token-sized batches, hands them to an LLM in a c
> L21: - **7 localization formats** — SRT, JSON (i18next/react-intl/vue-i18n), PO/POT, Android XML, iOS .strings, YAML (Ra
> L83: auto-creates or resumes a session and returns the next pending batch. designed for single-turn agent workflows.

## 星数曲线

```mermaid
xychart-beta
    title "yigitkonur/cli-localize 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b7510d4e8da1` · [字段定义](../../DATASET.md)*
