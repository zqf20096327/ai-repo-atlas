# SilkePilon/KnowledgeBook

⭐ 58 · TypeScript · MIT · 推送 2026-08-12 · [GitHub](https://github.com/SilkePilon/KnowledgeBook) · 个人维护

**Minecraft 机器人管理平台：用 Web 界面和节点流创建控制机器人**

开源的 Minecraft 机器人管理平台，提供 Web 界面供玩家创建与控制机器人，通过 React-Flow 风格的节点（flow_functions 目录中的 JavaScript 文件）编排机器人行为，内置物品递送、2D 地图视图等工具。README 描述其用开放免费 AI 模型生成可复用节点，但相关文档标注'即将添加'。安装以 Docker Compose 预构建镜像为推荐方式，也可用 Node.js 22+ 与 pnpm 手动运行；用户可按命名约定编写自定义节点并通过 PR 贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Web 界面创建与控制 Minecraft 机器人
- 基于节点的机器人行为编排（React-Flow）
- Docker Compose 一键部署，镜像发布于 GHCR
- 可按约定添加自定义 JavaScript 节点并通过 PR 合入

## 适用场景

- 在多人服务器中运行自动化机器人（如收集木材合成工作台）
- 通过节点流编排自定义机器人行为
- 下载现成 flow 快速部署机器人任务

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  🤖 Use open and free AI models to generate reusable nodes for Minecraft bots.
> L20: Project KnowledgeBook is an open-source Minecraft bot management platform that provides players with a user-friendl

## 星数曲线

```mermaid
xychart-beta
    title "SilkePilon/KnowledgeBook 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 56 --> 59
    line [57, 58, 58]
```

2026-10-18 57 → 2026-10-27 58（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `62ea52debb5e` · [字段定义](../../DATASET.md)*
