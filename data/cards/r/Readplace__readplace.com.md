# Readplace/readplace.com

⭐ 30 · TypeScript · 推送 2026-10-28 · [GitHub](https://github.com/Readplace/readplace.com) · [官网](https://readplace.com/) · 个人维护

**自托管的稍后阅读应用：保存文章/通讯链接，稍后阅读**

基于 10 年个人阅读系统构建的 read-it-later 应用：保存文章、AI 研究资料与 newsletter 邮件链接，供用户稍后阅读，无第三方跟踪。架构上采用超媒体设计（同一 URL 空间服务浏览器 HTML 与扩展的 Siren 协议）、SSR、Command→System→Event 异步模式，基础设施为 Pulumi 管理的 AWS 托管服务（Lambda/DynamoDB/EventBridge/S3/CloudFront）。README 详细记录了共享文章的防重定向劫持安全设计。AI 部分在开发流程内：Claude 作为工作 agent 审查每个 PR、修复 CI 失败并处理合并冲突。

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

- 同一 URL 空间经内容协商服务浏览器与扩展两种客户端
- 零客户端 JavaScript 的 SSR 交互（POST-Redirect-GET）
- Pulumi + AWS 托管服务的无 Kubernetes 基础设施
- Claude 在 GitHub Actions 中审查每个 PR 并修复 CI 失败

## 适用场景

- 保存文章与 newsletter 链接，空闲时再阅读
- 收集 AI 研究资料等阅读来源
- 了解超媒体架构与 AI agent 开发流程的参考实现

## 场景标签

 · 领域:阅读工具/Web 应用

## 证据(README 行号)

> L3: A read-it-later app. Save articles, read them later. Built from a personal reading system refined over 10 years.
> L43: Claude reviews every PR, fixes CI failures, resolves merge conflicts, and applies high-priority review comments — a

## 星数曲线

```mermaid
xychart-beta
    title "Readplace/readplace.com 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8e6c2fd388cd` · [字段定义](../../DATASET.md)*
