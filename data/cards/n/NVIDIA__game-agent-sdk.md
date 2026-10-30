# NVIDIA/game-agent-sdk

⭐ 29 · C++ · Apache-2.0 · 推送 2026-06-16 · [GitHub](https://github.com/NVIDIA/game-agent-sdk) · 组织维护

**游戏内 AI 伴侣开发 SDK：本地 GPU 推理的 C99/C++ 构建块**

面向游戏引擎与原生应用的端侧 AI 伴侣（AI companion）开发工具包：在终端用户 GPU 上本地运行小型语言模型（SLM，约 3.8 GB 显存），提供 C99 ABI 与薄 C++ 封装。API 分三组：有状态的 Agent（自主驱动推理与工具调用链）、无状态的 Chat（应用直接控制推理）、RAG（语义/词法/混合检索）。附带 SLM、两个嵌入模型与重排序模型（约 3 GB），并含扑克助手等示例与 RAG 数据库构建工具。限 Windows 10/11 与 NVIDIA Ampere 及以上 GPU，需 CUDA 12.8 与 570.65 以上驱动，从源码构建需 Visual Studio 2019+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent/Chat/RAG 三组 API，Agent 可自主驱动推理与工具调用链
- SLM 在终端用户 GPU 本地推理，附四个捆绑模型约 3 GB
- BuildRag.exe 从原始文本构建语义或词法 RAG 数据库
- 含扑克助手、多 Agent 共享单模型等示例工程

## 适用场景

- 在游戏引擎中集成本地运行的 AI 伴侣或助手角色
- 构建基于自建知识库的 RAG 对话能力
- 以多 Agent 共享一个 SLM 实现多角色对话

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: The Game Agent SDK provides on-device building blocks for AI companions, with a C99 ABI and a thin C++ wrapper for n
> L5: - **Agent** APIs: stateful APIs that own conversation history and drive the inference loop autonomously, including a

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/game-agent-sdk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-30 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d2a074a7b646` · [字段定义](../../DATASET.md)*
