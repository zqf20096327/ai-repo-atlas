# ZySec-AI/project-zysec

⭐ 79 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/ZySec-AI/project-zysec) · [官网](https://www.zysec.ai) · 个人维护

**面向安全专业人员的私有化网络安全 AI 助手（ZySec 7B）**

基于 Streamlit 的网络安全助手应用，搭载专门训练的 ZySec 7B 模型（构建于 Zephyr 系列，覆盖 30 余个安全领域），提供专家问答、Playbook 与文档检索、标准查询及可选的联网研究功能；默认离线运行以保障隐私。可本地通过 llama-cpp-python[server] 由 start.sh 一键下载模型并启动，也可远程部署到 GPU 实例，推荐 vLLM 服务（需兼容 openai API 格式）。限制：联网功能为可选项，仅限研究特性使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 搭载 ZySec 7B 网络安全专用模型（基于 Zephyr，30+ 领域训练）
- Playbook/文档检索与标准查询功能
- 默认离线运行保护隐私，联网研究为可选功能
- 支持本地 llama-cpp-python 或远程 GPU + vLLM 两种部署方式

## 适用场景

- SOC 值班时获取安全专家级问答支持
- 快速检索自有 Playbook、文档与安全标准
- 在无外网的隔离环境中运行私有安全 AI 助手

## 场景标签

`网络安全` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L12: 1. **AI-Driven Cybersecurity:** Experience the full potential of the ZySec 7B model, a specialized AI tool for cybe
> L30: **ZySec 7B**, the cornerstone of ZySec AI, is built on HuggingFace's Zephyr language model series. Custom-designed 

## 星数曲线

```mermaid
xychart-beta
    title "ZySec-AI/project-zysec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-24 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `df0cbef03fd6` · [字段定义](../../DATASET.md)*
