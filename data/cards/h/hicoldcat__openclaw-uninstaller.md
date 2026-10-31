# hicoldcat/openclaw-uninstaller

⭐ 19 · Shell · MIT · 推送 2026-03-17 · [GitHub](https://github.com/hicoldcat/openclaw-uninstaller) · 个人维护 · 中文 README

**给 OpenClaw 用户的跨平台一键卸载脚本**

面向 Windows/macOS/Linux 的 OpenClaw 卸载脚本，提供 PowerShell 与 Bash 两个核心脚本，可从 GitHub 远程执行或本地运行。流程为：先扫描命令、进程、服务、全局包与残留文件并列出待清理内容供确认，随后优先调用官方卸载命令，再执行 npm/pnpm/yarn 全局包卸载与残留目录清理，最后输出 PATH 与终端配置的手动清理指引。支持 --dry-run 预览与 --yes 跳过确认；默认不删除源码仓库、不改 Git 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 优先调用官方卸载命令，再做 npm/pnpm/yarn 与残留兜底清理
- 正式卸载前扫描并列出待清理内容供用户确认
- 支持 --dry-run 预览与 --yes 自动继续
- 可从 GitHub 远程一键执行，无需先下载脚本

## 适用场景

- 彻底卸载 OpenClaw 及其 Node 全局包与残留文件
- 执行前先用 dry-run 预览将要清理的内容
- 卸载后按指引清理 PATH 与 shell 配置残留

## 场景标签

 · 领域:开发工具/系统清理

## 证据(README 行号)

> L9: **跨平台 OpenClaw 一键卸载脚本**
> L18: - 🧭 优先调用官方卸载命令：`openclaw uninstall --all --yes`

## 星数曲线

```mermaid
xychart-beta
    title "hicoldcat/openclaw-uninstaller 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c874660c94ac` · [字段定义](../../DATASET.md)*
