# jackvial/lerobot-data-studio

⭐ 58 · TypeScript · MIT · 推送 2026-07-06 · [GitHub](https://github.com/jackvial/lerobot-data-studio) · 个人维护

**非官方的 LeRobot 数据集网页编辑器：删除 episode 生成干净数据集**

基于 LeRobot dataset tools API 构建的 Web GUI，用于编辑 LeRobot 机器人学习数据集：在界面中浏览并选择 episode、删除后生成新的过滤数据集并上传至 Huggingface Hub，全程非破坏性（始终新建数据集）。支持播放速度控制与键盘快捷键以加快数据集清理流程。需要 UV 包管理器、Python 3.10+、Node.js 24+ 与 Huggingface 账号，从源码克隆安装，脚本同时启动前后端服务。合并多数据集需另行使用 LeRobot datasets tool CLI。项目为非官方工具，与 Huggingface/LeRobot 团队无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网页界面选择并删除 episode，生成新的过滤数据集
- 非破坏性编辑：始终创建新数据集并上传 Huggingface Hub
- 播放速度控制与键盘快捷键辅助数据集清理

## 适用场景

- 清理 LeRobot 机器人演示数据集中的低质量 episode
- 从已有数据集筛选 episode 生成新数据集并上传 Hub

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: A web-based GUI for editing LeRobot datasets build on the LeRobot dataset tools api
> L65: Dataset creation for filtered (AKA edited) datasets is always none destructive and will always create a new dataset

## 星数曲线

```mermaid
xychart-beta
    title "jackvial/lerobot-data-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-30 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `79c7b4100455` · [字段定义](../../DATASET.md)*
