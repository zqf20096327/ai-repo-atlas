# project820/gjc-multivendor-setup-guide

⭐ 40 · Shell · NOASSERTION · 推送 2026-08-19 · [GitHub](https://github.com/project820/gjc-multivendor-setup-guide) · 个人维护

**GJC 多厂商 AI 编程代理的 5 订阅角色分配配置指南与安装脚本**

面向 GJC（Gajae Code）CLI 代理的多厂商配置仓库：用一条 curl 命令把 8 个预设配置包（4 层级：daily/cyber-cop/ultimate-opus/llm-council 等）合并进 ~/.gjc/agent/models.yml，将 Anthropic/OpenAI-Codex/xAI/Google/opencode-go 五类订阅按 planner/executor/architect/critic/default 五种角色分配到不同模型。文档还包含订阅-提供商标映射、effort 硬规则、基准依据与 2026-08-16/17 实调用验证矩阵，以及 cyber-cop 审查模式和迁移说明。需安装后逐个执行 /login 完成各提供者认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键安装脚本将 8 个配置包安全合并进 ~/.gjc/agent/models.yml 并自动备份
- 8 个配置包 × 5 角色的模型分配目录，按已持有订阅选择可用组合
- 提供订阅→provider-id 映射、effort 硬规则与验证矩阵（08-16/08-17 实调用记录）
- cyber-cop 审查模式：architect/critic 主导的高风险 PR 双票判定

## 适用场景

- 已持有多个 AI 订阅的用户在 GJC 中按角色分配不同厂商模型
- 按已有订阅组合快速选择可用的配置包
- 搭建带交叉验证 critic 的多代理编码工作流

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L28: curl -fsSL https://raw.githubusercontent.com/project820/gjc-multivendor-setup-guide/main/install.sh | bash
> L63: |`anthropic` + `openai-codex` + `xai`|⭐ **daily** · 🏎 **coding-sprint** · 🚨 **cyber-cop** · 🏆 **ultimate-opus** · 🛡
> L209: > ★ = 평소 권장. v3.0.0 카탈로그는 동등한 프로필 묶음이 아니라 4계층 8번들이다. 전 번들 `required_providers ≥ 2`, 기본 `critic=cross-family`(예외는 `

## 星数曲线

```mermaid
xychart-beta
    title "project820/gjc-multivendor-setup-guide 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-27 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4df292702ea8` · [字段定义](../../DATASET.md)*
