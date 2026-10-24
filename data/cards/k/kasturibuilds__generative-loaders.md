# kasturibuilds/generative-loaders

⭐ 212 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/kasturibuilds/generative-loaders) · [官网](https://generativeloaders.com) · 个人维护

**React 加载态组件库：面向生成式界面的流式文本/占位动画**

面向生成式 AI 界面的 React 加载态组件库，提供三个原语：TextLoader（16 种流式文本揭示变体，追加感知、前缀稳定）、InlineLoader（18 种紧凑活动指示器）、ImageLoader（12 种图像生成占位变体）。所有组件支持 aria 标签、respect prefers-reduced-motion、SSR 安全。以 npm 包发布，支持 React 18 及以上，TypeScript 类型从包根导出。

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

- TextLoader/InlineLoader/ImageLoader 三原语共 46 种变体
- 流式文本追加感知：已接收内容不重复动画
- 无障碍支持：polite live status、prefers-reduced-motion、SSR 安全
- TypeScript 类型与 props 全部导出

## 适用场景

- LLM 流式回答在前端展示时的加载动画
- 图像生成过程中预留占位框
- 按钮与状态行等待文本到达时的内联指示

## 场景标签

 · 领域:前端开发/生成式 UI 组件

## 证据(README 行号)

> L8: Accessible React loading states designed for generative interfaces: sixteen animated text reveals, eighteen compact 
> L35: |`TextLoader`|Responses that grow as tokens or chunks arrive|16|

## 星数曲线

```mermaid
xychart-beta
    title "kasturibuilds/generative-loaders 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 210 --> 213
    line [211, 212]
```

2026-10-18 211 → 2026-10-24 212（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `03281566b452` · [字段定义](../../DATASET.md)*
