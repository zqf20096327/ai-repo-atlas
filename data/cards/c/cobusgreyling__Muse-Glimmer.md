# cobusgreyling/Muse-Glimmer

⭐ 25 · JavaScript · NOASSERTION · 推送 2026-08-10 · [GitHub](https://github.com/cobusgreyling/Muse-Glimmer) · [官网](https://huggingface.co/meta-models/Muse-Glimmer-30B) · 个人维护

**Muse Glimmer 30B 本地 agent 模型的离线交互实验室与指南**

围绕 Meta 开放权重 30B agentic 多模态模型 Muse Glimmer 的非官方教育配套仓库：提供离线优先的交互式实验室（FastAPI + 浏览器 UI），展示 agent 循环、失败恢复、基准对比与内存占用计算，场景回放使用示意性 fixture 数据；可选接入自有 llama.cpp GGUF 服务或 Hugging Face Inference Endpoint 做 OpenAI 兼容实时对话。面向想在下载权重前了解该模型能力的开发者，附长文 BLOG.md。仓库代码 MIT，模型权重为 Meta 的 Apache 2.0 发布，基准数字取自公开发布材料。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 离线交互实验室：agent 循环、基准计分板、内存 envelope 计算器
- 可选 OpenAI 兼容实时对话，支持 llama.cpp GGUF 或 HF Inference Endpoint
- REST API 暴露场景 fixture、模型卡、基准数据与内存估算
- Docker compose 一键运行，无需 GPU 与 API key 即可离线演示

## 适用场景

- 下载权重前体验 agent 循环、失败恢复与多模态工具调用场景
- 估算 4-bit 量化下运行 30B 模型的内存需求
- 查找运行该模型的途径（GGUF、transformers、云推理）

## 场景标签

`多模态` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L15: This repository is a **search-friendly companion**: a long-form intro (`BLOG.md`) plus an **offline-first interacti
> L171: This lab is an **independent educational companion**, not an official Meta product.

## 星数曲线

```mermaid
xychart-beta
    title "cobusgreyling/Muse-Glimmer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `0b71143fcedb` · [字段定义](../../DATASET.md)*
