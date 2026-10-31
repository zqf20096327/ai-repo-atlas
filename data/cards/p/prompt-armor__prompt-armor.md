# prompt-armor/prompt-armor

⭐ 15 · Python · Apache-2.0 · 推送 2026-06-03 · [GitHub](https://github.com/prompt-armor/prompt-armor) · [官网](https://pypi.org/project/prompt-armor/) · 组织维护

**离线 LLM 提示注入检测器：5 层并行分析，毫秒级判定**

面向 LLM 应用开发者与安全工程师的提示注入/越狱检测库。Python 安装后提供 analyze() API 与 CLI，5 个分析层（正则、DeBERTa ONNX 分类器、FAISS 相似度匹配 2.5 万已知攻击、结构分析、Isolation Forest 异常检测）并行运行，经训练的逻辑回归元分类器融合评分，输出攻击类别、证据与置信度，无需 LLM 调用、可离线运行。支持 MCP Server、LangChain/FastAPI/Open WebUI 集成与 CI/CD 扫描。内部基准 F1 84.4%（留出集 85.5%±1.2%），需 Python 3.10+，首次运行自动下载模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 层并行分析 + 训练的元分类器评分融合，平均延迟约 24ms
- 识别 8 类攻击（注入、越狱、数据外泄、编码攻击等），离线运行无需 LLM
- 提供 MCP Server、CLI、LangChain/FastAPI/Open WebUI 集成与 CI/CD 扫描
- 基准含泄漏审计：留出集 F1 85.5%±1.2%，零日攻击召回 81%，多语言（EN/DE/ES/FR/PT）

## 适用场景

- 在 LLM 应用入口拦截提示注入与越狱攻击
- 通过 MCP 让 Claude Desktop/Cursor 等客户端在处理输入前先做检测
- 在 CI/CD 流水线中批量扫描 system prompt 文件的安全性

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L13: **prompt-armor** runs 5 analysis layers in parallel, fuses their scores via a trained meta-classifier, and tells yo
> L60: - **L2 Classifier** — DeBERTa-v3-xsmall (22M params) via ONNX Runtime. Understands semantic intent — catches subtle
> L61: - **L3 Similarity** — contrastive fine-tuned embeddings + FAISS IVF cosine similarity against 25,160 known attacks.

## 星数曲线

```mermaid
xychart-beta
    title "prompt-armor/prompt-armor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `eb947e55fc03` · [字段定义](../../DATASET.md)*
