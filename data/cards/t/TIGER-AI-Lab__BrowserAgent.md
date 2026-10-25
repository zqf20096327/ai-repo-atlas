# TIGER-AI-Lab/BrowserAgent

⭐ 37 · Python · MIT · 推送 2026-01-13 · [GitHub](https://github.com/TIGER-AI-Lab/BrowserAgent) · [官网](https://tiger-ai-lab.github.io/BrowserAgent/) · 组织维护

**浏览器操作 Web Agent 研究框架：模型、数据集与训练评测全流程**

TMLR 2025 论文配套研究框架，构建能以类人浏览器操作完成网页任务的 agent。提供 SFT 与 RFT 模型权重、种子数据集与训练数据集，流程包括：本地 Docker 部署 Wikipedia（WebArena 环境）、vllm 部署模型、生成 SFT/RFT 训练数据并转换为 ms-swift 格式、以规则或模型方式评测准确率。面向从事 web agent 研究与训练的开发者和科研人员，需自行准备 conda 环境与本地部署组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 SFT/RFT 模型权重与配套数据集（Hugging Face）
- SFT/RFT 训练数据生成与 ms-swift 格式转换脚本
- 支持规则与模型两种准确率评测方式
- 本地 Docker 部署 Wikipedia 网页环境

## 适用场景

- 复现论文中的 web agent 训练与评测流程
- 生成 SFT/RFT 数据训练自己的浏览器 agent 模型
- 在 WebArena 风格环境中评测 web agent 准确率

## 场景标签

`浏览器自动化` `模型评测` `微调` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L2: An agent that can interact with browser to complete tasks. Our paper (https://arxiv.org/abs/2510.10666) has been acc
> L61: Download 📊 BroswerAgent-SFT or 📊 BroswerAgent-RFT, and deploy using vllm.

## 星数曲线

```mermaid
xychart-beta
    title "TIGER-AI-Lab/BrowserAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `32248c62ea40` · [字段定义](../../DATASET.md)*
