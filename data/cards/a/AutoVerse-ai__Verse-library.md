# AutoVerse-ai/Verse-library

⭐ 39 · Jupyter Notebook · NCSA · 推送 2026-10-11 · [GitHub](https://github.com/AutoVerse-ai/Verse-library) · [官网](https://autoverse-ai.github.io/Verse-library/) · 组织维护

**多智能体混合系统场景的建模、仿真与形式化验证库**

UIUC Reliable Autonomy 研究组维护的 Python 库，用于创建、仿真并验证含决策智能体的交互场景：智能体决策逻辑用 Python 子集编写并被解析为 AST 构建混合自动机，连续演化以黑盒函数描述，地图可从零定义或导入 opendrive 文件。分析层提供 Simulator 与 Verifier，基于混合可达性算法（默认后端 DryVR、NeuReach，NeuReach 需 git submodule 拉取依赖）。要求 Python 3.8+，源码方式 pip 安装，附 Jupyter 与 PDF 教程及 demo 示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | NCSA |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 智能体决策逻辑以 Python 子集编写，解析为 AST 构建混合自动机
- 基于混合可达性分析的 Simulator 与 Verifier
- 地图支持从零定义或导入 opendrive 文件
- 可达集计算支持 DryVR / NeuReach 可插拔后端

## 适用场景

- 为自动驾驶等自主智能体场景做形式化安全验证
- 构建并仿真多智能体交互场景
- 复现论文中的混合系统验证实验（CAV/ATVA 等发表）

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Verse is a Python library for creating, simulating, and verifying scenarios with interacting, decision making agents
> L45:  - **verse/scenario** Scenario base class. A scenario is constructed by several **agents** with continuous dynamics

## 星数曲线

```mermaid
xychart-beta
    title "AutoVerse-ai/Verse-library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f00e0b5c5106` · [字段定义](../../DATASET.md)*
