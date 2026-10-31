# cwandev/vue-stick-to-bottom

⭐ 18 · TypeScript · MIT · 推送 2026-07-22 · [GitHub](https://github.com/cwandev/vue-stick-to-bottom) · [官网](https://vue-stick-to-bottom.netlify.app) · 个人维护

**Vue 3 聊天滚动组件：流式追加内容时保持平滑贴底**

面向 AI 聊天应用的 Vue 3 组件与 composable，在可滚动容器中自动贴底并在新内容追加时以速度弹簧动画平滑滚动保持视觉位置。基于 ResizeObserver 检测内容尺寸变化，支持内容收缩时保持粘性、正确处理滚动锚定、区分用户滚动与动画滚动、用户上滑可取消贴底；不依赖 overflow-anchor。零运行时依赖，提供 TypeScript 声明与 Tree-shakable ESM 构建，是 use-stick-to-bottom 的非官方 Vue 移植。

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

- 基于 ResizeObserver 检测内容尺寸变化，支持收缩时保持粘性
- 速度弹簧动画（阻尼/刚度/质量可配），适配流式追加的可变尺寸内容
- 区分用户滚动与动画滚动，用户上滑取消贴底
- 零运行时依赖，ESM + TypeScript 声明

## 适用场景

- AI 聊天应用中流式输出消息时保持平滑贴底滚动
- 自定义 DOM 结构时通过 composable 接入贴底能力
- 实现滚动到底部按钮等覆盖层交互

## 场景标签

 · 领域:前端 UI 组件/聊天应用

## 证据(README 行号)

> L3: > Designed with AI chat bots in mind, unofficial Vue port of use-stick-to-bottom.
> L8: A lightweight Vue 3 component and composable that automatically sticks to the bottom of a scrollable container and s

## 星数曲线

```mermaid
xychart-beta
    title "cwandev/vue-stick-to-bottom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `897b897f172d` · [字段定义](../../DATASET.md)*
