# lidge-ai/ima2-gen

⭐ 905 · TypeScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/lidge-ai/ima2-gen) · [官网](https://lidge-ai.github.io/ima2-gen/) · 组织维护 · 中文 README

**给个人与编程 agent 的本地图像/视频生成工作室与运行时**

在用户本机运行一个小型服务器与工作室界面，通过浏览器、Mac 应用、CLI 或编程 agent 调用多种图像/视频生成通道。每次生成保存提示词、耗时与参数到本地目录，支持节点图分支派生、Canvas 擦除抠图与矢量描摹、Grok 视频与分镜模式、本地画廊检索，并为 agent 附带三个 Markdown 技能文件。生成依赖用户自行连接的各家服务商账号或 API key，视频生成需 Grok OAuth。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地保存每次生成结果的提示词、耗时与参数，可复现
- 节点图分支：每个分支记录父节点，不覆盖原结果
- Canvas Mode 支持擦除、抠图、带 alpha 导出与栅格转矢量
- 内置 CLI 与三个供编程 agent 加载的 Markdown 技能

## 适用场景

- 在本机批量生成与分支迭代图像和视频
- 让编程 agent 通过 CLI 和技能文件调用图像/视频生成
- 需要透明背景或矢量导出的素材制作流程
- 多服务商账号集中在一个本地界面管理生成任务

## 场景标签

`图像生成` `视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L47: `ima2-gen` is a local-first visual generation runtime and studio for people and coding agents, with reproducible im
> L164: ima2-gen ships three Markdown skills that coding agents load for structured image, video, frontend-asset and desig

## 星数曲线

```mermaid
xychart-beta
    title "lidge-ai/ima2-gen 星数(近 25 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 877 --> 908
    line [879, 881, 884, 885, 886, 887, 888, 889, 890, 885, 897, 899, 900, 899, 900, 901, 900, 901, 903, 905, 904, 905, 906, 905, 905]
```

2026-10-22 879 → 2026-11-24 905（+26）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `a0cf180dced4` · [字段定义](../../DATASET.md)*
