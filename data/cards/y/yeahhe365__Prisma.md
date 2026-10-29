# yeahhe365/Prisma

⭐ 339 · TypeScript · MIT · 推送 2026-07-16 · [GitHub](https://github.com/yeahhe365/Prisma) · [官网](https://prisma-8yz.pages.dev/) · 个人维护 · 中文 README

**面向 Gemini 的可视化多智能体深度推理 Web 应用**

基于 React 19 + TypeScript + Vite 6 的纯前端 Web 应用：将用户问题动态分解为子任务，由 Manager 规划、自动生成的专家角色并行执行、Synthesis 综合回复，最多进行 2 轮专家执行（初始轮 + 1 轮复审修正）。提供思维流节点图、专家卡片内部独白查看、分阶段思考预算设置；不预置模型，用户自行添加 Gemini API 或 OpenAI 兼容 API 模型，支持自定义 Base URL 反向代理。会话存储于浏览器 IndexedDB。可通过 Google AI Studio、在线 Demo、本地 npm 或 Docker 运行。README 自述为实验性应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Manager -> Experts -> Synthesis 深度多智能体工作流，最多 2 轮专家执行
- 思维流动态节点图与专家卡片内部独白/草稿可视化
- 规划/执行/综合三阶段独立思考预算设置（Minimal~High）
- 支持 Gemini 与 OpenAI 兼容 API，可配置自定义 Base URL

## 适用场景

- 通过可视化节点图观察多智能体推理全过程
- 用多专家并行方式处理需要分解的复杂问题
- 国内网络环境经反向代理网关接入 Gemini/OpenAI 兼容模型

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L24: **Prisma** 是一款探索多模型推理极限的实验性应用。它不仅仅是一个聊天机器人，更是一个**可视化的思维实验室**。
> L26: 它引入了 **"深度多智能体推理 (Deep Multi-Agent Reasoning)"** 架构，将复杂的用户问题动态分解为子任务，分派给专门的 AI 专家角色并行处理。用户可以实时观看 AI 如何通过 **Manager（
> L92: 访问 `http://localhost:3000` 后，先在「设置 -> 模型管理」中添加至少一个 Gemini API 或 OpenAI 兼容 API 模型。

## 星数曲线

```mermaid
xychart-beta
    title "yeahhe365/Prisma 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 337 --> 340
    line [338, 339, 339]
```

2026-10-18 338 → 2026-10-29 339（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fa7864f83087` · [字段定义](../../DATASET.md)*
