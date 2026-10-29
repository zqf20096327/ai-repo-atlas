# Lostovayne/Complete-Clone-of-Youtube

⭐ 20 · TypeScript · 推送 2025-12-21 · [GitHub](https://github.com/Lostovayne/Complete-Clone-of-Youtube) · [官网](https://newtube-clone.up.railway.app/) · 个人维护

**个人开发的 YouTube 克隆视频平台，Next.js 15 全栈实验项目**

基于 Next.js 15、TypeScript、tRPC、Drizzle ORM 构建的 YouTube 克隆，含视频上传流水线（Mux Direct Uploads + UploadThing 缩略图）、Clerk 认证、Upstash 缓存与限流、Webhook 处理与 studio 内轮询。AI 相关仅有视频智能推荐列入开发计划，非现有功能。安装需 git clone 后用 bun/npm 装依赖，配置 Clerk/Mux 等环境变量，本地开发需 ngrok 隧道接收 Webhook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mux Direct Uploads 视频上传流水线与 Webhook 状态更新
- tRPC 端到端类型安全 API + Drizzle ORM + NeonDB
- Clerk 认证与 Upstash Redis 缓存/限流
- studio 页面轮询展示 asset 实时状态

## 适用场景

- 学习 Next.js 15 + tRPC 全栈架构的参考实现
- 作为视频平台类项目的起点二次开发
- 了解 Mux/UploadThing Webhook 集成方式

## 场景标签

 · 领域:Web 开发/视频平台

## 证据(README 行号)

> L7: **NewTube** es un clon avanzado de YouTube construido con Next.js 15, TypeScript y Tailwind CSS 4, pero va mucho más
> L34: - Recomendaciones de video inteligentes

## 星数曲线

```mermaid
xychart-beta
    title "Lostovayne/Complete-Clone-of-Youtube 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `fac584aa0008` · [字段定义](../../DATASET.md)*
