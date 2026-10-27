# asimov-platform/asimov-cli

⭐ 27 · Rust · Unlicense · 推送 2026-10-23 · [GitHub](https://github.com/asimov-platform/asimov-cli) · [官网](https://crates.io/crates/asimov-cli) · 组织维护

**面向 AI agent 的 ASIMOV 模块/资源管理命令行工具**

ASIMOV 平台的官方 CLI，用 Rust 编写。提供从 URL 抓取数据（自动选择已安装模块）、导入社交媒体资源（如配合 Bright Data 模块）、管理已安装模块（install/list）、以及 resource fetch/read/list/snap 等资源操作；自动发现并运行 asimov- 前缀的外部命令。Rust 1.99.1+ 为前置要求，支持 Cargo、Homebrew、Scoop、Nix、Flatpak 等多种安装方式。GitHub 发布的二进制带可选择退出的遥测（发送至 Statsig），源码构建不发送。项目自述处于早期建设阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动选择已安装模块从 URL 抓取与导入数据
- 模块管理（asimov module install）与 asimov- 前缀外部命令自动发现
- resource fetch/read/list/snap 资源操作（snap 需 unstable 特性）
- 覆盖 Cargo/Homebrew/Scoop/Nix/Flatpak 的多渠道安装

## 适用场景

- 为 AI agent 安装与管理 ASIMOV 模块
- 从 URL 抓取或导入数据供 agent 使用
- 通过 CLI 查询与读取已缓存资源

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L135: # Fetch data from a URL, automatically choosing from installed modules
> L159: The CLI automatically discovers and runs external commands starting with `asimov-`.

## 星数曲线

```mermaid
xychart-beta
    title "asimov-platform/asimov-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `708a58835635` · [字段定义](../../DATASET.md)*
