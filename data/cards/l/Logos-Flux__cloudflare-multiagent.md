# Logos-Flux/cloudflare-multiagent

⭐ 54 · TypeScript · MIT · 推送 2026-05-03 · [GitHub](https://github.com/Logos-Flux/cloudflare-multiagent) · 组织维护

**基于 Cloudflare Workers 的多 agent AI 服务平台（公开预览版）**

构建于 Cloudflare Workers 之上的多 agent AI 平台，以组织→实例→项目的层级管理服务，供任何已认证应用调用。包含配置服务（D1 数据库）、文本生成 Worker（OpenAI/Anthropic）、图像生成 Worker（Ideogram）、基于 Durable Objects 的限流、R2 存储、认证授权与 GitHub Actions CI/CD。技术栈为 TypeScript，测试用 Vitest。当前为 v0.1.0 公开预览，存在已知问题清单（KNOWN_ISSUES.md），MVP 不含视频生成与多租户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 组织→实例→项目的层级实例管理
- Provider 无关的可扩展框架，接入 OpenAI/Anthropic 文本生成与 Ideogram 图像生成
- 限流（Durable Objects）、R2 存储、认证授权与 CI/CD 部署自动化
- 提供测试 GUI 与带部署跟踪的管理面板

## 适用场景

- 在 Cloudflare Workers 上部署可被多应用调用的 AI 生成服务
- 以生产/预发实例隔离运行文本与图像生成 Worker
- 为团队提供带限流与监控的统一 AI 服务入口

## 场景标签

`多智能体` `图像生成` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: Cloudflare Multi-Agent is a production-ready multi-agent AI platform built on Cloudflare Workers infrastructure. It 
> L29: - **Text Generation Worker (OpenAI, Anthropic)** ✅

## 星数曲线

```mermaid
xychart-beta
    title "Logos-Flux/cloudflare-multiagent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-28 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7b49d5366710` · [字段定义](../../DATASET.md)*
