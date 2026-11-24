# ChenYu1991ppak/deepseek-harness-anatomy

⭐ 10 · Python · MIT · 推送 2026-11-05 · [GitHub](https://github.com/ChenYu1991ppak/deepseek-harness-anatomy) · 个人维护 · 中文 README

**DeepSeek Harness (dsh) 源码研读教程：18 章逐机制拆解**

对 DeepSeek 开源的 agent harness（dsh）的渐进式源码研读教程：以"一条消息变成一条回复"的最小闭环起步，逐章叠加工具执行、上下文压缩、子 agent 委派、权限守卫、跨进程 RPC 与遥测通道，共 18 章。每章附仅用 Python 标准库的可运行教学代码，章末提供 file:line 源码映射表；中英双语，全部引用锚定上游特定 commit。教学简化处均标注 [teaching simplification]。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 章渐进结构，每章只叠加一个机制且均可运行
- 教学代码仅用 Python 标准库，无需依赖与 API key
- 每章末附真实源码 file:line 映射表
- 中英双语版本与术语命名对照表

## 适用场景

- 自己写 agent 框架时参考 dsh 的设计取舍
- 读 dsh 源码时按章节地图逐块理解
- 作为教学或写作 agent 架构的素材
- 把各章教学代码改造成自己的 agent 骨架

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: **18 chapters. One mechanism at a time. Every chapter runnable.** Deconstruct the DeepSeek Harness engineering skele
> L41: - **Each chapter comes with runnable Python teaching code**: `chNN/code/` is self-contained and uses only the stand


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `ac9a74141fdd` · [字段定义](../../DATASET.md)*
