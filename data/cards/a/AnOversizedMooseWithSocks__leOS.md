# AnOversizedMooseWithSocks/leOS

⭐ 25 · Python · MIT · 推送 2026-04-30 · [GitHub](https://github.com/AnOversizedMooseWithSocks/leOS) · [官网](https://discoverleos.com/) · 个人维护

**面向 AI agent 的本地'潜空间操作系统'，以向量几何管理工具与知识**

leOS 是一个本地运行的 agent 基础设施：将知识、工具、路由决策等表示为单位超球面上的向量，通过三阶段动态工具选择（域质心过滤+语义评分+使用历史）从数百上千工具中挑出 6-8 个注入上下文；以'bone'为带类型原子操作，用 FABRIK 规划器组装执行链；分层执行阶梯从纯规则层逐级升级到 0.8B CPU 模型再到 9B GPU 主模型。含 Three.js 3D 桌面（感知层+人机观察窗口）、知识库、范围/计划管理。嵌入模型全部 CPU 运行。面向构建可扩展 agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段动态工具选择，先丢弃 80-90% 工具，只注入 6-8 个最相关工具
- FABRIK 规划器将带类型的 bone 组装成执行链，失败轨迹可被学习规避
- 分层执行阶梯：确定性规则→0.8B CPU 模型→9B GPU 主模型，逐级升级
- 四个 CPU 嵌入模型（nomic-embed 文本/视觉、Qwen3-Embedding、ImageBind）构成共享空间

## 适用场景

- 为拥有大量工具的 agent 解决上下文膨胀与选择困难问题
- 在本地搭建带知识库、计划与范围管理的 agent 工作环境
- 通过 3D 桌面观察并干预 agent 的运行状态

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L34: leOS takes a different approach. Instead of handing the agent a
> L40: **Dynamic tool selection.** The full tool catalog lives in an
> L216: It never calls an LLM directly — when language generation is needed,

## 星数曲线

```mermaid
xychart-beta
    title "AnOversizedMooseWithSocks/leOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `00df1a00e0fd` · [字段定义](../../DATASET.md)*
