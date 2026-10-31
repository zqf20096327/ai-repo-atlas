# RhinoDevel/mt_llm

⭐ 15 · C++ · MIT · 推送 2026-09-06 · [GitHub](https://github.com/RhinoDevel/mt_llm) · 个人维护

**封装 llama.cpp 的纯 C 接口库，用于单用户 LLM 推理**

C++ 编写、对外提供纯 C 接口的库，封装 llama.cpp 推理引擎，面向 Linux 与 Windows 上的单用户 LLM 推理。提供简化配置、init/query/reset/deinit 函数、嵌入向量生成、重排序打分、基于 RAM 的状态快照、回调控制推理停止与获取数字 token 概率、自动处理提示模板的整段对话插入等能力，读取 GGUF 模型文件。Linux 下用脚本/Makefile 从源码构建，Windows 需 Visual Studio 编译静态库并链接，CUDA 为可选构建路径。附带 STT→LLM→TTS 流水线 C 示例。

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

- 纯 C 接口封装 llama.cpp，简化配置参数
- 嵌入向量生成与重排序打分接口
- 基于 RAM 的 LLM 状态快照（存储/更新/重置）
- 自动处理提示模板，支持插入完整对话与回调控制推理

## 适用场景

- 在自己的 C/C++ 程序中集成单用户 LLM 推理
- 通过嵌入模型生成向量或用重排序模型打分
- 构建语音到语音的 STT-LLM-TTS 流水线

## 场景标签

`推理引擎` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: **mt_llm** is a C++ library for Linux and Windows that offers a pure C interface
> L9: **mt_llm** is intended to be used for single-user LLM inference.

## 星数曲线

```mermaid
xychart-beta
    title "RhinoDevel/mt_llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9acd3cc2d00f` · [字段定义](../../DATASET.md)*
