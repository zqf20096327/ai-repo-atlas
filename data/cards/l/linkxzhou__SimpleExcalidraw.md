# linkxzhou/SimpleExcalidraw

⭐ — · [GitHub]() · 个人维护 · 中文 README

**Excalidraw 中文分支：手绘白板增加 AI 生成与动画回放**

基于 Excalidraw 的中文定制版本，由个人开发者维护。在原白板基础上新增中文手写体、多画布、多模板字段适配、更多颜色选择、手机端体验优化，并增加两项功能：通过环境变量配置外部 AI 接口（兼容 OpenAI 格式的 chat completions 地址与密钥）实现 AI 生成；基于 SVG 与 Web Animations API 的画板动画回放，自动按路径长度分配时长，模拟笔迹书写，支持播放/暂停/跳转。本地运行需 Node.js 与 Yarn，或使用 docker-compose；另提供 Vercel 在线地址。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 中文手写体与多画布支持
- AI 生成功能：外部配置 OpenAI 格式接口与模型名
- 基于 SVG + WAAPI 的绘图过程动画回放（自动时长分配、循环与 seek）
- 提供 docker-compose 本地开发方式与 Vercel 在线地址

## 适用场景

- 中文用户使用手绘风格白板绘图与协作
- 回放绘图过程做演示或动画展示
- 接入 AI 接口由模型生成画板内容

## 场景标签

 · 领域:协作绘图/白板工具

## 证据(README 行号)

> L13: - [x] 增加 AI 生成功能
> L22: REACT_APP_AI_API= // 你的 AI 接口地址，样例：https://api.openai.com/v1/chat/completions
> L115: ### 核心架构

## 星数曲线

```mermaid
xychart-beta
    title "linkxzhou/SimpleExcalidraw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `74e95578e70f` · [字段定义](../../DATASET.md)*
