# arbade/konsil

⭐ 17 · HTML · MIT · 推送 2026-11-03 · [GitHub](https://github.com/arbade/konsil) · 个人维护

**给患者与临床者的 AI 多专科会诊板：产出带引证、保留异议的病例讨论纪要**

以 Claude Code 插件形式打包（命令、技能与 agent 章程均为可读可改的 Markdown），对患者的书面病史、化验值与影像科报告召集多个独立 AI 专科 agent。关键机制包括盲评轮次、固定唱反调角色（Challenger）、清单官审计、异议台账、会话内引证核验、缺数门与四审计员发布门。明确限制：非医疗器械、不输出单一诊断结论、AI 不在会诊推理中解读影像像素，仅有的 OFF-PROTOCOL 读图路径需逐字输入同意语，输出定位为与临床医生复核的准备材料。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 盲评多专科 agent 会诊，产出保留逐字异议的纪要
- 会话内引证核验：未验证的引证不存在
- DICOM 到 3D 场景的确定性管线（dcm2niix→TotalSegmentator→marching cubes→NiiVue），不经 AI 解读像素
- --solo 单 agent 基线模式用于对比测量

## 适用场景

- 就诊前整理病历资料并生成与医生讨论的问题清单与备查要点
- 对随访病例以 delta 模式复查化验与影像间隔变化
- 把 DICOM 光盘转换为可旋转 3D 场景与切片视图供复习
- 在自己的病例上对比多 agent 会诊与单 agent 的表现

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L18: **Konsil** (Turkish medical vernacular for a multi-physician case conference) convenes a board of **independent AI 
> L45: - Convenes a **blind, adversarial board** with live, verified literature retrieval, and outputs **board minutes**: 
> L16: > **⚠️ What this is not.** Konsil is **not a medical device, not a diagnostic tool, and not medical advice**. It pr


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `f6583c5730aa` · [字段定义](../../DATASET.md)*
