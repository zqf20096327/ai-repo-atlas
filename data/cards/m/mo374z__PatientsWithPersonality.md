# mo374z/PatientsWithPersonality

⭐ 10 · Jupyter Notebook · MIT · 推送 2026-11-23 · [GitHub](https://github.com/mo374z/PatientsWithPersonality) · [官网](https://mo374z.github.io/PatientsWithPersonality/) · 组织维护

**给临床 LLM 研究者：可控人格与选择性披露的患者模拟框架**

论文配套代码库，实现 PWP 患者模拟器：以 HEXACO 六轴人格加语言熟练度参数化患者角色，meta-LLM 在初始化阶段生成行为角色与披露网格（披露网格按问题类别门控事实的原始/淡化/否认/模糊/省略变体），逐轮仅将请求字段送入对话 LLM 生成口语或书面回答。共享接口下重实现 AgentClinic、PatientSim 等 7 个既有模拟器，附带基于 405 份 VHA 转录的医生对齐评测流水线、临床医生标注 GUI（Dash）、情境照护下游基准与 Streamlit 演示。实验数据需自行下载放置，临床医生原始标注未公开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HEXACO 六轴人格参数化与查询条件披露网格
- 共享接口下的 7 个既有患者模拟器重实现
- 基于 405 份 VHA 去标识转录的医生对齐评测流水线
- Streamlit 模拟器 playground 与 Dash 临床医生标注 GUI

## 适用场景

- 大规模基准测试临床 LLM 而无需昂贵用户研究
- 按人格配置与模拟患者进行问诊对话演练
- 复现论文中的模拟器对比与情境照护基准实验

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L15: This repository contains the full code for the paper: the **PWP simulator**, **re-implementations of prior patient 
> L21: Realistic patient simulation is needed to benchmark clinical LLMs at scale without costly user studies. Yet existin
> L69: Model backends are configured in `configs/experiment/models/`. Gemini and Claude run through Vertex AI: authenticat


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `693c2581a858` · [字段定义](../../DATASET.md)*
