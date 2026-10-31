# shipwords-dev/shipwords

⭐ 295 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/shipwords-dev/shipwords) · [官网](https://shipwords.dev) · 组织维护 · 中文 README

**新词站群框架：一个关键词一个 AI 图像/视频付费站**

MIT 许可的 Cloudflare 原生开源框架，用于运营新关键词 AI 图像/视频网站群：共享部分（登录、积分、Stripe/PayPal 收款、AI 生成运行时、SEO）写一次全站复用，每个站点独立部署，拥有自己的 D1 数据库、R2 存储与支付账户。生成能力通过 Yir API 单一密钥接入 GPT Image、FLUX、Veo、Kling 等模型，本地开发可用 mock 上游，无需模型密钥。以 pnpm 命令从模板脚手架创建站点，可配合 Claude Code 等 agent 按 llms.txt 自动建站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 共享核心：Better Auth 登录、Stripe/PayPal 积分与订阅、幂等积分账本、失败任务自动退款
- 一个 Yir API 密钥接入 GPT Image、Seedream、FLUX、Seedance、Veo、Kling、Wan 等模型
- 每站独立 Worker + D1 + R2 + Workflows 部署，站点间互不影响
- pnpm new-site 从模板脚手架建站，内置 tinydeskai.io 完整源码示例

## 适用场景

- 为新兴 AI 关键词快速上线可收费的图像/视频生成站
- 运营多个独立站点：起量的继续迭代，未起量的保留不动
- 用编码 agent（Claude Code/Codex/Cursor）按规则自动建站

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L14: shipwords is a free, MIT-licensed framework for running a fleet of new-keyword AI image and video sites on Cloudfla
> L24: - **The popular models, built in**: GPT Image, Nano Banana, Seedream, FLUX, Seedance, Veo, Kling, Wan and more, beh
> L104: |`packages/jobs`|Workflow-based generation runtime with a one-way job state machine and automatic refunds, upstrea

## 星数曲线

```mermaid
xychart-beta
    title "shipwords-dev/shipwords 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-10-31"]
    y-axis "stars" 40 --> 318
    line [63, 269, 295]
```

2026-10-29 63 → 2026-10-31 295（+232）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `9244397d4849` · [字段定义](../../DATASET.md)*
