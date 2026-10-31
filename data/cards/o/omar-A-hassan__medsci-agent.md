# omar-A-hassan/medsci-agent

⭐ 17 · TypeScript · MIT · 推送 2026-09-06 · [GitHub](https://github.com/omar-A-hassan/medsci-agent) · 个人维护

**给科研用户的生物医学研究 Agent：28 个 MCP 工具**

开源生物医学研究代理，向任意 LLM（经 OpenCode 编排）提供 28 个 MCP 工具，覆盖药物 ADMET 预测（TxGemma 模板）、蛋白结构检索（UniProt/PDB/AlphaFold）、文献检索与政策受控全文获取、医学影像解读（MedGemma 多模态）、单细胞 RNA-seq 分析（Scanpy）与 Docker 沙箱执行。核心模型调用默认走本地 Ollama，MedGemma 不可用时优雅降级（synthesize=false 跳过解读）。安装需 Bun、uv、Ollama、OpenCode；沙箱工具另需 Docker Desktop 4.40+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 28 个 MCP 工具覆盖药物、蛋白、文献、影像、组学、沙箱六类
- 核心模型默认本地 Ollama（MedGemma/TxGemma），可 synthesize=false 降级为原始数据
- Python sidecar 预导入科学库（RDKit/Scanpy）避免每次调用 2-5 秒启动开销
- PaperQA 深度合成与策略受控文档获取链路（BioC/Scrapling 双后端）

## 适用场景

- 让 LLM 编排药物类药性与 ADMET 六项安全性预测
- 对 H5AD 单细胞数据做预处理、聚类与差异表达分析
- PubMed/OpenAlex/ClinicalTrials.gov 文献检索与全文深度综合
- 在隔离 Docker 沙箱中执行不可信计算命令

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: MedSci Agent gives any LLM access to 28 biomedical and execution tools — drug ADMET prediction, protein structure s
> L42: You bring your own LLM. Configure any model in OpenCode (via `/model`) and it becomes the orchestrator — it reads y

## 星数曲线

```mermaid
xychart-beta
    title "omar-A-hassan/medsci-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `af16f2fa4bc5` · [字段定义](../../DATASET.md)*
