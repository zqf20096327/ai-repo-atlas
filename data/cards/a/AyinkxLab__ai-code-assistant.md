# AyinkxLab/ai-code-assistant

⭐ 23 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/AyinkxLab/ai-code-assistant) · 组织维护

**面向 GitHub 仓库的项目感知 AI 编码助手工作区**

AI 驱动的开发者工作区（Flask，MIT 许可）：接入 GitHub 仓库后可基于项目上下文对话、分析仓库/issue/PR、导入项目并跨文件搜索、运行 AI 代码审查与质量分析，支持带权限的团队协作工作区。内置 Stellar/Soroban 相关开发工作流（XDR 与交易解码、RPC/Horizon 检查、离线 mock 网络、合约脚手架）。插件系统默认 fail-closed，出站请求按白名单放行；LLM 用量记入仅元数据的账本，支持预算与 Prometheus 指标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于仓库/PR/issue 上下文的项目感知 AI 对话与代码审查
- Stellar/Soroban 工具链：XDR 与交易解码、RPC/Horizon 检查、离线 mock 网络、合约脚手架
- 能力型插件系统，默认 fail-closed（签名校验、网络白名单、执行超时）
- 仅元数据的用量账本，支持预算强制、Prometheus 指标与成本估算

## 适用场景

- 在我的代码库上下文中提问并审查 PR 质量
- 团队在带权限的共享工作区中协作分析项目
- Stellar/Soroban 合约开发中解码交易与检查 RPC/Horizon

## 场景标签

`AI 助手` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: - Chat with AI over project and repository context
> L16: - Run AI code review and quality analysis

## 星数曲线

```mermaid
xychart-beta
    title "AyinkxLab/ai-code-assistant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 15 --> 24
    line [16, 22, 23]
```

2026-10-18 16 → 2026-10-30 23（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7db6af5aa045` · [字段定义](../../DATASET.md)*
