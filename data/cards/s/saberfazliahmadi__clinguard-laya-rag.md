# saberfazliahmadi/clinguard-laya-rag

⭐ 5 · Python · NOASSERTION · 推送 2026-11-01 · [GitHub](https://github.com/saberfazliahmadi/clinguard-laya-rag) · 个人维护

**医疗 RAG 的安全与事实核查层：拦截误检、提示指南冲突、证据不足时拒答**

面向医疗检索增强生成系统的安全决策层，在检索前后设置五阶段检查点（筛查分诊、检索、拦截误配、事实核查、规则裁决），用快速 System-1 判定模型（Laya/Jev）输出结构化概率，再交由确定性 Python 规则引擎（policy.py）裁决，最终给出五种处置之一并生成 JSON 审计记录。默认离线运行，使用保存的概率数据，普通笔记本无需 GPU 即可跑完测试；自由文本生成部分为模拟实现，实时推理需可选模型权重或服务端。声明非认证医疗设备，不得用于真实患者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五阶段安全管线（筛查、路由、检索、过滤、核查、规则裁决）支持 5 种对比模式
- 混合检索：BM25 关键词 + TF-IDF 余弦向量，经 RRF 融合
- 选项顺序偏置检查与温度校准（T=1.4），降低过度自信评分
- 五种最终处置：验证回答、冲突警示、转人工、拒答、急诊升级，全部输出 JSON 审计记录

## 适用场景

- 为医疗问答 RAG 系统加入检索结果过滤与事实核查
- 检测新旧临床指南之间的冲突并向医生警示
- 在证据不足或问题超出范围时让系统明确拒答
- 离线复现 16 个医疗测试用例的基准评测

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L17: **A safety and fact-checking layer for medical AI search systems (RAG). It filters out wrong look-alike search resu
> L57:  Models like open-weight **Laya** (`convaiinnovations/laya-typed-decisions`, Apache 2.0) and **Jev** (`POST /v1/sys
> L67: |**5-stage safety pipeline** (screening, routing, search, filtering, fact-checking, and rulebook)|**Fully working &

## 星数曲线

```mermaid
xychart-beta
    title "saberfazliahmadi/clinguard-laya-rag 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-26"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-25 5 → 2026-11-26 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `489b903680e3` · [字段定义](../../DATASET.md)*
