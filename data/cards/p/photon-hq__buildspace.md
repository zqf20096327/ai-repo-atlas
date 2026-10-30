# photon-hq/buildspace

⭐ 15 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/photon-hq/buildspace) · [官网](https://photon.codes) · 组织维护

**可复用 GitHub Actions 发布流水线与组件库，供研发团队直接接入**

由 Photon 维护的 CI/CD 自动化仓库，提供两层结构：即插即用的 Workflows（覆盖 Rust/TypeScript/Go/Swift/npm 包/容器镜像的发布与晋级流水线）和可组合的 Blocks。机制上以 stage/promote 双阶段发布、镜像按 digest 推送并附 attestation、PR 标签触发发布为主。多数发布 workflow 需要 OPENAI_API_KEY 用于 AI 驱动的版本号生成与发布说明，update-docs/update-skills 使用 ANTHROPIC_API_KEY。通过在调用方仓库引用 workflow 文件并固定 commit SHA 接入，仓库本身不发布版本或标签。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两类结构：预置发布流水线（Workflows）与可组合 Blocks
- stage/promote 双阶段发布：staging 构建经审批后原样晋级生产，不重建
- 容器镜像按 digest 推送并强制 attestation，防标签被替换
- PR 标签（release/prerelease）控制是否触发发布，无标签不发布

## 适用场景

- 为自己的仓库接入预置的 Rust/TypeScript/Go/Swift 发布流水线
- npm 包或容器镜像做 staging 验证后晋级生产的发布管理
- 自动生成版本号与 AI 驱动的发布说明

## 场景标签

 · 领域:开发工具/CI-CD

## 证据(README 行号)

> L100: Most release workflows need `OPENAI_API_KEY` for AI-powered versioning and release notes. The `update-docs` and `u
> L105: |`ANTHROPIC_API_KEY`|Update Documentation, Update Skills|console.anthropic.com/settings/keys|

## 星数曲线

```mermaid
xychart-beta
    title "photon-hq/buildspace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `198fe071ea45` · [字段定义](../../DATASET.md)*
