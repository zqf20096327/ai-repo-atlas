# GetStream/meeting-summary-ollama-gemma

⭐ 27 · Python · 推送 2026-05-20 · [GitHub](https://github.com/GetStream/meeting-summary-ollama-gemma) · [官网](https://youtu.be/d3Y9kwufJp0) · 组织维护

**用 Python+Ollama+Gemma 生成会议转录摘要的示例工具**

配套 YouTube 视频的示例仓库：读取经转录的会议数据（如来自 Stream Video SDK），预处理后送入通过 Ollama 运行的 gemma:2b 模型，输出会议摘要。本体是 Python 脚本工具而非可复用库，README 未给出安装或运行命令，仅说明所用工具链与流程，主要作为教程配套代码提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取会议转录文本并预处理后送入模型
- 使用 Ollama 运行 gemma:2b 生成摘要
- 配套 YouTube 视频的教程示例代码

## 适用场景

- 学习如何用 Ollama 与 Gemma 搭建摘要生成工具
- 为自己的会议转录数据生成 AI 摘要

## 场景标签

`教程课程` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L13: It takes data transcribed from a meeting (e.g. using the Stream Video SDK) and preprocesses it first.
> L14: Then, it is fed to the Gemma model (in this case, the `gemma:2b` model) to produce a summary.

## 星数曲线

```mermaid
xychart-beta
    title "GetStream/meeting-summary-ollama-gemma 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `3c9e879b3bfa` · [字段定义](../../DATASET.md)*
