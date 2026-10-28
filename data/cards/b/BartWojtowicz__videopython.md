# BartWojtowicz/videopython

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/BartWojtowicz/videopython) · [官网](https://videopython.com/) · 个人维护

**面向 Python 与 AI agent 的本地视频编辑库：JSON 计划+流式渲染**

Python 库，将视频编辑表示为经校验的 Pydantic 模型或 JSON 计划，计划来源可为代码、LLM 或 MCP 客户端，经由同一流式引擎渲染，帧缓冲有界以控制内存。核心编辑功能不安装 PyTorch 等模型运行时，可选的 ai/mcp 扩展加入转录、场景理解、生成、配音、自动编辑等本地 AI 能力及 MCP 服务器。声明 pre-1.0，公开接口可能变动；不提供托管推理服务或交互式编辑应用。安装需先装 FFmpeg 再 pip/uv 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 编辑以 Pydantic 模型/JSON Schema 表示，渲染前校验尺寸与约束
- 流式解码/处理/编码，长视频内存占用有界
- 可选本地 AI：转录、检测、场景理解、生成、配音、自动编辑，无需云端推理 API
- 内置 MCP 服务器，向 agent 暴露分析、规划、校验、渲染工具

## 适用场景

- 用 Python 代码或 LLM 生成的 JSON 计划做程序化视频剪辑
- 为 AI agent 提供本地视频分析与渲染工具
- 在低内存环境下处理长视频的剪切、特效、字幕等流水线

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L8: Structured, local-first video editing for Python and AI agents.
> L26: - **Local AI** — add transcription, scene understanding, generation, dubbing, and
> L62: Core editing does not install PyTorch or other model runtimes. AI dependencies load only

## 星数曲线

```mermaid
xychart-beta
    title "BartWojtowicz/videopython 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `02d8720b702f` · [字段定义](../../DATASET.md)*
