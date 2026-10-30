# abczsl520/nodejs-project-arch

⭐ 21 · MIT · 推送 2026-10-20 · [GitHub](https://github.com/abczsl520/nodejs-project-arch) · [官网](https://clawhub.com/skills/nodejs-project-arch) · 个人维护

**面向 AI agent 的 Node.js 项目架构规范技能包**

一个 OpenClaw / AI agent 技能（skill），内容为 Node.js 项目架构规范：限定单文件 ≤400 行、config.json 集中管理可调参数、routes/services 分层目录结构、每个项目附带 admin.html 管理面板。目标是让 AI agent 读写代码时不超出上下文窗口，README 给出 65-93% 的 token 节省测算表。覆盖 H5 游戏、数据工具、API 服务、SDK 等 6 类项目模板，通过 git clone 复制到 ~/.agents/skills/ 安装，也可直接阅读参考文档。属于 project-arch 技能家族的 Node.js 分支。

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

- 单文件 ≤400 行 / index.html ≤200 行 / server.js ≤100 行的量化规则
- config.json 集中管理可调参数并支持 admin 仪表盘热更新
- 6 类项目类型（H5 游戏/数据工具/API/SDK 等）各自的参考架构
- 提供 token 节省对比测算（65-93%）

## 适用场景

- 让 AI agent 按 token 友好的规范创建新 Node.js 项目
- 指导 AI 拆分过大的单文件代码库
- 查各类 Node.js 项目（H5 游戏、API 服务、SDK）的参考目录结构

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: An OpenClaw / AI agent skill that enforces modular file structures, keeping every file small enough for AI to read a
> L61: The skill auto-activates when you ask your AI agent to:

## 星数曲线

```mermaid
xychart-beta
    title "abczsl520/nodejs-project-arch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0d561a4bb3a8` · [字段定义](../../DATASET.md)*
