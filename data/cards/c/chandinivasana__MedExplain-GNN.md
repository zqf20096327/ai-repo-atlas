# chandinivasana/MedExplain-GNN

⭐ 10 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/chandinivasana/MedExplain-GNN) · [官网](https://frontend-peach-five-22.vercel.app) · 个人维护

**医学科研者用 GAT+知识图谱做可解释疾病预测与饮食禁忌推理**

容器化微服务架构的临床推理引擎：前端收集症状描述，FastAPI 网关编排请求，AI 服务用 BioBERT 抽取症状实体并经 PyTorch Geometric 的 GAT 推理输出疾病预测与饮食禁忌，Neo4j 存储疾病-症状-食物关系图，Redis/RQ 处理异步任务，MongoDB 记录日志。解释机制基于注意力权重定位关键节点；针对过平滑与拓扑偏置采用 8 头注意力、Focal Loss 与嵌入缩放。声明仅限研究与教育用途，非医疗器械。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BioBERT 症状抽取 + GAT 校准推理的端到端管线
- 注意力权重驱动的预测解释生成
- Neo4j 知识图谱存储疾病/症状/食物禁忌关系
- 提供 setup.sh 一键容器编排、数据库灌种与模型校验

## 适用场景

- 从非结构化症状文本获得疾病预测与饮食禁忌建议
- 研究 GNN 在临床信息学中的可解释推理方法
- 复现或重训 GAT 模型并运行评估管线

## 场景标签

`知识图谱` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L13: **MedExplain-GNN** is an end-to-end, graph-based medical reasoning engine. It leverages Graph Attention Networks (G
> L28: 3. **AI Engine (FastAPI + PyTorch Geometric):** Extracts symptoms via BioBERT and performs calibrated GAT inference

## 星数曲线

```mermaid
xychart-beta
    title "chandinivasana/MedExplain-GNN 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `a7a1553bc374` · [字段定义](../../DATASET.md)*
