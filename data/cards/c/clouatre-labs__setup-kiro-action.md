# clouatre-labs/setup-kiro-action

⭐ 16 · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/clouatre-labs/setup-kiro-action) · [官网](https://github.com/clouatre-labs/setup-kiro-action) · 个人维护

**在 CI/CD 中安装并缓存 Kiro CLI 的 GitHub Action**

一个非官方的复合型 GitHub Action：从 AWS CDN 下载 Kiro CLI 二进制并缓存到 ~/.local/bin，供工作流后续使用；支持指定版本、SHA256 校验和，可导出 AMAZON_Q_SIGV4=1 以实现 IAM 无头认证（README 声明该功能在 kiro-cli-chat 中尚未由上游实现，仅发出警告无实际效果）。仅支持 GitHub 托管的 Ubuntu x64/ARM64 运行器，不支持 macOS/Windows。附三层 AI 增强流水线安全模式说明与 Q CLI 迁移对照表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动下载并缓存 Kiro CLI 二进制，加速后续运行
- SIGV4/IAM 与 GitHub OIDC 无凭证认证通道（上游功能未实现，有已知限制）
- 默认 SHA256 校验下载的二进制
- 仅支持 GitHub 托管 Ubuntu x64/ARM64 运行器

## 适用场景

- 在 CI 流水线中自动安装 Kiro CLI 供工作流调用
- 从 Q CLI Action 迁移到 Kiro CLI Action
- 按三层安全模式在 CI/CD 中使用 AI 分析工具输出

## 场景标签

 · 领域:DevOps/CI-CD

## 证据(README 行号)

> L5: A GitHub Action that installs and caches Kiro CLI for CI/CD workflows, with headless IAM authentication via SIGV4. O
> L37: - **Automatic caching** - Caches Kiro CLI binaries for faster subsequent runs
> L114: On first run, the action downloads the Kiro CLI binary from AWS CDN and caches it at `~/.local/bin/`. Subsequent r

## 星数曲线

```mermaid
xychart-beta
    title "clouatre-labs/setup-kiro-action 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `916b6f770704` · [字段定义](../../DATASET.md)*
