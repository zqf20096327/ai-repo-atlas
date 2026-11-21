# siciliatech/visualizador-neuronas

⭐ 3 · HTML · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/siciliatech/visualizador-neuronas) · 个人维护

**本地浏览器可视化工具：实时展示 transformer 逐词生成时的神经元激活**

基于 FastAPI + TransformerLens 的本地工具：模型逐词生成时捕获每层 MLP 神经元的真实后激活，经 WebSocket 推送到浏览器，以神经元地图、激活排名、注意力短语等方式展示，并支持 MoE 专家路由可视化、神经元消融对比（可复现种子）、A/B 对比与 CSV/Parquet 导出。内置 Qwen2.5-0.5B、GPT-2、Pythia-410m 与一个未训练的教学用 MoE 小模型，单次仅加载一个模型。面向教学与探索场景，配有教师指南，每个控件带 '?' 说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 TransformerLens run_with_cache 捕获 MLP 真实激活，WebSocket 实时推送
- MoE 模型可视化 router 选择专家与计算量节省
- 消融实验：关闭神经元/专家后对比生成文本（可复现种子）
- 纯 CPU 运行，无需 GPU；导出激活为 CSV/Parquet

## 适用场景

- 在课堂上向无 AI 背景的学生演示语言模型内部如何工作
- 探索模型生成文本时哪些神经元被激活、注意力看向哪里
- 对同一模型做消融前后生成结果的对比实验
- 离线教室环境预下载模型后进行无网演示

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L20: Técnicamente es una herramienta de **interpretabilidad mecanicista**: captura la activación **real de
> L21: las neuronas de la MLP** con **TransformerLens** y la envía al navegador por WebSocket. No entrena ni
> L106: prompt ──▶ server.py (FastAPI)

## 星数曲线

```mermaid
xychart-beta
    title "siciliatech/visualizador-neuronas 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-21"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-21 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `7db2bfc9587a` · [字段定义](../../DATASET.md)*
