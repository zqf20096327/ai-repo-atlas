# caiomadeira/llama2-psp

⭐ 22 · C++ · 推送 2026-10-01 · [GitHub](https://github.com/caiomadeira/llama2-psp) · [官网](https://caiomadeira.github.io/) · 个人维护

**在 PlayStation Portable 上运行 Llama 2 推理的 C 项目**

将 Llama 2 推理移植到 PSP 掌机的 C 语言实现，基于 ytmytm 的 c64 版本，后者又源自 llama2.c 的移植。支持运行 TinyStories 260K 参数模型（Tiny Llamas 系列），可在真机与 PPSSPP 模拟器上运行。安装方式为从 release 下载版本，将 Llama2PSP 文件夹复制到 PSP/GAME 或将 .ISO 复制到 PSP 根目录的 ISO 目录。附有 Changelog 与技术规格文档，并含论文引用条目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Llama 2 推理的 C 实现移植到 PSP 掌机
- 支持 TinyStories 260K 参数模型
- 支持真机与 PPSSPP 模拟器两种运行方式

## 适用场景

- 在 PSP 掌机或 PPSSPP 模拟器上体验小型语言模型推理
- 研究 LLM 向极低端硬件移植的技术方案

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L2: Inference Llama-2 in C on Playstation Portable (PSP) by Caio Madeira.
> L18: ## Supported models

## 星数曲线

```mermaid
xychart-beta
    title "caiomadeira/llama2-psp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d23ed52375fe` · [字段定义](../../DATASET.md)*
