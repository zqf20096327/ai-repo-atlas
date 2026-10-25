# RCGAI/SimplyRetrieve

⭐ 217 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/RCGAI/SimplyRetrieve) · 组织维护

**本地化私有检索中心生成（RCG）聊天平台，GUI+API**

面向机器学习社区和需要私有部署的用户：提供 GUI 与 API 两种界面的检索中心生成（RCG）聊天平台，支持接入 Hugging Face 上多种规模的开源 LLM（默认 Wizard-Vicuna-13B-Uncensored，检索器默认 multilingual-e5-base），内置私有知识库构建（支持 pdf/txt/docx 等格式，可在 GUI 的 Knowledge Tab 实时追加）、提示工程与检索分析调优模块，支持多用户并发访问。基于 Hugging Face、Gradio、PyTorch、Faiss 构建，可在单块 Nvidia GPU（T4/V100/A100）上运行；安装方式为 git clone 源码后 pip 安装依赖并运行 chat.py。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GUI 与 API 双界面的检索中心生成（RCG）平台
- 完全本地化的私有知识库构建，支持 pdf/docx/html 等 9 种文档格式
- 检索调优模块：提示工程、工具配置与检索分析
- 多用户并发访问（基于 Gradio 队列）

## 适用场景

- 用自有文档和本地开源 LLM 搭建私有聊天问答工具
- 研究检索中心生成方法的可解释性与效率
- 做检索与提示工程实验并分析检索过程
- 在边缘或单 GPU 环境部署本地 AI 助手

## 场景标签

`RAG` `AI 助手` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L10: *SimplyRetrieve* is an open-source tool with the goal of providing a fully localized, lightweight and user-friendly
> L13: - 📚 GUI and API based Retrieval-Centric Generation platform
> L16: - 🧠 Fully localized, private and lightweight access to various sizes of open-source Large Language Models (LLMs)

## 星数曲线

```mermaid
xychart-beta
    title "RCGAI/SimplyRetrieve 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 216 --> 218
    line [217, 217]
```

2026-10-18 217 → 2026-10-25 217（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `79c23df95747` · [字段定义](../../DATASET.md)*
