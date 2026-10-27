# mrgoonie/zuey-pi-setup

⭐ 52 · Shell · 推送 2026-09-20 · [GitHub](https://github.com/mrgoonie/zuey-pi-setup) · [官网](https://zuey.me) · 个人维护

**pi 编码 agent 配置的可移植快照与备份/恢复工具**

针对 pi coding agent 的 dotfiles 式仓库：利用 settings.json 中的 packages 数组在启动时自动 npm install 缺失扩展的机制，通过备份/恢复脚本（pi-setup-backup.sh / pi-setup-restore.sh）在另一台机器上重建 24 个扩展的完整配置。刻意排除密钥（auth.json、通知 token）、缓存与会话历史；支持 macOS/Linux/Windows(Git Bash)，提供 tarball 便携包与排除规则文件。面向 pi 用户做环境迁移，附带详细的 Windows 差异说明与越南语迁移文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 settings.json packages 数组的确定性扩展重建机制
- 备份/恢复脚本支持排除规则与外部配置清单，泄露密钥的配置被刻意排除
- macOS/Linux/Windows (Git Bash) 均验证过 restore→install→verify→backup 全流程
- 附带 10 文件预构建 tarball 便携包

## 适用场景

- 换新机器时重建整套 pi 编码 agent 配置
- 对 pi 扩展集合做可复现的版本化备份
- 在不同操作系统间迁移 agent 环境（需 Git Bash/WSL）

## 场景标签

 · 领域:开发者工具/AI agent 配置管理

## 证据(README 行号)

> L11: `pi` has no config export/import. This repo is a deterministic way to carry the **entire setup** to another machine
> L17: The mechanism: `settings.json` holds a `packages` array; pi reads it on startup and `npm install`s anything missing

## 星数曲线

```mermaid
xychart-beta
    title "mrgoonie/zuey-pi-setup 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 51 --> 54
    line [53, 52, 52]
```

2026-10-18 53 → 2026-10-27 52（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c16feb9d1a0e` · [字段定义](../../DATASET.md)*
