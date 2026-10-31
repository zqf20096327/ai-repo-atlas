# comet-ml/cometx

⭐ 15 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/comet-ml/cometx) · 组织维护

**Comet ML 的社区开源 CLI 扩展：实验数据下载、迁移与管理**

围绕 Comet SDK 构建的命令行工具集，非 Comet ML 官方项目。提供 list/count 查询工作区、项目与实验，download 按资源类型（指标、参数、代码、资产、模型注册表、面板等）批量下载，copy 将下载数据复制为新实验或建立符号链接，log 向实验写入指标/资产/面板，migrate-users 依据 chargeback 报告在 Comet 环境间迁移用户，panel-studio 在本地编写并测试 Python 面板后上传。通过 pip 安装，需 Comet API key；部分资产类型标注为弃用或未使用。

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

- 按资源类型批量下载实验、artifacts、模型注册表与面板
- 支持从 wandb、neptune 作为下载源复制数据
- Comet 环境间用户与工作区迁移（migrate-users，支持 dry-run）
- panel-studio 本地编写并测试 Comet Python 面板后上传

## 适用场景

- 批量备份或迁移 Comet 上的实验数据与模型
- 从 wandb/neptune 平台把数据复制到 Comet
- 本地开发和调试 Comet 项目面板
- 管理员在两个 Comet 环境间迁移用户与工作区成员关系

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L10: Open source extensions for the Comet SDK.
> L37: for ML management.

## 星数曲线

```mermaid
xychart-beta
    title "comet-ml/cometx 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c924a2abf2e3` · [字段定义](../../DATASET.md)*
