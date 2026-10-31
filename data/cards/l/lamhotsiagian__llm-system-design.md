# lamhotsiagian/llm-system-design

⭐ 21 · Python · NOASSERTION · 推送 2026-07-30 · [GitHub](https://github.com/lamhotsiagian/llm-system-design) · 个人维护

**LLM 系统设计参考平台与交互式实验台（150+离线测试）**

两部分组成：`project/llm_platform` 是纯 Python 标准库实现（无重型框架依赖）的 LLM serving + RAG 参考平台，含路由、安全护栏、Agent 循环、多 Agent 编排、缓存、评测、观测等约 35 个模块与 150+ 离线测试；`lab/llm_lab` 是基于 LangChain + Streamlit 的交互式界面，后端可选本地 Ollama（llama3.1 + nomic-embed-text）或确定性离线模式（无需服务器/GPU/API key）。定位为面向面试与学习的系统设计参考实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Python 标准库实现的 LLM serving + RAG 参考平台，150+ 离线测试
- 约 35 个系统模块：路由、护栏、Agent、多级缓存、评测、观测、网关等
- LangChain + Streamlit 交互式 UI，可视化测试并追踪各系统执行
- 离线确定性后端无需 GPU 与 API key，另有 Ollama 本地模型后端

## 适用场景

- 学习与拆解 LLM 系统设计各组件的参考实现
- 在交互式 UI 中运行与追踪路由、RAG、Agent、护栏等系统
- 准备 LLM 系统设计面试的动手实验环境

## 场景标签

`RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L10: 1. **`project/` (`llm_platform`)**: A minimal, production-shaped LLM serving + RAG reference platform built in pure
> L11: 2. **`lab/` (`llm_lab`)**: An interactive hands-on Streamlit web application built with **LangChain**, backing loca

## 星数曲线

```mermaid
xychart-beta
    title "lamhotsiagian/llm-system-design 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27", "2026-10-31"]
    y-axis "stars" 18 --> 22
    line [19, 20, 21, 21]
```

2026-10-18 19 → 2026-10-31 21（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e7169a13e209` · [字段定义](../../DATASET.md)*
