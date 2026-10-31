# this-is-not-a-dev/Neural-Nexus

⭐ 16 · TypeScript · MIT · 推送 2026-09-30 · [GitHub](https://github.com/this-is-not-a-dev/Neural-Nexus) · [官网](https://www.neuralnexus.biz/) · 个人维护

**AI 模型交易市场平台：上传、销售、区块链转移模型所有权**

基于 Next.js/Supabase 构建的 AI 模型集市 Web 应用：用户可上传、分享和出售模型与数据集，支持 Stripe、Razorpay(UPI)、加密货币(MetaMask) 等支付方式，通过区块链完成模型所有权转移，提供 Google/GitHub/钱包登录与 SendGrid 邮件通知。另发布 npm 包 neural-nexus，供通过 API key 接入平台部署、管理和分享模型。自建部署需配置 MongoDB Atlas、Supabase、SendGrid 等多项外部服务与环境变量，Firebase 为旧版可选依赖。

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

- 模型上传与免费/付费市场（Stripe/Razorpay/加密货币支付）
- 区块链安全的模型所有权转移与钱包登录
- 配套 TypeScript SDK 包 neural-nexus（API key 认证）
- Supabase 认证/存储 + MongoDB（含内存回退）双数据路径

## 适用场景

- 搭建自己的 AI 模型分享与售卖平台
- 通过 SDK 接入 Neural Nexus 平台管理模型与 API key
- 以付费方式分发团队的模型与数据集

## 场景标签

 · 领域:AI 模型市场/Web 平台

## 证据(README 行号)

> L24: Welcome to **Neural Nexus**, a comprehensive AI model hub where you can upload, sell, and transfer ownership of you
> L30: - **Upload AI Models**: Share your models with the world
> L188: A modern, TypeScript-first toolkit for connecting with AI models on the Neural Nexus platform. Effortlessly deploy

## 星数曲线

```mermaid
xychart-beta
    title "this-is-not-a-dev/Neural-Nexus 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-25 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `243b3f14d8a5` · [字段定义](../../DATASET.md)*
