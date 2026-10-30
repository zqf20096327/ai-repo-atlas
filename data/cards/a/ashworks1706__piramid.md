# ashworks1706/piramid

⭐ 15 · Rust · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/ashworks1706/piramid) · [官网](https://piramiddb.com) · 个人维护

**面向开发者的 Rust 推理系统：让语言模型在计算中直接使用外部信息**

Piramid 是一个 Rust 编写的 AI 推理系统项目，研究语言模型在计算过程中直接访问和使用外部信息的机制，涉及 GPU 内存管理、KV-cache 复用、检索感知执行与注意力层集成。长期目标是超越基于 prompt 的检索，将外部信息表示、保留并整合进 transformer 计算。提供 curl 安装脚本（预编译 CPU 版）与 cargo 构建（含 CUDA 特性），通过 piramid serve 启动 HTTP 服务（127.0.0.1:6333），另有 pip 安装的 Python 客户端。许可为专有（Proprietary）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 实现，研究模型原生知识集成（GPU 内存管理、KV-cache 复用、检索感知执行）
- 提供预编译 CPU 安装脚本与 cargo 构建（含 CUDA 特性）两种安装方式
- 通过 piramid serve 启动 HTTP API 服务
- 提供 pip 安装的 Python 客户端 SDK

## 适用场景

- 研究者探索检索感知推理与 KV-cache 复用机制
- 开发者本地运行带外部知识集成的小型语言模型服务
- 基于其 HTTP API 与 Python SDK 构建应用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Piramid is a Rust-based AI inference systems project investigating how language models can access and use external i
> L7: It combines low-level systems engineering with research into model-native knowledge integration, including GPU memor

## 星数曲线

```mermaid
xychart-beta
    title "ashworks1706/piramid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 low · 依据 README sha `d4303bcc7c13` · [字段定义](../../DATASET.md)*
