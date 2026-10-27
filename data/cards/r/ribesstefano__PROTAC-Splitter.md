# ribesstefano/PROTAC-Splitter

⭐ 31 · Jupyter Notebook · MIT · 推送 2026-10-14 · [GitHub](https://github.com/ribesstefano/PROTAC-Splitter) · [官网](https://huggingface.co/spaces/ailab-bio/PROTAC-Splitter-App) · 组织维护

**将 PROTAC 分子自动拆分为 E3 配体/连接子/POI 弹头的 ML 框架**

面向药物发现与化学信息学研究者的 PROTAC 子结构自动注释工具：输入 SMILES（字符串、列表或 DataFrame），输出点分隔的 e3.linker.poi 三段 SMILES，附 [*:1]/[*:2] 附着点标注。提供启发式图算法、XGBoost 边分类器与 Seq2Seq Transformer 三类策略，默认 adaptive 策略按 QC 评分逐级升级并报告获胜方法。模型托管于 HuggingFace Hub 首次使用自动下载。可用形式包括 Python API、CLI、HTTP 服务与 Gradio 应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种拆分策略（启发式/XGBoost/Transformer）及可组合的级联与 adaptive QC 门控
- 输入支持字符串/列表/DataFrame，输出带附着点编码的三段 SMILES
- XGBoost 与启发式路径无需 GPU，模型自动从 HuggingFace Hub 下载
- 提供 CLI、HTTP 服务（/split 批量接口）与本地 Gradio 应用

## 适用场景

- 批量标注 PROTAC 数据集中的 E3 配体、连接子与 POI 弹头
- 在生成式设计流程中通过 HTTP 服务调用分子拆分
- 整理 PROTAC 分子库时做子结构统计与 QC 检查

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains the program code to split PROTAC molecules into their three constituent substructures: the 
> L162: |`adaptive` *(default)*|QC-gated escalation, not just fallback-on-failure: a small heuristic `(betweenness_thresho

## 星数曲线

```mermaid
xychart-beta
    title "ribesstefano/PROTAC-Splitter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6ee64cc3c27a` · [字段定义](../../DATASET.md)*
