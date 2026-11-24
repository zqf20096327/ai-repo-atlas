# Iman/javid-no-code-uncensored

⭐ 19 · MIT · 推送 2026-08-31 · [GitHub](https://github.com/Iman/javid-no-code-uncensored) · 个人维护 · 中文 README

**本地无审查 LLM 选型与部署指南清单**

由 Iman's Lab 编写的参考文档，收录移除拒绝行为的开源权重模型（社区称 abliterated/uncensored），全部可在本地硬件离线运行。指南按参数规模分节（nano/手机/桌面/多 GPU 工作站），标注文件大小、RAM 需求、量化等级、许可证与验证标记（V/R）。部署路径以 Ollama 为主方法，覆盖 LM Studio、llama.cpp 与 Docker，并附量化文件选择与 RAM 匹配说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按参数规模分节收录本地可运行的 abliterated 模型清单
- 标注文件大小、RAM 需求、量化等级（Q8_0 到 Q2_K）与许可证
- 条目带 V（已验证）/R（未经核实）证据标记
- 覆盖从树莓派、Android/iOS 端侧到多 GPU 工作站的部署

## 适用场景

- 为内存受限设备（树莓派/手机）挑选可运行的本地模型
- 通过 Ollama 或 LM Studio 无代码部署本地无审查模型
- 手动从 Hugging Face 下载 GGUF 文件并选择合适量化等级

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L1: # Unrestricted LLMs on Devices
> L12: This reference lists open-weight language models with the refusal behaviour removed. The community calls them "abli
> L195: |ID|Model|Params|Quant|File Size|RAM Needed|Multilingual|Quality|Licence|Ev|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `abfe2417fd0a` · [字段定义](../../DATASET.md)*
