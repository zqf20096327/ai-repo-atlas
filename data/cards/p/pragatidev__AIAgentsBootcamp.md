# pragatidev/AIAgentsBootcamp

⭐ 36 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/pragatidev/AIAgentsBootcamp) · 个人维护

**AI Agents 课程配套实训仓库：LangGraph/RAG/多智能体实验**

Udemy 课程《AI Agents Bootcamp》的配套代码仓库，含三次课程重建后的实验体系：每讲对应 labs/ 下的 .py 脚本与 .ipynb 双版本。提供三个完整构建：LangGraph 客服工单台（检索、退款卡、引用与拒答）、研究报告 agent（规划、隔离子代理、落盘报告）、简历筛选 map-reduce 流水线。本地实验默认经 Ollama 运行 qwen3:8b 与 nomic-embed-text，RAG 用 FAISS 索引；克隆后可无 key 运行 pytest。2025 旧版归档于 original-2025 分支不再更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每讲提供 .py 与 .ipynb 双格式实验，按模块/测试/评测/部署组织
- 三个完整构建：LangGraph 客服台、研究报告 agent、简历筛选流水线
- 本地默认 Ollama qwen3:8b + nomic-embed-text，FAISS 索引
- 无 API key 即可 clone 后 pytest 通过（模型调用自动跳过）

## 适用场景

- 跟着课程系统学习 AI agent 开发从入门到进阶
- 参考 LangGraph 客服台与 RAG 拒答机制的工程化写法
- 复用评测集（golden.jsonl）与冒烟测试搭建自己的 agent 项目骨架

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: Companion repo for the Udemy course AI Agents Bootcamp (listing 6521157).
> L5: **Which branch do I need?** The course was rebuilt in September 2026, and the branch you are reading is the rebuilt 

## 星数曲线

```mermaid
xychart-beta
    title "pragatidev/AIAgentsBootcamp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7d665576db58` · [字段定义](../../DATASET.md)*
