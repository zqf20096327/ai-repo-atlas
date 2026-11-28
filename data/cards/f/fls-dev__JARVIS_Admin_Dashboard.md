# fls-dev/JARVIS_Admin_Dashboard

⭐ 3 · JavaScript · MIT · 推送 2026-11-18 · [GitHub](https://github.com/fls-dev/JARVIS_Admin_Dashboard) · [官网](https://fls-dev.github.io/JARVIS_Admin_Dashboard/) · 个人维护

**面向 AI agent 运维面板的开源管理台 HTML 模板（两套）**

为管理基础设施的 AI agent 提供两套纯静态管理台模板：Aurora 采用玻璃球 Canvas 2D 活动画布风格，Orbital 采用 three.js 3D 星球房间导航。共各含 11 个 HTML 页面（含 Operations、微调、内存、集成、审计等界面），纯 HTML/CSS/vanilla JS，无构建步骤与运行时依赖，支持 390–1920px 响应式与 reduced-motion。所有任务、聊天、模型响应均为虚构演示数据，不含后端、鉴权或真实集成，需自行接入 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两套模板各 11 页，含 Operations/微调/内存/审计等 AI agent 管理界面
- 纯 HTML/CSS/vanilla JS，无构建步骤，支持 file:// 直接打开
- three.js 与字体可打包离线使用，无 WebGL 时回退 CSS 星球
- 390–1920px 响应式，支持 prefers-reduced-motion 与键盘导航

## 适用场景

- 为自建 AI agent 管理面板选一套前端模板做定制起点
- 在无构建工具的环境中直接打开静态页面进行设计评审
- 需要移动端适配的暗色主题管理界面原型

## 场景标签

 · 领域:前端 UI 模板/管理台

## 证据(README 行号)

> L7: Open-source admin templates for an AI agent that runs your infrastructure — made for design feedback and real custom
> L155: With Python, visit **http://localhost:8080/**. `npx serve` prints its own local URL. There is no install, bundle, 
> L157: > These are **static UI templates, not a full application**. Tasks, hosts, costs, model responses and chat message

## 星数曲线

```mermaid
xychart-beta
    title "fls-dev/JARVIS_Admin_Dashboard 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `04f2a4bc62dc` · [字段定义](../../DATASET.md)*
