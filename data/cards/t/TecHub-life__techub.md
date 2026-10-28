# TecHub-life/techub

⭐ 23 · Ruby · MIT · 推送 2026-10-19 · [GitHub](https://github.com/TecHub-life/techub) · [官网](https://techub.life) · 组织维护

**为 GitHub 用户生成 AI 交易卡片的 Rails Web 应用**

Rails 8 + SQLite 的 Web 应用，为 GitHub 个人资料生成 AI 辅助的交易卡片（techub.life），集成 GitHub App 认证、用户 OAuth、webhook 摄取与个人资料摘要。含 Solid Queue 后台任务调度、Tailwind v4 界面、个人主页展示（链接/成就/经历，支持置顶与隐藏）、Ahoy 事件分析。面向希望建立此类站点或自行部署的开发者，通过 bin/setup/bin/dev 本地运行，支持 Kamal 部署与 Docker Compose。需配置 GitHub App 凭据等环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub App + 用户 OAuth + webhook 摄取的完整集成
- Solid Queue 后台刷新与图片优化任务
- 个人主页展示：置顶/隐藏/样式预设/控制台彩蛋
- Kamal 容器化部署与 Docker Compose 本地运行

## 适用场景

- 部署一个为 GitHub 用户生成 AI 交易卡片的网站
- 展示带链接、成就、经历的 GitHub 个人主页
- 基于 Rails 8 + Solid Queue 学习可运维的单机 Web 架构

## 场景标签

 · 领域:开发者社交/个人主页

## 证据(README 行号)

> L15: techub.life — AI-powered trading cards for GitHub profiles.
> L17: Rails 8 application powering AI-assisted trading cards for GitHub profiles. It bundles the GitHub
> L27: - **GitHub integrations** covering App authentication, user-to-server OAuth, webhook ingestion, and

## 星数曲线

```mermaid
xychart-beta
    title "TecHub-life/techub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f3540ce5bff8` · [字段定义](../../DATASET.md)*
