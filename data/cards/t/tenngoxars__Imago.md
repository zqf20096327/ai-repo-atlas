# tenngoxars/Imago

⭐ 16 · TypeScript · MIT · 推送 2026-01-14 · [GitHub](https://github.com/tenngoxars/Imago) · 个人维护 · 中文 README

**开源全栈 AI 图像/视频生成平台架构，含用户系统与积分付费**

基于 Next.js、Supabase 和 Stripe 的全栈 AI 图像生成应用架构，源自一个商业项目开源而来。提供三种核心模式：Fantasy（风格化预设）、Freeform（开放画布）、Flow（视频生成），并内置 Prompt 构建与清洗逻辑（Humanizer）、预设词自动补全与负面提示词。覆盖 Supabase Auth 用户系统、Stripe 充值支付、积分扣减与 webhook 回调，面向需要搭建生产级生成式 AI 产品的开发者。部署需自行配置 Supabase、Stripe 与 R2 Storage。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种生成模式：风格化预设、开放画布、视频生成
- Prompt 构建与清洗逻辑（Humanizer），支持自动补全与负面提示词
- Stripe 积分充值、webhook 回调与扣费逻辑
- Supabase Auth 邮箱与社交登录

## 适用场景

- 搭建带付费与用户体系的 AI 图像生成产品
- 复用其 Prompt 构建模块开发生成类应用
- 作为生成式 AI SaaS 项目的技术架构参考

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L9: **Imago** is an open-source full-stack AI image generation application architecture, designed for building high-perf
> L19: - **🎨 Multi-Mode Capability**: Supports three core modes: Fantasy (Styled Presets), Freeform (Open Canvas), and Flo

## 星数曲线

```mermaid
xychart-beta
    title "tenngoxars/Imago 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f34ea59dcda2` · [字段定义](../../DATASET.md)*
