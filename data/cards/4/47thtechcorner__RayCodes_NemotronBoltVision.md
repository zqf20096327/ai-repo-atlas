# 47thtechcorner/RayCodes_NemotronBoltVision

⭐ 3 · HTML · 推送 2026-11-24 · [GitHub](https://github.com/47thtechcorner/RayCodes_NemotronBoltVision) · [官网](https://youtu.be/HZBvr3SJr2Y) · 个人维护

**本地 4GB 显存多模态视觉流水线：离线 OCR/屏幕审计**

基于 NVIDIA Nemotron 3.5 Bolt E4B（mmproj 多模态投影器）与 Ollama/llama.cpp 的离线视觉流水线，在 4GB VRAM 内运行。提供三个生产测试工作流：收据视觉审计、幻灯片架构解析、屏幕隐私扫描（检测暴露的 JWT/.env/私钥）。README 给出 Windows PowerShell 快速启动步骤：创建 venv、pip 安装依赖、拉取权重并注册运行时后运行 main.py。License 表与模型架构说明部分在页面中列为占位条目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mmproj 多模态投影器支持屏幕阅读、文档 OCR 与 computer-use 工作流
- 4GB VRAM 内完全离线运行多模态推理
- 三个生产测试工作流：收据审计、幻灯片合成、隐私哨兵
- 附带 YouTube 视频教程

## 适用场景

- 直播/共享屏幕前自动扫描暴露的密钥并告警
- 离线从收据提取行项目、税号、日期生成结构化报表
- 把多层架构幻灯片转换为简报卡片和结构化文档
- 监控 Grafana/Datadog 面板并在异常时输出诊断

## 场景标签

`多模态` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L14: > *"NVIDIA-Nemotron-3.5-Bolt-E4B pairs Gemma 4's Per-Layer Embeddings architecture with pure reinforcement learning
> L20: |**Screen & Receipt Visual Auditor**|Offline document OCR and low-token structured extraction|Commercial expense re
> L31: pip install ollama pillow mss requests


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `93bebd0e40c4` · [字段定义](../../DATASET.md)*
