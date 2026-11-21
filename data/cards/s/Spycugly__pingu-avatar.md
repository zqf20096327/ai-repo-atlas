# Spycugly/pingu-avatar

⭐ 4 · TypeScript · MIT · 推送 2026-11-02 · [GitHub](https://github.com/Spycugly/pingu-avatar) · [官网](https://pingu-avatar.vercel.app) · 个人维护 · 中文 README

**给 AI 聊天助手的 React 动画头像组件**

React 头像组件，为 AI 助手界面提供监听、思考、说话、反应等动画表现。提供 36 种表情、10 种形状、任意颜色、口型同步与 PNG/SVG/GIF/MP4 导出。无独立安装包，直接复制 avatar/ 目录进项目，仅依赖 React 18/19 与 TypeScript，适配 Next.js App Router 与 Vite。开发者通过将助手状态映射到组件 state 控制显示，浏览器端另有定制工作室支持多语言与时间线动画导出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 36 种表情与 10 种身体形状，支持任意 hex 颜色并平滑过渡
- 通过 state 映射将助手状态（idle/listening/thinking/talking）接入头像
-  syllableFor 按打字机字符驱动口型同步
- 浏览器端工作室支持定制并导出 PNG/SVG/GIF/MP4

## 适用场景

- 给聊天机器人的流式回答配上会动嘴的头像
- 在 React/Next.js 项目中展示助手的等待、思考、出错等状态
- 为助手品牌形象定制形状颜色并导出静态图或动画视频

## 场景标签

 · 领域:前端 UI 组件/AI 助手界面

## 证据(README 行号)

> L7: Drop it into a React project and give your assistant a face that listens, thinks, talks and reacts.
> L36: ### 3. Connect it to your assistant
> L38: Map what your assistant is doing to a state:

## 星数曲线

```mermaid
xychart-beta
    title "Spycugly/pingu-avatar 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-23", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-19 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `7931046b874d` · [字段定义](../../DATASET.md)*
